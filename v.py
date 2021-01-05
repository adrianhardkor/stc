#!/usr/bin/env python3
import os
import sys
import json
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
# wc.jd(wc.wcheader)

def vREST(ip, url, u='', p=''):
    global TOKEN
    V = 'https://' + ip + '/velocity/api'
    if u != '' and p != '':
        # Get Token return
        V = V + '/auth/v2/token'
        wc.REST_GET(V, user=u, pword=p, verify=False)
    else:
        V = V + url
    wc.REST_GET()        

vIP = '10.88.48.31'
u = 'akrygows'
p = 'WowArc1'
V = 'https://%s/velocity/api' % vIP
# wc.jd(json.loads(wc.REST_GET(V + '/velocity/api/auth/v2/token')))
# curl -s -X GET --user $username:$password $velocityUri/velocity/api/auth/v2/token


wc.jd(json.loads(wc.REST_GET(V + '/inventory/v14/devices', user=u, pword=p, verify=False)))
exit(0)

