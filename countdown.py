#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParser
from datetime import datetime


def config(cfg='config.cfg'):
    c = RawConfigParser()
    c.read(cfg)
    r = {}
    r['year'] = int(c.get('target', 'year'))
    r['month'] = int(c.get('target', 'month'))
    r['day'] = int(c.get('target', 'day'))
    return r


def main():
    r = config()
    lastdays = 0
    target = datetime(r['year'], r['month'], r['day'])
    tyear = int(target.strftime("%Y"))
    tdays = int(target.strftime("%j"))

    current = datetime.now()
    cyear = int(current.strftime("%Y"))
    cdays = int(current.strftime("%j"))
    if cyear > tyear:
        print '已經退伍了喔！'
        return
    elif cyear == tyear:
        lastdays = tdays - cdays
    else:
        for y in xrange(cyear, tyear+1):
            if y == tyear:
                lastdays += tdays
            elif y == cyear:
                lastdays += (int(datetime(y, 12, 31).strftime("%j")) - cdays)
            else:
                lastdays += int(datetime(y, 12, 31).strftime("%j"))

    if lastdays < 0:
        print '已經退伍了喔！'
    else:
        print '退伍剩下{:03d}天'.format(lastdays)


if __name__ == '__main__':
    main()
