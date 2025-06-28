import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx',
                    engine='openpyxl', header=0)
df = df.ffill()
# print(df.head())

filter_seoul = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[filter_seoul]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
sr_one = df_seoul.loc['경기도']
print(sr_one)

plt.figure(figsize = (14,5))
plt.xticks(rotation = 90)
plt.plot(sr_one.index, sr_one.values)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'], loc='best')

plt.show()