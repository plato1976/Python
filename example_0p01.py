#coding=big5
#
# update 2015/12/2

import sys
print "(Edit coding type):"
print sys.getdefaultencoding()

test = '測試'
print test
print "--------------------------"
print "Python version:",
print sys.version_info[0]

#
s = "qwerty test"
print "string:" + s
print "Change first:"
print s.capitalize()

#
print s.center(20, "=")

#
print "string:" + s
print "find out q count:",
print s.count("q", 0, 6)

# 
print "string:" + s
print "change code to big5:",
print s.encode("big5", "error code")

#
print "y it 5 position:",
print s.endswith("y", 0, 5)

#
print "string:" + s
print "y it 6 position:",
print s.endswith("y", 0, 6)

#
print s.expandtabs()

#
print "string:" + s
print "find y position:",
print s.find("y", 0, 12)

#
s = "{0} {1}"
p = "test"
q = "sequence"
print "p:" + p
print "q:" + q
print "q+p:",
print s.format(p, q)


#
s = "qwerty"
print "string:" + s
print "witch t position:", 
print s.index("t", 0, 6)

#
print "string:" + s
print "if string not number return true:",
print s.isalnum()

#
print s.isalpha()

#
#print s.isdecimal()

s =  "qwerty"
print s.isdigit()

print s.isidentifier()

print s.islower()

print s.isnumeric()

print s.isprintable()

print s.isspace()

print s.istitle()

print s.isupper()


