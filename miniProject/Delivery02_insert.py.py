import cx_Oracle as cx
import requests, json

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()


url = 'https://openapi.gg.go.kr/GGEXPSDLV?'

for idx in range(1,36):
    params = dict(
        KEY='5939bac6996e4b469ef32b42afad4bd3',
        Type='json',
        pIndex=idx,
        pSize=1000,
    )

    # JSON 데이터 읽어오기
    raw_data = requests.get(url=url, params=params)
    binary_data = raw_data.content
    json_data = json.loads(binary_data)
    # print(json_data)

    # 제공된 데이터의 개수만큼 반복
    for jd in json_data['GGEXPSDLV'][1]['row']:
        SIGUN_NM = jd['SIGUN_NM']
        FACLT_NM = jd['STR_NM']
        REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
        REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
        REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']
        # print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

        sql = """insert into delivery_apps (idx, sigun, faclt, addr, latitude, longitude)
            values (seq_delivery_apps.nextval, :sigun, :faclt, :addr, :latitude, :longitude)"""

        try:
            cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                           latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
            conn.commit()
            print("1개의 레코드 입력")
        except Exception as e:
            conn.rollback()
            print("insert 실행시 오류발생", e)

conn.close()