#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generator: 60 feature-rich responsive Maintenance Pages (pure HTML/CSS/JS)

- Each template has: index.html, style.css, script.js, logo.svg, favicon.svg
- Uses colorful palettes, distinct layout variants, and varying fonts
- Includes SVG logo and SVG favicon, a countdown timer, and social/contact UI
- Adds a root connector gallery index.html to browse all templates
- Adds a tutorial.html with step-by-step customization guidance

Run:
  python3 generate_maintenance_templates.py

Output:
  /workspace/maintenance_pages/<01-60>_<slug>/{index.html,style.css,script.js,logo.svg,favicon.svg}
  /workspace/index.html (gallery)
  /workspace/tutorial.html (instructions)
"""

import os
import re
import random
import textwrap
from datetime import datetime, timedelta


OUTPUT_DIR = "/workspace/maintenance_pages"


random.seed(2087)


def ensure_dir(path: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\s-]", "", name).strip().lower()
    slug = re.sub(r"[\s_-]+", "-", slug)
    return slug


def initials(title: str) -> str:
    parts = [p for p in re.split(r"\s+|&|,|\.|-", title) if p]
    if not parts:
        return "M"
    caps = "".join(p[0].upper() for p in parts[:3])
    return caps[:3]


PALETTES = [
    {"name": "sunset", "primary": "#ff7e5f", "accent": "#feb47b", "bg": "#2b2d42", "text": "#ffffff"},
    {"name": "ocean", "primary": "#00c6ff", "accent": "#0072ff", "bg": "#0b132b", "text": "#e0fbfc"},
    {"name": "forest", "primary": "#11998e", "accent": "#38ef7d", "bg": "#042a2b", "text": "#e8fff1"},
    {"name": "royal", "primary": "#6a11cb", "accent": "#2575fc", "bg": "#0f1021", "text": "#f3f4ff"},
    {"name": "neon", "primary": "#ff00cc", "accent": "#333399", "bg": "#0a0a0a", "text": "#f8f8ff"},
    {"name": "candy", "primary": "#f857a6", "accent": "#ff5858", "bg": "#1a1b2e", "text": "#fff1f3"},
    {"name": "solar", "primary": "#f7971e", "accent": "#ffd200", "bg": "#291528", "text": "#fff8e1"},
    {"name": "aqua", "primary": "#00f2fe", "accent": "#4facfe", "bg": "#081229", "text": "#e6fbff"},
    {"name": "peach", "primary": "#ff9a9e", "accent": "#fecfef", "bg": "#1b1b3a", "text": "#fff6f7"},
    {"name": "mint", "primary": "#43cea2", "accent": "#185a9d", "bg": "#0d1b2a", "text": "#ecfff4"},
    {"name": "lava", "primary": "#f12711", "accent": "#f5af19", "bg": "#0d0d0d", "text": "#fff4e6"},
    {"name": "berry", "primary": "#8a2387", "accent": "#e94057", "bg": "#150019", "text": "#f9f1ff"},
    {"name": "aurora", "primary": "#00c9ff", "accent": "#92fe9d", "bg": "#06142e", "text": "#eafff4"},
    {"name": "space", "primary": "#1CB5E0", "accent": "#000046", "bg": "#040008", "text": "#f0f8ff"},
    {"name": "violet", "primary": "#7F00FF", "accent": "#E100FF", "bg": "#1a0033", "text": "#faf0ff"},
    {"name": "emerald", "primary": "#00b09b", "accent": "#96c93d", "bg": "#001a14", "text": "#f2fff9"},
    {"name": "blush", "primary": "#ec008c", "accent": "#fc6767", "bg": "#190019", "text": "#fff0f8"},
    {"name": "flame", "primary": "#ff512f", "accent": "#dd2476", "bg": "#10001f", "text": "#fff1ff"},
    {"name": "tropical", "primary": "#00d2ff", "accent": "#3a7bd5", "bg": "#081c24", "text": "#e9fbff"},
    {"name": "steel", "primary": "#3a6073", "accent": "#16222a", "bg": "#0a0f14", "text": "#e6f1f5"},
]


FONTS = [
    ("Poppins", "Inter"),
    ("Montserrat", "Roboto"),
    ("Playfair Display", "Source Sans 3"),
    ("Raleway", "Nunito"),
    ("DM Sans", "Manrope"),
    ("Outfit", "Work Sans"),
    ("Space Grotesk", "Inter"),
    ("Urbanist", "Inter"),
    ("Bricolage Grotesque", "Inter"),
    ("Rubik", "Inter"),
    ("Lato", "Merriweather Sans"),
    ("Quicksand", "Nunito"),
    ("Sora", "Inter"),
    ("Kanit", "Inter"),
    ("Exo 2", "Inter"),
    ("Bebas Neue", "Inter"),
    ("Merriweather", "Lora"),
    ("Josefin Sans", "Inter"),
    ("Barlow", "Inter"),
    ("Noto Sans", "Inter"),
    ("PT Sans", "Inter"),
    ("Heebo", "Inter"),
    ("Mulish", "Inter"),
    ("Red Hat Display", "Inter"),
]


ICON_LIBS = [
    {
        "name": "remix",
        "cdn": "https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css",
        "icons": {
            "tools": "ri-tools-fill",
            "mail": "ri-mail-fill",
            "phone": "ri-phone-fill",
            "twitter": "ri-twitter-x-line",
            "facebook": "ri-facebook-circle-fill",
            "instagram": "ri-instagram-fill",
            "github": "ri-github-fill",
            "spark": "ri-sparkling-fill",
            "clock": "ri-time-fill",
            "shield": "ri-shield-keyhole-fill",
            "rocket": "ri-rocket-2-fill"
        }
    },
    {
        "name": "boxicons",
        "cdn": "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
        "icons": {
            "tools": "bx bxs-cog",
            "mail": "bx bxs-envelope",
            "phone": "bx bxs-phone",
            "twitter": "bx bxl-twitter",
            "facebook": "bx bxl-facebook-circle",
            "instagram": "bx bxl-instagram",
            "github": "bx bxl-github",
            "spark": "bx bxs-magic-wand",
            "clock": "bx bxs-time",
            "shield": "bx bxs-shield-alt-2",
            "rocket": "bx bxs-rocket"
        }
    },
    {
        "name": "bootstrap",
        "cdn": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css",
        "icons": {
            "tools": "bi bi-tools",
            "mail": "bi bi-envelope-fill",
            "phone": "bi bi-telephone-fill",
            "twitter": "bi bi-twitter-x",
            "facebook": "bi bi-facebook",
            "instagram": "bi bi-instagram",
            "github": "bi bi-github",
            "spark": "bi bi-stars",
            "clock": "bi bi-clock-fill",
            "shield": "bi bi-shield-lock-fill",
            "rocket": "bi bi-rocket-takeoff-fill"
        }
    },
]


VARIANTS = [
    "glass",
    "neon",
    "wave",
    "blob",
    "mesh",
    "stripe",
    "radial",
    "conic",
    "pattern",
    "tiles",
]


NICHES = [
    {"brand": "Neuron AI", "niche": "AI SaaS", "tag": "Smarter decisions powered by ML."},
    {"brand": "BrewBunch", "niche": "Coffee Shop", "tag": "Fresh roasts and cozy vibes."},
    {"brand": "PixelForge Games", "niche": "Gaming Studio", "tag": "Crafting worlds that play back."},
    {"brand": "MintFlow", "niche": "Fintech App", "tag": "Money, simplified and secure."},
    {"brand": "CareHub", "niche": "Healthcare Portal", "tag": "Care that connects."},
    {"brand": "LearnSphere", "niche": "EduTech", "tag": "Learning without limits."},
    {"brand": "WanderWay", "niche": "Travel Agency", "tag": "Your route to wonder."},
    {"brand": "SoundSummit", "niche": "Music Festival", "tag": "Turn it up, together."},
    {"brand": "FrameCraft", "niche": "Photography Portfolio", "tag": "Focus on what matters."},
    {"brand": "Fork & Flame", "niche": "Restaurant", "tag": "Fire up your appetite."},
    {"brand": "IronPulse", "niche": "Fitness Gym", "tag": "Stronger every day."},
    {"brand": "Leaf & Letter", "niche": "Bookstore", "tag": "Pages that stay with you."},
    {"brand": "PawPals", "niche": "Pet Care", "tag": "Happy tails, healthy lives."},
    {"brand": "StudioNook", "niche": "Interior Design", "tag": "Spaces with soul."},
    {"brand": "Architext", "niche": "Architecture Firm", "tag": "Lines that last."},
    {"brand": "TorqueAuto", "niche": "Car Dealership", "tag": "Drive what drives you."},
    {"brand": "NestQuest", "niche": "Real Estate", "tag": "Find your next chapter."},
    {"brand": "ShopWize", "niche": "E-commerce Store", "tag": "Smarter shopping starts here."},
    {"brand": "Velvet Line", "niche": "Fashion Brand", "tag": "Tailored to turn heads."},
    {"brand": "Glitz & Glow", "niche": "Beauty Salon", "tag": "Shine in your own way."},
    {"brand": "Trim & Tonic", "niche": "Barbershop", "tag": "Cuts that keep up."},
    {"brand": "LunaSpa", "niche": "Spa", "tag": "Exhale. Reset. Glow."},
    {"brand": "Knot & Bloom", "niche": "Wedding Planner", "tag": "Moments made forever."},
    {"brand": "Eventum", "niche": "Event Management", "tag": "Where ideas take the stage."},
    {"brand": "AdLumen", "niche": "Digital Marketing", "tag": "Make every click count."},
    {"brand": "PeakRank", "niche": "SEO Agency", "tag": "Climb the results."},
    {"brand": "Spotlight Ads", "niche": "Ad Consultancy", "tag": "Own your audience."},
    {"brand": "Lex & Co.", "niche": "Legal Firm", "tag": "Counsel you can count on."},
    {"brand": "LedgerLeaf", "niche": "Tax Consultancy", "tag": "Numbers, neatly handled."},
    {"brand": "TalentHive", "niche": "HR Staffing", "tag": "Great teams start here."},
    {"brand": "HireSprint", "niche": "Recruitment", "tag": "Find fast, hire smart."},
    {"brand": "Crafted by Nova", "niche": "Freelancer Portfolio", "tag": "Design in high fidelity."},
    {"brand": "HopeBridge", "niche": "Nonprofit NGO", "tag": "Bridging needs to deeds."},
    {"brand": "GiveSpark", "niche": "Charity Campaign", "tag": "Small gifts, big change."},
    {"brand": "Grace Chapel", "niche": "Church", "tag": "Gather, grow, go."},
    {"brand": "MicDrop", "niche": "Podcast", "tag": "Where voices carry."},
    {"brand": "Inkwell Notes", "niche": "Blog", "tag": "Thoughts that travel."},
    {"brand": "Daily Horizon", "niche": "News Site", "tag": "See the bigger picture."},
    {"brand": "CoinPort", "niche": "Crypto Exchange", "tag": "Trade with trust."},
    {"brand": "ChainSmith", "niche": "Blockchain Startup", "tag": "Blocks that build value."},
    {"brand": "ShieldOps", "niche": "Cybersecurity", "tag": "Secure by default."},
    {"brand": "SkyVault", "niche": "Cloud Storage", "tag": "Your files, everywhere."},
    {"brand": "DeployKit", "niche": "DevOps Tools", "tag": "Ship confidently."},
    {"brand": "InsightFlow", "niche": "Analytics Dashboard", "tag": "Answers in an instant."},
    {"brand": "LinkMesh", "niche": "IoT Platform", "tag": "Devices that speak up."},
    {"brand": "AeroLens", "niche": "Drone Services", "tag": "The aerial advantage."},
    {"brand": "MotionCraft", "niche": "Video Production", "tag": "Stories in motion."},
    {"brand": "Immersion Lab", "niche": "AR/VR Studio", "tag": "Enter new dimensions."},
    {"brand": "NovaQuest", "niche": "Game Launch", "tag": "Press start to begin."},
    {"brand": "TapNest", "niche": "Mobile App", "tag": "Everything just a tap away."},
    {"brand": "Nimbus", "niche": "Weather App", "tag": "Forecasts you can feel."},
    {"brand": "TimeWeave", "niche": "Calendar/Scheduling", "tag": "Plans that stick."},
    {"brand": "DashDish", "niche": "Food Delivery", "tag": "Good food at speed."},
    {"brand": "GreenCart", "niche": "Grocery", "tag": "Fresh to your door."},
    {"brand": "MediBox", "niche": "Pharmacy", "tag": "Care, delivered."},
    {"brand": "PearlDent", "niche": "Dental Clinic", "tag": "Smiles, refined."},
    {"brand": "VetNest", "niche": "Veterinary", "tag": "Compassionate care for companions."},
    {"brand": "PlayLearn", "niche": "Kids Learning", "tag": "Play your way to smart."},
    {"brand": "LinguaLift", "niche": "Language Learning", "tag": "Find your fluent."},
    {"brand": "SiteWorks", "niche": "General", "tag": "We make great sites greater."},
]


HEADLINE_PHRASES = [
    "We\'re tuning things up.",
    "Scheduled maintenance in progress.",
    "Upgrades are underway.",
    "Polishing the experience.",
    "Brief pit stop for improvements.",
    "A fresh coat of paint is coming.",
    "Rebooting for better performance.",
]


def google_fonts_link(head_font: str, body_font: str) -> str:
    def fmt(f):
        return f.replace(" ", "+")
    families = f"family={fmt(head_font)}:wght@400;600;700&family={fmt(body_font)}:wght@400;500;700&display=swap"
    return f"https://fonts.googleapis.com/css2?{families}"


def build_logo_svg(title: str, palette: dict) -> str:
    mark = initials(title)
    grad_id = "g" + slugify(title)
    return textwrap.dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200" role="img" aria-label="{title} logo">
      <defs>
        <linearGradient id="{grad_id}" x1="0" x2="1" y1="0" y2="1">
          <stop offset="0%" stop-color="{palette['primary']}"/>
          <stop offset="100%" stop-color="{palette['accent']}"/>
        </linearGradient>
        <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
          <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#000" flood-opacity="0.25"/>
        </filter>
      </defs>
      <rect x="20" y="20" width="160" height="160" rx="32" fill="url(#{grad_id})" filter="url(#shadow)"/>
      <circle cx="160" cy="40" r="8" fill="rgba(255,255,255,0.8)"/>
      <circle cx="30" cy="170" r="6" fill="rgba(255,255,255,0.6)"/>
      <text x="100" y="120" text-anchor="middle" font-family="'Inter', system-ui" font-weight="800" font-size="68" fill="white">{mark}</text>
    </svg>
    """)


def build_favicon_svg(title: str, palette: dict) -> str:
    mark = initials(title)
    grad_id = "f" + slugify(title)
    return textwrap.dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
      <defs>
        <linearGradient id="{grad_id}" x1="0" x2="1" y1="0" y2="1">
          <stop offset="0%" stop-color="{palette['primary']}"/>
          <stop offset="100%" stop-color="{palette['accent']}"/>
        </linearGradient>
      </defs>
      <rect x="6" y="6" width="52" height="52" rx="12" fill="url(#{grad_id})"/>
      <text x="32" y="40" text-anchor="middle" font-family="'Inter', system-ui" font-weight="800" font-size="26" fill="white">{mark[:2]}</text>
    </svg>
    """)


def build_css(variant: str, palette: dict, head_font: str, body_font: str) -> str:
    base = f"""
    :root {{
      --bg: {palette['bg']};
      --bg-2: {palette['accent']};
      --text: {palette['text']};
      --muted: rgba(255,255,255,0.7);
      --primary: {palette['primary']};
      --accent: {palette['accent']};
      --card: rgba(255,255,255,0.08);
      --border: rgba(255,255,255,0.18);
      --shadow: 0 20px 60px rgba(0,0,0,0.35);
      --radius: 18px;
    }}

    * {{ box-sizing: border-box; }}
    html, body {{ height: 100%; }}
    body {{
      margin: 0;
      color: var(--text);
      font-family: '{body_font}', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica, Arial, 'Apple Color Emoji', 'Segoe UI Emoji';
      background: var(--bg);
      background-attachment: fixed;
      overflow-x: hidden;
    }}

    .wrap {{
      min-height: 100%;
      display: grid;
      place-items: center;
      position: relative;
      padding: 56px 20px;
    }}

    header.topbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0));
      z-index: 5;
    }}

    header.topbar a.home {{
      color: var(--muted);
      text-decoration: none;
      font-size: 14px;
    }}

    .card {{
      width: min(1080px, 100%);
      margin: 0 auto;
      background: var(--card);
      backdrop-filter: saturate(1.3) blur(8px);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      border-radius: var(--radius);
      overflow: hidden;
      position: relative;
    }}

    .card-inner {{
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 28px;
      padding: 36px;
    }}

    .brand {{ display: flex; align-items: center; gap: 14px; }}
    .brand img {{ width: 56px; height: 56px; border-radius: 12px; }}
    .brand .name {{ font-family: '{head_font}', sans-serif; font-weight: 700; font-size: 22px; letter-spacing: 0.3px; }}

    h1.title {{
      font-family: '{head_font}', sans-serif;
      font-size: clamp(30px, 4vw, 52px);
      line-height: 1.08;
      margin: 10px 0 8px;
      letter-spacing: -0.02em;
    }}
    p.subtitle {{
      font-size: clamp(16px, 2vw, 18px);
      color: var(--muted);
      margin: 0 0 18px;
    }}

    .timer {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 20px 0 12px; }}
    .tbox {{ background: rgba(255,255,255,0.08); border: 1px solid var(--border); border-radius: 14px; padding: 14px; text-align: center; }}
    .tbox .num {{ font-size: clamp(26px, 4vw, 44px); font-weight: 800; font-family: '{head_font}', sans-serif; }}
    .tbox .label {{ font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); }}

    .cta {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; align-items: center; }}
    .cta input[type="email"] {{
      flex: 1 1 220px;
      min-width: 200px;
      padding: 14px 16px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.06);
      color: var(--text);
      outline: none;
    }}
    .cta button.primary {{
      padding: 14px 18px;
      border: 0; border-radius: 12px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white; font-weight: 700; letter-spacing: 0.02em; cursor: pointer;
      box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }}
    .cta .note {{ font-size: 12px; opacity: 0.75; }}

    .features {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 26px; }}
    .feature {{ background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 14px; padding: 14px; }}
    .feature i {{ font-size: 20px; color: var(--primary); }}
    .feature h3 {{ margin: 8px 0 6px; font-size: 16px; font-weight: 700; font-family: '{head_font}', sans-serif; }}
    .feature p {{ margin: 0; font-size: 14px; color: var(--muted); }}

    .side {{ position: relative; min-height: 300px; display: grid; place-items: center; }}
    .art {{ width: 88%; max-width: 520px; aspect-ratio: 1.2 / 1; border-radius: 18px; background: linear-gradient(135deg, var(--primary), var(--accent)); filter: drop-shadow(0 24px 60px rgba(0,0,0,0.4)); position: relative; overflow: hidden; }}
    .art::after {{ content: ""; position: absolute; inset: -40%; background: radial-gradient(closest-side, rgba(255,255,255,0.18), transparent 60%); transform: rotate(25deg); }}

    .progress {{ margin-top: 10px; height: 8px; background: rgba(255,255,255,0.1); border-radius: 999px; overflow: hidden; border: 1px solid var(--border); }}
    .progress .bar {{ height: 100%; width: 48%; background: linear-gradient(90deg, var(--primary), var(--accent)); box-shadow: 0 8px 24px rgba(0,0,0,0.25) inset; border-radius: 999px; transition: width 1s ease; }}

    footer {{ text-align: center; color: var(--muted); font-size: 12px; margin-top: 20px; }}
    .socials {{ display: inline-flex; gap: 10px; margin-left: 10px; }}
    .socials a {{ color: var(--muted); text-decoration: none; }}
    .socials a:hover {{ color: var(--text); }}

    @media (max-width: 920px) {{
      .card-inner {{ grid-template-columns: 1fr; padding: 26px; }}
      .side {{ order: -1; }}
    }}
    """

    variant_css = ""
    if variant == "glass":
        variant_css = """
        body { background: radial-gradient(1000px 600px at -10% -20%, rgba(255,255,255,0.06), transparent), radial-gradient(800px 500px at 120% 120%, rgba(255,255,255,0.06), transparent), var(--bg); }
        .card::before { content: ""; position: absolute; inset: -2px; border-radius: inherit; padding: 2px; background: linear-gradient(45deg, rgba(255,255,255,0.22), rgba(255,255,255,0.02)); -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; }
        """
    elif variant == "neon":
        variant_css = """
        body { background: radial-gradient(60% 60% at 10% 10%, rgba(255,0,204,0.2), transparent), radial-gradient(60% 60% at 100% 0%, rgba(51,51,153,0.25), transparent), var(--bg); }
        .card { border: 1px solid rgba(255,255,255,0.22); box-shadow: 0 0 0 1px rgba(255,255,255,0.05), 0 0 80px rgba(255,0,200,0.25), var(--shadow); }
        .tbox { box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08), 0 6px 18px rgba(0,0,0,0.25); }
        """
    elif variant == "wave":
        variant_css = """
        body { background: conic-gradient(from 210deg at 60% 40%, rgba(255,255,255,0.08), rgba(255,255,255,0) 60%), var(--bg); }
        .art { background: linear-gradient(135deg, var(--primary), var(--accent)); position: relative; }
        .art::before { content: ""; position: absolute; inset: 0; background: url('data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 200 100\"><path d=\"M0 50 Q50 0 100 50 T200 50 V100 H0 Z\" fill=\"rgba(255,255,255,0.15)\"/></svg>'); background-size: cover; mix-blend-mode: overlay; opacity: .7; }
        """
    elif variant == "blob":
        variant_css = """
        body { background: radial-gradient(40% 40% at 20% 80%, rgba(255,255,255,0.08), transparent), var(--bg); }
        .wrap::before, .wrap::after { content: ""; position: absolute; width: 480px; height: 480px; filter: blur(80px); opacity: 0.4; border-radius: 50%; }
        .wrap::before { left: -120px; top: 20%; background: {palette['primary']}; }
        .wrap::after { right: -120px; bottom: 10%; background: {palette['accent']}; }
        """.replace("{palette['primary']}", palette['primary']).replace("{palette['accent']}", palette['accent'])
    elif variant == "mesh":
        variant_css = """
        body { background: radial-gradient(35% 40% at 20% 20%, rgba(255,255,255,0.06), transparent), radial-gradient(30% 60% at 80% 70%, rgba(255,255,255,0.05), transparent), var(--bg); }
        .art { background: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.25), transparent 40%), linear-gradient(135deg, var(--primary), var(--accent)); }
        """
    elif variant == "stripe":
        variant_css = """
        body { background: repeating-linear-gradient(135deg, rgba(255,255,255,0.03) 0 10px, rgba(0,0,0,0.05) 10px 20px), var(--bg); }
        .card { border-image: linear-gradient(90deg, var(--primary), var(--accent)) 1; border-width: 1px; border-style: solid; }
        """
    elif variant == "radial":
        variant_css = """
        body { background: radial-gradient(1200px 600px at 50% -10%, rgba(255,255,255,0.12), transparent), var(--bg); }
        """
    elif variant == "conic":
        variant_css = """
        body { background: conic-gradient(from 180deg at 30% 30%, rgba(255,255,255,0.09), rgba(255,255,255,0) 55%), var(--bg); }
        .art { transform: rotate(-2deg); }
        """
    elif variant == "pattern":
        variant_css = """
        body { background: var(--bg); }
        .wrap::before { content: ""; position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px); background-size: 24px 24px; opacity: .35; }
        """
    elif variant == "tiles":
        variant_css = """
        body { background: radial-gradient(closest-corner, rgba(255,255,255,0.06), rgba(255,255,255,0) 60%) fixed, var(--bg); }
        .wrap::after { content: ""; position: absolute; inset: 0; background: conic-gradient(from 0turn, rgba(255,255,255,0.05), transparent 20% 80%, rgba(255,255,255,0.05)); mix-blend-mode: overlay; }
        """

    return base + "\n" + variant_css


def build_js(slug: str, default_days: int) -> str:
    return textwrap.dedent(f"""
    const STORAGE_KEY = 'mp_target_{slug}';
    const DEFAULT_DAYS = {default_days};

    function getParam(name) {{
      const params = new URLSearchParams(window.location.search);
      return params.get(name);
    }}

    function getStoredTarget() {{
      try {{
        const t = localStorage.getItem(STORAGE_KEY);
        if (!t) return null;
        const n = parseInt(t, 10);
        if (Number.isNaN(n)) return null;
        return n;
      }} catch (e) {{
        return null;
      }}
    }}

    function storeTarget(ts) {{
      try {{ localStorage.setItem(STORAGE_KEY, String(ts)); }} catch (e) {{}}
    }}

    function resolveTarget() {{
      const stored = getStoredTarget();
      if (stored) return stored;
      const dateStr = getParam('date');
      if (dateStr) {{
        const t = Date.parse(dateStr);
        if (!Number.isNaN(t)) {{ storeTarget(t); return t; }}
      }}
      const daysParam = getParam('days');
      let days = DEFAULT_DAYS;
      if (daysParam && !Number.isNaN(parseInt(daysParam, 10))) days = parseInt(daysParam, 10);
      const target = Date.now() + days * 24 * 60 * 60 * 1000;
      storeTarget(target);
      return target;
    }}

    function pad(n) {{ return String(n).padStart(2, '0'); }}

    function updateCountdown(targetTs) {{
      const now = Date.now();
      let diff = Math.max(0, targetTs - now);
      const days = Math.floor(diff / (24*60*60*1000)); diff -= days * 24*60*60*1000;
      const hours = Math.floor(diff / (60*60*1000)); diff -= hours * 60*60*1000;
      const mins = Math.floor(diff / (60*1000)); diff -= mins * 60*1000;
      const secs = Math.floor(diff / 1000);

      document.getElementById('days').textContent = pad(days);
      document.getElementById('hours').textContent = pad(hours);
      document.getElementById('minutes').textContent = pad(mins);
      document.getElementById('seconds').textContent = pad(secs);

      const total = days*24*3600 + hours*3600 + mins*60 + secs;
      const initial = DEFAULT_DAYS * 24 * 3600;
      const ratio = Math.max(0.02, Math.min(1, 1 - total / initial));
      const bar = document.querySelector('.progress .bar');
      if (bar) bar.style.width = (ratio * 100).toFixed(1) + '%';
    }}

    function resetCountdown(days) {{
      const next = Date.now() + days * 24 * 60 * 60 * 1000;
      storeTarget(next);
      updateCountdown(next);
    }}

    function setupEmailCapture() {{
      const form = document.getElementById('notify-form');
      if (!form) return;
      form.addEventListener('submit', (e) => {{
        e.preventDefault();
        const email = form.querySelector('input[type=email]').value;
        form.querySelector('button').textContent = 'Added!';
        form.querySelector('button').disabled = true;
        try {{
          const key = 'mp_emails_{slug}';
          const list = JSON.parse(localStorage.getItem(key) || '[]');
          list.push({{ email, ts: Date.now() }});
          localStorage.setItem(key, JSON.stringify(list));
        }} catch (err) {{}}
      }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      let target = resolveTarget();
      updateCountdown(target);
      setInterval(() => updateCountdown(target), 1000);
      document.querySelectorAll('[data-reset]')?.forEach(btn => {{
        btn.addEventListener('click', () => {{ resetCountdown(parseInt(btn.getAttribute('data-reset'), 10) || {default_days}); window.scrollTo({{ top: 0, behavior: 'smooth' }}); }});
      }});
      const y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
      setupEmailCapture();
    }});
    """)


def build_html(i: int, niche: dict, palette: dict, head_font: str, body_font: str, icon_lib: dict, variant: str, default_days: int, folder_rel: str) -> str:
    brand = niche["brand"]
    slug = slugify(brand)
    headline = random.choice(HEADLINE_PHRASES)
    icon = icon_lib["icons"]

    gf_link = google_fonts_link(head_font, body_font)

    # Social icon classes depends on library
    socials = [
        (icon.get("twitter", ""), "https://twitter.com"),
        (icon.get("instagram", ""), "https://instagram.com"),
        (icon.get("github", ""), "https://github.com"),
    ]

    feature_data = [
        (icon.get("spark", ""), "Faster", "Performance boost and cleaner UX."),
        (icon.get("shield", ""), "Safer", "Security and reliability tuned up."),
        (icon.get("rocket", ""), "Smarter", "New features launching soon."),
    ]

    return textwrap.dedent(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta name="theme-color" content="{palette['primary']}">
      <title>{brand} — Maintenance</title>
      <meta name="description" content="{niche['niche']} maintenance page for {brand}. {niche['tag']}">
      <meta property="og:title" content="{brand} — Maintenance"/>
      <meta property="og:description" content="{niche['niche']} maintenance page for {brand}. {niche['tag']}"/>
      <meta property="og:type" content="website"/>
      <link rel="icon" type="image/svg+xml" href="favicon.svg"/>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="{gf_link}" rel="stylesheet">
      <link href="{icon_lib['cdn']}" rel="stylesheet">
      <link rel="stylesheet" href="style.css"/>
    </head>
    <body class="v-{variant}">
      <header class="topbar">
        <a class="home" href="{folder_rel}">⟵ Gallery</a>
        <div style="opacity:.6;font-size:12px">#{i:02d} {niche['niche']}</div>
      </header>

      <main class="wrap">
        <section class="card">
          <div class="card-inner">
            <div class="content">
              <div class="brand"><img src="logo.svg" alt="{brand} logo"/><div class="name">{brand}</div></div>
              <h1 class="title">{headline}</h1>
              <p class="subtitle">We\'re updating our {niche['niche'].lower()} experience for <strong>{brand}</strong>. {niche['tag']}</p>

              <div class="timer" role="timer" aria-live="polite">
                <div class="tbox"><div id="days" class="num">00</div><div class="label">Days</div></div>
                <div class="tbox"><div id="hours" class="num">00</div><div class="label">Hours</div></div>
                <div class="tbox"><div id="minutes" class="num">00</div><div class="label">Minutes</div></div>
                <div class="tbox"><div id="seconds" class="num">00</div><div class="label">Seconds</div></div>
              </div>
              <div class="progress" aria-hidden="true"><div class="bar"></div></div>

              <form id="notify-form" class="cta" autocomplete="on">
                <input type="email" placeholder="Get notified (email)" aria-label="Email" required>
                <button class="primary" type="submit"><i class="{icon['mail']}"></i> Notify me</button>
                <span class="note">ETA in ~{default_days} days</span>
              </form>

              <div class="features">
                <div class="feature"><i class="{feature_data[0][0]}"></i><h3>{feature_data[0][1]}</h3><p>{feature_data[0][2]}</p></div>
                <div class="feature"><i class="{feature_data[1][0]}"></i><h3>{feature_data[1][1]}</h3><p>{feature_data[1][2]}</p></div>
                <div class="feature"><i class="{feature_data[2][0]}"></i><h3>{feature_data[2][1]}</h3><p>{feature_data[2][2]}</p></div>
              </div>

              <div class="cta">
                <button type="button" class="primary" data-reset="{default_days}"><i class="{icon['clock']}"></i> Reset {default_days} days</button>
                <a style="color:var(--muted);text-decoration:none" href="mailto:hello@example.com"><i class="{icon['mail']}"></i> Contact</a>
                <a style="color:var(--muted);text-decoration:none" href="tel:+100200300"><i class="{icon['phone']}"></i> +1 002 003 000</a>
              </div>
            </div>

            <aside class="side">
              <div class="art"></div>
            </aside>
          </div>
        </section>

        <footer>
          © <span id="year"></span> {brand}
          <span class="socials">
            <a href="{socials[0][1]}" aria-label="Twitter"><i class="{socials[0][0]}"></i></a>
            <a href="{socials[1][1]}" aria-label="Instagram"><i class="{socials[1][0]}"></i></a>
            <a href="{socials[2][1]}" aria-label="GitHub"><i class="{socials[2][0]}"></i></a>
          </span>
        </footer>
      </main>

      <script src="script.js"></script>
    </body>
    </html>
    """)


def create_template(i: int, niche: dict, palette: dict, fonts: tuple, icon_lib: dict, variant: str, default_days: int, connector_rel: str):
    brand = niche["brand"]
    slug = f"{i:02d}_{slugify(brand)}"
    out_dir = os.path.join(OUTPUT_DIR, slug)
    ensure_dir(out_dir)

    head_font, body_font = fonts

    css = build_css(variant, palette, head_font, body_font)
    js = build_js(slug, default_days)
    html = build_html(i, niche, palette, head_font, body_font, icon_lib, variant, default_days, connector_rel)
    logo = build_logo_svg(brand, palette)
    favicon = build_favicon_svg(brand, palette)

    write_file(os.path.join(out_dir, "style.css"), css)
    write_file(os.path.join(out_dir, "script.js"), js)
    write_file(os.path.join(out_dir, "index.html"), html)
    write_file(os.path.join(out_dir, "logo.svg"), logo)
    write_file(os.path.join(out_dir, "favicon.svg"), favicon)

    return slug


def build_gallery(templates: list) -> str:
    # templates: list of dicts with keys slug, brand, niche, palette
    cards = []
    for t in templates:
        name = f"#{t['index']:02d} {t['brand']}"
        href = f"maintenance_pages/{t['slug']}/index.html"
        chip = t['niche']
        cards.append(f"""
        <a class=card href="{href}" target="_blank" rel="noopener">
          <div class=thumb><img src="maintenance_pages/{t['slug']}/logo.svg" alt="{t['brand']} logo"></div>
          <div class=meta>
            <div class=name>{name}</div>
            <div class=chip>{chip}</div>
          </div>
        </a>
        """)

    cards_html = "\n".join(cards)
    return textwrap.dedent(f"""
    <!DOCTYPE html>
    <html lang=en>
    <head>
      <meta charset=utf-8>
      <meta name=viewport content="width=device-width,initial-scale=1">
      <title>Maintenance Templates Gallery</title>
      <link rel=icon type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='64' height='64' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' x2='1' y1='0' y2='1'%3E%3Cstop offset='0%25' stop-color='%236a11cb'/%3E%3Cstop offset='100%25' stop-color='%232575fc'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect x='6' y='6' width='52' height='52' rx='12' fill='url(%23g)'/%3E%3Ctext x='32' y='40' text-anchor='middle' font-family='Inter' font-size='20' fill='white'%3E60%3C/text%3E%3C/svg%3E">
      <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=Inter:wght@400;600;700&display=swap" rel=stylesheet>
      <style>
        :root {{ --bg:#0f1021; --text:#ffffff; --muted:#cbd5e1; --card:#141532; --border:#2a2b4a; --primary:#6a11cb; --accent:#2575fc; }}
        *{{box-sizing:border-box}}
        body{{margin:0;background:linear-gradient(135deg,rgba(255,255,255,0.04),transparent),var(--bg);color:var(--text);font-family:'Inter',system-ui}}
        header{{padding:26px 18px;display:flex;align-items:center;justify-content:space-between}}
        h1{{font-family:'DM Sans',sans-serif;letter-spacing:-.02em;margin:0;font-size:clamp(22px,3vw,34px)}}
        .grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;padding:12px 18px 28px;max-width:1280px;margin:0 auto}}
        .card{{display:block;background:var(--card);border:1px solid var(--border);border-radius:16px;text-decoration:none;color:inherit;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.35)}}
        .thumb{{aspect-ratio: 3 / 2;display:grid;place-items:center;background:radial-gradient(closest-side,rgba(255,255,255,0.08),transparent),linear-gradient(135deg,var(--primary),var(--accent))}}
        .thumb img{{width:96px;height:96px;border-radius:16px;box-shadow:0 16px 40px rgba(0,0,0,.35)}}
        .meta{{padding:12px 14px 16px}}
        .name{{font-weight:700;font-size:16px}}
        .chip{{display:inline-block;margin-top:6px;padding:6px 10px;border-radius:999px;background:rgba(255,255,255,.06);border:1px solid var(--border);font-size:12px;color:var(--muted)}}
        footer{{padding:10px 18px 24px;color:var(--muted);font-size:12px;text-align:center}}
        @media(max-width:1100px){{.grid{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
        @media(max-width:780px){{.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
        @media(max-width:520px){{.grid{{grid-template-columns:1fr}}}}
      </style>
    </head>
    <body>
      <header>
        <h1>60 Maintenance Page Templates</h1>
        <nav><a href="tutorial.html" style="color:#cbd5e1;text-decoration:none">Tutorial</a></nav>
      </header>
      <section class=grid>
      {cards_html}
      </section>
      <footer>Open any template to view. Use the Tutorial to customize.</footer>
    </body>
    </html>
    """)


def build_tutorial() -> str:
    return textwrap.dedent(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width, initial-scale=1"/>
          <title>Customization Tutorial — Maintenance Templates</title>
          <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
          <style>
            :root { --bg:#0b1229; --card:#121a3a; --border:#263269; --text:#ffffff; --muted:#cbd5e1; --accent:#6a11cb; }
            *{box-sizing:border-box}
            body{margin:0;background:linear-gradient(135deg,rgba(255,255,255,0.04),transparent),var(--bg);color:var(--text);font-family:'Inter',system-ui}
            header{padding:28px 18px}
            h1{font-family:'Space Grotesk',sans-serif;letter-spacing:-.02em;margin:0;font-size:clamp(22px,3vw,34px)}
            main{max-width:920px;margin:0 auto;padding:12px 18px 40px}
            section{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:18px 18px 22px;margin:14px 0;box-shadow:0 20px 60px rgba(0,0,0,.35)}
            h2{margin:6px 0 8px;font-size:18px}
            p{margin:8px 0;color:var(--muted)}
            code, pre{background:rgba(255,255,255,.06);border:1px solid var(--border);border-radius:12px;padding:10px 12px;display:block;overflow:auto}
            ul{margin:6px 0 10px 18px}
            a{color:#9bbcff}
          </style>
        </head>
        <body>
          <header>
            <h1>Customization Tutorial</h1>
          </header>
          <main>
            <section>
              <h2>Project structure</h2>
              <p>Each template lives in its own folder under <code>maintenance_pages/</code> and includes <code>index.html</code>, <code>style.css</code>, <code>script.js</code>, <code>logo.svg</code>, and <code>favicon.svg</code>.</p>
            </section>

            <section>
              <h2>Change the logo (SVG)</h2>
              <p>Replace <code>logo.svg</code> in the template folder with your custom SVG, or edit colors and text inside. Update the image source if you rename the file:</p>
              <pre>&lt;img src="logo.svg" alt="Your brand"&gt;</pre>
              <p>Tip: Keep viewBox sizes around 128–256 and use a transparent background for best results.</p>
            </section>

            <section>
              <h2>Update the favicon (SVG)</h2>
              <p>Replace <code>favicon.svg</code> and ensure the <code>&lt;link rel="icon"&gt;</code> in <code>index.html</code> points to it:</p>
              <pre>&lt;link rel="icon" type="image/svg+xml" href="favicon.svg"&gt;</pre>
            </section>

            <section>
              <h2>Countdown timer</h2>
              <ul>
                <li><strong>Set target by days:</strong> In <code>script.js</code>, edit <code>DEFAULT_DAYS</code>.</li>
                <li><strong>Reset programmatically:</strong> Call <code>resetCountdown(14)</code> from the console or use the Reset button.</li>
                <li><strong>Override via URL:</strong> Append <code>?days=10</code> or <code>?date=2025-12-31T23:59:59Z</code> to the URL.</li>
                <li><strong>Persisted:</strong> The target time is stored in <code>localStorage</code>. Clear it to restart.</li>
              </ul>
              <pre>// script.js
const DEFAULT_DAYS = 14;
resetCountdown(7); // sets 7 days from now</pre>
            </section>

            <section>
              <h2>Change background and animations</h2>
              <p>Open <code>style.css</code> and adjust theme variables or switch the variant class on the <code>&lt;body&gt;</code>.</p>
              <pre>:root {
  --bg: #0f1021;
  --primary: #6a11cb;
  --accent: #2575fc;
}
&lt;body class="v-glass"&gt; ... &lt;/body&gt;
&lt;body class="v-neon"&gt;  ... &lt;/body&gt;
&lt;body class="v-wave"&gt;  ... &lt;/body&gt;</pre>
            </section>

            <section>
              <h2>Change title, paragraphs, and icons</h2>
              <p>Edit content in <code>index.html</code>. Icons use a CDN such as Remix Icons or Boxicons. Change icon classes to swap visuals:</p>
              <pre>&lt;i class="ri-tools-fill"&gt;&lt;/i&gt;  &lt;!-- Remix Icons --&gt;
&lt;i class="bx bxs-cog"&gt;&lt;/i&gt;     &lt;!-- Boxicons --&gt;</pre>
            </section>

            <section>
              <h2>Colors and typography</h2>
              <p>Colors are defined with CSS variables in <code>style.css</code>. Fonts are loaded from Google Fonts in the document <code>&lt;head&gt;</code>.</p>
            </section>

            <section>
              <h2>Make it your own</h2>
              <ul>
                <li>Swap social links and contact details.</li>
                <li>Adjust border radius and shadows via <code>--radius</code> and <code>--shadow</code>.</li>
                <li>Change component layout by editing the grid in <code>.card-inner</code>.</li>
              </ul>
            </section>

            <section>
              <h2>Troubleshooting</h2>
              <ul>
                <li>If timer doesn’t move, confirm your system clock and <code>localStorage</code> availability.</li>
                <li>Reset the countdown by removing the browser’s <code>localStorage</code> key <code>mp_target_&lt;slug&gt;</code>.</li>
              </ul>
            </section>
          </main>
        </body>
        </html>
        """
    )


def main():
    ensure_dir(OUTPUT_DIR)

    templates_meta = []
    total = 60

    for i in range(total):
        niche = NICHES[i % len(NICHES)]
        palette = PALETTES[i % len(PALETTES)]
        fonts = FONTS[i % len(FONTS)]
        icon_lib = ICON_LIBS[i % len(ICON_LIBS)]
        variant = VARIANTS[i % len(VARIANTS)]
        default_days = 10 + (i % 17)  # 10..26 days variety

        # connector relative path (go back to root index)
        connector_rel = "../../index.html" if OUTPUT_DIR.count("/") > 1 else "../index.html"

        slug = create_template(i + 1, niche, palette, fonts, icon_lib, variant, default_days, connector_rel)

        templates_meta.append({
            "index": i + 1,
            "slug": slug,
            "brand": niche["brand"],
            "niche": niche["niche"],
        })

    # Build gallery and tutorial
    gallery_html = build_gallery(templates_meta)
    write_file("/workspace/index.html", gallery_html)

    tutorial_html = build_tutorial()
    write_file("/workspace/tutorial.html", tutorial_html)

    print(f"Generated {len(templates_meta)} templates in {OUTPUT_DIR}")
    print("Gallery: /workspace/index.html")
    print("Tutorial: /workspace/tutorial.html")


if __name__ == "__main__":
    main()

