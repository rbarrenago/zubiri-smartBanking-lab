# ZUBIRI FinAI Lab — GitHub Pages v1.1

A self-contained bilingual educational demonstration. All transactions are fictitious and synthesized.

## How to publish an update (no command line)

1. Unzip this package on your computer.
2. Open the root of your existing GitHub repository `zubiri-smartBanking-lab`.
3. Choose **Add file → Upload files**, upload the extracted `index.html`, both demo HTML files, `README.md`, and `.nojekyll` into the **root**, not into a new subfolder. Use **Commit changes** to replace the older versions.
4. Check **Actions** for the latest GitHub Pages deployment; refresh the browser to see the new version.

If this is your first upload, configure Settings → Pages → Deploy from a branch → main → /(root).

## What changed

- Added 3 complete, navigable educational sections in both Basque and Spanish:
  1. What the demo does, including a concrete real row from the *synthetic* transactions CSV.
  2. The 493-day synthetic dataset and the crucial distinction between ML inputs and simulator inputs.
  3. The ML forecast, temporal holdout, baseline MAE, cash-balance equation, and simulation uncertainty.
- Added an explicitly **future, independent** SmartCity research connection focused on urban mobility, events, and public planning — **not** a bank service for local commerce or data sharing.
- Kept all interactive controls, forecasts and CSV export unchanged.

The demos are static HTML with embedded synthetic data; no external services or credentials are required.
Do not commit customer data or banking credentials. This is not financial advice or a production bank product.
