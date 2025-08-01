import pandas as pd

# 데이터프레임 정의
exam_data = {'이름' : [ '유비', '관우', '장비' ],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90],}
df = pd.DataFrame(exam_data)
print(df)

# 컬럼 추가 : 데이터프레임 명으로 직접 추가한다.
print(f"{'역사 열 추가':-^30}")
# 모든 행에 일괄적으로 80점으로 설정
df['역사'] = 80
print(df)

# 행 추가 : loc를 통해 추가
print(f"{'3행 추가':-^30}")
# 전체 0으로 초기화
df.loc[3] = 0 # 4번째 행
print(df)

# 4행으로 추가: 개별적인 데이터를 통해 추가됨
print(f"{'제갈량 행 추가':-^30}")
df.loc[4] = ['제갈량', 90, 80, 70, 60, 50] # 5번째 행
print(df)

# 5번째 행으로 추가
print(f"{'5행 추가':-^30}")
# 이 경우 숫자형이 아닌 문자형으로 인덱스가 지정된다.
# 데이터는 2번 행을 그대로 복사해서 추가한다.
df.loc['행5'] = df.loc[2]
print(df)