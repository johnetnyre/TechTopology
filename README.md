# Tech Topology — GitHub Pages site

A lightweight, accessible static website for the Tech Topology Conference at Georgia Tech. The site is generated from simple YAML data and deployed automatically with GitHub Pages.

## What to edit most years

Routine conference updates happen in `_data/`:

- `conference.yml` — year, dates, location, organizers, deadlines, navigation
- `speakers.yml` — invited speakers and affiliations
- `schedule.yml` — daily schedule, lightning talks, invited abstracts
- `lightning_abstracts.yml` — lightning-talk abstracts
- `local.yml` — venue and hotel information
- `previous.yml` — links to earlier meetings
- `past_speakers.yml` — long-term speaker archive
- `photos.yml` — photo filenames, alternative text, and captions

The visual design is in `assets/css/site.css`. Most annual updates should not require touching it.

## Publish on GitHub Pages

1. Create a new GitHub repository, for example `TechTopology`.
2. Upload the contents of this folder to the repository.
3. Make sure the default branch is named `main`.
4. In **Settings → Pages**, set **Source** to **GitHub Actions**.
5. Push a change or run **Actions → Build, test, and deploy GitHub Pages → Run workflow**.
6. GitHub will build, run structural checks, run Pa11y WCAG 2 AA automated tests, and deploy the site.

The templates use a deployment base path supplied by GitHub Pages, so the same repository works as either a project site such as `username.github.io/TechTopology/` or, after DNS setup, a custom domain.

## Local preview

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python scripts/build.py
python scripts/check_html.py
python -m http.server 8000 --directory _site
```

Then open `http://localhost:8000/`.

## Starting a new conference year

1. Change the year, dates, deadlines, status, and organizers in `_data/conference.yml`.
2. Replace `_data/speakers.yml` with the new speaker list.
3. Replace the program in `_data/schedule.yml` and `_data/lightning_abstracts.yml`.
4. Add the previous year to `_data/previous.yml`.
5. Add the previous year's invited speakers to `_data/past_speakers.yml`.
6. Add conference photos to `assets/images/photos/` and `_data/photos.yml` when available.
7. Set `status: current` and change `status_label` to something appropriate, such as `2026 conference`.
8. Commit and push. GitHub Pages republishes automatically.

## Accessibility

The site includes:

- semantic header, navigation, main, section, article, and footer landmarks;
- one page-level H1 per page and a consistent heading hierarchy;
- skip navigation;
- keyboard-accessible responsive menus and disclosure widgets;
- conspicuous keyboard focus states;
- responsive reflow down to narrow mobile widths;
- Georgia Tech-inspired color combinations selected for WCAG AA contrast;
- reduced-motion support;
- touch targets sized for mobile use;
- live status text for the past-speaker search;
- automated structural HTML checks;
- Pa11y CI checks against WCAG 2 AA before deployment.

Automated testing cannot prove complete WCAG compliance. New content should still be reviewed with keyboard-only navigation and, when practical, a screen reader. Images added to the photo gallery should have meaningful alternative text or be marked decorative as appropriate.

See `ACCESSIBILITY.md` for the editorial checklist.

## Georgia Tech branding

The theme uses Georgia Tech-inspired colors and a text treatment rather than redistributing official proprietary logo files. If an approved Georgia Tech logo is desired, obtain it from the Institute's official brand resources and add it locally with appropriate alternative text.

## Source migration note

The site is configured for the 2026 Tech Topology Conference, December 11–13, 2026. The long-term archive retains earlier Tech Topology speaker and conference information. The layout, navigation, accessibility structure, and content workflow are designed for simple annual reuse.
