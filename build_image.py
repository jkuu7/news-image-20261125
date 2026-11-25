"""Build entry.png: a 1024x1024 newspaper-style summary of 25 Nov 2026 world news.
Deterministic: no randomness, no clock, no network. Run: python3 build_image.py
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

NAVY = (15, 42, 68)
RED = (178, 34, 34)
TEAL = (0, 110, 110)
GOLD = (176, 124, 0)
GREY = (90, 90, 90)
LIGHT = (238, 240, 243)
LINE = (200, 205, 210)

# Masthead
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((36, 18), "THE WORLD TODAY", font=font(SERIF_BOLD, 52), fill="white")
d.text((36, 78), "WEDNESDAY  •  25 NOVEMBER 2026  •  SIX STORIES THAT DEFINED THE DAY",
       font=font(BOLD, 17), fill=(180, 205, 225))
d.rectangle([0, 118, W, 124], fill=RED)

# Lead story
d.rectangle([28, 142, 996, 348], outline=LINE, width=2)
d.rectangle([28, 142, 996, 182], fill=RED)
d.text((44, 150), "LEAD  —  STRAIT OF HORMUZ", font=font(BOLD, 20), fill="white")
d.text((44, 192), "Two oil tankers hit mines",
       font=font(BOLD, 36), fill=NAVY)
d.text((44, 234), "and catch fire in Hormuz",
       font=font(BOLD, 36), fill=NAVY)
body = ("Iran's Revolutionary Guard says the tankers struck naval mines "
        "on an unauthorised route through the strait. Fresh fears for "
        "global energy shipping as the Iran confrontation widens.")
y = 282
for line in wrap(d, body, font(REG, 20), 920):
    d.text((44, y), line, font=font(REG, 20), fill=(40, 40, 40))
    y += 26

stories = [
    ("UKRAINE", TEAL, "Drones hit two Russian refineries",
     "Ukrainian drones set two Rosneft refineries in Samara ablaze. "
     "Russia struck Odesa and Kyiv, killing two in Odesa."),
    ("HUAWEI VERDICT", NAVY, "US jury convicts Huawei",
     "Guilty on 10 of 12 counts, including bank fraud, sanctions "
     "violations and conspiracy to steal trade secrets."),
    ("MARKETS", GOLD, "Asia tumbles, Dow tops 50,000",
     "KOSPI -6.2%, Nikkei -2.8%, Nasdaq -1.5%. The Dow closed "
     "above 50,000 for the first time, up 0.9%."),
    ("CLIMATE", (60, 120, 60), "COP31 talks collapse",
     "No deal in Antalya as oil producers blocked any mention of "
     "phasing out fossil fuels. Pope Leo XIV voices concern."),
    ("SPACE & PACIFIC", (110, 60, 140), "Shenzhou-24 docks",
     "China's Shenzhou-24 docks with Tiangong, carrying Pakistan's "
     "first astronaut. Australia and Solomon Islands sign a pact "
     "barring foreign military bases."),
]

cells = [
    (28, 366, 474, 200),
    (522, 366, 474, 200),
    (28, 586, 474, 200),
    (522, 586, 474, 200),
    (28, 806, 474, 168),
]
for (x, y0, w, h), (tag, color, head, body) in zip(cells, stories):
    d.rectangle([x, y0, x + w, y0 + h], outline=LINE, width=2)
    d.rectangle([x, y0, x + w, y0 + 38], fill=color)
    d.text((x + 14, y0 + 9), tag, font=font(BOLD, 18), fill="white")
    yy = y0 + 50
    for line in wrap(d, head, font(BOLD, 23), w - 28):
        d.text((x + 14, yy), line, font=font(BOLD, 23), fill=NAVY)
        yy += 29
    yy += 4
    for line in wrap(d, body, font(REG, 18), w - 28):
        d.text((x + 14, yy), line, font=font(REG, 18), fill=(40, 40, 40))
        yy += 23

# Also box
x, y0, w, h = 522, 806, 474, 168
d.rectangle([x, y0, x + w, y0 + h], outline=LINE, width=2, fill=LIGHT)
d.text((x + 14, y0 + 12), "ALSO TODAY", font=font(BOLD, 18), fill=NAVY)
also = ("Colombia frees all hostages in a Cartagena supermarket siege. "
        "Sudan: RSF drone strikes kill 19 civilians. Houthis hit a "
        "Saudi refinery; 11 hurt in a Riyadh tower strike.")
yy = y0 + 40
for line in wrap(d, also, font(REG, 18), w - 28):
    d.text((x + 14, yy), line, font=font(REG, 18), fill=(40, 40, 40))
    yy += 23

d.text((28, 992), "Compiled from public news briefs  •  25 November 2026",
       font=font(REG, 14), fill=GREY)

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png")
