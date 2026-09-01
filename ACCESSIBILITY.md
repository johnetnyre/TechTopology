# Accessibility maintenance checklist

The templates establish an accessible baseline, but accessibility also depends on future conference content.

Before publishing a substantial update:

- Keep exactly one descriptive H1 on each page.
- Do not skip heading levels merely for visual styling.
- Use descriptive link text; avoid repeated links labeled only “click here.”
- Provide alternative text for informative images.
- Use empty alternative text (`alt=""`) for purely decorative images.
- Include captions or transcripts for time-based media.
- Do not communicate meaning through color alone.
- Keep tables for genuinely tabular data and provide header cells.
- Test every interactive control by keyboard.
- Zoom the page to 200% and confirm that content still reflows and remains usable.
- Check mobile widths for horizontal scrolling.
- Run the GitHub Actions accessibility workflow and resolve failures.
- Perform a manual screen-reader spot check for major structural changes.

The repository's automated tests use Pa11y with the WCAG 2 AA standard. They are intended as a regression guard, not a substitute for manual accessibility review.
