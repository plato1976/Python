#!/usr/bin/env python
# -*- coding: utf8 -*-

print '直接印出 Unicode 一'

msg = u'直接印出 Unicode 二'
print msg

msg2 = u'Unicode 編碼 UTF-8 String 一'
encoded = msg2.encode('utf8')
print encoded

print u'Unicode 編碼 UTF-8 String 二'.encode('utf8')

msg3 = 'UTF-8 String \xe8\xa7\xa3\xe7\xa2\xbc Unicode'
decoded = msg3.decode('utf8')
print decoded