#!/usr/bin/env python3
import os
import sys
sys.path.insert(1, './lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
# wc.jd(wc.wcheader)

ARC = '10.88.240.60'
WP = '10.44.0.21'

STC_PRIVATE_INSTALL_DIR = '/opt/STC_5.16/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
# STC_PRIVATE_INSTALL_DIR = '~/wow/STC/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
os.environ['STC_PRIVATE_INSTALL_DIR'] = STC_PRIVATE_INSTALL_DIR

sys.path.insert(1,STC_PRIVATE_INSTALL_DIR + 'API/Python/')



import sys,os,time
current_dir = os.path.split(os.path.realpath(__file__))[0]
if current_dir not in sys.path :
	sys.path.append(current_dir)

import StcPython as zte
######################################

stc = zte.StcPython()
print("Spirent TestCenter version : %s" % stc.get("system1", "version"))
