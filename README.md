# ZUBIRI smart Banking Lab — GitHub Pages v1.2 · Banking review

Bilingual (Basque / Spanish) educational proof of concept showing ML daily-sales forecasting plus a **separate** simplified business cash-flow simulator. All balances, revenues and payments are synthetic; this is **not** a regulated stress test, a bank's liquidity-risk model, a creditworthiness assessment, or operational financial advice.

## Open in browser
- `index.html`: bilingual entry point
- `ZUBIRI_FinAI_Lab_Demo_EU.html`: Basque interactive demo
- `ZUBIRI_FinAI_Lab_Demo.html`: Spanish interactive demo
- `data/synthetic_transactions.csv`: complete 493-row synthetic training case
- `technical/MODEL_CARD_EU.md`, `technical/MODEL_CARD_ES.md`: methods, caveats and validation gates
- `technical/build_model.py`: code to regenerate synthetic dataset/model outputs

## Update an existing GitHub Pages repository (no command line)
1. Extract the ZIP on your computer.
2. Open your existing `zubiri-smartBanking-lab` repository → **Add file → Upload files**.
3. Upload the files and folders to the **repository root**, preserving the `data/` and `technical/` folders. Confirm the replacements and **Commit changes**.
4. GitHub Pages configuration: `Settings → Pages → Deploy from a branch → main → /(root)`. After deployment, refresh your page.

Only `index.html`, the two demo HTML files, and `data/synthetic_transactions.csv` are required for the interactive site. The technical resources are recommended for due diligence/reproducibility.

## Changes from v1.1
- Tightened bank-domain terminology: settlements vs sales; projected business cash balance vs available account balance; simulation threshold vs credit-risk alert; stress scenario vs regulatory stress testing.
- Added bank-facing section 04 in both languages (business banking, data science, security/risk and regulatory governance).
- Added glossary, pilot validation gates, student skill mappings and explicit methodological cautions.
- Kept the SmartCity future research section independent of any banking/commercial data exchange.
- Kept simulation controls (30/60/90 days; scenarios and sliders), output and CSV exports.

## Important methodological limitation
The baseline in the 75-day test uses prior *observed* test-window sales for rolling weekday averages. The ML comparison is therefore **not** a fully horizon-matched forecasting study. For a serious pilot, run comparable rolling-origin backtests at defined horizons, and test actual cash-balance predictions as well as sales.

No private banking/customer data, API keys or credentials should be added to this public GitHub repository.
