#!/usr/bin/env python
import urllib2 , json,webbrowser,sys,os,textwrap,oauth2
from twitter import *

url="http://www.reddit.com/r/todayilearned/new/.json"


try:
    result = urllib2.urlopen(url)
    data = json.loads(result.read())
    children = data['data']['children']
    print  "n = next TIL,  o = open link in browser, q = quit"
    print "."*100+"\n"

    for js in children:
        title = js['data']['title'].replace("TIL that",'',1).replace("TIL:",'',1) \
                                                            .replace("TIL of",'',1).replace("TIL",'',1).lstrip().capitalize()
        url = js['data']['url']
        for ti in textwrap.wrap(title,100):
            print ti

        print "\n"

        while True:
            choice=raw_input('n = next,o = open link,q= quit?')

            if choice == 'n':
                print "."*100+"\n"
                break;
            elif choice == 'o':
                try:
                    savout = os.dup(1)
                    os.close(1)
                    os.open(os.devnull, os.O_RDWR)
                    webbrowser.open_new_tab(url)
                finally:
                    os.dup2(savout, 1)
                
            elif choice == 'q':
               sys.exit(0)
            
except  urllib2.URLError, e:
    print "An error occured! It's not your fault"