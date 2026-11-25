#!/usr/bin/env python3
"""Draw 'Tuesday 24 November 2026' as a vertical 24-hour timeline.

Original artwork for the make.fun news-image-20261124 competition.
All shapes, icons and text are drawn here with Pillow; no external
images, fonts beyond system DejaVu, or network access are used.
Output: entry.png, 1024x1024, well under 1 MiB.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

# --- palette: deep ink navy, warm paper, one accent per story family ---
INK      = (16, 24, 40)
PAPER    = (247, 243, 234)
CARD     = (255, 255, 255)
MUTED    = (90, 100, 118)
GOLD     = (201, 162, 39)
SPINE    = (201, 162, 39)
RED      = (178, 44, 36)
TEAL     = (18, 120, 110)
BLUE     = (36, 84, 160)
ORANGE   = (196, 96, 20)
PURPLE   = (104, 68, 150)
GREEN    = (46, 125, 60)
BROWN    = (120, 72, 32)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

# --- the day's verified stories, in UTC order ---
# Times are first-reported times (UTC) from the day's reporting.
EVENTS = [
    dict(time="01:32", color=ORANGE, tag="NEPAL",
         head="Magnitude 5.6 quake hits eastern Nepal",
         sub="Epicentre Olangchung Gola, by the Tibet border; felt across the region.",
         icon="quake"),
    dict(time="14:27", color=RED, tag="SAUDI ARABIA",
         head="Drone attack hits Riyadh finance-district tower",
         sub="At least 11 wounded in the King Abdullah Financial District.",
         icon="tower"),
    dict(time="15:47", color=GOLD, tag="SPORT",
         head="Senegal get the Africa Cup title back",
         sub="Sports court upholds Senegal's appeal; the 1-0 final win stands.",
         icon="trophy"),
    dict(time="16:51", color=RED, tag="YEMEN",
         head="Houthis 60 km from Aden, 'ready to attack'",
         sub="Yemen's military warns the rebels are closing on the capital.",
         icon="advance"),
    dict(time="17:35", color=PURPLE, tag="COLOMBIA",
         head="Gunmen hold 25 hostage in Cartagena shop",
         sub="Armed men seize a supermarket; the president confirms the siege.",
         icon="shop"),
    dict(time="18:58", color=TEAL, tag="STRAIT OF HORMUZ",
         head="Iran's Guards say they hit a container ship",
         sub="IRGC says it hit a ship; four tankers earlier reported mined.",
         icon="ship"),
    dict(time="19:52", color=BROWN, tag="T\u00dcRKIYE",
         head="Air Force helicopter crash kills five",
         sub="AS-532 comes down after take-off from Eskisehir on training.",
         icon="heli"),
    dict(time="20:41", color=BLUE, tag="UNITED STATES",
         head="Huawei guilty of trade-secret theft, bank fraud",
         sub="US jury convicts the tech giant — but clears it of racketeering.",
         icon="gavel"),
]

def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

# --- small pictogram icons, drawn with primitives inside a 44x44 box ---
def icon_quake(d, x, y, c):
    d.line([(x+4, y+34), (x+14, y+22), (x+20, y+30), (x+28, y+14), (x+40, y+26)],
           fill=c, width=4)
    d.ellipse([x+16, y+4, x+28, y+16], outline=c, width=3)

def icon_tower(d, x, y, c):
    d.rectangle([x+16, y+10, x+28, y+40], fill=c)
    for yy in (y + 16, y + 23, y + 30):
        d.line([(x+19, yy), (x+25, yy)], fill=PAPER, width=2)
    d.line([(x+6, y+6), (x+12, y+12)], fill=c, width=3)
    d.line([(x+38, y+6), (x+32, y+12)], fill=c, width=3)
    d.line([(x+22, y+2), (x+22, y+10)], fill=c, width=3)

def icon_trophy(d, x, y, c):
    d.polygon([(x+14, y+8), (x+30, y+8), (x+27, y+26), (x+17, y+26)], fill=c)
    d.arc([x+6, y+8, x+16, y+22], 90, 270, fill=c, width=3)
    d.arc([x+28, y+8, x+38, y+22], 270, 90, fill=c, width=3)
    d.rectangle([x+20, y+26, x+24, y+34], fill=c)
    d.rectangle([x+14, y+34, x+30, y+39], fill=c)

def icon_advance(d, x, y, c):
    d.polygon([(x+6, y+22), (x+26, y+22), (x+26, y+12), (x+40, y+24),
               (x+26, y+36), (x+26, y+26), (x+6, y+26)], fill=c)
    d.line([(x+6, y+34), (x+38, y+34)], fill=c, width=3)

def icon_shop(d, x, y, c):
    d.polygon([(x+6, y+14), (x+38, y+14), (x+34, y+24), (x+10, y+24)], fill=c)
    d.rectangle([x+9, y+24, x+35, y+40], outline=c, width=3)
    d.line([(x+22, y+28), (x+22, y+40)], fill=c, width=3)

def icon_ship(d, x, y, c):
    d.polygon([(x+8, y+26), (x+36, y+26), (x+31, y+36), (x+13, y+36)], fill=c)
    d.rectangle([x+14, y+14, x+26, y+26], fill=c)
    d.line([(x+20, y+6), (x+20, y+14)], fill=c, width=3)
    d.line([(x+20, y+6), (x+30, y+10), (x+20, y+14)], fill=c, width=2)

def icon_heli(d, x, y, c):
    d.line([(x+4, y+12), (x+40, y+12)], fill=c, width=3)
    d.ellipse([x+12, y+16, x+30, y+30], fill=c)
    d.line([(x+30, y+22), (x+40, y+18)], fill=c, width=3)
    d.line([(x+16, y+30), (x+14, y+38), (x+28, y+38)], fill=c, width=3)

def icon_gavel(d, x, y, c):
    d.line([(x+10, y+34), (x+34, y+10)], fill=c, width=4)
    d.rectangle([x+6, y+28, x+16, y+38], fill=c)
    d.rectangle([x+28, y+6, x+38, y+16], fill=c)
    d.line([(x+8, y+40), (x+36, y+40)], fill=c, width=3)

ICONS = dict(quake=icon_quake, tower=icon_tower, trophy=icon_trophy,
             advance=icon_advance, shop=icon_shop, ship=icon_ship,
             heli=icon_heli, gavel=icon_gavel)

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- header band: the day, named in full ---
    d.rectangle([0, 0, W, 148], fill=INK)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    f_day = font(FONT_B, 52)
    f_sub = font(FONT_R, 24)
    d.text((48, 26), "TUESDAY 24 NOVEMBER 2026", font=f_day, fill=(255, 255, 255))
    d.text((48, 96), "The world in one day \u2014 hour by hour, all times UTC",
           font=f_sub, fill=(200, 205, 215))

    # --- timeline spine ---
    top, bottom = 196, 948
    spine_x = 148
    d.line([(spine_x, top), (spine_x, bottom)], fill=SPINE, width=5)
    d.text((44, top - 30), "00:00", font=font(FONT_B, 19), fill=MUTED)
    d.text((44, bottom - 6), "24:00", font=font(FONT_B, 19), fill=MUTED)

    f_time = font(FONT_B, 30)
    f_tag = font(FONT_B, 19)
    f_head = font(FONT_B, 27)
    f_sub2 = font(FONT_R, 20)

    # rows in chronological order, evenly spaced so no two cards collide;
    # each row's time badge gives its exact time of day (UTC)
    n = len(EVENTS)
    step = (bottom - top - 80) / max(n - 1, 1)

    for i, ev in enumerate(EVENTS):
        y = top + 40 + i * step
        c = ev["color"]
        # node on the spine
        d.ellipse([spine_x - 27, y - 27, spine_x + 27, y + 27], fill=c,
                  outline=PAPER, width=3)
        ICONS[ev["icon"]](d, spine_x - 22, y - 22, PAPER)
        # time badge
        d.text((16, y - 15), ev["time"], font=f_time, fill=c)
        # white card
        card_x0, card_x1 = 196, 984
        card_y0, card_y1 = y - 42, y + 42
        d.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=12,
                            fill=CARD, outline=(225, 220, 208), width=2)
        d.rectangle([card_x0, card_y0, card_x0 + 8, card_y1], fill=c)
        d.text((card_x0 + 22, card_y0 + 8), ev["tag"], font=f_tag, fill=c)
        d.text((card_x0 + 22, card_y0 + 30), ev["head"], font=f_head, fill=INK)
        sub = ev["sub"]
        if d.textlength(sub, font=f_sub2) > card_x1 - card_x0 - 44:
            sub = sub[:78].rsplit(" ", 1)[0] + "\u2026"
        d.text((card_x0 + 22, card_y0 + 58), sub, font=f_sub2, fill=MUTED)

    # --- footer ---
    d.text((48, 968), "All times UTC. Events reported on Tuesday 24 November 2026.",
           font=font(FONT_R, 19), fill=MUTED)
    d.text((700, 968), "8 stories \u00b7 6 regions", font=font(FONT_B, 19), fill=MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
