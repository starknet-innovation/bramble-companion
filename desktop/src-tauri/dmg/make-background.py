"""Draw the DMG installer background (#83): install hint plus the experimental warning.

Run from this directory on macOS with Pillow installed:

    python3 make-background.py

It writes background.png (660x400, the window size set in tauri.conf.json). The warning text matches EXPERIMENTAL_NOTICE in desktop/src/brand.ts.
Icon positions in tauri.conf.json (app at 180,170; Applications at 480,170) must stay
clear of the drawn text.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 660, 400
BG = (245, 245, 245)
TEXT = (23, 23, 23)
MUTED = (100, 100, 100)
BAND = (255, 237, 213)  # warning band, light orange
WARN = (154, 52, 18)  # dark orange text on the band
FONT = "/System/Library/Fonts/HelveticaNeue.ttc"


def draw(scale: int) -> Image.Image:
    s = lambda v: int(v * scale)  # noqa: E731
    img = Image.new("RGB", (s(W), s(H)), BG)
    d = ImageDraw.Draw(img)
    hint = ImageFont.truetype(FONT, s(13))
    bold = ImageFont.truetype(FONT, s(16), index=1)
    body = ImageFont.truetype(FONT, s(12))

    d.text((s(W / 2), s(40)), "Drag Bramble Companion to Applications", font=hint,
           fill=MUTED, anchor="mm")
    # Arrow between the two icons.
    y = s(170)
    d.line([(s(265), y), (s(390), y)], fill=MUTED, width=s(2))
    d.polygon([(s(395), y), (s(383), y - s(7)), (s(383), y + s(7))], fill=MUTED)

    # Warning band.
    d.rectangle([(0, s(300)), (s(W), s(H))], fill=BAND)
    d.text((s(W / 2), s(328)), "EXPERIMENTAL. NOT FOR REAL FUNDS.", font=bold, fill=WARN,
           anchor="mm")
    d.text((s(W / 2), s(354)), "The cryptography has not been audited.", font=body, fill=TEXT,
           anchor="mm")
    d.text((s(W / 2), s(372)),
           "Use a throwaway test seed only: never a real recovery phrase or one that controls funds.",
           font=body, fill=TEXT, anchor="mm")
    return img


if __name__ == "__main__":
    draw(1).save("background.png")
