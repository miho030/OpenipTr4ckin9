# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com


# 임포트 목록 => os, sys
import sys
import os
import cprint

#=======================================================================================
# 콘솔 색깔 출력 위한 클래스와 함수들
#=======================================================================================
FOREGROUND_BLACK = 0x0000 # 검은색
FOREGROUND_BLUE = 0x0001 # 파란색
FOREGROUND_GREEN = 0x0002 # 초록색
FOREGROUND_CYAN = 0x0003 # ?
FOREGROUND_RED = 0x0004 # 빨강색
FOREGROUND_MAGENTA = 0x0005 # ?
FOREGROUND_YELLOW = 0x0006 # 노란색
FOREGROUND_GREY = 0x0007 # 회색
FOREGROUND_INTENSITY = 0x0008  # foreground color is intensified.

BACKGROUND_BLACK = 0x0000
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_CYAN = 0x0030
BACKGROUND_RED = 0x0040
BACKGROUND_MAGENTA = 0x0050
BACKGROUND_YELLOW = 0x0060
BACKGROUND_GREY = 0x0070
BACKGROUND_INTENSITY = 0x0080  # background color is intensified.

NOCOLOR = False  # 색깔 옵션값

if os.name == 'nt': # 만약 os명에 nt가 포함된다면 -> 윈도우 시리즈
	from ctypes import windll, Structure, c_short, c_ushort, byref #로고 임포트를 위한 ctype 라이브러리에서 wintypes를 임포트

	SHORT = c_short
	WORD = c_ushort

# 구조체 구축

	class Coord(Structure):
		_fields_ = [
			("X", SHORT),
			("Y", SHORT)]


	class SmallRect(Structure):
		_fields_ = [
			("Left", SHORT),
			("Top", SHORT),
			("Right", SHORT),
			("Bottom", SHORT)]

# 콘솔 스크린 버퍼에 관한 정보 설정
	class ConsoleScreenBufferInfo(Structure):
		_fields_ = [
			("dwSize", Coord),
			("dwCursorPosition", Coord),
			("wAttributes", WORD),
			("srWindow", SmallRect),
			("dwMaximumWindowSize", Coord)]

	# Winbase.h
	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE = -11
	STD_ERROR_HANDLE = -12

	stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
	GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo


	def get_text_attr():
		csbi = ConsoleScreenBufferInfo()
		GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
		return csbi.wAttributes


	def set_text_attr(color):
		SetConsoleTextAttribute(stdout_handle, color)

	def cprint(msg, color):
		if not NOCOLOR:
			default_colors = get_text_attr()
			default_bg = default_colors & 0x00F0

			set_text_attr(color | default_bg)
			sys.stdout.write(msg)
			set_text_attr(default_colors)
		else:
			sys.stdout.write(msg)
			sys.stdout.flush()
else:
	def cprint(msg, color):
		sys.stdout.write(msg)
		sys.stdout.flush()

# 에러 구문 처리 :> Exception
def print_error(msg):
	cprint('Error: ', FOREGROUND_RED | FOREGROUND_INTENSITY)
	print (msg)
