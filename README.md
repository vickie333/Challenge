# Challenge: Estrategia de Trading y Backtesting en BTC/USDT

## Enfoque

Este proyecto implementa un pipeline completo de análisis cuantitativo sobre el par **BTC/USDT**. El flujo abarca:

1. **Carga y limpieza de datos**: Se importan datos históricos OHLCV, se filtran columnas irrelevantes y se selecciona el rango de fechas de interés.
2. **Cálculo de indicadores técnicos**: Se generan indicadores clásicos (SMA, EMA, RSI, Bandas de Bollinger, ATR, Volatilidad, Momentum) y features derivados.
3. **Estrategia de trading**: Se implementa una estrategia basada en el cruce de medias móviles (50/200) para generar señales de compra/venta.
4. **Backtesting y evaluación**: Se simulan operaciones, se calcula la curva de capital, drawdown y métricas clave (CAGR, Sharpe, Sortino, win rate, etc.).

## Supuestos

- **Datos**: El análisis parte de un archivo CSV con datos diarios de BTC/USDT (OHLCV). El archivo debe estar en `data/Bitstamp_BTCUSDT_d.csv`.
- **Fechas**: El rango de análisis es desde `2024-01-20` hasta `2025-06-20`.
- **Estrategia**: Solo se consideran posiciones largas (compra-venta). No se usan apalancamientos ni comisiones.
- **Herramientas**: Todo el código está en Python 3 y organizado en módulos para reutilización y claridad.

## Estructura

- `modules/`: Funciones para carga de datos, indicadores técnicos y utilidades de backtesting.
- `01_load_and_clean_data.ipynb`: Carga y limpieza de datos.
- `02_indicadores_tecnicos.ipynb`: Cálculo de indicadores y features.
- `03_estrategia_trading.ipynb`: Implementación y visualización de la estrategia de cruce de medias.
- `04_backtesting_evaluacion.ipynb`: Simulación de operaciones y evaluación de resultados.

## Cómo ejecutar

1. **Instala dependencias**  
   Para instalar las dependencias usando un archivo requirements.txt, sigue estos pasos en tu terminal:
   ```bash
   pip install -r requirements.txt
   ```

2. **Coloca el archivo de datos**  
   Descarga el archivo `Bitstamp_BTCUSDT_d.csv` y colócalo en la carpeta `data/`.

3. **Ejecuta los notebooks en orden**  
   Abre Visual Studio Code o JupyterLab y ejecuta, en orden:
   - `01_load_and_clean_data.ipynb`
   - `02_indicadores_tecnicos.ipynb`
   - `03_estrategia_trading.ipynb`
   - `04_backtesting_evaluacion.ipynb`

   Cada notebook genera archivos intermedios (`btc_data_clean.csv`, `btc_data_features.csv`) usados por el siguiente paso.

4. **Visualiza resultados**  
   Los gráficos y métricas se muestran en los propios notebooks.

---

**Autor:**  
Maria Victoria Pérez Contrera
