import pandas as pd

# 讀取 CSV 文件
df = pd.read_csv('./data2330.csv')

# 反轉行順序
df_reversed = df[::-1]

# 打印結果
print(df_reversed)

# 如果需要保存到新的 CSV 文件
df_reversed.to_csv('./reversed_file.csv', index=False)
