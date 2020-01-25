import urls
import pandas as pd
from functions import scrape, tweet, write_df, merge_df

dfs = []
for url in urls.urls:
    print(f"Processing {url[54:-5]}...")
    dfs.append(write_df(url[54:-5]))

big_df = pd.DataFrame()

i = 0
while i < len(dfs):
    cols_to_use = dfs[i].columns.difference(big_df.columns, sort=False)
    big_df = pd.merge(big_df, dfs[i][cols_to_use], left_index=True, right_index=True, how='outer')
    i += 1

tweet()
