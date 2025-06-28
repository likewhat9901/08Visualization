import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx',
                   engine='openpyxl', header=0)
# print("df1\n", df.head())

filter_seoul = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[filter_seoul]
# print("df_seoul\n", df_seoul)

df_seoul = df_seoul.drop(['전출지별'], axis=1)
# print("df_seoul\n", df_seoul)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# print("df_seoul\n", df_seoul)
df_seoul.set_index('전입지', inplace=True)
# print("df_seoul\n", df_seoul)

df_seoul_gyeongi = df_seoul.loc['경기도']
# print("df_seoul_gyeongi\n", df_seoul_gyeongi)

plt.plot(df_seoul_gyeongi.index, df_seoul_gyeongi.values)

plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')


plt.show()