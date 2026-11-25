#!/usr/bin/env python3
"""Render the news-image-20261124 front page (1024x1024, <=1 MiB).

Build-time tooling only: written by hand in this session, run locally to
produce entry.png. The graded program (main.ts) only copies entry.png.
Flat vector illustrations drawn in code; real TTF fonts (DejaVu).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 239, 221)
CARD = (255, 253, 244)
INK = (25, 23, 19)
RED = (179, 39, 30)
NAVY = (27, 42, 74)
GREY = (90, 84, 72)
RULE = (180, 168, 140)
GOLD = (200, 162, 74)

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)

SERIF_B = lambda s: F("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: F("DejaVuSerif.ttf", s)
SANS_B = lambda s: F("DejaVuSans-Bold.ttf", s)
SANS = lambda s: F("DejaVuSans.ttf", s)

# ---------------------------------------------------------------- stories
# tag: CONFIRMED (2+ outlets) / OFFICIAL (on the record) / REPORTED (1 outlet)
#      / CLAIM (one side's claim).  All headlines/briefs in our own words.
LEADS = [
    dict(n=1, region="NORTH AMERICA", place="NEW YORK, USA", tag="CONFIRMED",
         tagcol=(46, 125, 60), scene="court",
         kicker="TECH \u00b7 LAW",
         head="Huawei guilty of trade theft and bank fraud",
         body="A US jury convicts the telecom giant on 10 of 12 counts, but clears "
              "it of racketeering. Sentencing is set for September 2027.",
         source="Reuters \u00b7 AP", lat=40.7, lon=-74.0),
    dict(n=2, region="MIDDLE EAST", place="STRAIT OF HORMUZ", tag="CLAIM",
         tagcol=(200, 140, 20), scene="tanker",
         kicker="ENERGY \u00b7 SHIPPING",
         head="Four tankers reported hit by mines in the Strait of Hormuz",
         body="Iran says four tankers struck mines and caught fire. Separately, "
              "its Guards say they attacked a container ship. A maritime centre "
              "calls both claims unconfirmed.",
         source="Reuters \u00b7 AP", lat=26.5, lon=56.0),
    dict(n=3, region="EUROPE", place="GULF OF FINLAND", tag="CONFIRMED",
         tagcol=(46, 125, 60), scene="shipstrike",
         kicker="WAR \u00b7 UKRAINE",
         head="Ukraine hits Russian ships in Gulf of Finland and off Libya",
         body="Kyiv says drones hit the cargo ship Sparta II in the Gulf of Finland "
              "and two Russian ships off Libya, as Poland accuses Russia of a new "
              "airspace breach.",
         source="Reuters \u00b7 Kyiv Independent", lat=59.8, lon=24.0),
]

MEDIUMS = [
    dict(n=4, region="AFRICA", place="LAUSANNE", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="trophy", kicker="SPORT \u00b7 FOOTBALL",
         head="Senegal champions again, title restored",
         body="Court overturns the award to Morocco, which vows a challenge.",
         source="Reuters \u00b7 AP", lat=46.5, lon=6.6),
    dict(n=5, region="MIDDLE EAST", place="RIYADH", tag="REPORTED",
         tagcol=(90, 84, 72), scene="tower", kicker="CONFLICT \u00b7 SAUDI ARABIA",
         head="Drone hits PIF tower; 11 wounded",
         body="Suspected Houthi strike on the fund's HQ; second hit in a week.",
         source="Saudi authorities \u00b7 Reuters", lat=24.7, lon=46.7),
    dict(n=6, region="MIDDLE EAST", place="ADEN, YEMEN", tag="CLAIM",
         tagcol=(200, 140, 20), scene="desert", kicker="WAR \u00b7 YEMEN",
         head="Houthis 60 km from Aden, ready to attack",
         body="Army says fighters near the temporary capital; defences built.",
         source="Yemen military \u00b7 Reuters", lat=12.8, lon=45.0),
    dict(n=7, region="LATIN AMERICA", place="CARTAGENA, COLOMBIA", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="market", kicker="CRIME \u00b7 COLOMBIA",
         head="25 hostages seized at a Cartagena supermarket",
         body="Gunmen hold shoppers for hours; five older women freed.",
         source="President de la Espriella \u00b7 AP", lat=10.4, lon=-75.5),
    dict(n=8, region="MIDDLE EAST", place="GAZA CITY", tag="CONFIRMED",
         tagcol=(46, 125, 60), scene="blast", kicker="CONFLICT \u00b7 GAZA",
         head="Israel kills Hamas security chief",
         body="Hamas security chief Naeem Abu Nahel and six others die.",
         source="Gaza officials \u00b7 Reuters", lat=31.5, lon=34.5),
    dict(n=9, region="ASIA", place="ESKISEHIR, T\u00dcRKIYE", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="heli", kicker="DISASTER \u00b7 T\u00dcRKIYE",
         head="Turkish helicopter crash kills five crew",
         body="Helicopter falls after take-off; second such crash in 12 days.",
         source="Defence Ministry \u00b7 AFP", lat=39.8, lon=30.5),
    dict(n=10, region="MIDDLE EAST", place="BAGHDAD, IRAQ", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="oil", kicker="POLITICS \u00b7 IRAQ",
         head="Iraq orders federal control of oilfields",
         body="Baghdad to run Kurdish oilfields and crossings; Erbil objects.",
         source="Reuters \u00b7 AP", lat=33.3, lon=44.4),
    dict(n=11, region="SOUTH ASIA", place="DHAKA, BANGLADESH", tag="CLAIM",
         tagcol=(200, 140, 20), scene="plane", kicker="POLITICS \u00b7 BANGLADESH",
         head="Exiled ex-PM Hasina to return 16 Dec",
         body="Hasina to fly home for Victory Day; Dhaka demands extradition.",
         source="Hasina spokesperson \u00b7 Reuters", lat=23.8, lon=90.4),
    dict(n=12, region="OCEANIA", place="CARRARA, AUSTRALIA", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="cricket", kicker="SPORT \u00b7 CRICKET",
         head="England level T20 series with eight-wicket rout",
         body="England chase 184 in 13.1 overs; the series stands at 1\u20131.",
         source="ESPNcricinfo", lat=-28.0, lon=153.4),
    dict(n=13, region="EUROPE", place="OSLO, NORWAY", tag="OFFICIAL",
         tagcol=(46, 104, 158), scene="aid", kicker="AID \u00b7 UKRAINE WAR",
         head="Norway pledges $7bn Ukraine aid for 2027",
         body="Oslo commits $7bn+ for 2027; Kyiv seeks \u20ac115bn more.",
         source="Reuters \u00b7 AP", lat=59.9, lon=10.7),
]

ALSO = [
    (14, "Car bomb injures 23 in Villavicencio, Colombia"),
    (15, "Saudi strikes on Yemen buses: 25 dead or missing"),
    (16, "Gaza meningitis alert: 272 cases in October"),
    (17, "DR Congo hunts missing plane; rebels claim hit"),
    (18, "Hanoi restaurant blast kills six; gas suspected"),
    (19, "Malaysia to return thousands of migrants to Myanmar"),
    (20, "South Korea shelters Ulleungdo as Russian jets near"),
    (21, "Indonesia names two to replace VP Gibran"),
    (22, "China death sentence for official who spied"),
    (23, "NATO vows to defend space from new threats"),
    (24, "US drone helped capture \u2018El Chapo Isidro\u2019"),
    (25, "Bukele names three soldiers killed in Haiti"),
    (26, "Pentagon rebukes Canada over defence gaps"),
    (27, "US blacklists Megaspeed in Nvidia chip scandal"),
    (28, "Zelensky urges four-party peace talks soon"),
    (29, "Sooryavanshi smashes 204 off 53 balls for India A"),
    (30, "Ukraine needs \u20ac115bn outside help in 2027"),
    (31, "Germany first into Ukraine\u2019s Delta war system"),
    (32, "Moldova: seven Russian drones crossed airspace"),
    (33, "UK sanctions Yemen\u2019s Houthis, four officials"),
]

NUMBERS = [
    ("4", "tankers reported hit by mines in the Strait of Hormuz"),
    ("10 of 12", "counts on which a US jury convicted Huawei"),
    ("25", "hostages seized at a supermarket in Cartagena"),
    ("$7bn", "Norway\u2019s Ukraine aid pledge for 2027"),
    ("60 km", "how close Houthi fighters are to Aden"),
    ("\u20ac115bn", "outside help Ukraine says it needs in 2027"),
]

REGIONS = [
    ("N. AMERICA", 2, (51, 104, 158)),
    ("LATIN AMERICA", 4, (62, 142, 90)),
    ("EUROPE", 7, (108, 75, 158)),
    ("MIDDLE EAST", 8, (179, 39, 30)),
    ("AFRICA", 2, (208, 124, 31)),
    ("ASIA", 9, (31, 122, 110)),
    ("OCEANIA", 1, (138, 123, 45)),
]

TIMELINE = [
    ("00:00", "Iran: four tankers hit mines in Hormuz"),
    ("02:15", "NATO vows to defend space"),
    ("08:14", "Ukraine hits Russian ships at sea"),
    ("11:40", "Israel kills Hamas security chief"),
    ("14:27", "Drone hits PIF tower in Riyadh"),
    ("17:35", "Gunmen seize Cartagena supermarket"),
    ("20:41", "US jury convicts Huawei"),
]

DATECHECK_OUT = [
    "ICJ Myanmar ruling (19 Nov)", "COP31 collapse (22 Nov)",
    "Russia barrage (21\u201322 Nov)", "\u2018El Chapo\u2019 capture (weekend)",
    "Las Vegas GP \u00b7 ATP Finals (22 Nov)", "Peru quake (20 Nov)",
]
DATECHECK_NOTYET = [
    "Huawei sentencing (Sept 2027)", "Hasina return (16 Dec)",
    "Morocco CAS challenge (not filed)", "Hormuz claims (unconfirmed)",
]

# ---------------------------------------------------------------- helpers
def wrap(d, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(d, x, y, lines, font, fill, lh=None):
    lh = lh or int(font.size * 1.22)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def chip(d, x, y, text, font, fg, bg):
    w = int(d.textlength(text, font=font)) + 10
    h = font.size + 7
    d.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=bg)
    d.text((x + 5, y + 3), text, font=font, fill=fg)
    return w

def num_badge(d, cx, cy, n, r=10):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(255, 255, 255), width=1)
    f = SANS_B(11 if n < 10 else 9)
    tw = d.textlength(str(n), font=f)
    d.text((cx - tw / 2, cy - f.size / 2 - 1), str(n), font=f, fill=(255, 255, 255))

# ---------------------------------------------------------------- scenes
def scene(d, kind, x, y, w, h):
    """Flat vector illustration inside box (x, y, w, h). All coords scaled."""
    X = lambda f: x + f * w
    Y = lambda f: y + f * h
    if kind == "court":
        d.rectangle([x, y, x + w, y + h], fill=(217, 228, 236))
        d.rectangle([x, Y(0.66), x + w, y + h], fill=(196, 178, 140))
        d.rectangle([X(0.10), Y(0.34), X(0.90), Y(0.66)], fill=(250, 248, 240))
        d.polygon([(X(0.06), Y(0.34)), (X(0.50), Y(0.12)), (X(0.94), Y(0.34))], fill=(179, 39, 30))
        d.ellipse([X(0.46), Y(0.20), X(0.54), Y(0.30)], fill=(250, 248, 240))
        for i in range(5):
            cx = X(0.20 + i * 0.15)
            d.rectangle([cx - w * 0.025, Y(0.36), cx + w * 0.025, Y(0.64)], fill=(120, 110, 90))
        d.rectangle([X(0.10), Y(0.64), X(0.90), Y(0.70)], fill=(120, 110, 90))
        d.rectangle([X(0.06), Y(0.70), X(0.94), Y(0.76)], fill=(150, 138, 110))
        d.rectangle([X(0.02), Y(0.76), X(0.98), Y(0.82)], fill=(170, 158, 128))
        d.rectangle([X(0.40), Y(0.44), X(0.60), Y(0.64)], fill=(27, 42, 74))
    elif kind == "tanker":
        d.rectangle([x, y, x + w, y + h], fill=(232, 217, 176))
        d.rectangle([x, Y(0.55), x + w, y + h], fill=(46, 94, 140))
        d.rectangle([X(0.10), Y(0.42), X(0.86), Y(0.58)], fill=(40, 40, 44))
        d.rectangle([X(0.14), Y(0.30), X(0.30), Y(0.42)], fill=(179, 39, 30))
        d.rectangle([X(0.34), Y(0.34), X(0.50), Y(0.42)], fill=(200, 162, 74))
        d.rectangle([X(0.54), Y(0.32), X(0.70), Y(0.42)], fill=(90, 120, 90))
        d.rectangle([X(0.72), Y(0.26), X(0.78), Y(0.42)], fill=(220, 220, 210))
        for ang in range(0, 360, 45):
            import math
            a = math.radians(ang)
            d.line([X(0.88) + math.cos(a) * w * 0.02, Y(0.30) + math.sin(a) * h * 0.05,
                    X(0.88) + math.cos(a) * w * 0.09, Y(0.30) + math.sin(a) * h * 0.16],
                   fill=(232, 120, 30), width=3)
        d.ellipse([X(0.84), Y(0.22), X(0.92), Y(0.38)], fill=(232, 120, 30))
        d.arc([X(0.05), Y(0.60), X(0.25), Y(0.80)], 200, 340, fill=(255, 255, 255), width=2)
        d.arc([X(0.55), Y(0.62), X(0.75), Y(0.82)], 200, 340, fill=(255, 255, 255), width=2)
    elif kind == "shipstrike":
        d.rectangle([x, y, x + w, y + h], fill=(24, 32, 54))
        for i in range(6):
            d.ellipse([X(0.05 + i * 0.16), Y(0.08 + (i % 2) * 0.07),
                       X(0.12 + i * 0.16), Y(0.15 + (i % 2) * 0.07)], fill=(200, 162, 74))
        d.rectangle([x, Y(0.60), x + w, y + h], fill=(38, 68, 110))
        d.rectangle([X(0.06), Y(0.46), X(0.88), Y(0.62)], fill=(20, 20, 24))
        d.rectangle([X(0.14), Y(0.32), X(0.28), Y(0.46)], fill=(60, 60, 66))
        d.line([X(0.21), Y(0.32), X(0.21), Y(0.20)], fill=(60, 60, 66), width=3)
        d.ellipse([X(0.30), Y(0.36), X(0.36), Y(0.44)], fill=(180, 220, 240))
        d.ellipse([X(0.90), Y(0.34), X(0.97), Y(0.43)], fill=(232, 120, 30))
        d.line([X(0.93), Y(0.34), X(0.93), Y(0.18)], fill=(232, 120, 30), width=3)
        d.line([X(0.89), Y(0.18), X(0.97), Y(0.18)], fill=(232, 120, 30), width=3)
        d.arc([X(0.74), Y(0.58), X(0.98), Y(0.98)], 180, 360, fill=(255, 255, 255), width=3)
        d.arc([X(0.06), Y(0.62), X(0.24), Y(0.86)], 180, 360, fill=(255, 255, 255), width=2)
    elif kind == "trophy":
        d.rectangle([x, y, x + w, y + h], fill=(62, 142, 90))
        d.rectangle([x, Y(0.70), x + w, y + h], fill=(46, 110, 70))
        d.line([x, Y(0.70), x + w, Y(0.70)], fill=(255, 255, 255), width=2)
        d.polygon([(X(0.38), Y(0.18)), (X(0.62), Y(0.18)), (X(0.58), Y(0.42)), (X(0.42), Y(0.42))], fill=(232, 190, 60))
        d.rectangle([X(0.46), Y(0.42), X(0.54), Y(0.58)], fill=(232, 190, 60))
        d.rectangle([X(0.38), Y(0.58), X(0.62), Y(0.64)], fill=(232, 190, 60))
        d.arc([X(0.30), Y(0.20), X(0.40), Y(0.38)], 90, 270, fill=(232, 190, 60), width=4)
        d.arc([X(0.60), Y(0.20), X(0.70), Y(0.38)], 270, 90, fill=(232, 190, 60), width=4)
        for cx, cy, c in [(0.2, 0.2, RED), (0.8, 0.15, (255, 255, 255)), (0.15, 0.45, (232, 190, 60)),
                          (0.85, 0.5, RED), (0.7, 0.75, (255, 255, 255)), (0.3, 0.8, RED)]:
            d.ellipse([X(cx) - 3, Y(cy) - 3, X(cx) + 3, Y(cy) + 3], fill=c)
    elif kind == "tower":
        d.rectangle([x, y, x + w, y + h], fill=(232, 176, 75))
        d.rectangle([x, Y(0.68), x + w, y + h], fill=(90, 80, 70))
        d.rectangle([X(0.38), Y(0.18), X(0.62), Y(0.78)], fill=(27, 42, 74))
        d.polygon([(X(0.38), Y(0.18)), (X(0.50), Y(0.08)), (X(0.62), Y(0.18))], fill=(27, 42, 74))
        for r in range(4):
            for c in range(2):
                d.rectangle([X(0.42 + c * 0.09), Y(0.26 + r * 0.12), X(0.47 + c * 0.09), Y(0.33 + r * 0.12)],
                            fill=(232, 190, 60))
        d.ellipse([X(0.68), Y(0.30), X(0.78), Y(0.44)], fill=(150, 150, 150))
        d.ellipse([X(0.72), Y(0.22), X(0.84), Y(0.38)], fill=(170, 170, 170))
        d.rectangle([X(0.20), Y(0.45), X(0.32), Y(0.78)], fill=(60, 60, 66))
        d.rectangle([X(0.68), Y(0.52), X(0.80), Y(0.78)], fill=(60, 60, 66))
    elif kind == "desert":
        d.rectangle([x, y, x + w, y + h], fill=(238, 214, 150))
        d.ellipse([X(0.78), Y(0.10), X(0.92), Y(0.28)], fill=(232, 190, 60))
        d.polygon([(x, Y(0.72)), (X(0.35), Y(0.48)), (X(0.70), Y(0.72)), (x, y + h)], fill=(224, 192, 120))
        d.polygon([(X(0.45), Y(0.78)), (X(0.75), Y(0.55)), (x + w, Y(0.78)), (x + w, y + h)], fill=(210, 172, 100))
        d.line([X(0.12), Y(0.62), X(0.42), Y(0.62)], fill=RED, width=4)
        d.polygon([(X(0.42), Y(0.62)), (X(0.34), Y(0.56)), (X(0.34), Y(0.68))], fill=RED)
        d.rectangle([X(0.60), Y(0.30), X(0.63), Y(0.52)], fill=(90, 80, 70))
        d.polygon([(X(0.63), Y(0.30)), (X(0.76), Y(0.35)), (X(0.63), Y(0.40))], fill=RED)
    elif kind == "market":
        d.rectangle([x, y, x + w, y + h], fill=(214, 228, 238))
        d.rectangle([X(0.14), Y(0.34), X(0.86), Y(0.82)], fill=(250, 248, 240))
        for i in range(6):
            c = RED if i % 2 == 0 else (255, 255, 255)
            d.polygon([(X(0.14 + i * 0.12), Y(0.34)), (X(0.26 + i * 0.12), Y(0.34)),
                       (X(0.23 + i * 0.12), Y(0.48)), (X(0.17 + i * 0.12), Y(0.48))], fill=c)
        d.rectangle([X(0.42), Y(0.58), X(0.58), Y(0.82)], fill=(90, 70, 60))
        d.rectangle([X(0.20), Y(0.56), X(0.34), Y(0.70)], fill=(120, 180, 220))
        d.rectangle([X(0.66), Y(0.56), X(0.80), Y(0.70)], fill=(120, 180, 220))
        d.rectangle([X(0.30), Y(0.14), X(0.70), Y(0.28)], fill=NAVY)
        d.text((X(0.34), Y(0.16)), "SHOP", font=SANS_B(int(h * 0.12)), fill=(255, 255, 255))
    elif kind == "blast":
        d.rectangle([x, y, x + w, y + h], fill=(200, 196, 188))
        d.rectangle([X(0.08), Y(0.40), X(0.30), Y(0.82)], fill=(120, 118, 112))
        d.rectangle([X(0.34), Y(0.30), X(0.56), Y(0.82)], fill=(140, 138, 130))
        d.rectangle([X(0.60), Y(0.48), X(0.82), Y(0.82)], fill=(120, 118, 112))
        for bx, by in [(0.14, 0.48), (0.40, 0.38), (0.66, 0.56)]:
            d.rectangle([X(bx), Y(by), X(bx + 0.06), Y(by + 0.08)], fill=(60, 58, 54))
        import math
        cx, cy = X(0.72), Y(0.30)
        for k in range(8):
            a = math.radians(k * 45)
            d.line([cx + math.cos(a) * w * 0.03, cy + math.sin(a) * h * 0.06,
                    cx + math.cos(a) * w * 0.11, cy + math.sin(a) * h * 0.20],
                   fill=(232, 120, 30), width=4)
        d.ellipse([cx - w * 0.05, cy - h * 0.08, cx + w * 0.05, cy + h * 0.08], fill=(232, 120, 30))
        d.ellipse([X(0.18), Y(0.18), X(0.30), Y(0.32)], fill=(150, 150, 150))
    elif kind == "heli":
        d.rectangle([x, y, x + w, y + h], fill=(191, 211, 224))
        d.polygon([(x, Y(0.75)), (X(0.40), Y(0.55)), (X(0.75), Y(0.75)), (x, y + h)], fill=(110, 160, 110))
        d.polygon([(X(0.55), Y(0.80)), (X(0.85), Y(0.60)), (x + w, Y(0.80)), (x + w, y + h)], fill=(90, 140, 95))
        d.ellipse([X(0.30), Y(0.30), X(0.52), Y(0.52)], fill=(60, 60, 66))
        d.rectangle([X(0.52), Y(0.38), X(0.78), Y(0.44)], fill=(60, 60, 66))
        d.polygon([(X(0.78), Y(0.36)), (X(0.88), Y(0.32)), (X(0.88), Y(0.48)), (X(0.78), Y(0.46))], fill=(60, 60, 66))
        d.line([X(0.18), Y(0.28), X(0.64), Y(0.28)], fill=(40, 40, 44), width=3)
        d.line([X(0.41), Y(0.30), X(0.41), Y(0.52)], fill=(60, 60, 66), width=3)
        d.ellipse([X(0.34), Y(0.36), X(0.42), Y(0.44)], fill=(180, 220, 240))
        d.ellipse([X(0.80), Y(0.72), X(0.88), Y(0.82)], fill=(232, 120, 30))
    elif kind == "oil":
        d.rectangle([x, y, x + w, y + h], fill=(232, 220, 192))
        d.rectangle([x, Y(0.70), x + w, y + h], fill=(196, 178, 140))
        d.line([X(0.30), Y(0.72), X(0.48), Y(0.18)], fill=(40, 40, 44), width=4)
        d.line([X(0.66), Y(0.72), X(0.48), Y(0.18)], fill=(40, 40, 44), width=4)
        d.line([X(0.36), Y(0.55), X(0.60), Y(0.55)], fill=(40, 40, 44), width=3)
        d.line([X(0.41), Y(0.40), X(0.55), Y(0.40)], fill=(40, 40, 44), width=3)
        d.line([X(0.48), Y(0.18), X(0.62), Y(0.30)], fill=(40, 40, 44), width=3)
        d.ellipse([X(0.74), Y(0.42), X(0.82), Y(0.54)], fill=(232, 120, 30))
        d.ellipse([X(0.76), Y(0.46), X(0.80), Y(0.52)], fill=(232, 190, 60))
        d.rectangle([X(0.12), Y(0.62), X(0.24), Y(0.72)], fill=(90, 80, 70))
    elif kind == "plane":
        d.rectangle([x, y, x + w, y + h], fill=(207, 224, 234))
        for cx, cy in [(0.18, 0.20), (0.82, 0.16), (0.65, 0.30)]:
            d.ellipse([X(cx), Y(cy), X(cx + 0.12), Y(cy + 0.10)], fill=(255, 255, 255))
        d.polygon([(X(0.20), Y(0.48)), (X(0.55), Y(0.44)), (X(0.80), Y(0.52)), (X(0.55), Y(0.58)),
                   (X(0.20), Y(0.56))], fill=(250, 248, 240))
        d.polygon([(X(0.42), Y(0.44)), (X(0.48), Y(0.30)), (X(0.54), Y(0.44))], fill=(179, 39, 30))
        d.polygon([(X(0.42), Y(0.58)), (X(0.46), Y(0.70)), (X(0.52), Y(0.58))], fill=(179, 39, 30))
        d.arc([X(0.15), Y(0.62), X(0.85), Y(0.92)], 180, 360, fill=RED, width=3)
        d.polygon([(X(0.82), Y(0.62)), (X(0.74), Y(0.58)), (X(0.74), Y(0.68))], fill=RED)
    elif kind == "cricket":
        d.rectangle([x, y, x + w, y + h], fill=(120, 170, 110))
        d.rectangle([X(0.30), Y(0.30), X(0.70), Y(0.85)], fill=(210, 190, 140))
        for i in range(3):
            d.rectangle([X(0.42 + i * 0.06), Y(0.32), X(0.45 + i * 0.06), Y(0.52)], fill=(232, 190, 60))
        d.rectangle([X(0.40), Y(0.30), X(0.60), Y(0.33)], fill=(232, 190, 60))
        d.line([X(0.22), Y(0.72), X(0.34), Y(0.55)], fill=(150, 110, 60), width=5)
        d.rectangle([X(0.30), Y(0.48), X(0.38), Y(0.58)], fill=(150, 110, 60))
        d.ellipse([X(0.68), Y(0.60), X(0.74), Y(0.68)], fill=RED)
        d.arc([X(0.10), Y(0.70), X(0.30), Y(0.90)], 270, 360, fill=(255, 255, 255), width=2)
    elif kind == "bat":
        d.rectangle([x, y, x + w, y + h], fill=(120, 170, 110))
        d.rectangle([X(0.30), Y(0.28), X(0.70), Y(0.85)], fill=(210, 190, 140))
        d.ellipse([X(0.44), Y(0.30), X(0.52), Y(0.38)], fill=(240, 210, 170))
        d.line([X(0.48), Y(0.38), X(0.48), Y(0.58)], fill=(60, 50, 40), width=3)
        d.line([X(0.48), Y(0.58), X(0.62), Y(0.72)], fill=(60, 50, 40), width=3)
        d.line([X(0.62), Y(0.72), X(0.72), Y(0.80)], fill=(150, 110, 60), width=5)
        d.ellipse([X(0.76), Y(0.22), X(0.84), Y(0.32)], fill=RED)
        d.arc([X(0.60), Y(0.30), X(0.90), Y(0.60)], 200, 330, fill=(255, 255, 255), width=2)
        d.arc([X(0.55), Y(0.38), X(0.85), Y(0.68)], 200, 330, fill=(255, 255, 255), width=2)
    elif kind == "aid":
        d.rectangle([x, y, x + w, y + h], fill=(207, 224, 234))
        for cx, cy in [(0.15, 0.75), (0.80, 0.70)]:
            d.ellipse([X(cx), Y(cy), X(cx + 0.14), Y(cy + 0.10)], fill=(255, 255, 255))
        d.pieslice([X(0.30), Y(0.10), X(0.70), Y(0.42)], 180, 360, fill=(179, 39, 30))
        d.line([X(0.32), Y(0.26), X(0.46), Y(0.58)], fill=(60, 50, 40), width=2)
        d.line([X(0.68), Y(0.26), X(0.54), Y(0.58)], fill=(60, 50, 40), width=2)
        d.rectangle([X(0.42), Y(0.58), X(0.58), Y(0.78)], fill=(150, 110, 60))
        d.line([X(0.50), Y(0.58), X(0.50), Y(0.78)], fill=(90, 60, 30), width=2)
        d.rectangle([X(0.46), Y(0.63), X(0.54), Y(0.73)], fill=(255, 255, 255))
        d.rectangle([X(0.488), Y(0.645), X(0.512), Y(0.715)], fill=(179, 39, 30))
        d.rectangle([X(0.472), Y(0.668), X(0.528), Y(0.692)], fill=(179, 39, 30))
    else:
        d.rectangle([x, y, x + w, y + h], fill=(220, 214, 196))

# ---------------------------------------------------------------- map
NA = [(-168,66),(-140,70),(-125,71),(-110,68),(-95,69),(-85,66),(-80,73),(-75,72),(-65,60),(-55,52),(-60,46),(-70,42),(-75,35),(-80,32),(-81,26),(-84,30),(-90,29),(-97,26),(-105,20),(-95,16),(-87,13),(-83,9),(-79,9),(-85,11),(-90,14),(-97,16),(-105,20),(-110,23),(-114,29),(-120,34),(-125,40),(-125,49),(-130,55),(-140,60),(-155,58),(-165,60),(-168,66)]
SA = [(-79,9),(-77,4),(-80,-3),(-81,-6),(-77,-12),(-72,-18),(-70,-23),(-70,-30),(-72,-37),(-73,-44),(-74,-50),(-70,-54),(-66,-55),(-68,-50),(-65,-45),(-62,-40),(-58,-35),(-52,-32),(-48,-28),(-41,-23),(-35,-9),(-35,-6),(-40,-3),(-44,-2),(-50,0),(-53,4),(-58,6),(-62,9),(-68,11),(-72,12),(-77,7),(-79,9)]
AF = [(-6,35),(-10,31),(-15,27),(-17,21),(-17,15),(-15,11),(-13,8),(-8,5),(-4,5),(0,6),(6,4),(9,4),(9,-1),(12,-6),(13,-12),(12,-18),(14,-22),(16,-29),(19,-34),(26,-34),(32,-29),(35,-24),(40,-16),(40,-10),(42,-4),(46,-1),(51,2),(51,11),(44,11),(40,15),(38,18),(37,22),(35,28),(32,31),(30,32),(22,33),(19,32),(11,34),(10,37),(5,37),(-1,35),(-6,35)]
EUAS = [(-10,36),(-9,43),(-2,44),(-1,46),(-4,48),(-2,50),(0,51),(3,53),(7,54),(8,57),(10,59),(5,60),(5,62),(12,65),(18,69),(25,71),(30,70),(35,68),(40,68),(45,68),(50,69),(55,68),(60,69),(68,73),(75,73),(80,73),(90,75),(100,77),(110,74),(120,73),(130,72),(140,72),(150,70),(158,69),(162,66),(170,66),(178,65),(178,62),(170,60),(162,60),(158,56),(156,51),(150,59),(142,50),(140,45),(135,43),(130,42),(127,40),(126,38),(122,37),(120,32),(121,28),(118,25),(110,21),(108,18),(105,10),(103,8),(100,7),(98,10),(94,16),(92,21),(89,22),(86,20),(80,16),(77,8),(75,12),(72,20),(68,23),(66,25),(62,25),(58,25),(56,26),(59,22),(58,20),(55,17),(52,15),(48,14),(44,13),(43,12),(40,15),(39,21),(38,24),(36,28),(35,29),(34,31),(33,35),(30,36),(27,37),(23,36),(22,37),(19,40),(18,42),(15,44),(12,44),(10,44),(8,44),(6,43),(3,43),(0,40),(-2,37),(-6,36),(-9,37),(-10,36)]
AU = [(113,-22),(114,-30),(115,-35),(118,-35),(124,-33),(129,-32),(132,-32),(135,-35),(138,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),(146,-19),(142,-15),(142,-11),(140,-17),(136,-15),(135,-12),(132,-11),(130,-13),(126,-14),(122,-17),(118,-20),(113,-22)]
UK = [(-5,50),(-3,53),(-5,56),(-3,58),(-1,57),(0,53),(1,51),(-3,50),(-5,50)]
JP = [(130,31),(132,33),(135,34),(137,35),(139,36),(140,38),(141,41),(142,44),(143,42),(141,39),(139,37),(136,35),(133,34),(131,32),(130,31)]
CONTINENTS = [NA, SA, AF, EUAS, AU, UK, JP]

def draw_map(d, x, y, w, h, stories):
    """Schematic world map with numbered story dots."""
    d.rectangle([x, y, x + w, y + h], fill=(215, 229, 238))
    def proj(lon, lat):
        return (x + (lon + 180) / 360.0 * w, y + (90 - lat) / 180.0 * h)
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=(239, 230, 200), outline=(150, 135, 105))
    pts = []
    for s in stories:
        px, py = proj(s["lon"], s["lat"])
        pts.append([px, py, s["n"]])
    for _ in range(3):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                dx, dy = pts[j][0] - pts[i][0], pts[j][1] - pts[i][1]
                dist = (dx * dx + dy * dy) ** 0.5
                if 0 < dist < 14:
                    push = (14 - dist) / 2
                    ux, uy = dx / dist, dy / dist
                    pts[i][0] -= ux * push; pts[i][1] -= uy * push
                    pts[j][0] += ux * push; pts[j][1] += uy * push
    for px, py, n in pts:
        px = min(max(px, x + 8), x + w - 8)
        py = min(max(py, y + 8), y + h - 8)
        num_badge(d, px, py, n, r=8)

# ---------------------------------------------------------------- cards
def lead_card(d, s, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=RULE, width=1)
    ih = int(h * 0.38)
    scene(d, s["scene"], x + 1, y + 1, w - 2, ih - 1)
    d.rectangle([x + 1, y + 1, x + w - 1, y + 24], fill=(0, 0, 0, 0))
    d.rectangle([x + 6, y + 6, x + 6 + int(d.textlength(s["place"], font=SANS_B(10))) + 12, y + 22],
                fill=(0, 0, 0))
    d.text((x + 12, y + 8), s["place"], font=SANS_B(10), fill=(255, 255, 255))
    tw = chip(d, x + w - 6 - 62, y + ih - 24, s["tag"], SANS_B(9), (255, 255, 255), s["tagcol"])
    num_badge(d, x + 16, y + ih + 2, s["n"], r=11)
    ty = y + ih + 8
    d.text((x + 34, ty), s["kicker"], font=SANS_B(11), fill=RED)
    ty += 17
    for ln in wrap(d, s["head"], SERIF_B(18), w - 16):
        d.text((x + 8, ty), ln, font=SERIF_B(18), fill=INK)
        ty += 22
    ty += 2
    for ln in wrap(d, s["body"], SANS(11), w - 16):
        d.text((x + 8, ty), ln, font=SANS(11), fill=(50, 46, 38))
        ty += 13
    d.text((x + 8, y + h - 13), s["source"], font=SANS(9), fill=GREY)

def medium_card(d, s, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=RULE, width=1)
    ih = int(h * 0.36)
    scene(d, s["scene"], x + 1, y + 1, w - 2, ih - 1)
    pw = int(d.textlength(s["place"], font=SANS_B(9))) + 10
    d.rectangle([x + 5, y + 5, x + 5 + pw, y + 19], fill=(0, 0, 0))
    d.text((x + 10, y + 6), s["place"], font=SANS_B(9), fill=(255, 255, 255))
    chip(d, x + w - 6 - 58, y + ih - 21, s["tag"], SANS_B(8), (255, 255, 255), s["tagcol"])
    num_badge(d, x + 14, y + ih + 1, s["n"], r=10)
    ty = y + ih + 7
    d.text((x + 30, ty), s["kicker"], font=SANS_B(9), fill=RED)
    ty += 13
    for ln in wrap(d, s["head"], SERIF_B(13), w - 12)[:2]:
        d.text((x + 6, ty), ln, font=SERIF_B(13), fill=INK)
        ty += 16
    ty += 1
    for ln in wrap(d, s["body"], SANS(10), w - 12)[:2]:
        d.text((x + 6, ty), ln, font=SANS(10), fill=(50, 46, 38))
        ty += 12
    d.text((x + 6, y + h - 10), s["source"], font=SANS(8), fill=GREY)

# ---------------------------------------------------------------- layout
MAP_DOTS_EXTRA = [
    dict(n=14, lat=4.1, lon=-73.6), dict(n=17, lat=-3.0, lon=29.0),
    dict(n=19, lat=3.1, lon=101.7), dict(n=20, lat=37.5, lon=130.9),
    dict(n=24, lat=25.0, lon=-108.0),
]

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=2)
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=1)
    MX = 14
    CW = W - 2 * MX

    # kicker
    y = 14
    d.text((MX, y), "THE WORLD IN ONE DAY", font=SANS_B(12), fill=INK)
    mid = "33 STORIES \u00b7 7 REGIONS \u00b7 ALL FROM THIS ONE DAY"
    d.text(((W - d.textlength(mid, font=SANS_B(12))) / 2, y), mid, font=SANS_B(12), fill=INK)
    rt = "PRESS TIME 23:30 UTC"
    d.text((W - MX - d.textlength(rt, font=SANS_B(12)), y), rt, font=SANS_B(12), fill=INK)
    y += 16
    d.line([MX, y, W - MX, y], fill=RULE, width=1)
    y += 3

    # masthead
    mast = "Tuesday 24 November 2026"
    f = SERIF_B(50)
    d.text(((W - d.textlength(mast, font=f)) / 2, y), mast, font=f, fill=INK)
    y += 54
    sub = "Huawei convicted \u00b7 Four tankers hit in Hormuz \u00b7 Ukraine strikes Russian ships at sea"
    fs = SERIF_B(15)
    d.text(((W - d.textlength(sub, font=fs)) / 2, y), sub, font=fs, fill=(60, 54, 44))
    y += 20
    d.line([MX, y, W - MX, y], fill=INK, width=2)
    y += 3

    # number strip
    ny = y
    cellw = CW / 6
    for i, (num, cap) in enumerate(NUMBERS):
        cx = MX + i * cellw
        fv = SERIF_B(22)
        d.text((cx + 6, ny), num, font=fv, fill=RED if i % 2 == 0 else NAVY)
        cy = ny + 30
        for ln in wrap(d, cap, SANS(10), cellw - 12):
            d.text((cx + 6, cy), ln, font=SANS(10), fill=(50, 46, 38))
            cy += 11
        if i:
            d.line([cx, ny + 2, cx, ny + 48], fill=RULE, width=1)
    y = ny + 52
    d.line([MX, y, W - MX, y], fill=RULE, width=1)
    y += 3

    # region bar
    d.text((MX, y), "WHERE THE NEWS CAME FROM", font=SANS_B(10), fill=GREY)
    y += 12
    total = sum(c for _, c, _ in REGIONS)
    bx = MX
    for name, cnt, col in REGIONS:
        bw = CW * cnt / total
        d.rectangle([bx, y, bx + bw - 1, y + 14], fill=col)
        bx += bw
    y += 17
    lx = MX
    for name, cnt, col in REGIONS:
        d.rectangle([lx, y + 1, lx + 9, y + 10], fill=col)
        t = "%s %d" % (name, cnt)
        d.text((lx + 12, y), t, font=SANS_B(10), fill=INK)
        lx += 12 + d.textlength(t, font=SANS_B(10)) + 16
    y += 13
    d.line([MX, y, W - MX, y], fill=RULE, width=1)
    y += 2

    # timeline
    d.text((MX, y), "THE DAY BY HOURS \u2014 UTC", font=SANS_B(10), fill=GREY)
    y += 12
    colw = CW / 7
    for i, (tm, txt) in enumerate(TIMELINE):
        cx = MX + i * colw
        d.text((cx + 2, y), tm, font=SANS_B(11), fill=RED)
        ty = y + 14
        for ln in wrap(d, txt, SANS(9), colw - 8):
            d.text((cx + 2, ty), ln, font=SANS(9), fill=(50, 46, 38))
            ty += 11
        if i:
            d.line([cx, y, cx, y + 34], fill=RULE, width=1)
    y += 34
    d.line([MX, y, W - MX, y], fill=INK, width=2)
    y += 3

    # leads
    gap = 8
    lw = (CW - 2 * gap) / 3
    for i, s in enumerate(LEADS):
        lead_card(d, s, MX + i * (lw + gap), y, lw, 204)
    y += 204 + 6

    # mediums, 2 rows x 5
    mw = (CW - 4 * gap) / 5
    for row in range(2):
        for i in range(5):
            s = MEDIUMS[row * 5 + i]
            medium_card(d, s, MX + i * (mw + gap), y, mw, 138)
        y += 138 + 6

    # ALSO + map
    d.line([MX, y, W - MX, y], fill=INK, width=2)
    y += 3
    ay = y
    also_w = 668
    map_x = MX + also_w + 10
    map_w = W - MX - map_x
    d.text((MX, ay), "ALSO ON TUESDAY 24 NOVEMBER \u2014 20 MORE STORIES", font=SANS_B(12), fill=INK)
    d.text((map_x, ay), "WHERE IT HAPPENED", font=SANS_B(12), fill=INK)
    d.text((map_x + map_w - d.textlength("pins = story numbers", font=SANS(9)), ay + 2),
           "pins = story numbers", font=SANS(9), fill=GREY)
    ay += 16
    col1 = ALSO[:10]
    col2 = ALSO[10:]
    colw2 = (also_w - 16) / 2
    for col, items in ((0, col1), (1, col2)):
        iy = ay
        for n, txt in items:
            d.text((MX + col * (colw2 + 16), iy), str(n), font=SANS_B(10), fill=RED)
            d.text((MX + col * (colw2 + 16) + 20, iy), txt, font=SANS(10), fill=INK)
            iy += 11
    draw_map(d, map_x, ay, map_w, 127, LEADS + MEDIUMS + MAP_DOTS_EXTRA)
    y = ay + 133
    d.line([MX, y, W - MX, y], fill=RULE, width=1)
    y += 3

    # DATE CHECK
    d.rectangle([MX, y, W - MX, y + 70], outline=RED, width=2)
    d.rectangle([MX, y, MX + 108, y + 18], fill=RED)
    d.text((MX + 8, y + 2), "DATE CHECK", font=SANS_B(11), fill=(255, 255, 255))
    d.text((MX + 116, y + 3), "Every story on this page happened, or was first reported, on Tue 24 Nov 2026 (UTC).",
           font=SANS(10), fill=INK)
    yy = y + 22
    d.text((MX + 8, yy), "LEFT OUT \u2014 happened on an earlier day:", font=SANS_B(9), fill=RED)
    yy += 12
    for ln in wrap(d, " \u00b7 ".join(DATECHECK_OUT), SANS(9), CW - 16):
        d.text((MX + 8, yy), ln, font=SANS(9), fill=(50, 46, 38))
        yy += 11
    d.text((MX + 8, yy), "NOT YET at press time 23:30 UTC:", font=SANS_B(9), fill=RED)
    yy += 12
    for ln in wrap(d, " \u00b7 ".join(DATECHECK_NOTYET), SANS(9), CW - 16):
        d.text((MX + 8, yy), ln, font=SANS(9), fill=(50, 46, 38))
        yy += 11
    y += 72
    d.line([MX, y, W - MX, y], fill=RULE, width=1)
    y += 4

    # footer
    f1 = ("Every story happened, or was first reported, on Tuesday 24 November 2026. Disputed claims are "
          "attributed. Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 Kyiv Independent \u00b7 CAS \u00b7 ESPNcricinfo")
    for ln in wrap(d, f1, SANS(9), CW):
        d.text((MX, y), ln, font=SANS(9), fill=GREY)
        y += 11
    f2 = ("CONFIRMED official / 2+ outlets   \u00b7   OFFICIAL on the record   \u00b7   REPORTED one outlet / witnesses"
          "   \u00b7   CLAIM one side\u2019s claim        Scenes are drawn illustrations \u00b7 wires read to 23:30 UTC")
    for ln in wrap(d, f2, SANS(9), CW):
        d.text((MX, y), ln, font=SANS(9), fill=GREY)
        y += 11
    print("final y:", y, "bottom margin:", H - y)
    img.save("/home/hatch/workspace/makefun/news-image-20261124/entry.png", optimize=True)
    print("saved entry.png")

if __name__ == "__main__":
    main()
