
# selection of 100 trees, le random state sera determiné de façon random verifiable le Vendredi matin

import pandas as pd
import random

df = pd.read_csv('../arbres_grenoble_epsg4326.csv', sep=',', encoding='utf-8')
df.dropna(subset=['anneedeplantation'], inplace=True)


random_state = random.randint(0, 10000)
print(f"Random state generated: {random_state}")
df_sample = df.sample(n=100, random_state=random_state)
print(f"Random state used: {random_state}")
df_sample.to_csv('../selection_100_arbres.csv', index=False, encoding='utf-8')

print("Source file: arbres_grenoble_epsg4326.csv")
print("Output file: ../selection_100_arbres.csv")
print(f"Random state used: {random_state}")