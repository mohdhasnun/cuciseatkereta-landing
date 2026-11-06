# Landing-page visual redesign

Development branch: `dev/customer-cases-carousel`.
Content baseline: commit `1d0348e`, the approved header/hero iteration before the new full-page mockup request. Production has not been deployed.

The existing landing page now follows the requested sequence: hero, real customer cases, four service/price cards, a reviews/guarantee/location group, blue FAQ and a dark navy footer with three information groups. Existing photos are reused. The before/after controls and three real cases remain; the rainwater video is still loaded only after Play. No mockup photos, unverified popularity badges, new review claims or new prices were introduced.

The original service descriptions, headings, prices, testimonials, address, hours, FAQ answers and links are retained verbatim. Additional service detail sections and the extra before/after gallery are in labelled expandable panels to keep the main page compact. The original booking/journey content is accessible below the FAQ. Fragment links into those panels remain functional. All eight original FAQ questions remain, and all three original reviews are in a manual horizontal track.

Intentional differences from the mockup: actual workshop photography, the existing RM160 seat starting price and RM80–120 carpet range, 76 reviews and all eight FAQs. Odour treatment displays “Semak Harga” because the mockup's RM50 price is not verified. The original SEO heading text is retained instead of replacing it with the mockup's shorter copy.

Validation completed:

- `verify-redesign.py`: all original text nodes, heading text, hrefs and IDs preserved; no duplicate IDs; original metadata, schema and conversion code unchanged; four service cards, three customer cases and eight FAQs.
- JavaScript syntax and Git whitespace checks passed.
- Browser layout checks at 320, 390, 768, 980 and 1440 px: no horizontal overflow. At phone widths, service cards, trust/location content and footer groups stack into one column.
- Mobile navigation, FAQ accordion, gallery expansion, direct service anchors and review navigation verified. Expanded SEO detail panels also checked at 320 px.
- WhatsApp destinations keep the existing phone number and conversion listener. No synthetic Google Ads conversion was sent during this review.

This is a static site; there is no package build. No Lighthouse or physical-device performance benchmark was run. SEO ranking changes are not measured by this visual review.

Local preview: `http://127.0.0.1:8766/` while the local preview server is running. Desktop and mobile screenshots and the content audit are saved in the task's `outputs` folder. Owner review and explicit approval are required before any production deployment.
