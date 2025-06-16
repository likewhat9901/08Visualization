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
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

# 스타일 지정
plt.style.use('ggplot')
# 그래프의 크기 지정 및 틀 생성
fig = plt.figure(figsize=(20, 5))
# 2행 1열 중 1번째 영역에 Axe 객체 생성
ax1 = fig.add_subplot(2,1,1) # 2행 1열을 만들고 1번째
# Axe 객체에 plot 함수로 그래프 생성
ax1.plot(
        sr_one,
        marker = 'o',
        markersize=10,
        markerfacecolor='orange',
        color='olive',
        linewidth=2,
        label='서울->경기'
        )
ax1.legend(loc='best') # 범례표시

ax1.set_ylim(50000, 800000) # y축 범위
# 그래프의 제목 및 각 축의 라벨
ax1.set_title('서울 -> 경기 인구 이동', size=20) # 제목 표시
ax1.set_xlabel('기간', size=12) # x축 이름 설정
ax1.set_ylabel('이동인구수', size=12) # y축 이름 설정
ax1.set_xticks(range(len(sr_one.index)))  # 눈금 위치 설정
ax1.set_xticklabels(sr_one.index, rotation=75) # x축 눈금라벨 지정, 75도 각도로 회전

# x축과 y축 눈금 글씨 크기 설정
ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)

# 그래프 출력
plt.show()
