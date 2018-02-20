#!/usr/bin/env python

# -*- coding: utf-8 -*-

import re
import urllib
import urllib2

url = 'http://10.7.15.2/'
file = 'c:/python27/scripts/download_file.txt'

def main():
    r = urllib2.urlopen(url)

    f = open(file, 'w')
    f.write(r.read())
    f.close()

main();
