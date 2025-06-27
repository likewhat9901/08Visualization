import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pytrends.request import TrendReq

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 1. pytrends 객체 생성
pytrends = TrendReq(hl='ko', tz=540)

# 2. 검색 키워드 리스트
keywords = ["몬스테라", "스투키", "선인장", "아레카야자"]

# 3. 데이터 요청
pytrends.build_payload(keywords, timeframe='today 12-m')  # 최근 12개월

# 4. 데이터 가져오기
data = pytrends.interest_over_time()
print(data.head())

# isPartial 열 제거
data_clean = data.drop(columns=['isPartial'])

# 키워드별 총합 계산
keyword_sums = data_clean.sum()
print(keyword_sums)

# 파이 차트
plt.figure(figsize=(7,7))
plt.pie(
    keyword_sums,
    labels=keyword_sums.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#8BC34A', '#4CAF50', '#CDDC39', '#FFC107']
)
plt.title('식물 키워드 12개월 검색 비중')

# 파이 차트의 비율을 원에 가깝게 조정
plt.axis('equal')
plt.legend(labels=keyword_sums.index, loc='upper right')
plt.show()
