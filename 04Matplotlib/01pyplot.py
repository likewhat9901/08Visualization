# 데이터프레임 사용을 위한 모듈
import pandas as pd
# 데이터 시각화를 위한 모듈
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 import
'''
font_manager : 폰트와 관련된 설정을 도와주는 모듈
rc : 그래프의 전역 설정을 바꾸는 함수
'''
from matplotlib import font_manager, rc
# 폰트 경로 설정
font_path = "../resData/malgun.ttf"
# 폰트 파일의 이름을 속성으로 지정
'''
FontProperties(fname=font_path): 해당 경로에 있는 폰트 파일을 가져오는 객체를 생성합니다.
.get_name(): 이 폰트의 이름을 가져옵니다. 예를 들어 Malgun Gothic 같은 이름입니다.
이걸 사용하는 이유는 폰트 이름은 파일 이름과 다를 수 있어서, 실제 matplotlib에서 인식할 수 있는 이름을 가져오기 위해 필요합니다.
'''
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
# rc('font', family=...): matplotlib에서 사용하는 기본 폰트를 설정
rc('font', family=font_name)

# 엑셀 파일을 데이터프레임으로 변환. header가 0이므로 첫번째 행은 타이틀로 인식하여 제외
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx',
                   engine='openpyxl', header=0)
print("df1\n", df.head())

# 누락값(NaN)을 앞 부분의 데이터로 채워준다.
# NaN이 '전국'으로 대체된다.
df = df.fillna(method='ffill')
# fillna() : 결측값(NaN)을 원하는 값으로 채워주는 함수
# method='ffill' : 결측값을 바로 앞 행의 값으로 채우는 -> ffill = forward fill (앞에서 채우기)
'''
데이터는 일반적으로 근접한 것끼리 관련이 높을 수 있으므로 누락값은 보통 이런방식으로 대체한다.'''
print("df2\n", df.head())

'''
'전출지별'에서는 '서울특별시'만 추출
'전입지별'에서는 '서울특별시'가 아닌 데이터만 추출한다.
즉 서울에서 다른 지역으로 전출한 데이터만 남게 된다.
'''
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
# 위 조건을 데이터 프레임에 적용
df_seoul = df[mask]
print("df_seoul1\n", df_seoul)

''' 전출지별 컬럼(열)을 삭제한다. 축 옵션을 1로 설정했다.
inplace 옵션이 없으므로 변경된 새로운 객체를 반환한다. '''
df_seoul = df_seoul.drop(['전출지별'], axis=1)

# 컬럼명을 변경한 후 원본 데이터프레임을 저장한다.
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)

# '전입지' 컬럼을 인덱스로 설정한다. 설정 전에는 정수형 인덱스가 부여된다.
df_seoul.set_index('전입지', inplace=True)
print("df_seoul2\n", df_seoul)

''' 문자형 인덱스를 이용해서 서울에서 경기도로 전출한 행만 추출한다. 
만약 숫자형 인덱스를 사용하려면 iloc를 사용한다. '''
sr_one = df_seoul.loc['경기도']
print("sr_one\n", sr_one)

# 그래프의 x, y축에 데이터를 적용
plt.plot(sr_one.index, sr_one.values)

# 그래프의 제목과 x,y축의 라벨을 추가한다.
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 모든 변경사항을 저장한 후 그래프 출력
plt.show()
