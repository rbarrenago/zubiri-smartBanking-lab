# ZUBIRI Smart Banking Lab · Ereduaren fitxa v1.4

**Egoera:** hezkuntzarako kontzeptu-proba. **Arduraduna:** IES Xabier Zubiri-Manteo BHI. **Datuak:** % 100 sintetikoak. **Azken data:** 2026/11/05.

## Helburua eta mugak
Fikziozko kafetegi baten eguneroko salmenten aurreikuspen esperimentala; aparteko simulazio-moduluak kobrantza geroratuak, kostuak eta diruzaintza-saldoa proiektatzen ditu. Ez da kaudimen-, kreditu-puntuazio-, ez-ordaintze-probabilitate-, iruzur- edo bankuaren likidezia-arriskuaren eredua. Ez du bezeroen daturik erabiltzen, eta ez du finantza-erabakirik automatizatzen.

## Datuak
- CSV: `data/synthetic_transactions.csv` (493 egun, 2025/07/01etik 2026/11/05era).
- `sales`: eguneko salmentak. **ML ereduaren helburu-aldagaia bakarrik**.
- `receipts`: salmenta guztiak TPV bidez egin eta bi egun natural geroago likidatzen direla suposatuz kalkulatutako sarrerak (jaiegunak modelizatu gabe).
- `supplier_cost`, `other_cost`: irteera simulatuak.
- `balance`: 17.000 EUR-ko hasierako saldo batetik kalkulatutako itxierako saldoa; ez da benetako saldo erabilgarria.
- ML aldagaiak: asteko eguna, hileko eguna, hila, urteko egunaren sinua/kosinua, asteburua, uda eta denbora-joera. Ez ditu `receipts`, `supplier_cost`, `other_cost` edo `balance` zuzenean ML iragarle gisa erabiltzen.

## Metodoa eta egungo baliozkotzea
`HistGradientBoostingRegressor` (160 iterazio, 12 hosto gehienez, L2=15, ikasketa-tasa=.045, gutxieneko hosto-lagina=16, seed=12); 418 egun entrenamendurako eta 75 denborazko probarako. MAE=121,89 EUR; asteko egunaren araberako **erreferentzia finkoa**=137,31 EUR. Erreferentzia hasierako 418 entrenamendu-egunekin soilik kalkulatzen da; ez du proba-aldiko daturik erabiltzen, eta bi metodoek abiapuntu-data bera dute. % 11,2ko aldea datu sintetikoetan bakarrik da adierazgarria. Ez da rolling-origin edo horizonteen araberako baliozkotzea. Baliozkotu ondoren, eredua historia sintetiko osoarekin entrenatzen da.

Simulazioak 90 egun proiektatzen ditu, kobrantza geroratuak eta ordainketa sintetikoak aplikatuz. Denborazko probako hondarren birlaginketarekin 240 ibilbide sortzen ditu. P10–P90 tartea eta 5.000 EUR-ko atalasea gurutzatzen duten simulazioen maiztasuna ez dira kalibratutako tarte edo ez-ordaintze/likidezia-arrisku probabilitate fidagarriak. Agertokien aldaketak salmenten, kostuen, atzerapenen eta aparteko gastuaren hipotesi deterministikoak dira.

## Benetako erabileraren aurretik falta diren kontrolak
1. Helburua, arduradunak, baimendutako datuak, oinarri juridikoa, segurtasuna eta giza gainbegiratzea adostea.
2. Datu-iturrien kontziliazioa: kontuen estaldura, eskudiruzko ordainketak, saldo erabilgarriak, zergak, finantzaketa, TPV-likidazioak eta aparteko gastuak.
3. Horizonteen eta segmentuen araberako rolling-origin baliozkotzea, informazio-baldintza bereko erreferentziarekin; salmenta- eta saldo-erroreak.
4. Egonkortasuna, ereduen bilakaera, tarteen kalibrazioa, abisu faltsuak, bertsioak eta monitorizazioa.
5. Erabilera zehatzaren araberako pribatutasun- eta betetze-azterketa; prototipoak ez du baimenik ematen.

## Erreproduzigarritasuna
`technical/build_model.py` fitxategiak datu eta aurreikuspen sintetikoak sortzen ditu; mendekotasunak `technical/requirements.txt` fitxategian daude. Paketeen bertsioek aldaketa txikiak eragin ditzakete berriro exekutatzean.

## Erreferentzia profesionalak (ez dira ziurtagiriak)
- EBZ 2026: https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp260224~6c5b64a77a.de.html
- EBA: https://www.eba.europa.eu/publications-and-media/publications/special-topic-artificial-intelligence
