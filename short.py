import sys
import mechanize
import requests
from ast import Try , Break , ExceptHandler

if sys.version_info[0] !=3:
    print('run script with python3')

    Try
    import python3 

print("""\033[2;34m
 
'||''|.   '||' |''||''| '||'      '||' '|' 
 ||   ||   ||     ||     ||         || |   
 ||'''|.   ||     ||     ||          ||    
 ||    ||  ||     ||     ||          ||    
.||...|'  .||.   .||.   .||.....|   .||.   
                                                                          
                    \033[2;0m""")
print("""\033[1;33m
[+] FRAMEWORK : bitly
[+] FACEBOOK PROFILE : facebook/shade234sherif
[+] FACEBOOK PAGE : facebook/cyberhacks6
[+] FACEBOOK GROUP : facebook/groups/shade234sherif
\033[2;33m""")

print("""
This software is said to be on a free plan\n
users can only create 50lnks\monthly\n
To help shift to the premium features\n
[+]please make use of the socials provided to contact me.""" )

Break

import bitly_api
import sys

API_USER = "cyberneticsdev3"
API_KEY = "efd964e5885b8848da704db07278140542f83ef6"

b = bitly_api.BitLy(API_USER, API_KEY)

usage = """Usage: python short.py [url]
e.g python shortener.py http://www.google.com"""

if len(sys.argv) != 2:
    print (usage)
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(longUrl=longurl)

print (response['url'])