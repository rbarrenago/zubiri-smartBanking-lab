# ZUBIRI Smart Banking Lab — GitHub Pages v1.4 · Banking edition

Bilingual (Basque / Spanish) educational prototype: **ML forecasting of daily sales** plus a separate simulated SME cash-flow projection. All data and balances are synthetic. Not a bank liquidity-risk model, credit score, regulatory stress test, or financial advice.

## Open in browser
- `index.html`: bilingual landing page
- `ZUBIRI_Smart_Banking_Lab_Demo_EU.html`: Basque interactive demo
- `ZUBIRI_Smart_Banking_Lab_Demo.html`: Spanish interactive demo
- `data/synthetic_transactions.csv`: complete 493-day synthetic history (daily aggregates, not individual transactions)
- `technical/MODEL_CARD_EU.md`, `technical/MODEL_CARD_ES.md`: data, validation, assumptions, limitations
- `technical/build_model.py`: reproducible synthetic data generator and ML trainer (writes CSV into `data/` and model payload into `technical/`)
- `technical/requirements.txt`: Python dependencies

## Upload to your existing GitHub Pages repository
1. Unzip the package on your device.
2. Open the **repository you are already using** for this project. The repository itself does not have to be renamed for its displayed project title to change.
3. Select **Add file → Upload files**. Upload these files and folders to the **root of the repository**, preserving `technical/`, `data/`, and `materials/`. Commit to `main`.
4. IMPORTANT: the previous demo files had older names. **Delete those old demo HTML files** from the repository after uploading these new versions, so visitors do not find outdated pages. (GitHub's web interface can delete them individually.)
5. Check `Actions` for a successful GitHub Pages deployment. If needed: `Settings → Pages → Deploy from a branch → main → /(root)`.
6. Optional, separately: to rename the GitHub repository itself, open its `Settings → General → Repository name` and choose `zubiri-smart-banking-lab`. If you rename it, check GitHub Pages settings and share the updated site URL; the prior GitHub Pages address should not be assumed to redirect automatically.

## v1.4 improvements / review findings
- Removed unrelated future-research content from both language versions and landing page.
- Corrected the backtest comparison: fixed weekday-mean baseline calculated **only on the original training period**, same information cutoff as the ML predictor. Synthetic 75-day holdout: **ML MAE €121.89** versus **baseline €137.31** (illustrative **11.2%** improvement). Not proven on real merchant data.
- Explicit assumption: **100% of synthetic daily sales settle through a hypothetical POS/TPV after two calendar days**; weekends/holidays, cash sales, other bank accounts and working-capital facilities are not modeled.
- CSV exports include scenario parameters (sales change, supplier-cost change, extra settlement delay, exceptional expense, simulation count) to facilitate review.
- Kept clear separation between sales forecast, cash-flow rules, simulated outcome distribution, and operational or credit-risk decisions.
- Main interactive functionality is unchanged: 30/60/90 days, scenario presets, sliders, reset, chart, and CSV.

## Scientific and banking limitations
One synthetic dataset and one time-based holdout do not establish generalization. No rolling-origin/multi-horizon backtests, independently calibrated predictive intervals, external validation, or actual cash-balance accuracy tests have been completed. Simulated crossings of the €5,000 illustrative threshold are **not real financial-risk probabilities**. Any real pilot requires approved data, consent or other lawful basis where applicable, reconciliation, governance, security, human oversight, and model validation.

The current webpage is self-contained and makes no banking API calls. **Never commit private customer/bank information, API keys or credentials to a public repo.**

## Branding update in v1.4
- Project title, two demo titles, HTML branding, navigation, metadata, downloadable CSV filenames, model cards, and README now use **ZUBIRI Smart Banking Lab**.
- Included a matching Spanish outreach PDF in `materials/`.
- No changes were made to the forecasting model or financial calculations.
- Existing URLs that point directly to the *old demo filenames* must be updated to the newly named demo filenames.
