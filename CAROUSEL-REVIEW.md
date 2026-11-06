# Customer case carousel — development review

Branch: `dev/customer-cases-carousel`. No production deployment requested or performed.

The existing vomit case is now one of three server-rendered HTML stories immediately after the hero. The other stories use the two user-supplied seat images and the complete rainwater extraction video. Images were resized and compressed without retouching. The video retains its content, duration and audio, converted from HEVC to browser-friendly H.264/AAC (540 × 960, about 3.4 MB). The poster is a frame from the actual video at 8 seconds.

The carousel has manual previous/next buttons, pagination, Left/Right/Home/End keyboard navigation, visible focus, and polite announcements. There is no automatic rotation. All stories are present in the HTML; without JavaScript they remain stacked. Video has no source until Play is pressed, and is paused when its story is left.

Existing title, metadata, LocalBusiness/FAQ schema, prices, reviews, location and WhatsApp conversion code are unchanged. Hero wording follows the requested copy. FAQ retains its questions with a blue background and a desktop WhatsApp action on the right. No new prices, reviews or claims of odour removal were added to the urine or rainwater cases.

Validation: JavaScript syntax, Git whitespace checks, metadata/schema/conversion regression checks; visual and functional checks at widths 320, 390, 768 and 1440 px, all three stories at each width. No horizontal overflow. Carousel height stays consistent within each viewport. Verified video is not sourced before Play, plays after click and pauses when changing slides. A static site, so no package build is required. No Lighthouse or real-device benchmark was performed.

Local preview: run `python -m http.server 8766 --bind 127.0.0.1` in this directory, then open `http://127.0.0.1:8766/#servis-rawatan-bau`.

Before production: owner review of desktop/mobile preview and confirmation to publish.
`nHeader/hero update: compact white navigation and full-width navy image treatment, white headline with yellow emphasis, green WhatsApp action. Uses the existing real workshop photo. Price and review values remain unchanged. Added FAQ navigation anchor and moved existing assurance items into the hero. Checked 320, 390, 768, 980 and 1440 px; no overflow. Mobile menu and FAQ anchor verified.
