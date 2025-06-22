# Quantitative Trading Challenge - Estrategia de Cruce de Medias Móviles

Este proyecto fue desarrollado como solución al [Quantitative Trading Challenge], con el objetivo de diseñar, implementar y evaluar una estrategia de trading cuantitativa aplicando principios clásicos del análisis técnico.

---

## 🎯 Enfoque

Se implementa una estrategia **basada en el cruce de medias móviles simples (SMA)**, un método ampliamente utilizado para identificar cambios de tendencia en mercados financieros.

### ✅ Reglas de la estrategia:

- **Entrada (BUY):**
  - La media móvil corta (SMA de 30 días) cruza por encima de la media móvil larga (SMA de 70 días).

- **Salida (SELL):**
  - La media móvil corta cruza por debajo de la larga.

Esta lógica busca capturar movimientos alcistas sostenidos evitando entradas tardías o en zonas de sobrevaloración.

---

## 📊 Indicadores utilizados

- SMA 30, SMA 70
- RSI (Relative Strength Index)
- Retornos, posición, señales de trading

Todos los indicadores fueron implementados desde cero usando únicamente `pandas` y `numpy`, sin librerías externas de análisis técnico.

---

## 📈 Evaluación de la estrategia

Se construyó un módulo de backtesting simple que simula el comportamiento histórico de la estrategia y calcula métricas clave de rendimiento:

- **Total Return**
- **CAGR (Tasa de crecimiento anual compuesta)**
- **Sharpe Ratio**
- **Sortino Ratio**
- **Max Drawdown**
- **Tasa de aciertos (win rate)**
- **Curva de capital (equity curve)**
- **Curva de drawdown**


