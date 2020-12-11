import os
from behave import given, when, then
import sys
# context: where behave runs
sys.path.insert(1, 'lib/')
import wcommon as wc
wc.wcheader['packages']['wc'] = wc.__file__
wc.jd(wc.wcheader)
os.environ['STC_PRIVATE_INSTALL_DIR'] = '/opt/STC_CLIENT/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux64Client/'
# os.environ['STC_PRIVATE_INSTALL_DIR'] = wc.argv_dict['STC_INSTALLDIR']
import Stc


@given(u'Spirent config built')
def step_impl(context):
	project = Stc.init('adrian')
	portlist = [ '//10.44.0.21/9/9', '//10.44.0.21/9/10' ]; # later will be from LaaS
	for port in portlist:
		Stc.port_config(project,port)
	assert True

@when(u'I try to ping "{ip}"')
def step_impl(context, ip):
	context.ip = ip
	context.pingable = bool(wc.is_pingable(ip))
	pass

@then(u'I expect response "{expectationBoolean}"')
def step_impl(context, expectationBoolean):
	expectationBoolean = wc.bdd_bool_inp(expectationBoolean)
	print('\t'.join(['',context.ip,'actual:' + str(context.pingable),'','expected:' + str(expectationBoolean)]))
	assert context.pingable == expectationBoolean
