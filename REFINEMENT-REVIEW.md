# Final UI/UX refinement — development review

Branch: `dev/customer-cases-carousel`. Before baseline: `a91278d`. No merge into the production branch and no deployment performed.

## Hero

- The original workshop image is unchanged. Desktop uses a capped image width and a 38% vertical position so the full cap/head, face, seat and cleaning activity remain visible. Tablet uses its own 18% position. Phone layouts show the original photo in a separate 290 px frame below the copy, with a top fade into navy.
- The existing H1 text is unchanged. Only “Selesa.” has the gold, two-path SVG brush underline; there is no animation or glow. “Kereta —” stays together to prevent a stranded dash on tablet.
- The description is shortened to two lines on tested desktop/tablet widths. The starting RM160 price, Seri Kembangan location, WhatsApp and service/price actions remain. The three ancillary hero badges are removed.

## Content changes

| Previous component | Final treatment | Unique information retained |
| --- | --- | --- |
| “Interior kereta, kami uruskan” service overview | Removed as a repeated visual section | Four primary service cards retain their full descriptions and prices; extra service rates remain accessible. The original `#servis` anchor now leads to the pricing section. |
| “Cuci kusyen kereta. Jaga keselesaan perjalanan” about panel | Merged into the service/benefit/location content | Fabric/leather scope, inspection of material and affected areas, price/time confirmation, shop location and phone remain. The original `#tentang` anchor leads to the three advantages. |
| Four “Kenapa Pilih Kami” cards | Three visible advantages | Focus on upholstery/interior, clear scope/price/time and cleaning according to the cause. The existing three-day reclean guarantee remains in the trust section and FAQ. |
| Four repeated cause-of-odour cards | One short visible diagnostic paragraph | Smoke, milk, vomit, urine, food, moisture, concealed residue and rain/flood context remain; no new outcome claim is added. |
| Hidden extra before/after gallery | Three compact visible comparison cards after pricing | Original gallery photos and individual case headings retained. |
| Repeated mid-page CTA and expandable booking panel | Removed as repeated promotional panels | The three-step contact/price/drop-off process is consolidated below the advantages. WhatsApp actions, FAQ booking instructions and the existing `/book/` route remain. |

Final order: header/hero → three real cases → four service cards → compact gallery → three advantages → reviews/guarantee/location → FAQ → footer. Content is no longer stored in a broad expandable SEO panel. The additional-service price accordion and FAQ are functional disclosure components.

## Google proof corrections

The public Google Maps profile was checked on 6 November 2026: 5.0 from 76 reviews. Rupert Chen, Weng Ji and Fatin Syafinaz were all found. The Weng Ji and Fatin quotations on the previous page were paraphrases inside quotation marks; these are now exact, clearly labelled excerpts from their Google reviews. Reviewer profile-wide review counts were removed because they change over time. No fabricated reviewer, rating or price was added.

Source: https://www.google.com/maps/place/Cuci+Seat,+Kusyen,+Karpet+Kereta+l+Pakar+Hygiene+Dalaman+Kereta/@2.9851355,101.6599821,18z/data=!4m8!3m7!1s0x31cdc9695874d8e5:0x88d49dc3d959a4c2!8m2!3d2.9851328!4d101.6612675!9m1!1b1!16s%2Fg%2F11hzd06vbb

## Validation

- Source text decreases from 1,716 to 1,360 words (about 21%), including the expressly requested consolidation and verified review excerpts.
- Unchanged: canonical and metadata, schema, conversion code, main H1 wording, four service cards and prices, three real customer cases, all eight FAQs, address, hours and booking route.
- All original ID targets remain; no duplicate IDs or broken fragment links. All ten WhatsApp links use the correct number, populated messages and safe new-tab attributes.
- Layouts checked at 320, 390, 600, 768, 980, 1440 and 1920 px without horizontal overflow. Cropping visually checked on desktop, tablet and phone; desktop description stays within two lines.
- Carousel buttons/keyboard, before/after range keyboard, delayed video loading/playback/pause, FAQ, review navigation, mobile menu and gallery navigation tested.
- JavaScript syntax, local media existence, HTML invariants and Git whitespace checks passed. This static site has no package build; no bundle build is required. No synthetic Ads conversion was sent, and no physical-device/Lighthouse benchmark was performed.

Preview: `http://127.0.0.1:8766/`. Before screenshots remain in `outputs/redesign-desktop.png` and `outputs/redesign-mobile.png`; final screenshots use the `refinement-` prefix. Content and browser audit results are saved alongside them. Production publication awaits explicit owner approval.
