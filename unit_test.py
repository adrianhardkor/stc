#!/usr/bin/python3
import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.jd(wc.wcheader)


data = {
                "fields": {
                    "project": {
                    "id": "10606"
                },
                "labels":["regression","automated_regression"],
                "description":"[Jenkins_BUILD_URL|http://10.88.48.21:8080/job/stc/46/]",
                "summary": "Sample Jenkins STC - Automated Regression Execution @ 2020-12-09 17:16:01 UTC DEV " ,
                "issuetype": {
                "id": "10552"
                }
                }
                }

wc.jd(data)
print(); exit(0)


os.environ['STC_PRIVATE_INSTALL_DIR'] = wc.argv_dict['STC_INSTALLDIR']
import Stc
project = Stc.init('adrian')
for port in [ '//10.44.0.21/9/1', '//10.44.0.21/9/11', '//10.44.0.21/9/12' ]:
	Stc.port_config(project,port)
print('adrian')
exit(0)




