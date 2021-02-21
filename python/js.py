# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:25:02 2021

@author: Oliver
"""


f=open("name_CN.txt",encoding='utf-8')
out=open("code.txt","r+",encoding='utf-8')
line=f.readlines()
name=[]
i=0
for l in line:
    
    name.append(l.split("="))
    name[i][1]=name[i][1].replace("\n","")
    s="	      { \"name\": \""+name[i][1]+"\", \"key\": \""+name[i][0]+"\", \"img\": \"spc82-"+str(i)+"\", \"status\": false},\n"
    out.writelines(s)
    i+=1
out.close()
    