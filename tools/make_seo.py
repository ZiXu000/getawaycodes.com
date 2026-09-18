#!/usr/bin/env python3
"""Generate robots.txt and sitemap.xml for getawaycodes.com.

robots.txt is three lines: User-agent, Allow, Sitemap (the sitemap URL has no trailing slash).
sitemap.xml lists every page that is in the site: the homepage, the five brand pages and the
three required pages (privacy, about, contact). Each entry carries a lastmod date.

Run:  python tools/make_seo.py
"""
import datetime
import os

DOMAIN = "getawaycodes.com"
BASE = "https://" + DOMAIN
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    ("/", "1.0"),
    ("/brand/priceline.html", "0.9"),
    ("/brand/royal-caribbean.html", "0.9"),
    ("/brand/hilton.html", "0.9"),
    ("/brand/celebrity-cruises.html", "0.9"),
    ("/brand/wyndham.html", "0.9"),
    ("/privacy.html", "0.3"),
    ("/about.html", "0.3"),
    ("/contact.html", "0.3"),
]

today = datetime.date.today().isoformat()

with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: " + BASE + "/sitemap.xml")

rows = []
for path, pri in PAGES:
    rows.append("  <url>\n    <loc>" + BASE + path + "</loc>\n    <lastmod>" + today +
                "</lastmod>\n    <priority>" + pri + "</priority>\n  </url>")

with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")

print("wrote robots.txt (3 lines) and sitemap.xml (" + str(len(PAGES)) + " urls)")
