import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임으로 변환 시 header 옵션이 없으므로 첫행은 컬럼명으로 인식한다.
df = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl')
print("df", df)

# [0,5] => 엑셀의 2행과 7행을 의미한다.
# 3: => 3열부터 마지막을 의미
# 즉, 남한(0행)과 북한(5행)의 연도별 발전량 데이터만 추출
df_ns = df.iloc[[0,5], 3:]

# 남북한 데이터에 인덱스를 부여
df_ns.index = ['South', 'North']
print(df_ns)

# 열 이름의 자료형을 정수형으로 변경
print("열 이름의 자료형을 정수형으로 변경\n")
print("변경전", df_ns.columns.map(type))
df_ns.columns = df_ns.columns.map(int)
print("변경후", df_ns.columns.map(type))

# 처음 5개 데이터 확인하기
print("원본 데이터", "="*30)
print(df_ns.head())
print("전치한 데이터", "="*30)
print(df_ns.T.head())

# 선 그래프1(원본 데이터프레임)
df_ns.plot()
plt.show()

# 선 그래프2(전치한 데이터프레임)
df_ns.T.plot()
plt.show()

# 막대 그래프1(원본 데이터프레임)
df_ns.T.plot(kind='bar')
plt.show()

# 히스토그램(전치한 데이터프레임)
# pd.to_numeric() : 문자열이나 기타 데이터들을 숫자형(int 또는 float)으로 변환해주는 pandas 함수
# .apply(pd.to_numeric): 각 열마다 pd.to_numeric()을 적용
# errors='coerce': 변환 안 되는 값은 NaN(결측치) 처리
df_ns = df_ns.apply(pd.to_numeric, errors='coerce')
df_ns.T.plot(kind='hist')
plt.show()