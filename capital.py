# -*-coding: utf-8-*-
import random
source_str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#s="".join([random.choice(source_str) for x in xrange(0,n)])
print 'please put number for making random'
n=input('>>>  ')
s="".join([random.choice(source_str) for x in xrange(0,n)])
print s

if s.islower()==False:
    print "all not capital"
    print s.islower()
else:
    print "all capital"
    print s.islower()
