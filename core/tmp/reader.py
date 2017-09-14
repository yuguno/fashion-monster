import os, sys

def none_detector(obj):
    if obj == "":
        return "NaN"
    else:
        return obj

f = open('./2016_6scraping.csv', 'r')
cnt = 0
pattern = []
for line in f:
    line = line.rstrip()
    l = line.split(',')

    l5 = none_detector(l[5])
    l6 = none_detector(l[6])
    l7 = none_detector(l[7])
    l8 = none_detector(l[8])
    patt = 'top1: '+l5+'\ttop2: '+l6+'\ttop3: '+l7+'\tbottom: '+l8
    cnt = cnt + 1
