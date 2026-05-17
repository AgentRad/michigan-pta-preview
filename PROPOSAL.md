# Michigan PTA. Phase 1 Proposal.

**Working preview:** https://michigan-pta-preview.vercel.app/

The link above is the full site, built before this pitch so direction is visible, not promised. All 8 pages are live, all routes verified, WCAG 2.1 AA implemented end to end.

---

## EMAIL VERSION (paste into a fresh message)

**Subject:** Built a Michigan PTA preview before pitching, Phase 1 ready for June 8

Hi Tracey,

Saw the brief for Michigan PTA's website rebuild and wanted to show direction before I pitch. Built a working preview that hits every Phase 1 page (Home, About, Advocacy, Membership, Events, Resources, Contact) plus an accessibility statement page:

https://michigan-pta-preview.vercel.app/

WCAG 2.1 AA is built into every page from the start. Skip link, semantic landmarks, visible focus, 4.5:1+ contrast everywhere, autoComplete on forms, keyboard nav, prefers-reduced-motion, ARIA where native HTML is not enough. No overlays. You can audit the live site with axe DevTools or WAVE right now.

I can deliver Phase 1 fully live by June 5, three business days ahead of your June 8 grant deadline. Fixed price in the $5,000 to $6,000 band you specified.

Quick answers to the 5 application questions are below. Happy to jump on a 20 minute call this week.

Rad

---

## LINKEDIN DM (shorter, paste into a fresh message)

Hi Tracey,

Saw Michigan PTA's brief for the website rebuild. Built a working preview before pitching so you can see direction first:

https://michigan-pta-preview.vercel.app/

All Phase 1 pages, WCAG 2.1 AA from the start, no overlays. June 8 deliverable, fixed price in your band.

Quick call this week?

Rad

---

# ANSWERS TO THE 5 APPLICATION QUESTIONS

## 1. Can you deliver a fully live WordPress site by June 8, 2026, and a week by week outline of Phase 1?

Yes. Phase 1 lands live by Friday June 5, three business days before the June 8 grant deadline. Three week build with one buffer week.

**Week 1 (May 18 to 24). Discovery, IA, design lock.**
Kickoff call with leadership. Audit current michiganpta.org and map every page to a Phase 1 route or to the Phase 2 backlog. Lock visual direction against the working preview. Provision hosting and staging. Install WordPress with a vetted accessibility first theme (GeneratePress or Kadence) and a child theme.

**Week 2 (May 25 to 31). Build.**
Build all six core templates (Home, About, Advocacy, Membership, Events, Contact) as Gutenberg block patterns so non technical volunteers edit content by replacing patterns, not by writing HTML. Install internal search (Relevanssi). Migrate Phase 1 content with 301 redirects. Mobile and cross browser test. Analytics (GA4 + Search Console) and security (Wordfence, automatic backups).

**Week 3 (Jun 1 to 5). Accessibility audit, training, ship.**
Full automated and manual accessibility audit. Cross browser final pass on BrowserStack. Two live volunteer training sessions on Zoom, recorded for the library. Final QA with the content owner. DNS cutover by close of business Friday June 5.

**Week 4 (Jun 6 to 8). Buffer.**
Reserved for any post launch fixes or last mile content edits before the grant deadline.

---

## 2. Specific approach to WCAG 2.1 AA compliance. Tools and process.

Three layers, applied on every commit, not bolted on at the end.

**Build time discipline.**
Semantic HTML5 first. ARIA only where native HTML is insufficient. Visible focus indicators on every interactive element (3px outline, 2px offset). Skip to main content link on every page. Color contrast verified with the WebAIM Contrast Checker during palette selection. Touch targets minimum 44 by 44 pixels. `prefers-reduced-motion` honored. Form labels explicitly associated, errors tied to fields with `aria-describedby`, never color only state. All of this is visible and auditable right now on the live preview.

**Automated CI on every push.**
- axe-core via `@axe-core/cli`. Zero violations gates the deploy.
- Pa11y CI configured per route against WCAG2AA standard.
- Lighthouse accessibility scored on every PR, target 95 or higher.
- W3C HTML validator catches malformed semantic structure.

**Manual testing on every release.**
- Keyboard only navigation through every interactive element on every page.
- Screen reader testing with VoiceOver (macOS and iOS), NVDA (Windows, the most used SR in nonprofit testing), and TalkBack (Android).
- 200% browser zoom on desktop and 400% with reflow on a 1280px viewport.
- Color blindness simulation in Chrome DevTools.
- WAVE browser extension spot checks.

No overlays. Tools like accessiBe and UserWay are explicitly excluded per industry consensus and your brief.

Volunteer deliverable: a "Maintain Accessibility" doc that shows how to write alt text, descriptive link text (never "click here"), correct heading levels, and how to add ARIA labels inside Gutenberg block patterns.

---

## 3. 2 to 3 nonprofit or information focused WordPress sites you have personally built.

1. **Michigan PTA preview.** https://michigan-pta-preview.vercel.app/
   Built specifically for this proposal in 48 hours. Eight pages, WCAG 2.1 AA throughout, semantic landmarks, focus management, screen reader friendly, sitemap, robots, OG meta, JSON-LD NGO schema, security headers. Full IA, design, code, deploy. Solo build.

2. *[Insert your strongest information focused site here, with one line describing your specific role.]*

3. *[Insert your second site here, with one line describing your specific role.]*

> Honesty note: if these spots are static HTML or non WordPress builds, lead with what they prove (information architecture for content heavy sites, accessibility, content owner friendly editing) rather than overclaim a WordPress portfolio that does not exist. A confident "here is the preview, here are two adjacent projects, here is why the skills transfer cleanly" reads better than a vague claim.

---

## 4. Training and documentation package for rotating non technical volunteers.

Included in the Phase 1 price. No upcharge. Four pieces.

**A. Written documentation site.**
Single, searchable on site docs at `/admin-docs/` behind a board controlled password. Sections:
- Logging in and dashboard tour
- Editing pages with block patterns
- Adding events to the calendar
- Publishing a news post
- Uploading PDFs and making them accessible
- Writing accessible alt text and link text
- Managing the resource library
- User roles and adding officers
- "Do not touch" list (theme files, database)
- Backup and recovery
- "I broke something, what do I do"

**B. Video training library.**
8 to 12 screencasts, 3 to 7 minutes each, hosted on a private Vimeo channel and embedded inside the docs:
1. Dashboard tour
2. Edit a page
3. Add an event
4. Publish a news post
5. Add a resource to the library
6. Update officer info
7. Manage user accounts
8. Restore from backup
9. The accessibility quick check

**C. Two live training sessions on Zoom.**
60 minutes each, recorded and added to the library. Session 1 for content owners (editing). Session 2 for board officers (administration).

**D. Six months of email "did this break" support.**
Included. After that, hourly support or a low cost retainer is available but never required.

Every doc and video uses plain language, screenshots, and a "you can't break the site by following these steps" framing.

---

## 5. Hosting recommendation. Will GoDaddy work?

**Primary recommendation: Pressable, Kinsta, or WP Engine (managed WordPress).**

For an information heavy nonprofit site with grant funding, managed WordPress is the right call. Pressable, Kinsta, and WP Engine all include automatic daily backups, free SSL, a staging environment, plugin and core auto update with rollback, 24/7 WordPress specialist support, a real CDN, and a meaningful uptime SLA.

Typical cost for a site this size: $25 to $35 per month. Pressable is the most nonprofit friendly on price and a clean fit for the plugins this project needs.

**Will GoDaddy work?** Yes. Specifically:
- Wordfence (security): works on GoDaddy.
- Relevanssi (search): works on GoDaddy.
- Yoast SEO: works on GoDaddy.
- WP Accessibility plugin: works on GoDaddy.
- UpdraftPlus (backups): works on GoDaddy.
- axe-core, WAVE, Pa11y (accessibility audits): external tools, work regardless of host.

**What you give up on GoDaddy.** Slower TTFB on shared plans, no built in staging on lower tiers, slower customer support for WordPress specific issues, manual backup management on shared plans, occasional plugin restrictions on the "Managed WordPress" tier.

**My recommendation order.** Pressable ($25/month, best value for nonprofits) > Kinsta ($35/month) > WP Engine ($30/month) > GoDaddy Managed WordPress ($15 to $20/month, will work) > GoDaddy shared (functional but not recommended).

If staying on GoDaddy keeps the grant scope clean, I will build there and the site will be fully functional. I just want to be transparent that one of the managed hosts is a meaningful upgrade for roughly $10 more per month and saves the volunteer team real ongoing time.

---

## Itemized Phase 1 estimate

| Item | One time |
|---|---|
| Discovery, IA, design lock | $700 |
| WordPress build (6 core pages, block patterns, search, analytics, security) | $3,200 |
| WCAG 2.1 AA implementation and audit | $900 |
| Content migration and 301 redirects (Phase 1 pages) | $400 |
| Documentation site, 12 training videos, 2 live sessions | $600 |
| 6 months post launch email support | included |
| **Phase 1 total** | **$5,800** |

Recurring: hosting (Pressable recommended) $25/month. Domain (existing). Plugin licenses (Relevanssi Premium if filtering needed) $100/year.

Phase 1 lands inside the $5,000 to $6,000 band you specified. Phase 2 quoted separately on Phase 1 sign off.

---

## Phase 2 readiness

Phase 2 ($2,500 to $3,000) builds on the Phase 1 foundation:
- Full resource library with searchable, filterable content hubs (FacetWP or SearchWP filters)
- Flipbook and publication embedding (Real3D FlipBook or PDF.js)
- Full content migration and redirects from current site
- Advanced search with tagging and category filtering
- Multilingual framework, Spanish first (WPML or Polylang)
- Approval workflows and governance docs for leadership transitions (PublishPress Capabilities)

All of these are considered in the Phase 1 architecture. Phase 2 is additive, not a rebuild.
