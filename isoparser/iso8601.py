import re


def parse(dur):
    rex = lambda x, y: re.match(x, y)
    test1 = rex(r"^PT([0-9]+)H$", dur)
    if test1:
        return int(test1.group(1)) * 3600
    test2 = rex(r"^PT([0-9]+)H([0-9]+)M$", dur)
    if test2:
        h, m = [int(x) for x in test2.group(1, 2)]
        return 3600 * h + 60 * m
    test3 = rex(r"^PT([0-9]+)H([0-9]+)S$", dur)
    if test3:
        h, s = [int(x) for x in test3.group(1, 2)]
        return 3600 * h + s
    test4 = rex(r"^PT([0-9]+)H([0-9]+)M([0-9]+)S$", dur)
    if test4:
        h, m, s = [int(x) for x in test4.group(1, 2, 3)]
        return 3600 * h + 60 * h + s
    test5 = rex(r"^PT([0-9]+)M$", dur)
    if test5:
        return int(test5.group(1)) * 60
    test6 = rex(r"^PT([0-9]+)M([0-9]+)S$", dur)
    if test6:
        m, s = [int(x) for x in test6.group(1, 2)]
        return 60 * m + s
    test7 = rex(r"^PT([0-9]+)S$", dur)
    if test7:
        return int(test7.group(1))
    print("CAN'T PARSE FUCKING GOOGLE FORMATTING:", dur)
    return False
