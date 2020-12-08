import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.jd(wc.wcheader)
os.environ['STC_PRIVATE_INSTALL_DIR'] = wc.argv_dict['STC_INSTALLDIR']
import Stc
project = Stc.init('adrian')
for port in [ '//10.44.0.21/9/1', '//10.44.0.21/9/11', '//10.44.0.21/9/12' ]:
	Stc.port_config(project,port)
print('adrian')
exit(0)

