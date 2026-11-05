# ZUBIRI FinAI Lab — GitHub Pages v1.3 · Banking edition

Bilingual (Basque / Spanish) educational prototype: **ML forecasting of daily sales** plus a separate simulated SME cash-flow projection. All data and balances are synthetic. Not a bank liquidity-risk model, credit score, regulatory stress test, or financial advice.

## Open in browser
- `index.html`: bilingual landing page
- `ZUBIRI_FinAI_Lab_Demo_EU.html`: Basque interactive demo
- `ZUBIRI_FinAI_Lab_Demo.html`: Spanish interactive demo
- `data/synthetic_transactions.csv`: complete 493-day synthetic history (daily aggregates, not individual transactions)
- `technical/MODEL_CARD_EU.md`, `technical/MODEL_CARD_ES.md`: data, validation, assumptions, limitations
- `technical/build_model.py`: reproducible synthetic data generator and ML trainer (writes CSV into `data/` and model payload into `technical/`)
- `technical/requirements.txt`: Python dependencies

## Upload to your existing GitHub Pages repository
1. Unzip the package on your device.
2. In `rbarrenago/zubiri-finai-lab`, select **Add file → Upload files**.
3. Upload the extracted contents **to the root of the repo**, preserving `technical/` and `data/` directories; replace the existing files; commit to `main`.
4. GitHub Pages should deploy from `Settings → Pages → Deploy from a branch → main → /(root)`; check **Actions** for successful deployment.

## v1.3 improvements / review findings
- Removed unrelated future-research content from both language versions and landing page.
- Corrected the backtest comparison: fixed weekday-mean baseline calculated **only on the original training period**, same information cutoff as the ML predictor. Synthetic 75-day holdout: **ML MAE €121.89** versus **baseline €137.31** (illustrative **11.2%** improvement). Not proven on real merchant data.
- Explicit assumption: **100% of synthetic daily sales settle through a hypothetical POS/TPV after two calendar days**; weekends/holidays, cash sales, other bank accounts and working-capital facilities are not modeled.
- CSV exports include scenario parameters (sales change, supplier-cost change, extra settlement delay, exceptional expense, simulation count) to facilitate review.
- Kept clear separation between sales forecast, cash-flow rules, simulated outcome distribution, and operational or credit-risk decisions.
- Main interactive functionality is unchanged: 30/60/90 days, scenario presets, sliders, reset, chart, and CSV.

## Scientific and banking limitations
One synthetic dataset and one time-based holdout do not establish generalization. No rolling-origin/multi-horizon backtests, independently calibrated predictive intervals, external validation, or actual cash-balance accuracy tests have been completed. Simulated crossings of the €5,000 illustrative threshold are **not real financial-risk probabilities**. Any real pilot requires approved data, consent or other lawful basis where applicable, reconciliation, governance, security, human oversight, and model validation.

The current webpage is self-contained and makes no banking API calls. **Never commit private customer/bank information, API keys or credentials to a public repo.**
