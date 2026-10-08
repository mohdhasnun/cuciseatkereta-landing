# CUCISEAT landing page

Upload `index.html`, `smooth.css`, `assets/`, `robots.txt` and `sitemap.xml` to the same website root in GitHub. Keep any existing admin application and deployment settings. The source file in Downloads has not been overwritten.

The redesign uses the supplied business brief: all seats from RM150+, SUV around RM180–190, MPV around RM200–230, Full Interior Detailing RM600, re-clean warranty within 3 days, operating hours 9am–6pm. Confirm these details before publishing. Other individual service prices were retained from the original HTML.

Preserved: Google Ads tag AW-723532476, conversion AW-723532476/Mm2cCPKwpIkdELz1gNkC, Search Console verification, canonical URL, social metadata/images, business and service schema, real photos, existing customer reviews, Maps links, phone number and WhatsApp enquiry form. FAQ schema matches the revised visible FAQ. No separate GA4 measurement ID was present in the supplied file.

Main WhatsApp links use the existing delegated click handler and `gtag_report_conversion()` once per click, before native navigation. No additional onclick conversion handler was added. The form keeps the existing conversion callback with timeout fallback and includes model, optional plate, seat material, service and issue in the message.

QA: 320, 375, 430, 768, 1024 and 1440px. No horizontal overflow, missing local images, missing section targets or JavaScript runtime errors in the local test. Seven WhatsApp links produced seven mocked conversion events; one valid form submission produced one conversion. FAQ interaction passed. Desktop, tablet and mobile hero previews inspected visually. Images have reserved dimensions; external services were blocked during local QA.

After deployment: use Google Tag Assistant / Google Ads diagnostics to check live conversion receipt, test WhatsApp destination/message and enquiry form on a phone, and verify Google Maps and review profile images. Review the current 5.0 / 76 reviews rating inherited from the original site. Live delivery of Ads conversion events, external links and field performance/layout shift were not verified offline.

`preview-*.png`, `hero-*.png` and `qa-results.json` are review evidence and do not need to be uploaded.

## Second review: spacious layout and search intent

Four core service groups, four benefits, three before/after examples, two main packages and three existing reviews are visible initially. Native HTML details/summary sections hold additional services, individual prices, further gallery examples, the fourth review, the map and enquiry form. All content remains in the served HTML, on desktop and mobile. In-page links automatically open an enclosing details section before navigating.

Search Console terms are covered naturally: cuci seat, cuci seat kereta, cuci kusyen kereta, cuci kusyen, car seat cleaning, car cushion cleaning and basuh seat kereta. Near-me intent is answered by the location section, real address, Maps link and FAQ, including the search phrases cuci seat kereta near me and cuci kusyen kereta near me. No list of hidden keywords or fabricated location pages was added.

Title, description, canonical, social metadata, image alt text, ten service schemas and visible FAQ/schema agreement were checked. Expanded details sections also passed overflow checks at 320, 375, 768 and 1440px. Empty form submission recorded zero conversions. Search rankings, actual Google indexing and live Ads conversion delivery require post-deployment verification.

Google guidance: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing

Latest review changes: removed extra review disclosure and Google review button, extra gallery/process disclosure, method disclosure and additional service disclosure. Retained three existing reviews and three unedited before/after examples. All five individual service prices are now visible as boxes matching the two main packages. Necessary service descriptions and drying information remain in the price section and FAQ, with matching FAQ schema. The about photo uses the second user-supplied brown-seat photo enhanced with the built-in image tool; see IMAGE-NOTES.md for provenance and prompt. QA passed at 320, 375, 430, 768, 832, 1024 and 1440px, with the seven WhatsApp links each recording one mocked conversion. No changes are published yet.

Review 4: starting price updated to RM160 throughout visible copy, FAQ, description and social metadata. The map is now a compact 240px embedded panel below the shop address and directions, 220px on mobile. Service introduction aligns at the top of the heading. Gallery/location padding and preceding section spacing reduced. The duplicate enquiry form section has been removed; WhatsApp links and their conversion handler remain. Seven viewport checks passed, with no broken section targets, FAQ/schema mismatch or runtime errors. External Google Maps loading remains a live-preview/deployment check.

Review 5: removed dashboard/sanitisation paragraph, price-section CTA and price note as requested. Related standalone service schema entries removed to avoid dangling schema URLs; eight service schemas remain. About section now focuses on expertise, with steps 01–03 moved into the final WhatsApp CTA. Spacing between the benefits and problem section reduced to 40px per side on desktop and 28px on mobile. QA: seven widths passed; six remaining WhatsApp links each produced one mocked conversion.

Review 6: top spacing for services, benefits, pricing, reviews and FAQ reduced from 88px to 36px on desktop/tablet and from 60px to 28px on mobile. Bottom spacing after the about/pricing sections and the middle CTA was reduced as well. Content, pricing, SEO and conversion behavior are unchanged. Seven viewport QA checks passed.
