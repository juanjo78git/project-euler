# -*- coding: utf-8 -*-


def result():
    d = ""
    for i in range(0, 1000000):
        d = d + str(i)

    # print len(d)
    # print (int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000])
    #     * int(d[100000]) * int(d[1000000]))
    return (int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000])
            * int(d[100000]) * int(d[1000000]))
