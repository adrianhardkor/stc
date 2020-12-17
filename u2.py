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

######################################

def getChassisList():
	hMgr = stc.get('system1','children-PhysicalChassisManager')
	return(stc.get(hMgr,'children-PhysicalChassis').split())

def getConnectedChassisPhysical(szChassisIpList):
	chassisLocationList = []
	chassisInfoDict = {}
	tmLocationList = []
	tmInfoDict ={}
	timestamp = time.strftime('%Y.%m.%d.%H.%M.%S')
	 #  Chassis Information	
	hChassisList = getChassisList()
	for hChassis in hChassisList :
		chassisProps = stc.get(hChassis)
		chassisIpAddr = chassisProps['Hostname']
		chassisLocation = '//%s' % chassisIpAddr
		chassisInfoDict[chassisLocation] = stc.get(hChassis)
	
		 #Get TestModules Information
		hTmList = stc.get(hChassis,'children-PhysicalTestmodule')
		for hTm in hTmList :
			tmProps = stc.get(hTm)
			tmSlot = tmProps['Index']
			tmLocation = '//%s/%s' %(chassisIpAddr, tmSlot)
			chassisInfoDict[chassisLocation][tmLocation] = tmProps
			for hPortGroup in stc.get(hTm,'children-PhysicalPortgroup').split():
				pgProps = stc.get(hPortGroup)
				pgSlotIndex = pgProps['Index']
				pgLocation = '//%s/%s/%s' %(chassisIpAddr,tmSlot,pgSlotIndex)
				if pgProps['OwnershipState'] != 'OWNERSHIP_STATE_RESERVED' :
					pgProps['OwnerUser'] = 'Idle'
				else :
					pgProps['OwnerUser'] = pgProps['OwnerUserId'] + '@' + pgProps['OwnerHostname']
				chassisInfoDict[chassisLocation][tmLocation][pgLocation] = pgProps
				for hPort in stc.get(hPortGroup,'children-PhysicalPort').split():
					pProps = stc.get(hPort)
					portLocation = '//%s/%s/%s' %(chassisIpAddr,tmSlot,pProps['Index'])
					for iPortProp in pProps.keys():
						# append to dict
						chassisInfoDict[chassisLocation][tmLocation][portLocation][iPortProp] = pProps[iPortProp]

	return(chassisInfoDict)

stc.connect(ARC)
# wc.jd(main([ARC]))
wc.jd(main2([ARC]))
stc.perform("ChassisDisconnectAll")

