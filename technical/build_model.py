"""Reproducible synthetic SME cashflow dataset and a small ML sales forecaster.
NON-PRODUCTION: educational prototype; no real banking/customer data.
"""
from pathlib import Path
from datetime import datetime, timedelta
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

OUT = Path(__file__).parent
rng = np.random.default_rng(70452)
start = pd.Timestamp('2025-07-01')
end = pd.Timestamp('2026-11-05')
dates = pd.date_range(start, end, freq='D')

def feat(ds):
    v=[]
    for d in ds:
        doy=int(d.dayofyear)
        v.append([d.weekday(), int(d.day), int(d.month),
            np.sin(2*np.pi*doy/365.25), np.cos(2*np.pi*doy/365.25),
            float(d.weekday()>=5), int(d.month in [6,7,8,9]),
            (d-start).days/365.25])
    return np.array(v, dtype=float)

sales=[]
for d in dates:
    dow=d.weekday(); m=d.month
    base=610 + [35,50,85,125,235,455,350][dow]
    season=1.22 if m in [7,8] else 1.13 if m in [6,9] else 0.92 if m in [1,2] else 1.0
    city_events= 245 if (d.month==9 and 19<=d.day<=27) else 0
    trend=55*((d-start).days/365.25)
    noise=rng.normal(0,105)
    sales.append(max(110, base*season+city_events+trend+noise))

sales=np.array(sales)
features=feat(dates)
train_cut=len(dates)-75
model=HistGradientBoostingRegressor(max_iter=160,max_leaf_nodes=12,l2_regularization=15,
                                    learning_rate=.045,min_samples_leaf=16,random_state=12)
model.fit(features[:train_cut],sales[:train_cut])
pred_hold=model.predict(features[train_cut:])
mae=float(mean_absolute_error(sales[train_cut:],pred_hold))
# A calendar-aware and realistic naive baseline: weekday average over trailing 28 days
naive=[]
for j in range(train_cut,len(dates)):
    prior=[sales[k] for k in range(max(0,j-28),j) if dates[k].weekday()==dates[j].weekday()]
    naive.append(np.mean(prior))
naive_mae=float(mean_absolute_error(sales[train_cut:],naive))
residuals=[float(x) for x in sales[train_cut:]-pred_hold]
# Fit final estimator using the full synthetic history.
model.fit(features,sales)
future_dates=pd.date_range(end+pd.Timedelta(days=1),periods=90,freq='D')
forecast=np.maximum(110,model.predict(feat(future_dates)))

def costs(d):
    supplier = 320 if d.weekday()>=5 else 225
    misc = 75
    fixed=(2550 if d.day==1 else 0)+(11600 if d.day==5 else 0)
    fixed+=(975 if d.day==18 else 0)
    fixed+=(1100 if d.day==12 else 0)
    return {'supplier': supplier, 'misc': misc, 'fixed': fixed}
# past observed historic cash, receipts arrive two days after card sales.
starting_balance=17000
records=[]
balance=starting_balance
for i,d in enumerate(dates):
    settled=sales[i-2] if i>=2 else 0
    c=costs(d)
    balance+=settled-c['supplier']-c['misc']-c['fixed']
    records.append({'date':d.strftime('%Y-%m-%d'),'sales':round(float(sales[i]),2),
        'receipts':round(float(settled),2),'supplier_cost':c['supplier'],
        'other_cost':c['misc']+c['fixed'],'balance':round(float(balance),2)})

future=[{'date':d.strftime('%Y-%m-%d'),'predicted_sales':round(float(s),2),
         **costs(d)} for d,s in zip(future_dates,forecast)]
payload={'title':'Gros Café - ejemplo sintético','currency':'EUR',
         'last_date':str(end.date()), 'last_balance':round(float(balance),2),
         'history':records[-100:],'tail_sales':records[-20:],
         'future':future,'residuals':residuals,'backtest':{
         'split':'Last 75 calendar days of synthetic history',
         'holdout_days':75,'mae_model':round(mae,2),'mae_weekday_baseline':round(naive_mae,2),
         'trained_on':'All synthetic history after holdout evaluation',
         'method':'HistGradientBoostingRegressor; calendar features; 75-day time-ordered holdout',
         }}
(OUT/'demo_data.json').write_text(json.dumps(payload,ensure_ascii=False),encoding='utf-8')
pd.DataFrame(records).to_csv(OUT/'synthetic_transactions.csv',index=False)
print(json.dumps({'history_days':len(dates),'last_balance':round(balance,2),'ML_MAE':round(mae,2), 'baseline_MAE':round(naive_mae,2), 'future30_sales_mean':round(np.mean(forecast[:30]),2)},indent=2))
