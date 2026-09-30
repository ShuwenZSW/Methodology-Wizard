#!/usr/bin/env python3
"""Generate Tiny Atlas brand assets: favicon PNGs + Open Graph share card."""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent

PAPER = (246, 241, 231)
PAPER_LIGHT = (255, 253, 247)
INK = (26, 23, 18)
MUTED = (111, 106, 94)
LINE = (221, 211, 191)
QUAL = (14, 125, 102)
QUANT = (58, 79, 208)
MIXED = (200, 80, 31)
GOLD = (184, 137, 46)

GEORGIA_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
HELVETICA = "/System/Library/Fonts/Helvetica.ttc"


def cubic(p0, p1, p2, p3, n=120):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def trail_colors(n):
    """gradient teal -> indigo -> terracotta sampled along the trail"""
    out = []
    for i in range(n):
        t = i / (n - 1)
        if t < 0.5:
            out.append(lerp(QUAL, QUANT, t * 2))
        else:
            out.append(lerp(QUANT, MIXED, (t - 0.5) * 2))
    return out


def draw_icon(size):
    """Tiny Atlas app icon: paper tile, dashed trail through three map nodes."""
    s = size
    img = Image.new("RGBA", (s * 4, s * 4), (0, 0, 0, 0))  # supersample
    d = ImageDraw.Draw(img)
    pad = s * 4 * 0.06
    d.rounded_rectangle([pad, pad, s * 4 - pad, s * 4 - pad], radius=s * 4 * 0.24,
                        fill=PAPER_LIGHT, outline=LINE, width=max(2, s * 4 // 90))

    # trail: bottom-left -> center -> top-right (bezier through two segments)
    p0, p1, p2, p3 = (0.25, 0.72), (0.46, 0.74), (0.38, 0.42), (0.50, 0.50)
    q0, q1, q2, q3 = (0.50, 0.50), (0.62, 0.58), (0.54, 0.26), (0.77, 0.27)
    S = s * 4
    pts = [(x * S, y * S) for x, y in cubic(p0, p1, p2, p3)[:-1]] + \
          [(x * S, y * S) for x, y in cubic(q0, q1, q2, q3)]
    cols = trail_colors(len(pts))
    step = max(1, len(pts) // 26)
    for i in range(0, len(pts), step):
        r = S * 0.016
        d.ellipse([pts[i][0] - r, pts[i][1] - r, pts[i][0] + r, pts[i][1] + r], fill=cols[i] + (255,))

    # nodes
    nodes = [(0.26, 0.70, QUAL), (0.50, 0.50, QUANT), (0.76, 0.28, MIXED)]
    for nx, ny, col in nodes:
        cx, cy = nx * S, ny * S
        if col == QUANT:  # hub node gets a gold ring
            rr = S * 0.088
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=GOLD, width=max(2, S // 110))
        r = S * 0.055
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (255,))
        hr = S * 0.018  # highlight
        d.ellipse([cx - r * 0.4 - hr, cy - r * 0.5 - hr, cx - r * 0.4 + hr, cy - r * 0.5 + hr],
                  fill=(255, 255, 255, 130))

    return img.resize((s, s), Image.LANCZOS)


def gradient_text(draw_img, xy, text, font, stops, anchor="la"):
    """Render text filled with a diagonal multi-stop gradient."""
    mask = Image.new("L", draw_img.size, 0)
    md = ImageDraw.Draw(mask)
    md.text(xy, text, font=font, fill=255, anchor=anchor)
    bbox = md.textbbox(xy, text, font=font, anchor=anchor)
    x0, y0, x1, y1 = bbox
    grad = Image.new("RGB", draw_img.size, stops[0][1])
    gd = ImageDraw.Draw(grad)
    n = stops[-1][0]
    for y in range(y0, y1 + 1):
        t = (y - y0) / max(1, y1 - y0) * n
        # find segment
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                col = lerp(c0, c1, (t - t0) / max(1e-6, t1 - t0))
                break
        else:
            col = stops[-1][1]
        gd.line([(x0, y), (x1, y)], fill=col)
    draw_img.paste(grad, (0, 0), mask)


def og_card():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ambient washes (like the site's body::before)
    washes = [
        (-200, -260, 700, (62, 79, 208, 22)),
        (800, -240, 640, (200, 80, 31, 20)),
        (330, 430, 620, (14, 125, 102, 20)),
    ]
    for cx, cy, r, col in washes:
        wash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wd = ImageDraw.Draw(wash)
        wd.ellipse([cx, cy, cx + r, cy + r], fill=col)
        wash = wash.filter(ImageFilter.GaussianBlur(120))
        img.paste(wash, (0, 0), wash)
    d = ImageDraw.Draw(img)

    # hairline frame
    d.rectangle([28, 28, W - 28, H - 28], outline=LINE, width=2)

    # kicker
    f_kick = ImageFont.truetype(HELVETICA, 24, index=0)
    d.text((90, 96), "R E G O V N E T   R E S E A R C H   G R O U P", font=f_kick, fill=MUTED)
    d.line([(90, 136), (252, 136)], fill=GOLD, width=3)

    # wordmark with gallery gradient
    f_title = ImageFont.truetype(GEORGIA_BOLD, 118)
    gradient_text(img, (86, 158), "Tiny Atlas", f_title,
                  [(0.0, QUAL), (0.45, QUANT), (0.8, MIXED), (1.0, GOLD)])

    # tagline
    f_tag = ImageFont.truetype(GEORGIA_ITALIC, 37)
    d.text((92, 332), "Small maps of big fields —", font=f_tag, fill=INK)
    d.text((92, 384), "every node is a rabbit hole.", font=f_tag, fill=INK)

    # footer chips
    f_chip = ImageFont.truetype(HELVETICA, 22, index=0)
    chips = [("METHODOLOGY", QUAL), ("PUBLIC ADMINISTRATION", QUANT), ("MORE MAPS COMING", MIXED)]
    x = 92
    for label, col in chips:
        tw = d.textlength(label, font=f_chip)
        d.rounded_rectangle([x, 500, x + tw + 36, 544], radius=22, outline=col, width=2)
        d.text((x + 18, 511), label, font=f_chip, fill=col)
        x += tw + 36 + 20

    # right-side mini atlas: trail through three nodes
    icon = draw_icon(340).convert("RGBA")
    img.paste(icon, (W - 470, H // 2 - 170), icon)

    img.save(ROOT / "og-cover.png", optimize=True)


def favicons():
    draw_icon(180).save(ROOT / "apple-touch-icon.png")
    draw_icon(32).save(ROOT / "favicon-32.png")
    draw_icon(16).save(ROOT / "favicon-16.png")


if __name__ == "__main__":
    og_card()
    favicons()
    print("done")
