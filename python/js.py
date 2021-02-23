# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:25:02 2021

@author: Oliver
"""

f=open("name_CN.txt",encoding='utf-8')
out=open("code.txt","r+",encoding='utf-8')
line=f.readlines()
name={}

cnt=0
for l in line:
    l=l.lower()
    n=l.split("=")
    n[1]=n[1].replace("\n", "")
    name[n[0]]=n[1]
name=sorted(name.items(),key=lambda d:d[0])
for k,v in name:
    s="	      { \"name\": \""+v+"\", \"key\": \""+k+"\", \"img\": \"spc82-"+str(cnt)+"\", \"status\": false},\n"
    if cnt==len(name)-1:
        s="	      { \"name\": \""+v+"\", \"key\": \""+k+"\", \"img\": \"spc82-"+str(cnt)+"\", \"status\": false}\n"
    cnt+=1
    print(s)
    out.writelines(s)

out.close()
    