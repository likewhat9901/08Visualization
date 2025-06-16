import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 import
from matplotlib import font_manager, rc
# 폰트 경로 설정
font_path = "../resData/malgun.ttf"
# 폰트 파일의 이름을 속성으로 지정
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
rc('font', family=font_name)

# 엑셀 파일에서 서울 > 경기도로 이동한 데이터만 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx',
                   engine='openpyxl', header=0)
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

# 그래프 설정 추가 start
# 그래프 이미지의 전체 사이즈 지정. 14:5로 비율을 설정한다.
plt.figure(figsize=(14, 5)) # 그래프 크기 설정: 가로 14인치, 세로 5인치 (와이드형 그래프)

# x축 라벨을 수직방향으로 설정. 텍스트가 겹쳐지는 부분 처리
plt.xticks(rotation='vertical') # x축 눈금 라벨 세로로 회전해서 표시 (90도)
# plt.xticks(rotation=45)      # 45도 기울이기
# plt.xticks(rotation=0)       # 기본 가로 상태
# 그래프 설정 추가 end

#그래프 설정

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values)

# 타이틀 및 라벨 설정
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 범례 추가(그래프의 우상단에 설명 문구 추가)
plt.legend(labels=['서울->경기'], loc='best')

# 그래프 출력
plt.show()
