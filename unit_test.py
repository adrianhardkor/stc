#!/usr/bin/python3
import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.jd(wc.wcheader)



os.environ['STC_PRIVATE_INSTALL_DIR'] = '/opt/STC_CLIENT/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux64Client/'
import Stc
project = Stc.init('adrian')
print(Stc.connect_attempt('10.44.0.21'))
for port in [ '//10.44.0.21/9/1', '//10.44.0.21/9/11', '//10.44.0.21/9/12' ]:
	Stc.port_config(project,port)
print('adrian')
exit(0)




