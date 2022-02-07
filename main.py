#!/bin/python3
import os
from googlesearch import search

dir_path = os.path.dirname(os.path.realpath(__file__))
try : 
  os.remove(os.path.join(dir_path,"output.mp4"))
  os.remove(os.path.join(dir_path,"output.mp4.part"))
except :
  pass

query = input(" [ $ YOUTUBE $ ]  ")
query = "site:youtube.com/watch " + query


results = []
i = 0
for result in search(query, 10):
    lines = os.popen("yt-dlp --get-title --get-duration " + result).readlines()
    title = lines[0].strip('\n')
    duration = lines[1].strip('\n')
    print(f' {i} : {title} [{duration}]  ')
    results.append(result)
    i+=1
    
url = results[int(input("Choose the video (0,1,etc..) : "))]
print(url)

cmd = """yt-dlp -o """ + os.path.join(dir_path,"output.mp4") + """  --exec " """ + os.path.join(dir_path,"video-to-ascii") +""" -a --strategy ascii-color -f {}" -f mp4 """ + url 

os.system(cmd)



