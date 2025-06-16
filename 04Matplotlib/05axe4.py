import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 서울에서 경기로 전출할 데이터만 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.ffill()
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1) # axis=1 : 열
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print('df_seoul 테이블\n', df_seoul)

'''
map 함수를 통해 1970~2017까지의 문자열로 구성된 리스트를 생성한다.
map의 첫번재 인수는 str함수이므로 범위만큼 반복하면서 호출하게된다.
'''
col_years = list(map(str, range(1970,2018))) # 열 지정
print('col_years\n', col_years)

df3 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

plt.style.use('ggplot')
fig = plt.figure(figsize=(15,8))
fig.subplots_adjust(hspace=0.5)
axe1 = fig.add_subplot(2,2,1)
axe2 = fig.add_subplot(2,2,2)
axe3 = fig.add_subplot(2,2,3)
axe4 = fig.add_subplot(2,2,4)

'''
1개의 그래프에 3개의 꺽은선을 추가한다.
x축은 기간으로 설정
y축은 df3.loc['충청남도',:] -> 충남 행의 전체기간을 선택
'''
axe1.plot(
        col_years,
        df3.loc['충청남도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='green',
        color='olive',
        linewidth=2,
        label='서울->충남'
        )
axe2.plot(
        col_years,
        df3.loc['경상북도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='blue',
        color='skyblue',
        linewidth=2,
        label='서울->경북'
        )
axe3.plot(
        col_years,
        df3.loc['강원도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='red',
        color='magenta',
        linewidth=2,
        label='서울->강원'
        )
axe4.plot(
        col_years,
        df3.loc['전라남도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='orange',
        color='yellow',
        linewidth=2,
        label='서울->전남'
        )

# 범례, 타이틀, 라벨, 기울기 등 설정
for ax, region in zip([axe1, axe2, axe3, axe4], ['충남', '경북', '강원', '전남']):
    ax.legend(loc='best')
    ax.set_title(f'서울 -> {region} 인구 이동', size=15) # 제목 표시
    ax.set_xlabel('기간', size=12) # x축 이름 설정
    ax.set_ylabel('이동인구수', size=12) # y축 이름 설정
    ax.set_xticklabels(col_years, rotation=90) # x축 눈금라벨 지정, 75도 각도로 회전
    # x축과 y축 눈금 글씨 크기 설정
    ax.tick_params(axis='x', labelsize=7)
    ax.tick_params(axis='y', labelsize=7)

# 그래프 출력
plt.show()
