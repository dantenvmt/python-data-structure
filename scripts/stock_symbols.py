import pandas as pd
from iexfinance.refdata import get_symbols


df = get_symbols(output_format='pandas')['symbol']
df.to_csv('symbols.csv', index=False)