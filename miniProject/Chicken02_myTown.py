import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.style.use('ggplot')
font_name = (font_manager.FontProperties(fname="../resData/malgun.ttf").get_name())
rc('font', family=font_name)


df = pd.read_csv('./치킨집가공.csv')

print(df.head(100))

# 3. 동 이름만 추출
df['동'] = df['소재지전체주소'].str.extract(r'(\S+동)')

# 4. 동별 개수 세기
dong_counts = df['동'].value_counts().reset_index()
dong_counts.columns = ['동', '매장수']
print("주소 NaN 개수:", df['소재지전체주소'].isna().sum())
print("동 추출 성공 개수:", df['동'].notna().sum())
print("추출된 동 종류:", df['동'].unique())


dong_counts["label"] = dong_counts['동'] + "\n(" + dong_counts['매장수'].astype(str) + ")"
plt.figure(figsize=(12, 8))
squarify.plot(sizes=dong_counts['매장수'],
              label=dong_counts["label"],
              alpha=.8)
plt.axis('off')
plt.title('영등포구 동별 치킨/호프 음식점 분포')
plt.show()