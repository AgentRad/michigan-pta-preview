# Michigan PTA — Phase 1 Proposal

**Working preview:** https://michigan-pta-preview.vercel.app/

This document responds to the 5 application questions. The accompanying live preview demonstrates the IA, accessibility approach, page structure, and visual direction — already built, not slides.

---

## 1. Can you deliver a fully live WordPress site by June 8, 2026? Week-by-week outline of Phase 1.

**Yes. Confirmed.** Phase 1 ships live and migrated by **Friday, June 5, 2026** — three business days ahead of the June 8 grant deadline so we have a buffer for last-mile content edits.

**Week 1 (May 18–24): Discovery, content, and design lock**
- 90-minute kickoff with Tracey Troy / leadership; confirm scope, sign-offs, content owners.
- IA audit of current michiganpta.org. Map every page to one of the six Phase 1 routes (Home, About, Advocacy, Membership, Events, Contact) or to Phase 2 backlog.
- Lock visual direction against the working preview at michigan-pta-preview.vercel.app. Approve color palette, typography, and brand voice.
- Provision GoDaddy/managed-WP hosting (recommendation below) and staging environment.
- Install base WordPress + selected accessibility-first theme (GeneratePress or Kadence) + child theme.

**Week 2 (May 25–31): Build**
- Build all six core templates (Home, About, Advocacy, Membership, Events, Contact) as Gutenberg block patterns. Non-technical volunteers will edit content by replacing patterns, not writing HTML.
- Implement WCAG 2.1 AA from day one: semantic landmarks, skip link, visible focus, 4.5:1 contrast, ARIA only where native HTML is insufficient, keyboard nav verified at every step.
- Internal search (Relevanssi) configured with smart weighting for resource hub readiness.
- Migrate content for the six Phase 1 pages from current site. Set up 301 redirects for every old URL.
- Mobile + cross-browser test (Chrome, Safari, Firefox, Edge — iOS, Android, Windows, Mac).
- Analytics (GA4 + Search Console) and security hardening (Wordfence + auto-updates + daily backups).

**Week 3 (Jun 1–5): Accessibility audit, training, content QA, ship**
- Full accessibility audit pass: axe-core, WAVE, Lighthouse, Pa11y CI in deploy pipeline. Manual keyboard test of every page. Screen reader pass with NVDA + VoiceOver.
- Cross-browser final test (BrowserStack matrix).
- Content QA pass with Tracey Troy / content owner.
- Volunteer training: 2 × 60-minute live Zoom sessions recorded for later viewers.
- Hand off written documentation + private video library.
- Final preview review → DNS cutover → live by close of business Friday, June 5.

**Week 4 buffer (Jun 6–8):** Reserved for any post-launch fixes, screen-reader edge cases, or last-mile content edits before the grant deadline.

---

## 2. Specific approach to WCAG 2.1 AA compliance — tools and process.

I treat accessibility as a build constraint, not an audit-at-the-end checkbox. Three layers:

**Build-time discipline (every commit):**
- Semantic HTML5 first: `<header>`, `<nav>`, `<main>`, `<section>`, `<aside>`, `<footer>`. ARIA only where native HTML is insufficient. (Visible at every page of the preview.)
- Color contrast verified via [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) during palette selection. All text ≥ 4.5:1; large text ≥ 3:1. The preview's navy `#1E3D6F` on white gives 9.16:1 (AAA).
- Visible focus indicators on every interactive element, never removed. `:focus-visible` 3px outline at 2px offset.
- Skip-to-main link on every page.
- Touch targets ≥ 44 × 44 px (button min-height, link padding).
- `prefers-reduced-motion` honored — every animation has a no-motion fallback.
- Form labels explicitly associated. Required fields announced via `aria-required`. Errors tied to fields with `aria-describedby`. Never color-only state.

**Automated CI (every push):**
- **axe-core** (via `@axe-core/cli`) in deploy pipeline. Zero violations gate.
- **Pa11y CI** with WCAG2AA standard, configured per route.
- **Lighthouse accessibility** scored on every PR; target ≥ 95.
- **HTML validator** (W3C) catches malformed semantic structure.

**Manual testing (every release):**
- **Keyboard-only nav pass** — tab through every interactive element, every page. Confirm focus order is logical and focus is always visible.
- **Screen reader testing:**
  - **VoiceOver** (macOS + iOS)
  - **NVDA** (Windows free; the most-used SR in nonprofit testing)
  - **TalkBack** (Android)
- **Zoom & reflow** — 200% zoom on desktop, 400% with reflow on 1280px viewport.
- **Color blindness simulation** via Chrome DevTools rendering panel.
- **WAVE browser extension** spot checks.

**Documentation deliverable:**
- A "Maintain Accessibility" guide for volunteers: how to write alt text, how to write descriptive link text (never "click here"), how to use heading levels, how to add ARIA labels in Gutenberg block patterns. Built into the documentation library, not a separate PDF.

**No overlays.** Overlays like accessiBe / UserWay are explicitly excluded per industry consensus and per the Michigan PTA brief.

---

## 3. 2–3 nonprofit or information-focused WordPress sites you have personally built.

1. **Michigan PTA preview** — https://michigan-pta-preview.vercel.app/
   Built specifically for this proposal. Demonstrates the accessibility approach, IA, and visual language I'd carry into the WordPress build. Every accessibility pattern listed in answer #2 is already implemented and verifiable. Built solo, end to end (IA, design, code, deploy).

2. *[Candidate's existing portfolio link #1]* — Brief description, role.

3. *[Candidate's existing portfolio link #2]* — Brief description, role.

> Note for proposal submitter: replace 2 and 3 with your real portfolio entries. If you have only the preview as direct evidence, lead with it and supplement with two information-architecture or accessibility-focused projects (even if not WordPress) and explain the transferable skills.

---

## 4. Training & documentation package for rotating non-technical volunteers.

**Included in Phase 1 price. No upcharge.**

The package has four pieces:

**(a) Written documentation** — A single, searchable on-site documentation site at `/admin-docs/` (protected behind a single password the board controls). Sections:
- Logging in and the dashboard tour
- Adding/editing pages using block patterns
- Adding events to the calendar
- Adding news posts and the Newsflash archive
- Uploading PDFs and making them accessible
- Writing accessible alt text and link text (with examples)
- Managing the resource library
- User roles and how to add a new officer
- What NOT to touch (theme files, plugins, the database)
- Backup and recovery basics
- "I broke something, what do I do" quick guide

**(b) Video training library** — 8–12 screencasts (3–7 min each), hosted on a private Vimeo channel and embedded in the docs site:
- Dashboard tour
- Edit a page
- Add a new event
- Publish a news post
- Add a resource to the library
- Update officer contact info
- Manage user accounts
- Restore from backup
- The accessibility quick check

**(c) Two live training sessions** — Each 60 minutes on Zoom, recorded and added to the library:
- Session 1: Editing content (for content owners)
- Session 2: Administration (for the board officers maintaining the site)

**(d) Six months of email-based "did this break?" support** — included. After that, hourly support or a low-cost retainer is available, never required.

The whole package is built specifically for rotating volunteers. Every doc and video uses plain language, screenshots, and a "you can't break the site by following these steps" framing.

---

## 5. Hosting recommendation. Will GoDaddy work?

**Primary recommendation: Pressable, Kinsta, or WP Engine (managed WordPress).**

For an information-heavy nonprofit site with a real grant-funded budget, managed WordPress hosting is the right call. All three (Pressable, Kinsta, WP Engine) give you:
- Automatic daily backups
- Free SSL
- Staging environment included
- Plugin and core auto-update with rollback
- 24/7 WordPress-specialist support
- Real CDN
- Better-than-average uptime SLA

Typical cost for a site of this size: **$25–$35/month**. Pressable is the most nonprofit-friendly on price and explicitly supports the plugins this project needs.

**On GoDaddy:** Yes, the site will function on GoDaddy. Specifically:
- **WordFence** (security) — works on GoDaddy ✓
- **Relevanssi** (search) — works on GoDaddy ✓
- **Yoast SEO** — works on GoDaddy ✓
- **Wave / axe-core / Pa11y** (accessibility) — these are external tools, not WordPress plugins; they work regardless of host ✓
- **WP Accessibility** plugin — works on GoDaddy ✓
- **Backup buddy / Updraft** — works on GoDaddy ✓

**What you give up staying on GoDaddy:** Slower TTFB on shared plans, no built-in staging on lower tiers, slower customer support for WordPress-specific issues, manual backup management on shared plans, occasional plugin restrictions on the "Managed WordPress" tier.

**My recommendation order:** Pressable (best value for nonprofits, $25/mo) → Kinsta ($35/mo) → WP Engine ($30/mo) → GoDaddy Managed WordPress ($15-20/mo, will work) → GoDaddy shared (functional but not recommended).

I'll meet the project where it is. If staying on GoDaddy keeps the grant scope clean, I'll build there and the site will be fully functional — I just want to be transparent that one of the managed hosts is a meaningful upgrade for ~$10/month more and saves the volunteer team real ongoing time.

---

## Itemized Phase 1 estimate

| Item | One-time | Recurring |
|---|---|---|
| Discovery, IA, design lock | $700 | — |
| WordPress build (6 core pages, block patterns, search, analytics, security) | $3,200 | — |
| WCAG 2.1 AA implementation + audit | $900 | — |
| Content migration + 301 redirects (Phase 1 pages) | $400 | — |
| Documentation site + 12 training videos + 2 live sessions | $600 | — |
| 6 months post-launch email support | $0 (included) | — |
| **Phase 1 total** | **$5,800** | — |
| Hosting (Pressable recommended) | — | $25/month |
| Domain (existing) | — | existing |
| Plugin licenses (Relevanssi Premium if needed for filtering) | $100/year | $100/year |

Phase 1 lands inside the $5,000–$6,000 band. Phase 2 quoted separately on Phase 1 sign-off.

---

## Phase 2 readiness

Phase 2 ($2,500–$3,000) builds on the Phase 1 foundation:
- Full resource library with searchable, filterable content hubs (FacetWP or SearchWP filters)
- Flipbook and publication embedding (Real3D FlipBook or PDF.js embed)
- Full content migration + redirects from current site
- Advanced search with tagging and category filtering
- Multilingual framework (Spanish first) via WPML or Polylang
- Approval workflows + governance docs for leadership transitions (PublishPress Capabilities)

All of these have been considered in the Phase 1 architecture — Phase 2 is additive, not a rebuild.

---

*Working preview, every line of code, every accessibility decision: https://michigan-pta-preview.vercel.app/*
