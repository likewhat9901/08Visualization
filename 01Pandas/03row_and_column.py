import pandas as pd

exam_data = {'국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90],}
# Dictionary를 데이터프레임으로 변환 시 인덱스를 지정한다.
df = pd.DataFrame(exam_data, index=['유비', '관우', '장비'])
print(f"{'df전체출력':-^30}")
print(df, '\n')

# 행 선택하기
'''
    loc() : 인덱스명을 기준으로 행을 선택. 선택한 모든 범위가 포함된다.
    iloc() : 정수형 위치 인덱스를 통해 행을 선택. 마지막 부분은 제외(파이썬 기본 규칙과 동일)
'''
print(f"{'유비1':-^30}")
# 첫번째 행을 선택해서 출력
label1 = df.loc['유비'] # loc() : 문자형 인덱스명으로 하나의 행을 선택.
print(label1, '\n')

print(f"{'유비2':-^30}")
label1 = df.loc[['유비']] # loc() : 문자형 인덱스명으로 하나의 행을 선택.
print(label1, '\n')

print(f"{'인덱스1':-^30}")
# 두번째 행을 선택해서 출력
position1 = df.iloc[1] # iloc() : 정수형 인덱스를 통해 행을 선택
print(position1, '\n')

print(f"{'인덱스2':-^30}")
# 두번째 행을 선택해서 출력
position1 = df.iloc[[1]] # iloc() : 정수형 인덱스를 통해 행을 선택
print(position1, '\n')

# 2개 이상 선택
'''
행 인덱스를 사용해서 2개 이상의 행을 선택한다. 단 이경우
범위가 아니므로 주의해야 한다. 아래 2개의 문장은 동일한 결과를 출력한다.
'''
print(f"{'유비, 장비':-^30}")
label2 = df.loc[['유비', '장비']]
print(label2, '\n')

print(f"{'인덱스 0,2':-^30}")
position2 = df.iloc[[0, 2]]
print(position2, '\n')

# 범위선택
'''
문자형인 경우 마지막 부분이 포함되고, 숫자형인 경우 마지막이 제외된다.
'''
print(f"{'유비:장비':-^30}")
# 여기서는 3개의 행을 출력함.
label3 = df.loc['유비':'장비']
print(label3, '\n')

print(f"{'0:2':-^30}")
# 여기서는 마지막이 제외되므로 2개의 행만 출력됨.
position3 = df.iloc[0:2]
print(position3, '\n')

# 열 선택
'''
열을 선택할때는 대괄호를 사용하거나, 닷(.)을 사용한다.
닷을 사용하는 경우 열 이름이 문자형이어야 함.
이 경우 시리즈 객체를 반환한다.
'''
print(f"{'수학 열':-^30}")
# 대괄호로 수학 컬럼을 선택 후 출력
math1 = df['수학']
print(math1, '\n')
print(type(math1), '\n') # 시리즈 타입

print(f"{'수학 열2':-^30}")
math1 = df[['수학']]
print(math1, '\n')

# 닷을 사용해서 선택 후 출력
print(f"{'영어 열':-^30}")
english = df.영어
print(english, '\n')
# 타입은 시리즈 임을 확인할 수 있다.
print(type(english), '\n') # 시리즈 타입

# 2개 이상의 열 선택 시 대괄호를 겹쳐서 사용
print(f"{'국어, 체육 열':-^30}")
column1 = df[['국어', '체육']]
print(column1, '\n')
# 시리즈가 2개 이상 묶였으므로 데이터프레임 타입으로 출력
print(type(column1), '\n')

'''
1개의 열을 선택했지만, 원소가 리스트로 주어졌으므로 타입은 데이터프레임이 된다.
'''
print(f"{'수학 열':-^30}")
math2 = df[['수학']]
print(math2, '\n')
print(type(math2), '\n')