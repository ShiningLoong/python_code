string = 'aksjakfnalfnBDVSG是多少kjlaf'
dic = dict()
for ch in string:
    if ch not in dic.keys():
        dic[ch] = 1
    else:
        dic[ch] += 1

print(dic)