import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
print(df.head())

# 서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

plt.style.use('ggplot')
plt.figure(figsize=(14, 5)) # 그래프 크기 설정: 가로 14인치, 세로 5인치 (와이드형 그래프)
plt.xticks(rotation='vertical')
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

# 타이틀 및 라벨, 범례 설정
plt.title('서울 -> 경기 인구 이동', size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)
plt.legend(labels=['서울->경기'], loc='best')

# y축에 표시할 데이터의 범위 지정(최소값, 최대값)
plt.ylim(50000, 800000) # y축 범위 고정

'''
위치를 나타내는 x,y좌표에서 x는 인덱스 번호를 사용한다. (0:1970, 1:1971)
y는 인구수를 나타내는 숫자이므로 그대로 사용할 수 있다.
즉 (2,290000) 이라면 1972년의 29만의 좌표값이 된다.
'''
# 첫번째 화살표
plt.annotate('', # 텍스트 표시(화살표이므로 생략)
             xytext=(2, 290000), # 화살표의 꼬리부분(시작점) (1972년, 29만명)
             xy=(20, 620000), # 화살표의 머리부분(끝점) (1990년, 62만명)
             xycoords='data', # 좌표체계(데이터를 사용) -> 좌표: 실제 데이터 기준
             # 화살표의 스타일 지정. 모양, 컬러, 두께를 딕셔너리로 지정.
             arrowprops=dict( # 화살표 표시
                 arrowstyle='->', # 화살표 모양
                 color='skyblue',
                 lw=2), # 선 굵기
             )
plt.annotate('',
             xytext=('2000', 580000),
             xy=('2017', 450000),
             xycoords='data',
             arrowprops=dict(
                 arrowstyle='->',
                 color='olive',
                 lw=5),
             )
'''
va: 글자를 위아래 세로(수직) 방향으로 정렬
    속성값은 center, top, bottom, baseline 등
ha: 글자를 좌우(수평) 방향으로 정렬
    속성값은 center, left, right 등
'''
plt.annotate('인구이동 증가(1970-1995)', # 출력할 텍스트
             xy=(10, 450000), # 텍스트의 위치(글자 위치 좌표)
             rotation=25, # 회전각도, 글자 기울임(25도)
             va='baseline', # 수직정렬(vertical align)
             ha='center', # 수평정렬(horizontal align)
             fontsize=15,
             )
plt.annotate('인구이동 감소(1995-2017)',
             xy=(40, 560000),
             rotation=-10,
             va='baseline',
             ha='center',
             fontsize=15,
             )

# 그래프 출력
plt.show()
