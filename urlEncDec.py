#!/usr/bin/python
#
# urlEncDec.py
#
# script to encode or decode a url string
#
# d3adlyv3n0m
#
#########################################


import re
import os
import sys
import time
import urllib

# banner
os.system('clear')
name = 'Created by ' + u'\u262f' + ' d3adlyv3n0m ' + u'\u262f'
print '#################################'
print '#                               #'
print '#  ' + name + '   #'    
print '#                               #'
print '#################################'
print
time.sleep(2)

# retrieve the url string
print '[*] Enter the URL'
url = raw_input('>>> ')

# make sure something was entered
if not url:
    print '[!] WARNING: Must enter a URL.'
    sys.exit(1)

# determine if url needs to be encoded (no hex characters)
# or decoded (contains hex characters)
hxChars = re.findall(r'\%..', url)
if hxChars:
    decUrl = urllib.unquote(url.encode('ascii')).decode('utf-8')
    print '[+] Decoded URL'
    print '>>> ' + decUrl
else:
    encUrl = urllib.quote_plus(url)
    print '[+] Encoded URL'
    print '>>> ' + encUrl

# done
sys.exit(0)
