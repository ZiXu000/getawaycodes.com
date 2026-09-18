# getawaycodes.com

Travel promo codes, copied from each brand's own website. One brand per page.

Every offer on the site is copied word for word from the deals or promotions block on the brand's
own website, with the exact place it came from and the date it was checked. Where a brand prints no
promo code, the page says so instead of inventing one. Where an offer is limited to members of
another organisation, the row says so next to the discount. Where a deadline is a countdown we
cannot read, the row says that too.

## Pages

- `/` — brand directory
- `/brand/priceline.html`
- `/brand/royal-caribbean.html`
- `/brand/hilton.html`
- `/brand/celebrity-cruises.html`
- `/brand/wyndham.html`
- `/privacy.html`, `/about.html`, `/contact.html`
- `/404.html` — served for any path that does not exist (we do not redirect to the homepage)

## Build

There is no bundler. The files in this repository are the site. To regenerate the SEO files:

```
python tools/make_seo.py
```

That writes `robots.txt` (three lines) and `sitemap.xml` (every page above, each with a `lastmod`).

## Not in this repository

Six brand pages that were researched but did not make it into the site are deliberately not
included here, so they cannot be published by accident.
