# Python Learning Hub — Design System (`DESIGN.md`)

**Direction:** Modern Academic — Clear, Focused, Distinctive  
**Language Standard:** Bahasa Indonesia for explanations; English for established technical terminology.

---

## 1. Design Philosophy & Identity

Python Learning Hub is a university-level open educational resource (OER) for learning Python 3, from programming foundations to production engineering and domain specializations.

The interface must feel like a **well-typeset academic textbook and engineering workbench**, never like a generic SaaS landing page, gamified LMS, or analytics dashboard.

### Anti-Slop Design Read
- **Character:** Disciplined academic clarity. Generous reading measure, crisp hairline borders, restrained color accents, and zero decorative filler.
- **What we reject:** Pulsing status dots, repeated statistic counters, gratuitous blue-purple gradients, uniform pill-shaped everything, floating heavy shadows, and generic AI hype copy.
- **Liveliness Dials:**
  - **Rhythm:** Structured variation between wide catalog grids (home/level) and focused reading columns (`65ch–72ch` prose, side-by-side code + output).
  - **Density:** Compact, scannable cards with real metadata (level, difficulty, duration, competency) rather than tall padded boxes.
  - **Restraint:** Solid surfaces, `1px` borders, subtle elevation only on interactive hover or sticky chrome.

---

## 2. Color System (Semantic Tokens)

All color pairings must meet **WCAG 2.1 AA** contrast minimums (`>= 4.5:1` for normal text, `>= 3.0:1` for large text and UI boundaries/focus indicators).

### Light Mode (`[data-theme="light"]`)
| Token | Hex | Role |
|---|---|---|
| `--bg` | `#f8fafc` | Cool off-white page canvas |
| `--surface` | `#ffffff` | Primary card and content surface |
| `--surface2` | `#f1f5f9` | Secondary inset surface (code headers, callouts) |
| `--surface-high` | `#e2e8f0` | Hover/active subtle fill |
| `--ink` | `#0f172a` | Primary text (dark navy, 17.06:1 on `--bg`) |
| `--muted` | `#475569` | Secondary text, metadata (slate, 7.24:1 on `--bg`) |
| `--line` | `#cbd5e1` | Hairline structural borders |
| `--primary` | `#1556c0` | Academic blue (primary actions, active links) |
| `--on-primary` | `#ffffff` | Text on primary fill (6.72:1) |
| `--primary-soft` | `#e8f0fe` | Tinted blue surface for active states |
| `--accent` | `#006878` | Restrained teal (secondary academic accent, 6.46:1 on white) |
| `--cyan-soft` | `#e0f2f4` | Tinted teal surface |
| `--success` | `#047857` | Verified/ready state |
| `--warning` | `#b45309` | Intermediate/caution state |
| `--danger` | `#b91c1c` | Error/advanced warning state |

### Dark Mode (`[data-theme="dark"]`)
| Token | Hex | Role |
|---|---|---|
| `--bg` | `#0b1320` | Deep navy page canvas |
| `--surface` | `#131f33` | Primary card and content surface |
| `--surface2` | `#1b2a44` | Secondary inset surface |
| `--surface-high` | `#243756` | Hover/active subtle fill |
| `--ink` | `#f8fafc` | Primary text (soft white) |
| `--muted` | `#94a3b8` | Secondary text (muted blue-gray, 6.44:1 on `--surface`) |
| `--line` | `#2d4059` | Structural borders in dark mode |
| `--primary` | `#8ab4f8` | Bright academic blue |
| `--on-primary` | `#041e49` | Deep navy text on bright blue (7.74:1) |
| `--primary-soft` | `#182e4e` | Tinted blue surface |
| `--accent` | `#70d8ec` | Controlled teal accent |
| `--cyan-soft` | `#123847` | Tinted teal surface |
| `--success` | `#34d399` | Verified/ready state |
| `--warning` | `#fbbf24` | Intermediate/caution state |
| `--danger` | `#f87171` | Error/advanced warning state |

---

## 3. Typography

- **Sans-Serif (UI & Long-form Reading):** `'Google Sans Flex Variable', system-ui, -apple-system, sans-serif`
- **Monospace (Python Code, Terminal Output, CLI):** `'Google Sans Code Variable', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`

### Typographic Hierarchy
| Element | Size | Weight | Line Height | Notes |
|---|---|---|---|---|
| Homepage Hero H1 | `clamp(2rem, 4vw, 3rem)` | `700` | `1.12` | Tight tracking `-0.025em` |
| Page / Chapter H1 | `clamp(1.65rem, 3vw, 2.25rem)` | `700` | `1.18` | Clear chapter/module prefix |
| Section H2 | `clamp(1.35rem, 2.2vw, 1.75rem)` | `650` | `1.25` | Sentence case, no forced uppercase |
| Subsection / Card H3 | `1.05rem – 1.2rem` | `650` | `1.3` | Concise, scannable |
| Body Prose | `1rem` (`16px`) | `400` | `1.65` | Optimal for long Indonesian explanations (`max-width: 70ch`) |
| Metadata / Captions | `0.8125rem – 0.875rem` | `500` | `1.45` | Uses `--muted`, never below `12px` |
| Code & Terminal | `0.875rem` (`14px`) | `400` | `1.55` | Tabular alignment, line numbers muted |

---

## 4. Layout, Spacing & Elevation

- **Max Content Width:** `1200px` for hub/catalog pages; `960px` for focused reading/guide pages; `68ch–72ch` for prose paragraphs.
- **Border Radius Scale:**
  - `6px` (`--radius-sm`): Tags, code chips, inline badges.
  - `10px` (`--radius-md`): Buttons, inputs, code blocks, nav links.
  - `14px` (`--radius-lg`): Content cards, section panels.
- **Elevation:** Flat by default with `1px solid var(--line)`. Subtle `--shadow-sm` only on interactive hover or sticky header. No heavy floating shadows on static content.

---

## 5. Component Standards

1. **Header & Navigation:** Single-line nav items (`white-space: nowrap`) on desktop/laptop; clean collapsible drawer/toggle on mobile (`< 768px`) with `>= 44px` touch targets.
2. **Chapter Actions:** Consistent student-facing labels: **Buka Slide**, **Baca Materi**, **Lihat Tugas**. Never expose internal engine names ("Reveal.js") in student-facing labels. Show PPTX download only when the file exists.
3. **Specialization Modules:** Compact horizontal rows or balanced grids showing module ID, order, difficulty, estimated hours, description, and direct action without excessive vertical height.
4. **Code & Output:** High-contrast Shiki tokens in both themes, explicit filename header, accessible copy button with `role="status"` feedback, and clear separation between Python source and verified CPython terminal output.
5. **Accessibility:** Visible `2px solid var(--primary)` `:focus-visible` ring with `2px` offset, proper `role="tablist"` / `role="tab"` / `role="tabpanel"` semantics, `prefers-reduced-motion` respected, zero horizontal overflow across `390px`, `768px`, `1024px`, and `1440px`.

