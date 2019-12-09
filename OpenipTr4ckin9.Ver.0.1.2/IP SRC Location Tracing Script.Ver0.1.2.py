# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import sys
import pygeoip



print ("#===========================================================================#")
print ("#                       OpenipTr4ckin9.Ver0.1.2                             #")
print ("#---------------------------------------------------------------------------#")
print ("#                                                                           #")
print ("#          IP Tracking Script [OpenIPTr4ckin9]; made by Nicht               #")
print ("#             CopyRight (C) 2016-2017 GNU/GPL, Lee Joon Sung                #")
print ("#                                                                           #")
print ("#===========================================================================#")

gi = pygeoip.GeoIP('GeoLiteCity.dat')
ip = raw_input("추적할 공격자 IP 주소 입력:  ")



def printTGTinfor(tgt):
    if os.path.isfile('GeoLiteCity.dat'):
        print "[*] ", "The GeoIP DB is normally recognized.", "\n[*] ","GeoIP DB가 정상적으로 인식되었습니다."

        print "[*] ", "Find Physical location using IP Addr"

        def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
            formatStr = "{0:." + str(decimals) + "f}"
            percent = formatStr.format(100 * (iteration / float(total)))
            filledLength = int(round(barLength * iteration / float(total)))
            bar = '#' * filledLength + '-' * (barLength - filledLength)
            sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
            if iteration == total:
                sys.stdout.write('\n')
            sys.stdout.flush()

        for i in range(0, 100):
            printProgress(i, 100, 'Progress:', 'Complete', 1, 50)

        print "\n[*] ", "Find Longitude and Latitude.\n"

        rec = gi.record_by_name(tgt)

        countryname = rec['country_name']
        time = rec['time_zone']
        country = rec['country_name']
        long = rec['longitude']
        lat = rec['latitude']
        print '[*] Target: ' + tgt + ' Geo-located. '
        print '[+] ' + str(countryname) + ', ' + str(time) + ', ' + str(country)
        print '[+] Latitude: ' + str(lat) + ', Longitude: ' + str(long)

    else:
        print "Cannot Find GeoIP DB. pls refer Readme File in folder.\nGeoIP DB를 인식할 수 없습니다. 폴더 안의 Readme 파일을 참고하세요."
tgt = ip
printTGTinfor(tgt)




