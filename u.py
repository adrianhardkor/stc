#!/home/akrygowski/.pyenv/shims/python3
import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.jd(wc.wcheader)


STC_PRIVATE_INSTALL_DIR = '/home/akrygowski/wow/STC/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
# STC_PRIVATE_INSTALL_DIR = '/home/akrygowski/wow/STC/Client/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux64Client'
os.environ['STC_PRIVATE_INSTALL_DIR'] = STC_PRIVATE_INSTALL_DIR

sys.path.insert(1,STC_PRIVATE_INSTALL_DIR + 'API/Python/')
import Stc
project = Stc.init('adrian')
for port in ['//10.44.0.21/9/9', '//10.44.0.21/9/10' ]:
#	try:
#		Stc.port_config(project,port)
#	except Exception as err:
#		wc.pairprint('Cannot add ' + port + ' to project', str(err))
	pass
Stc.connectChassis('10.44.0.21')
exit(0)
