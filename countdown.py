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
    target = datetime(r['year'], r['month'], r['day'])

    current = datetime.now()

    last = target - current

    if last.days <= 0:
        print '已經退伍了喔！'
    else:
        print '退伍剩下{:03d}天'.format(last.days+1)


if __name__ == '__main__':
    main()
