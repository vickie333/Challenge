import pandas as pd
import numpy as np


def detectar_cruces(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['precio'] = data['close']
    
    # Calcular medias móviles
    signals['media_corta'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    signals['media_larga'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    # Generar señales de compra (1) y venta (-1)
    signals['señal'] = 0.0
    signals['señal'] = np.where(signals['media_corta'] > signals['media_larga'], 1.0, 0.0)
    signals['cruce'] = signals['señal'].diff()
    
    return signals

def simular_operaciones(señales):
    trades = []
    posicion_abierta = None
    
    for fecha, fila in señales.iterrows():
        if fila['cruce'] == 1.0 and posicion_abierta is None:
            posicion_abierta = {'fecha_entrada': fecha, 'precio_entrada': fila['precio']}
        elif fila['cruce'] == -1.0 and posicion_abierta is not None:
            posicion_abierta['fecha_salida'] = fecha
            posicion_abierta['precio_salida'] = fila['precio']
            posicion_abierta['retorno_%'] = (fila['precio'] - posicion_abierta['precio_entrada']) / posicion_abierta['precio_entrada'] * 100
            trades.append(posicion_abierta)
            posicion_abierta = None
    
    if posicion_abierta is not None:
        ultima_fecha = señales.index[-1]
        ultima_precio = señales.iloc[-1]['precio']
        posicion_abierta['fecha_salida'] = ultima_fecha
        posicion_abierta['precio_salida'] = ultima_precio
        posicion_abierta['retorno_%'] = (ultima_precio - posicion_abierta['precio_entrada']) / posicion_abierta['precio_entrada'] * 100
        trades.append(posicion_abierta)

            
    return pd.DataFrame(trades)


def calcular_metricas(trades_df, capital_inicial=10000):
    trades_df['retorno'] = trades_df['precio_salida'] / trades_df['precio_entrada'] - 1
    trades_df['capital'] = capital_inicial * (1 + trades_df['retorno']).cumprod()

    total_return = trades_df['capital'].iloc[-1] / capital_inicial - 1
    num_years = (trades_df['fecha_salida'].iloc[-1] - trades_df['fecha_entrada'].iloc[0]).days / 365.0
    cagr = (1 + total_return) ** (1 / num_years) - 1

    # Sharpe y Sortino
    daily_returns = trades_df['retorno']
    sharpe = daily_returns.mean() / daily_returns.std() * np.sqrt(252)
    downside_std = daily_returns[daily_returns < 0].std()
    sortino = daily_returns.mean() / downside_std * np.sqrt(252)

    # Drawdown
    equity = trades_df['capital']
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    max_drawdown = drawdown.min()

    # Win rate
    win_rate = (trades_df['retorno'] > 0).sum() / len(trades_df)

    resumen = {
        "Total Return (%)": total_return * 100,
        "CAGR (%)": cagr * 100,
        "Sharpe Ratio": sharpe,
        "Sortino Ratio": sortino,
        "Máximo Drawdown (%)": max_drawdown * 100,
        "Número de trades": len(trades_df),
        "Win Rate (%)": win_rate * 100
    }
    
    return resumen, trades_df
