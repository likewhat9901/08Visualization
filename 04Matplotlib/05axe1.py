import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 서울에서 경기로 전출할 데이터만 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

'''
여러개의 Axe객체를 생성하여 서로 다른 그래프를 표현할 수 있다.
figure() 함수로 그림의 틀을 만든 후 figsize 옵션으로 크기를 지정한다.
add_subplot() 함수로 그림의 틀을 분할한다. 여기서 분할된 틀을 Axe객체라고 한다.
    형식] add_subplot(행의 크기, 열의 크기, 서브플롯 순서)
'''
plt.style.use('ggplot') # ggplot 스타일 적용 -> 배경, 선 색깔, 격자 등 그래프가 더 세련되고 부드럽게 보임
fig = plt.figure(figsize=(10, 10)) # 그래프 크기 설정: 가로 14인치, 세로 5인치 (와이드형 그래프)
# 2행 1열 중 첫번째 Axe 객체 생성
ax1 = fig.add_subplot(2,1,1) # 2행 1열을 만들고 1번째
# 두번째 객체 생성
ax2 = fig.add_subplot(2,1,2) # 2행 1열을 만들고 2번째

'''
marker : 마커를 표시한 선 그래프를 그려준다.
    마커의 종류: o, *, +, . 등
markerfacecolor : 마커의 배경색
color : 마커의 컬러
'''
ax1.plot( # .plot : 꺽은선 그래프
         sr_one,
         'o',
         markersize=10
        )
ax2.plot(
         sr_one,
         marker='*',
         markersize=10,
         markerfacecolor='green', # 마커 안쪽 색깔
         color='olive', # 선색
         linewidth=2, # 선 굵기
         label='서울->경기' # 범례 라벨
         )

ax2.legend(loc='best') # 범례표시

# y축 범위 고정
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# x축 눈금 라벨 지정 및 텍스트 회전 각도 설정
ax1.set_xticklabels(sr_one.index, rotation=70)
ax2.set_xticklabels(sr_one.index, rotation=-75)

# 그래프 출력
plt.show()
