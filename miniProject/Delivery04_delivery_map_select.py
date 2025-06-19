import cx_Oracle as cx
import folium
from folium import FeatureGroup

# 오라클 연결
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

# 전체 시군명 조회
cursor.execute("SELECT DISTINCT sigun FROM delivery_apps")
sigun_list = [r[0] for r in cursor]

delivery_map = folium.Map(location=[37.40, 127.38], zoom_start=10, tiles=None)

# 시군별 FeatureGroup 생성
# groups = {}
for sigun in sigun_list:
    group = FeatureGroup(name=sigun, show=False)
    sql = "SELECT faclt, latitude, longitude FROM delivery_apps WHERE sigun = :sigun"
    cursor.execute(sql, sigun=sigun)
    for faclt, lat, lon in cursor:
        if lat and lon:
            folium.Marker([float(lat), float(lon)], popup=faclt).add_to(group)
    group.add_to(delivery_map)
    # groups[sigun] = group

# LayerControl 추가
folium.TileLayer('OpenStreetMap', name='시군명').add_to(delivery_map)
folium.LayerControl().add_to(delivery_map)

# 저장
delivery_map.save('../saveFiles/delivery_map_all.html')
print("맵이 생성되었습니다: delivery_map_all.html")
