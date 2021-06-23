# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

    
word = input()
li=[]
res=[]

def most_frequent():

    for i in word:
        if i not in li:
            li.append(i)
            
    for i in li:
        count=0
        for j in word:
            if i==j:
                count+=1
        else:
            res.append({"letter":i,"count":count})
        
    sorted_result = sorted(res, key = lambda i: i['count'], reverse = True)
    
    for dict in sorted_result:
        print(dict['letter'],'=',dict['count'])
        
most_frequent()
    
    




            

    



       
            
