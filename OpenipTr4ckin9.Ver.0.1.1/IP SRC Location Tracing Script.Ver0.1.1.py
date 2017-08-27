# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import sys

import pygeoip
# interface
sys.path.insert(0, '/IP/ui')
import print_logo()

if os.name =='nt':
    pass

print_logo()


gi = pygeoip.GeoIP('')
ip = raw_input("추적할 공격자 IP 주소 입력:  ")


def printTGTinfor(tgt):



    if os.path.isfile('GeoLiteCity.dat'):
        print "The GeoIP DB is normally recognized.\nGeoIP DB가 정상적으로 인식되었습니다."
    else:
        print "Cannot Find GeoIP DB. pls refer Readme File in folder.\nGeoIP DB를 인식할 수 없습니다. 폴더 안의 Readme 파일을 참고하세요."
        
    rec = gi.record_by_name(tgt)

    countryname = rec['country_name']
    time = rec['time_zone']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt +' Geo-located. '
    print '[+] '+str(countryname)+', '+str(time)+', '+str(country)
    print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
    

def retKML(tgt):
    rec = gi.record_by_name(tgt)
    try:
        longitude = rec['longitude']
        latitude = rec['latitude']
        kml = (
            '<Placmerk>\n'
            '<name>%s<name>\n'
            '<Point>\n'
            '<coordinates>%6f,%6f</corrdinates>\n'
            '</Point>\n'
            '<\Placemark>\n'
           )%(tgt,longitude, latitude)
        return kml
    except Exception, e:
        return ''

tgt = ip
printTGTinfor(tgt)