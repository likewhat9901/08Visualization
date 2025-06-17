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

''' range 함수로 1970~2017까지를 반환하면 str 함수를 통해 문자열로 변경
그리고 리스트로 생성한다. '''
col_years = list(map(str, range(1970,2018))) # 열 지정
# 연도를 지정한 후 각 4개의 도를 선택하여 데이터 추출
print('col_years\n', col_years)

df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# 그래프 사이즈 지정. 와이드하게 긴 사각형의 형태
plt.style.use('ggplot')
fig = plt.figure(figsize=(15,8))
fig.subplots_adjust(hspace=0.5)
# Axe객체 생성. 2행 2열의 첫번째부터 순서대로 그래프의 영역을 설정
axe1 = fig.add_subplot(2,2,1)
axe2 = fig.add_subplot(2,2,2)
axe3 = fig.add_subplot(2,2,3)
axe4 = fig.add_subplot(2,2,4)

# 각 Axe객체에 plot함수로 그래프를 출력
'''
x축은 1970~2017까지의 연도를 설정. y축은 각 전출지의 전체 데이터를 설정.
나머지는 마커, 컬러, 두께 등을 설정한다. '''
axe1.plot(
        col_years,
        df4.loc['충청남도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='green',
        color='olive',
        linewidth=2,
        label='서울->충남'
        )
axe2.plot(
        col_years,
        df4.loc['경상북도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='blue',
        color='skyblue',
        linewidth=2,
        label='서울->경북'
        )
axe3.plot(
        col_years,
        df4.loc['강원도',:],
        marker = 'o',
        markersize=7,
        markerfacecolor='red',
        color='magenta',
        linewidth=2,
        label='서울->강원'
        )
axe4.plot(
        col_years,
        df4.loc['전라남도',:],
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
    # 타이틀
    ax.set_title(f'서울 -> {region} 인구 이동', size=15) # 제목 표시
    ax.set_xlabel('기간', size=12) # x축 이름 설정
    ax.set_ylabel('이동인구수', size=12) # y축 이름 설정
    # x축 눈금, 회전
    ax.set_xticklabels(col_years, rotation=90) # x축 눈금라벨 지정, 75도 각도로 회전
    # x축과 y축 눈금 글씨 크기 설정
    ax.tick_params(axis='x', labelsize=7)
    ax.tick_params(axis='y', labelsize=7)

# 그래프 출력
plt.show()
