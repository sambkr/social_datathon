import pandas as pd

df = pd.read_csv('data/Lightcast, UK Postings Sample.csv')
df_remote = df[['POSTED','IS_REMOTE']]



