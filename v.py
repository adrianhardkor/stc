#!/usr/bin/env python3
import os
import sys
import json
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
# wc.jd(wc.wcheader)


V = '10.88.48.31'
url = '/velocity/api/inventory/v14/devices'
u = 'akrygows'
p = 'WowArc1'
wc.jd(json.loads(wc.REST_GET('https://' + V + url, user=u, pword=p, verify=False)))
exit(0)

