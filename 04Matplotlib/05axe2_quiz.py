import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 서울에서 경기로 전출할 데이터만 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.ffill()
mask = (df['전출지별']=='강원도') & (df['전입지별']!='강원도')
print('df 테이블\n', df)
df_gangwon = df[mask]
print('df_gangwon 테이블\n', df_gangwon)
df_gangwon = df_gangwon.drop(['전출지별'], axis=1)
df_gangwon.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_gangwon.set_index('전입지', inplace=True)

sr_one = df_gangwon.loc['서울특별시']
sr_one = sr_one[10:]
print('sr_one 테이블\n', sr_one)

sr_two = df_gangwon.loc['부산광역시'][10:]
print('sr_two 테이블\n', sr_two)

# 스타일 지정
plt.style.use('ggplot')
# 그래프의 크기 지정 및 틀 생성
fig = plt.figure(figsize=(15, 7))
fig.subplots_adjust(hspace=0.5) # Fiqure 내 서브플롯 간격 조절 (hspace: 수직간격, wspace: 수평간격)
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
        label='강원도->서울'
        )
ax1.legend(loc='best') # 범례표시

ax1.set_ylim(0, 100000) # y축 범위
# 그래프의 제목 및 각 축의 라벨
ax1.set_title('강원 -> 서울 인구 이동', size=20) # 제목 표시
ax1.set_xlabel('기간', size=12) # x축 이름 설정
ax1.set_ylabel('이동인구수', size=12) # y축 이름 설정
ax1.set_xticks(range(len(sr_one.index)))  # 눈금 위치 설정
ax1.set_xticklabels(sr_one.index, rotation=75) # x축 눈금라벨 지정, 75도 각도로 회전

# x축과 y축 눈금 글씨 크기 설정
ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)


# 강원도 -> 부산광역시
ax2 = fig.add_subplot(2,1,2) # 2행 1열을 만들고 1번째
# Axe 객체에 plot 함수로 그래프 생성
ax2.plot(
        sr_two,
        marker = 'o',
        markersize=10,
        markerfacecolor='orange',
        color='olive',
        linewidth=2,
        label='강원도->부산'
        )
ax2.legend(loc='best') # 범례표시

ax2.set_ylim(0, 10000) # y축 범위
# 그래프의 제목 및 각 축의 라벨
ax2.set_title('강원 -> 부산 인구 이동', size=20) # 제목 표시
ax2.set_xlabel('기간', size=12) # x축 이름 설정
ax2.set_ylabel('이동인구수', size=12) # y축 이름 설정
ax2.set_xticks(range(len(sr_two.index)))  # 눈금 위치 설정
ax2.set_xticklabels(sr_two.index, rotation=75) # x축 눈금라벨 지정, 75도 각도로 회전

# x축과 y축 눈금 글씨 크기 설정
ax2.tick_params(axis='x', labelsize=10)
ax2.tick_params(axis='y', labelsize=10)

# 그래프 출력
plt.show()
