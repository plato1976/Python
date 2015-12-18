#coding: utf-8
#Python OS information
#update 2015/12/18

import os

print "OS platform(windows: nt; Linux/unix: posix):",
print os.name

#create folder
#os.mkdir(path [,mode=0777])

#del folder
#os.rmdir()

#create multi folder
#os.mkdirs()

#del multi folder
#os.removedirs()

print "working folder:",
print os.getcwd()

print "return working folder file list:",
print os.listdir(os.getcwd())

#remove file
#os.remove()

#run shell command
#os.system()


#replace system default path split mark
#os.sep

#return file or folder exist (value: true / false)
print "is test.py exist??",
print os.path.isfile("test.py")

print "is /home/programming/Python/example exist??",
print os.path.isdir("/home/programming/Python/example")
