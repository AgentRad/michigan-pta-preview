"""Build a clean, premium PDF proposal for Michigan PTA."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether,
    Table, TableStyle, Frame, PageTemplate, BaseDocTemplate, NextPageTemplate, Image, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

NAVY        = HexColor('#0D1F3D')
NAVY_LIGHT  = HexColor('#1A3358')
GOLD        = HexColor('#B8861F')
GOLD_LIGHT  = HexColor('#D6AF5C')
INK         = HexColor('#14181F')
INK_MUTED   = HexColor('#5C6373')
CREAM       = HexColor('#F4EFE2')
PAPER       = HexColor('#FAF7F0')
LINE        = HexColor('#D6CFC0')

PAGE_W, PAGE_H = LETTER
MARGIN_L = 0.85 * inch
MARGIN_R = 0.85 * inch
MARGIN_T = 0.9 * inch
MARGIN_B = 0.85 * inch

OUTPUT = r"C:\Users\radfe\michigan-pta-preview\Michigan-PTA-Proposal.pdf"
LOGO   = r"C:\Users\radfe\michigan-pta-preview\img\logo-mark.png"

# ---------- Styles ----------
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontName='Times-Bold',
                    fontSize=22, leading=26, textColor=NAVY, spaceAfter=10, spaceBefore=0, alignment=TA_LEFT)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Times-Bold',
                    fontSize=15.5, leading=20, textColor=NAVY, spaceAfter=8, spaceBefore=14, alignment=TA_LEFT)
H3 = ParagraphStyle('H3', parent=styles['Heading3'], fontName='Times-Bold',
                    fontSize=12, leading=16, textColor=NAVY_LIGHT, spaceAfter=4, spaceBefore=8, alignment=TA_LEFT)
Eyebrow = ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8.5, leading=11,
                         textColor=GOLD, spaceAfter=4, alignment=TA_LEFT, letterSpacing=2.2)
Body = ParagraphStyle('Body', fontName='Helvetica', fontSize=10.5, leading=15.5,
                      textColor=INK, spaceAfter=8, alignment=TA_LEFT)
BodyMuted = ParagraphStyle('BodyMuted', parent=Body, textColor=INK_MUTED, fontSize=9.5, leading=14)
Bold = ParagraphStyle('Bold', parent=Body, fontName='Helvetica-Bold')
Italic = ParagraphStyle('Italic', parent=Body, fontName='Helvetica-Oblique', textColor=INK_MUTED)
Mono = ParagraphStyle('Mono', fontName='Courier', fontSize=8.8, leading=12.5,
                      textColor=INK, leftIndent=12, rightIndent=12,
                      spaceBefore=6, spaceAfter=6, backColor=PAPER, borderColor=LINE,
                      borderWidth=0.5, borderPadding=10, alignment=TA_LEFT)
ListItem = ParagraphStyle('ListItem', parent=Body, leftIndent=14, bulletIndent=2, spaceAfter=3)
CoverEyebrow = ParagraphStyle('CoverEyebrow', fontName='Helvetica-Bold', fontSize=9.5,
                              leading=14, textColor=GOLD_LIGHT, letterSpacing=3.5, alignment=TA_LEFT)
CoverTitle = ParagraphStyle('CoverTitle', fontName='Times-Bold', fontSize=46,
                            leading=52, textColor=white, alignment=TA_LEFT, spaceAfter=14)
CoverSub = ParagraphStyle('CoverSub', fontName='Times-Italic', fontSize=21,
                          leading=26, textColor=GOLD_LIGHT, alignment=TA_LEFT, spaceAfter=20)
CoverBody = ParagraphStyle('CoverBody', fontName='Helvetica', fontSize=11.5, leading=17,
                           textColor=HexColor('#E8E0CC'), alignment=TA_LEFT, spaceAfter=12)
CoverMeta = ParagraphStyle('CoverMeta', fontName='Helvetica', fontSize=9, leading=14,
                           textColor=HexColor('#B7AC97'), alignment=TA_LEFT, letterSpacing=1.5)

# ---------- Page decorations ----------
def cover_page(canvas, doc):
    canvas.saveState()
    # Full-bleed navy background
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Subtle gold gradient strip top
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)
    canvas.restoreState()

def interior_page(canvas, doc):
    canvas.saveState()
    # Subtle top gold rule
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 4, PAGE_W, 4, fill=1, stroke=0)
    # Header brand
    canvas.setFillColor(NAVY)
    canvas.setFont('Times-Bold', 10.5)
    canvas.drawString(MARGIN_L, PAGE_H - 0.55 * inch, "Michigan PTA")
    canvas.setFillColor(GOLD)
    canvas.setFont('Helvetica-Bold', 7)
    canvas.drawString(MARGIN_L + 1.05 * inch, PAGE_H - 0.55 * inch, "PHASE 1 PROPOSAL")
    # Right brand
    canvas.setFillColor(INK_MUTED)
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 0.55 * inch, "Prepared by Rad / agentgaming.gg")
    # Footer divider
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN_L, 0.6 * inch, PAGE_W - MARGIN_R, 0.6 * inch)
    # Footer page
    canvas.setFillColor(INK_MUTED)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(MARGIN_L, 0.42 * inch, "michigan-pta-preview.vercel.app")
    canvas.drawRightString(PAGE_W - MARGIN_R, 0.42 * inch, f"{doc.page}")
    canvas.restoreState()

# ---------- Document ----------
doc = BaseDocTemplate(OUTPUT, pagesize=LETTER,
                      leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                      topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                      title="Michigan PTA - Phase 1 Proposal",
                      author="Rad", subject="Website rebuild proposal")

cover_frame = Frame(0.85 * inch, 1.0 * inch, PAGE_W - 1.7 * inch, PAGE_H - 2.0 * inch, id='cover', showBoundary=0)
interior_frame = Frame(MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R, PAGE_H - MARGIN_T - MARGIN_B, id='int', showBoundary=0)

doc.addPageTemplates([
    PageTemplate(id='cover', frames=[cover_frame], onPage=cover_page),
    PageTemplate(id='interior', frames=[interior_frame], onPage=interior_page),
])

# ---------- Story ----------
story = []

# COVER
story.append(Spacer(1, 1.8 * inch))
story.append(Paragraph("PHASE&nbsp;1 &nbsp;&middot;&nbsp; WEBSITE REBUILD PROPOSAL", CoverEyebrow))
story.append(Spacer(1, 14))
story.append(Paragraph("Michigan&nbsp;PTA", CoverTitle))
story.append(Paragraph("Every child. <i>One voice.</i>", CoverSub))
story.append(HRFlowable(width="35%", thickness=2, color=GOLD, spaceBefore=4, spaceAfter=22, lineCap='round'))
story.append(Paragraph(
    "A complete Phase 1 build, accessible from the first line of code, "
    "delivered live by Friday June 5, three business days before your June 8 grant deadline. "
    "Inside your $5,000 to $6,000 band.", CoverBody))
story.append(Paragraph(
    "A working preview is already deployed and auditable today: "
    "<font color='#D6AF5C'>https://michigan-pta-preview.vercel.app/</font>", CoverBody))
story.append(Spacer(1, 1.0 * inch))
story.append(Paragraph("PREPARED FOR", CoverMeta))
story.append(Paragraph("<font color='white' size='12'>Dr. Tonya Whitehead</font><br/>"
                       "<font color='#B7AC97'>President, Michigan PTA</font>", CoverBody))
story.append(Spacer(1, 14))
story.append(Paragraph("PREPARED BY", CoverMeta))
story.append(Paragraph("<font color='white' size='12'>Rad</font><br/>"
                       "<font color='#B7AC97'>rad@agentgaming.gg &nbsp;&middot;&nbsp; agentgaming.gg</font>", CoverBody))

# Switch templates
story.append(NextPageTemplate('interior'))
story.append(PageBreak())

# ---- Executive summary
story.append(Paragraph("AT A GLANCE", Eyebrow))
story.append(Paragraph("Phase 1, live by June 5.", H1))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=4, spaceAfter=14))

summary_data = [
    ['Deadline', 'Phase 1 live by Friday June 5, 2026. Three business days before the grant deadline.'],
    ['Budget', '$5,800 total, inside your $5,000 to $6,000 band. Itemized on the last page.'],
    ['Accessibility', 'WCAG 2.1 AA built into every page from line one. No overlays.'],
    ['Preview', 'https://michigan-pta-preview.vercel.app/ (live now, audit with axe DevTools or WAVE).'],
    ['Volunteer training', 'Written docs site, 8 to 12 screencasts, 2 live Zoom sessions, 6 months email support. Included.'],
    ['Hosting', 'Pressable recommended. GoDaddy fully supported if you stay there.'],
]
tbl = Table(summary_data, colWidths=[1.35 * inch, 4.85 * inch])
tbl.setStyle(TableStyle([
    ('FONT', (0,0), (0,-1), 'Helvetica-Bold', 9),
    ('FONT', (1,0), (1,-1), 'Helvetica', 10),
    ('TEXTCOLOR', (0,0), (0,-1), NAVY),
    ('TEXTCOLOR', (1,0), (1,-1), INK),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('LINEBELOW', (0,0), (-1,-1), 0.4, LINE),
    ('LINEABOVE', (0,0), (-1,0), 0.4, LINE),
]))
story.append(tbl)
story.append(Spacer(1, 0.4 * inch))

# Section helper
def section(num, eyebrow, heading, blocks):
    story.append(Paragraph(eyebrow, Eyebrow))
    story.append(Paragraph(f"<font color='#B8861F'>{num}.</font> &nbsp;{heading}", H1))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=2, spaceAfter=14))
    for block in blocks:
        story.append(block)

def p(text, style=Body):
    return Paragraph(text, style)

def bullet_list(items, style=ListItem):
    out = []
    for it in items:
        out.append(Paragraph(f"&bull;&nbsp; {it}", style))
    return out

# Q1
story.append(PageBreak())
section("Q1", "QUESTION ONE &middot; DELIVERY",
        "Can you deliver a live WordPress site by June 8?",
        [
            p("<b>Yes. Confirmed.</b> Phase 1 lands live by <b>Friday June 5</b>, three business days before your June 8 grant deadline. Three-week build plus one buffer week."),
            Spacer(1, 8),
            p("<b>Week 1 (May 18 to 24). Discovery, IA, design lock.</b>", H3),
            p("Kickoff call with leadership. Audit current michiganpta.org and map every page to a Phase 1 route or to the Phase 2 backlog. Lock visual direction against the working preview. Provision hosting and staging. Install WordPress with an accessibility-first theme (GeneratePress or Kadence) and a child theme."),
            p("<b>Week 2 (May 25 to 31). Build.</b>", H3),
            p("Build all six core templates (Home, About, Advocacy, Membership, Events, Contact) as Gutenberg block patterns so non-technical volunteers edit content by replacing patterns, not by writing HTML. Install internal search (Relevanssi). Migrate Phase 1 content with 301 redirects from the old site. Mobile and cross-browser test. Analytics (GA4 plus Search Console) and security hardening (Wordfence, daily automatic backups)."),
            p("<b>Week 3 (Jun 1 to 5). Accessibility audit, training, ship.</b>", H3),
            p("Full automated and manual accessibility audit. Cross-browser final pass on BrowserStack. Two live volunteer training sessions on Zoom, recorded for the library. Final QA with the content owner. DNS cutover by close of business Friday June 5."),
            p("<b>Week 4 (Jun 6 to 8). Buffer.</b>", H3),
            p("Reserved for any post-launch fixes or last-mile content edits before the grant deadline."),
        ])

# Q2
story.append(PageBreak())
section("Q2", "QUESTION TWO &middot; ACCESSIBILITY",
        "Specific approach to WCAG 2.1 AA. Tools and process.",
        [
            p("Three layers, applied on every commit, never bolted on at the end."),
            p("<b>Build-time discipline (visible on the live preview right now)</b>", H3),
            p("Semantic HTML5 first. ARIA only where native HTML is insufficient. Visible focus indicators on every interactive element (3px outline, 2px offset). Skip-to-main link on every page. Color contrast verified with the WebAIM Contrast Checker during palette selection. Touch targets minimum 44 by 44 pixels. <font face='Courier' size='9'>prefers-reduced-motion</font> honored on every animation. Form labels explicitly associated, errors tied to fields with <font face='Courier' size='9'>aria-describedby</font>, never color-only state."),
            p("<b>Automated CI on every push</b>", H3),
            *bullet_list([
                "<b>axe-core</b> via <font face='Courier' size='9'>@axe-core/cli</font>. Zero violations gates the deploy.",
                "<b>Pa11y CI</b> configured per route against WCAG2AA standard.",
                "<b>Lighthouse</b> accessibility scored on every PR, target 95 or higher.",
                "<b>W3C HTML validator</b> catches malformed semantic structure.",
            ]),
            p("<b>Manual testing on every release</b>", H3),
            *bullet_list([
                "<b>Keyboard-only navigation</b> through every interactive element on every page.",
                "<b>Screen reader testing</b> with VoiceOver (macOS and iOS), NVDA (Windows, the most-used SR in nonprofit testing), and TalkBack (Android).",
                "200% browser zoom on desktop and 400% with reflow on a 1280px viewport.",
                "Color blindness simulation in Chrome DevTools.",
                "WAVE browser extension spot checks.",
            ]),
            p("<b>No overlays.</b> Tools like accessiBe and UserWay are explicitly excluded per industry consensus and your brief."),
            p("<b>Volunteer deliverable:</b> a <i>Maintain Accessibility</i> guide that shows how to write alt text, descriptive link text (never &ldquo;click here&rdquo;), correct heading levels, and how to add ARIA labels inside Gutenberg block patterns."),
        ])

# Q3
story.append(PageBreak())
section("Q3", "QUESTION THREE &middot; PORTFOLIO",
        "Two to three nonprofit or information-focused WordPress sites.",
        [
            p("<b>1. Michigan PTA preview.</b> <font color='#234A82'>https://michigan-pta-preview.vercel.app/</font>", H3),
            p("Built specifically for this proposal in 48 hours. Eight pages, WCAG 2.1 AA throughout, semantic landmarks, focus management, screen-reader friendly, sitemap, robots.txt, OG meta, JSON-LD NGO schema, security headers (HSTS, X-Frame, X-Content-Type, Referrer-Policy, Permissions-Policy, CORP). Solo build, end to end: information architecture, design, code, deploy."),
            p("<b>2. [INSERT YOUR REAL SECOND PORTFOLIO LINK]</b>", H3),
            p("One-sentence description of the site, then a sentence about your specific role."),
            p("<b>3. [INSERT YOUR REAL THIRD PORTFOLIO LINK]</b>", H3),
            p("One-sentence description of the site, then a sentence about your specific role."),
        ])

# Q4
story.append(PageBreak())
section("Q4", "QUESTION FOUR &middot; TRAINING",
        "Training and documentation for rotating non-technical volunteers.",
        [
            p("<b>Included in the Phase 1 price. No upcharge.</b> Four pieces."),
            p("<b>A. Written documentation site.</b>", H3),
            p("Single, searchable on-site docs at <font face='Courier' size='9'>/admin-docs/</font> behind a board-controlled password. Sections: logging in and dashboard tour, editing pages with block patterns, adding events to the calendar, publishing a news post, uploading PDFs and making them accessible, writing accessible alt text and link text, managing the resource library, user roles and adding officers, &ldquo;Do not touch&rdquo; list (theme files, database), backup and recovery, and an &ldquo;I broke something, what do I do&rdquo; quick guide."),
            p("<b>B. Video training library.</b>", H3),
            p("8 to 12 screencasts, 3 to 7 minutes each, hosted on a private Vimeo channel and embedded in the docs. Covers dashboard tour, editing a page, adding an event, publishing a news post, adding a resource to the library, updating officer info, managing user accounts, restoring from backup, and the accessibility quick check."),
            p("<b>C. Two live training sessions on Zoom.</b>", H3),
            p("60 minutes each, recorded and added to the library. Session 1 for content owners (editing). Session 2 for board officers (administration)."),
            p("<b>D. Six months of email support.</b>", H3),
            p("Included. After that, hourly support or a low-cost retainer is available, never required."),
            p("Every doc and video uses plain language, screenshots, and a &ldquo;you can't break the site by following these steps&rdquo; framing.", Italic),
        ])

# Q5
story.append(PageBreak())
section("Q5", "QUESTION FIVE &middot; HOSTING",
        "Hosting recommendation, plus GoDaddy compatibility.",
        [
            p("<b>Primary recommendation: Pressable, Kinsta, or WP Engine (managed WordPress).</b>"),
            p("For an information-heavy nonprofit site with grant funding, managed WordPress is the right call. All three include automatic daily backups, free SSL, a staging environment, plugin and core auto-update with rollback, 24/7 WordPress-specialist support, a real CDN, and a meaningful uptime SLA. Typical cost: $25 to $35 per month. <b>Pressable</b> is the most nonprofit-friendly on price at $25 and a clean fit for the plugins this project needs."),
            p("<b>Will GoDaddy work?</b> Yes. Specifically:", H3),
            *bullet_list([
                "<b>Wordfence</b> (security): works on GoDaddy.",
                "<b>Relevanssi</b> (search): works on GoDaddy.",
                "<b>Yoast SEO</b>: works on GoDaddy.",
                "<b>WP Accessibility</b> plugin: works on GoDaddy.",
                "<b>UpdraftPlus</b> (backups): works on GoDaddy.",
                "<b>axe-core, WAVE, Pa11y</b> (accessibility audits): external tools, work regardless of host.",
            ]),
            p("<b>What you give up on GoDaddy.</b> Slower TTFB on shared plans, no built-in staging on lower tiers, slower customer support for WordPress-specific issues, manual backup management on shared plans, occasional plugin restrictions on the &ldquo;Managed WordPress&rdquo; tier."),
            p("<b>Recommendation order:</b> Pressable ($25/mo, best value for nonprofits) &gt; Kinsta ($35/mo) &gt; WP Engine ($30/mo) &gt; GoDaddy Managed WordPress ($15 to $20/mo, fully functional) &gt; GoDaddy shared (functional but not recommended)."),
            p("If staying on GoDaddy keeps the grant scope clean, I will build there and the site will be fully functional. I want to be transparent that one of the managed hosts is a meaningful upgrade for roughly $10 more per month and saves the volunteer team real ongoing time."),
        ])

# Itemized estimate
story.append(PageBreak())
story.append(Paragraph("INVESTMENT", Eyebrow))
story.append(Paragraph("Itemized Phase 1 estimate.", H1))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=4, spaceAfter=14))

estimate_data = [
    ['Line item', 'One-time'],
    ['Discovery, IA, design lock', '$700'],
    ['WordPress build (6 core pages, block patterns, search, analytics, security)', '$3,200'],
    ['WCAG 2.1 AA implementation and audit', '$900'],
    ['Content migration and 301 redirects (Phase 1 pages)', '$400'],
    ['Documentation site, 12 training videos, 2 live sessions', '$600'],
    ['6 months post-launch email support', 'included'],
    ['Phase 1 total', '$5,800'],
]
est = Table(estimate_data, colWidths=[5.0 * inch, 1.2 * inch])
est.setStyle(TableStyle([
    ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 9),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('BACKGROUND', (0,0), (-1,0), NAVY),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 9),
    ('BOTTOMPADDING', (0,0), (-1,-1), 9),
    ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ('FONT', (0,1), (-1,-2), 'Helvetica', 10),
    ('TEXTCOLOR', (0,1), (-1,-2), INK),
    ('BACKGROUND', (0,1), (-1,-2), PAPER),
    ('LINEBELOW', (0,1), (-1,-2), 0.3, LINE),
    ('FONT', (0,-1), (-1,-1), 'Helvetica-Bold', 11),
    ('BACKGROUND', (0,-1), (-1,-1), CREAM),
    ('TEXTCOLOR', (0,-1), (-1,-1), NAVY),
    ('LINEABOVE', (0,-1), (-1,-1), 1.5, GOLD),
]))
story.append(est)
story.append(Spacer(1, 18))

story.append(Paragraph("Recurring (paid directly to vendors, not invoiced by me)", H3))
recurring_data = [
    ['Hosting (Pressable recommended)', '$25 / month'],
    ['Domain (existing)', 'no charge'],
    ['Plugin licenses (Relevanssi Premium, if filtering needed)', '$100 / year'],
]
rec = Table(recurring_data, colWidths=[5.0 * inch, 1.2 * inch])
rec.setStyle(TableStyle([
    ('FONT', (0,0), (-1,-1), 'Helvetica', 10),
    ('TEXTCOLOR', (0,0), (-1,-1), INK),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ('LINEBELOW', (0,0), (-1,-1), 0.3, LINE),
    ('LINEABOVE', (0,0), (-1,0), 0.3, LINE),
]))
story.append(rec)
story.append(Spacer(1, 18))
story.append(Paragraph("Phase 1 lands inside the $5,000 to $6,000 band you specified. Phase 2 quoted separately on Phase 1 sign-off.", Italic))

# Phase 2 readiness
story.append(Spacer(1, 16))
story.append(Paragraph("PHASE TWO PREVIEW", Eyebrow))
story.append(Paragraph("Built into the Phase 1 architecture.", H2))
story.append(p("Phase 2 ($2,500 to $3,000) is additive, not a rebuild. It includes:"))
story.extend(bullet_list([
    "Full resource library with searchable, filterable content hubs (FacetWP or SearchWP filters).",
    "Flipbook and publication embedding (Real3D FlipBook or PDF.js).",
    "Full content migration and redirects from the current site.",
    "Advanced search with tagging and category filtering.",
    "Multilingual framework, Spanish first (WPML or Polylang).",
    "Approval workflows and governance documentation for leadership transitions (PublishPress Capabilities).",
]))

# Final page: Next steps + contact
story.append(PageBreak())
story.append(Paragraph("NEXT STEPS", Eyebrow))
story.append(Paragraph("Three ways to move this forward.", H1))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=4, spaceAfter=14))

story.append(p("<b>1. Open the preview.</b> Audit it with axe DevTools or WAVE. Click every nav item. Hit Tab through the page to verify keyboard accessibility. The site is the proposal.", H3))
story.append(p("<font color='#234A82'>https://michigan-pta-preview.vercel.app/</font>"))
story.append(Spacer(1, 8))

story.append(p("<b>2. Email me back to lock in a 20-minute call.</b> Walk through the IA together. Ask the hard questions. We can sign and start Week 1 the same day.", H3))
story.append(p("<font color='#234A82'>rad@agentgaming.gg</font>"))
story.append(Spacer(1, 8))

story.append(p("<b>3. If you have feedback on direction, send it.</b> I will spin up a second preview in 24 hours showing the revisions.", H3))

story.append(Spacer(1, 0.6 * inch))
story.append(HRFlowable(width="40%", thickness=1, color=GOLD, spaceBefore=4, spaceAfter=18))
story.append(Paragraph("PREPARED BY", CoverEyebrow.clone('FootCoverEyebrow', textColor=GOLD)))
story.append(Spacer(1, 6))
story.append(p("<b>Rad</b><br/>"
               "Independent web designer and developer<br/>"
               "<font color='#234A82'>rad@agentgaming.gg</font> &nbsp;&middot;&nbsp; agentgaming.gg"))

# Build
doc.build(story)
print(f"PDF built: {OUTPUT}")
print(f"Size: {os.path.getsize(OUTPUT)} bytes")
