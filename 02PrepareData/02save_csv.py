import pandas as pd

data = {
    'name' : [ 'Jerry', 'Riah', 'Paul'],
    'algol' : [ 'A', 'A+', 'B'],
    'basic' : [ 'C', 'B', 'B+'],
    'c++' : [ 'B+', 'C', 'C+'],
}

# 데이터프레임으로 변환 후 name컬럼을 인덱스로 지정
df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_csv("../saveFiles/hakjum.csv")
