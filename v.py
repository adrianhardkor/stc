#!/usr/bin/env python3
import os
import sys
import json
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
# wc.jd(wc.wcheader)


vIP = '10.88.48.31'
u = 'akrygows'
p = 'WowArc1'
V = 'https://%s/velocity/api' % vIP
url = '/inventory/v14/devices'
wc.jd(json.loads(wc.REST_GET(V + url, user=u, pword=p, verify=False)))
exit(0)

