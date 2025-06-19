import cx_Oracle as cx
import requests, json

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()


url = 'https://openapi.gg.go.kr/GGEXPSDLV?'

params = dict(
    KEY='5939bac6996e4b469ef32b42afad4bd3',
    Type='json',
    pIndex=1,
    pSize=10,
)

# JSON 데이터 읽어오기
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)
# print(json_data)

for jd in json_data['GGEXPSDLV'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM']
    FACLT_NM = jd['STR_NM']
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']
    print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

conn.close()