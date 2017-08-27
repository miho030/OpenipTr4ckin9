# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import sys

from core.__init__ import VERSION
from core.__init__ import BUILDDATA
from core.__init__ import LASTYEAR

from Color import cprint
from Color import FOREGROUND_GREEN
from Color import FOREGROUND_INTENSITY

def print_logo():
	"""
	스크립트 로고 정의와 출력
	:return: not used.
	"""

	logo = """IP Tracking Script [OpenIPTr4ckin9] (for %s) Ver %s (%s)
CopyRight (C) 1995-%s GNU/GPL, Lee Joon Sung"""

	print '==========================================================================='
	s = logo % (sys.platform.upper(), VERSION, BUILDDATA, LASTYEAR)
	cprint(s, FOREGROUND_GREEN | FOREGROUND_INTENSITY)
	print '==========================================================================='
