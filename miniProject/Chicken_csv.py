import pandas as pd

# 엑셀 파일 열기
df = pd.read_csv(
    './서울특별시_일반음식점.csv',
    usecols=['영업상태구분코드', '업태구분명', '소재지전체주소', '사업장명'],
    encoding='cp949',
    skiprows=range(1, 150000),
    nrows=50000,
)

filtered_df = df[df['소재지전체주소'].str.contains('영등포구', na=False)]
filtered_df = filtered_df[filtered_df['업태구분명'].isin(['통닭(치킨)', '호프/통닭'])]
filtered_df = filtered_df[filtered_df['영업상태구분코드']==1]


# CSV 파일로 저장
filtered_df.to_csv('./치킨집가공.csv', index=False, encoding='utf-8-sig')