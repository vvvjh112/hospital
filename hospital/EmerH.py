# -*- coding: utf-8 -*-
import requests
import pprint
import bs4
import pymysql.cursors

#응급실 운영 판단을 위해 True False 추가
def emergency_Check(input_xml):
    if input_xml.text == "1":
        return "True"
    else:
        return "False"

#응급실가용여부업데이트
def Update_hospitalization(ID):
    result = []
    decoding = 'JWgg0HGk6X1/iSamZNl29O5awvu46mP+wM/j8WNoLfNNfMeo2zhjPECwNdheapXHpIKbEZ0GCg1sWUm+rTdBfg=='
    # request url정의
    url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire'

    conn = pymysql.connect(
        host="heejun-db.ccg9hgcld4q0.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user='master',
        password='lhj981023!',
        database='hospitalDB',
        charset='utf8'
    )
    params = {'serviceKey': decoding}
    response = requests.get(url, params=params)
    curs = conn.cursor()
    params = {'serviceKey' : decoding, 'HPID' : ID, 'pageNo' : 1, 'numOfRows' : '1000'}
    response = requests.get(url, params=params)
    content = response.text.encode('utf-8')
    xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
    rows = xml_obj.findAll('item')
    try:
        sql = "UPDATE normalH SET 입원가능여부=%s, 응급실병상=%s, 수술실병상=%s, 입원실병상=%s WHERE 기관ID=%s"
        val = (emergency_Check(rows[0].dutyHayn)), (rows[0].find("hvec").text), (rows[0].find("hvoc").text), (rows[0].find("hvgc").text), (ID)
        curs.execute(sql, val)
        conn.commit()
        conn.close()
    except:
        pass

#기관명을 입력받아 기관ID 검색후 반환
def Check_ID(name):
    conn = pymysql.connect(
        host="heejun-db.ccg9hgcld4q0.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user='master',
        password='lhj981023!',
        database='hospitalDB',
        charset='utf8'
    )
    curs = conn.cursor()
    sql = "select 기관ID from normalH where 기관명 = %s"
    val = name
    curs.execute(sql, val)
    temp = curs.fetchone()
    return temp[0]


# lat : 위도 lon : 경도를 파라미터로 받아 11킬로미터 미만 응급실 병원 json타입 반환
def search_Emergency(lon, lat):
    conn = pymysql.connect(
        host="heejun-db.ccg9hgcld4q0.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user='master',
        password='lhj981023!',
        database='hospitalDB',
        charset='utf8'
    )

    curs = conn.cursor()
    curs1 = conn.cursor()
    sql = "SELECT 기관명, 기관ID, (6371*acos(cos(radians(%s))*cos(radians(병원위도))*cos(radians(병원경도) -radians(%s))+sin(radians(%s))*sin(radians(병원위도)))) AS distance FROM normalH where 응급실운영여부 = \"True\" Having distance<11 order by distance;"
    val = (lat), (lon), (lat)
    curs.execute(sql, val)
    temp = list(curs.fetchall())
    names = get_name(temp)
    data = {}
    attribute = ["id", "주소", "병원분류명", "응급의료기관코드명", "응급실운영여부", "입원가능여부", "응급실병상", "수술실병상", "입원실병상", "기관명", "대표전화1", "응급실전화", "월요진료", "화요진료", "수요진료", "목요진료", "금요진료", "토요진료", "일요진료", "공휴일진료", "기관ID", "병원경도", "병원위도"]

    for k in range(len(temp)):
        Update_hospitalization(temp[k][1])
        conn.commit()

    for i in range(len(names)):
        values = {}
        values["거리"] = temp[i][2]
        sql1 = "select * from normalH where 기관ID = %s;"
        val1 = (temp[i][1])
        curs1.execute(sql1, val1)
        value = curs1.fetchall()
        for j in range(len(attribute)):
            values[attribute[j]] = value[0][j]
        data[names[i]] = values


    conn.close()
    return data

def get_name(list):
    length = len(list)
    names = []
    for i in range(length):
        names.append(list[i][0])
    return names