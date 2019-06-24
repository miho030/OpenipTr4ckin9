# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import pygeoip

gi = pygeoip.GeoIP('C:\Python27\GeoDB\GeoLiteCity.dat')

ip = raw_input("추적할 공격자 IP 주소 입력 : ")


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    countryname = rec['country_name']
    time = rec['time_zone']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt +' Geo-located. '
    print '[+] '+str(countryname)+', '+str(time)+', '+str(country)
    print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
tgt = ip

printRecord(tgt)
