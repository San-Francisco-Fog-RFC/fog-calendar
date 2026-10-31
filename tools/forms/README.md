# Jotform form styles

Styles for the Fog Rugby liability waiver (Jotform form `263017776830057`) are self-hosted here instead of living in Jotform's "Inject Custom CSS" box, which silently truncates anything over about 41 KB.

- **Live file:** `docs/assets/forms/fog-waiver.css` → `https://events.fogrugby.com/assets/forms/fog-waiver.css`
- **Jotform box:** contains only the `@import` line for that file. Bump the `?v=` value after each change so browsers fetch the new version straight away.

## Scoping

Jotform's builder doesn't rewrite imported files, so the file scopes itself:

| Selector starts with | Applies to |
|---|---|
| `html.supernova body …` | Live form only (layout: photo panel, steps, pinned buttons, pride stripe) |
| `.supernova …` | Live form and the builder canvas (fonts, colours, labels, section cards) |

The live form is `<html class="supernova">`; the builder's `<html>` has no class.

## Editing

1. Edit `docs/assets/forms/fog-waiver.css` directly for small changes.
2. Put brand-new behaviour in `tools/forms/features.css` and fixes that must not change the current look in `tools/forms/extra-rules.css` if you regenerate.
3. To regenerate from what Jotform is serving and prune dead rules: `node tools/forms/prune-jotform-css.js` (needs Playwright + Chromium). It refuses to write the file unless the result renders identically on all three pages at desktop and phone width.
4. Commit to `main`, wait for GitHub Pages (about a minute), then bump `?v=` in the Jotform box.

Nothing in these tools submits the form.
