#!/usr/bin/env python3
"""
Programm, mis võtab etteantud arvu ruutu
"""

__author__ = "Maria Fomitsenko"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Maria Fomitsenko", "Friend1", "Friend2"]
__version__ = "0.2"
__email__ = "mariafomit@ya.ru"


def ruut(number):  #võtab mingi arvu ruutu
	return number ** 2
	
def main():
	print("ruutu võtmine arvust")
	number = int(input())
	text_file = open("tulemus.txt", "w")
	text_file.write(str(ruut(number)))
	text_file.close()

if __name__ == "__main__":
	main()