import cx_Oracle as cx
import folium

# 오라클 연결
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()


delivery_map = folium.Map(location=[37.40, 127.38], zoom_start=10)
delivery_map.save('../saveFiles/delivery_map.html')

SIGUN_NM = input('시군명를 입력해주세요: ')
print(SIGUN_NM)
# 지도 데이터를 오름차순 정렬해서 인출
sql = "select * from delivery_apps where sigun = :sigun order by idx asc"
cursor.execute(sql, sigun=SIGUN_NM)
for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    faclt = rs[2]
    addr = rs[3]
    latitude = rs[4]
    longitude = rs[5]
    # 대학 정보를 통해 마커 생성
    folium.Marker([latitude, longitude], popup=faclt).add_to(delivery_map)
    print(faclt, latitude, longitude)

# 마커가 포함된 지도 생성 및 저장
delivery_map.save('../saveFiles/delivery_map_'+SIGUN_NM+'_marker.html')
print("맵이 생성되었습니다.")