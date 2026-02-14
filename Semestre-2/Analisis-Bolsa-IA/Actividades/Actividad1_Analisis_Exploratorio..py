import yfinance as yf
import pandas as pd

# CONFIGURACIÓN INICIAL
# Especificar los símbolos de los tickers (identificador alfanumerico unico de las empresas
# dentro de la bolsa de valores).
tickers = ['NVDA', 'MSFT', 'TSLA', 'META']

# Descargar datos históricos para el último año (valores diarios) - Se hizo el 14/02/2026
data = yf.download(tickers, period='1y', interval='1d')


# VALORES ANUALES DE CIERRE
# Filtrar solo la columna 'Close'
filtered_data_close = data['Close']

# Mostrar los primeros registros para ver los datos filtrados
print(filtered_data_close.head())

# Guardar los datos filtrados en un archivo CSV
filtered_data_close.to_csv('Actividad1_filtered_data_close.csv')


# VALORES ANUALES DE VOLUMEN
# Filtrar solo la columna 'Volume'(Cantidad de acciones vendidad y compradas en ese dia)
filtered_data_volume = data['Volume']

# Mostrar los primeros registros
print(filtered_data_volume.head())

# Guardar los datos filtrados en un archivo CSV
filtered_data_volume.to_csv('Actividad1_filtered_data_volume.csv')