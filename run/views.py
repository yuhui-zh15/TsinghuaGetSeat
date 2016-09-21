# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import urllib
import urllib2
import re

url = 'http://seat.lib.tsinghua.edu.cn/roomshow/'

def go(request):

    while True:

        response = urllib2.urlopen(url) 
        html = response.read().decode("utf-8")
    
        a = re.compile(r"""(?<=>).+?(?=</td>)""", re.X)
    
        items = a.findall(html)
        
        for i in range(8, 24, 3):
            check = int(items[i])
            if check > 0:
                return HttpResponse(items[i-2])
