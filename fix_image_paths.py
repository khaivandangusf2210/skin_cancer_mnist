import pandas as pd

df = pd.read_csv('old_processed_fixed.csv')
df['image_path'] = df['image_path'].str.replace(r'^.*?/', 'old_processed/', regex=True)
df.to_csv('old_processed_fixed.csv', index=False)
print('Updated image_path to use old_processed/.') 