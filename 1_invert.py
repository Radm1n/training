# -*- coding: utf-8 -*-
# 3 задание
# код меняющий в словаре ключи и значения местами, это программа ну или как то так )
def invert_mydictionary(d):
    newdict = {}
    for k, v in d.iteritems():
        newdict.setdefault(v, []).append(k)
    return newdict
d = {'a':'1','b':'2','c':'3'}
print invert_mydictionary(d)