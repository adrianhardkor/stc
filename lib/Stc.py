import wcommon as wc
from StcPython import StcPython
stc = StcPython()

def get_object(name):
   return sys._getframe(1).f_locals[name]

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
	return(Project_1)

def connectChassis(ip):
	global hPhysical
	connect_time = wc.timer_index_start()
	result = stc.connect(ip)
	sApply()
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
