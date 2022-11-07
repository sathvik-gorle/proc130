import pandas as pd

df = pd.read_csv('pro130/Merged_Stars.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']

df.to_csv('pro130_data_cleaned_file.csv')