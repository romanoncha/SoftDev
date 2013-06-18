'''
Created on 16.06.2013

@author: Ivan
'''
# -*- coding: cp1251 -*-
smiles=[":)",":(",":D"]
textSmiles=["*SMILLING*","*SAD*","*HAPPY*"]


def FindSmiles(str,enableSpaces):
    i=0
    if (enableSpaces==True):
        spaces=" "
    else: spaces=""
    for element in smiles:
        str=str.replace(element, spaces+textSmiles[i]+spaces)
        i+=1
    print str

str="Hello:) My:)sadsd Fri:Dend^(:("
FindSmiles(str,True)