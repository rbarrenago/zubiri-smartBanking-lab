# ZUBIRI FinAI Lab · Ficha de modelo v1.3

**Estado:** prueba de concepto educativa. **Propietario:** IES Xabier Zubiri-Manteo BHI. **Datos:** 100 % sintéticos. **Corte de datos:** 05/11/2026.

## Caso de uso y límites
Previsión experimental de ventas diarias de un café ficticio; módulo de simulación independiente para cobros diferidos, costes y saldo de tesorería. No es un modelo de solvencia, scoring, probabilidad de impago, prevención del fraude ni liquidez de la entidad bancaria. No se emplean datos de clientes ni se automatizan decisiones financieras.

## Datos y definición
- CSV: `data/synthetic_transactions.csv` (493 filas diarias del 01/07/2025 al 05/11/2026).
- `sales`: ventas generadas en el día. **Única variable objetivo ML**.
- `receipts`: entradas simuladas, suponiendo que el 100 % de las ventas son por TPV y se liquidan dos días naturales después (sin calendario de festivos).
- `supplier_cost`, `other_cost`: salidas de caja ficticias.
- `balance`: saldo de cierre obtenido por recurrencia desde 17.000 EUR iniciales, no saldo disponible real.
- Features ML: día de semana, día de mes, mes, seno/coseno del día del año, fin de semana, verano y tendencia temporal. No usa directamente `receipts`, `supplier_cost`, `other_cost` o `balance` como predictores.

## Método y validación actual
`HistGradientBoostingRegressor(max_iter=160, max_leaf_nodes=12, l2_regularization=15, learning_rate=.045, min_samples_leaf=16, random_state=12)`; 418 días entrenamiento, 75 días holdout temporal. MAE = 121,89 EUR frente a baseline **fijo** por día de semana = 137,31 EUR. El baseline calcula medias por día de semana **sólo con los 418 días de entrenamiento**; no observa datos de la prueba y comparte con el modelo la misma fecha de origen. La diferencia del 11,2 % es ilustrativa en datos sintéticos, no un beneficio comercial validado. No es una validación rolling-origin ni por horizontes. Después de la evaluación se reajusta el modelo con todos los días sintéticos.

La simulación proyecta 90 días, aplica cobros diferidos y pagos sintéticos, y construye 240 trayectorias por remuestreo de residuos del holdout temporal. La banda P10–P90 y la frecuencia de cruzar el umbral de 5.000 EUR son resultados de esta simulación; NO son intervalos calibrados ni probabilidades fiables de impago o iliquidez. Los cambios de escenarios son hipótesis deterministas sobre ventas, costes, retrasos y gasto puntual.

## Controles faltantes antes de uso real
1. Acotar finalidad, responsable, datos permitidos, base jurídica, seguridad y supervisión humana.
2. Reconciliar fuentes, cobertura por cuentas, pagos en efectivo, saldos disponibles, vacaciones, impuestos, financiación, conciliación TPV y gastos extraordinarios.
3. Validación rolling-origin por horizontes y segmentos, contra baseline con la misma información de origen, con métricas de ventas y de saldos.
4. Diagnóstico de estabilidad, deriva, calibración, bandas y falsos avisos; registro de versiones y monitorización.
5. Evaluación de impacto, privacidad y compliance según uso real definido por la entidad; nunca inferir autorización de este demo.

## Reproducción
La fuente `technical/build_model.py` genera el dataset y datos para el demo con dependencias en `technical/requirements.txt`. Los archivos estáticos publicados preservan el caso simulado; diferencias menores pueden aparecer al ejecutar en versiones distintas de paquetes.

## Contexto profesional (no certificación)
- BCE 2026: https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp260224~6c5b64a77a.de.html
- EBA: https://www.eba.europa.eu/publications-and-media/publications/special-topic-artificial-intelligence
