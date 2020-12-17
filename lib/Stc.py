import wcommon as wc
from StcPython import StcPython
stc = StcPython()

def init(project_name):
	global hPhysical
	global Project_1
	if 'Project_1' in locals() or 'Project_1' in globals():
		print("Already Found Project")
		return(Project_1)
	system_time = wc.timer_index_start()
	system1 = "system1"
	stc.config('system1', \
		InSimulationMode='FALSE', \
		UseSmbMessaging='FALSE', \
		IsLoadingFromConfiguration='TRUE', \
		ApplicationName='TestCenter', \
		TSharkPath='', \
		Active='TRUE', \
		LocalActive='TRUE', \
		Name='StcSystem 1')
	wc.pairprint('\n\nBuilt System', wc.timer_index_since(system_time))
	project_time = wc.timer_index_start()
	wc.jd(stc.get('system1'))
	Project_1 = stc.create('Project', \
		TableViewData='', \
		TestMode='L2L3', \
		SelectedTechnologyProfiles='dhcp', \
		Active='TRUE', \
		LocalActive='TRUE', \
		Name=project_name)
	wc.pairprint('\n\nBuilt Project: ' + project_name, wc.timer_index_since(project_time))
	wc.jd(stc.get(Project_1))
	return(system1,Project_1)

def getChassisList():
	hMgr = stc.get('system1','children-PhysicalChassisManager')
	return(stc.get(hMgr,'children-PhysicalChassis').split())

def disconnectChassis():
        stc.perform("ChassisDisconnectAll")

def connectChassis(ip):
	global hPhysical
	connect_time = wc.timer_index_start()
	result = stc.connect(ip)
	stc.apply()
	hPhysical = stc.create('PhysicalChassisManager', under='system1')
	wc.pairprint('\n\nConnect to CHASSIS: ' + ip, wc.timer_index_since(connect_time))
	wc.jd(stc.get(hPhysical))
	return(result)

def port_config(hProject, portname):
	portbuild_time = wc.timer_index_start()
	Port_1 = stc.create('Port', under=hProject, \
		location = portname, \
		UseDefaultHost='TRUE', \
		AppendLocationToPortName='TRUE', \
		Layer3Type='IPV4', \
		PortGroupSize='1', \
		TestModuleProfile='Default', \
		IsFlexEthernetPort='FALSE', \
		IsFlexEthernetPhy='FALSE', \
		IsFlexEthernetClient='FALSE', \
		IsPgaPort='TRUE', \
		Active='TRUE', \
		LocalActive='TRUE', \
		Name="Port @ ' + portname")
	wc.pairprint('\n\nBuilt Port: ' + portname, wc.timer_index_since(portbuild_time))
	return(Port_1)

def getConnectedChassisPhysical(szChassisIpList):
	chassisLocationList = []
	chassisInfoDict = {}
	tmLocationList = []
	tmInfoDict ={}
	hChassisList = getChassisList()
	for hChassis in hChassisList :
		chassisProps = stc.get(hChassis)
		chassisIpAddr = chassisProps['Hostname']
		chassisLocation = '//%s' % chassisIpAddr
		chassisInfoDict[chassisLocation] = stc.get(hChassis)
		hTmList = stc.get(hChassis,'children-PhysicalTestmodule').split()
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
						chassisInfoDict[chassisLocation][tmLocation][portLocation][iPortProp] = pProps[iPortProp]; # append

	return(chassisInfoDict)



def getConnectedChassisPhysical2(szChassisIpList):
        chassisLocationList = []
        chassisInfoDict = {}
        tmLocationList = []
        tmInfoDict ={}
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

