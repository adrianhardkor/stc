#!/usr/bin/env python3
import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.jd(wc.wcheader)
STC_PRIVATE_INSTALL_DIR = '/opt/STC_5.16/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
# STC_PRIVATE_INSTALL_DIR = '~/wow/STC/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
os.environ['STC_PRIVATE_INSTALL_DIR'] = STC_PRIVATE_INSTALL_DIR
sys.path.insert(1,STC_PRIVATE_INSTALL_DIR + 'API/Python/')
import Stc



ARC = '10.88.240.60'
WP = '10.44.0.21'
system1,project = Stc.init('adrian')
Stc.connectChassis(ARC)
wc.jd(Stc.getConnectedChassisPhysical([ARC]))





ARC = ['//10.88.240.60/1/1', '//10.88.240.60/1/4']
WP = ['//10.44.0.21/9/9', '//10.44.0.21/9/10' ]
for port in ARC:
#	try:
#		Stc.port_config(project,port)
#	except Exception as err:
#		wc.pairprint('Cannot add ' + port + ' to project', str(err))
	pass

Stc.disconnectChassis()
exit(0)
