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
		InSimulationMode="FALSE", \
		UseSmbMessaging="FALSE", \
		IsLoadingFromConfiguration="TRUE", \
		ApplicationName="TestCenter", \
		TSharkPath="", \
		Active="TRUE", \
		LocalActive="TRUE", \
		Name="StcSystem 1")
	wc.pairprint('\n\nBuilt System', wc.timer_index_since(system_time))
	project_time = wc.timer_index_start()
	wc.jd(stc.get('system1'))
	Project_1 = stc.create("Project", \
		TableViewData="", \
		TestMode="L2L3", \
		SelectedTechnologyProfiles="dhcp", \
		Active="TRUE", \
		LocalActive="TRUE", \
		Name=project_name)
	wc.pairprint('\n\nBuilt Project: ' + project_name, wc.timer_index_since(project_time))
	wc.jd(stc.get(Project_1))
	return(Project_1)

def connectChassis(ip):
	global hPhysical
	connect_time = wc.timer_index_start()
	result = stc.connect(ip)
	stc.apply()
	hPhysical = stc.create('PhysicalChassisManager', under='system1')
	wc.pairprint('\n\nConnect to CHASSIS: ' + ip, wc.timer_index_since(connect_time))
	# wc.jd(stc.get(result))
	wc.jd(stc.get(hPhysical))
	return(result)

def port_config(hProject, portname):
	portbuild_time = wc.timer_index_start()
	Port_1 = stc.create("Port", under=hProject, \
		location = portname, \
		UseDefaultHost="TRUE", \
		AppendLocationToPortName="TRUE", \
		Layer3Type="IPV4", \
		PortGroupSize="1", \
		TestModuleProfile="Default", \
		IsFlexEthernetPort="FALSE", \
		IsFlexEthernetPhy="FALSE", \
		IsFlexEthernetClient="FALSE", \
		IsPgaPort="TRUE", \
		Active="TRUE", \
		LocalActive="TRUE", \
		Name="Port @ " + portname)
	wc.pairprint('\n\nBuilt Port: ' + portname, wc.timer_index_since(portbuild_time))
	return(Port_1)

def config(Project_1, resultsDir,portLocations):
    # StcTest.config( sys.path[0], [ '//10.44.0.21/9/1', '//10.44.0.21/9/11', '//10.44.0.21/9/12' ] )
    Tags_1 = (stc.get( Project_1, 'children-Tags' )).split(' ')[0]
    stc.config(Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Tags 1")

    Tag_1 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    Tag_2 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Router")

    Tag_3 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Client")

    Tag_4 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Server")

    Tag_5 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Core")

    Tag_6 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Edge")

    TestInfo_1 = (stc.get( Project_1, 'children-TestInfo' )).split(' ')[0]
    stc.config(TestInfo_1, \
    OwnerDisplayName="", \
    TestName="Untitled", \
    Description="", \
    UserTags="", \
    WebUILaunched="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestInfo 1")

    FrameLengthDistribution_1 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Default")

    FrameLengthDistributionSlot_1 = (stc.get( FrameLengthDistribution_1, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 5")

    FrameLengthDistributionSlot_2 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 6")

    FrameLengthDistributionSlot_3 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 7")

    FrameLengthDistribution_2 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Spirent")

    FrameLengthDistributionSlot_4 = (stc.get( FrameLengthDistribution_2, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 13")

    FrameLengthDistributionSlot_5 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="44", \
    MinFrameLength="43", \
    MaxFrameLength="45", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 14")

    FrameLengthDistributionSlot_6 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 15")

    FrameLengthDistributionSlot_7 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 16")

    FrameLengthDistribution_3 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="4-Point")

    FrameLengthDistributionSlot_8 = (stc.get( FrameLengthDistribution_3, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_8, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="55", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 8")

    FrameLengthDistributionSlot_9 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="15", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 9")

    FrameLengthDistributionSlot_10 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 10")

    FrameLengthDistributionSlot_11 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="RANDOM", \
    FixedFrameLength="730", \
    MinFrameLength="40", \
    MaxFrameLength="1500", \
    Weight="20", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 11")

    FrameLengthDistribution_4 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TCPv4")

    FrameLengthDistributionSlot_12 = (stc.get( FrameLengthDistribution_4, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_12, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 17")

    FrameLengthDistributionSlot_13 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 18")

    FrameLengthDistributionSlot_14 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 19")

    FrameLengthDistributionSlot_15 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 20")

    FrameLengthDistribution_5 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPSEC")

    FrameLengthDistributionSlot_16 = (stc.get( FrameLengthDistribution_5, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_16, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 21")

    FrameLengthDistributionSlot_17 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 22")

    FrameLengthDistributionSlot_18 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 23")

    FrameLengthDistributionSlot_19 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1400", \
    MinFrameLength="1399", \
    MaxFrameLength="1401", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 24")

    FrameLengthDistribution_6 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Downstream")

    FrameLengthDistributionSlot_20 = (stc.get( FrameLengthDistribution_6, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_20, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 53")

    FrameLengthDistributionSlot_21 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 54")

    FrameLengthDistributionSlot_22 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 55")

    FrameLengthDistributionSlot_23 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="5", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 56")

    FrameLengthDistribution_7 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Upstream")

    FrameLengthDistributionSlot_24 = (stc.get( FrameLengthDistribution_7, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_24, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 49")

    FrameLengthDistributionSlot_25 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="8", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 50")

    FrameLengthDistributionSlot_26 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 51")

    FrameLengthDistributionSlot_27 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 52")

    CustomFillPattern_1 = stc.create("CustomFillPattern",under = Project_1, \
    PatternData="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Pattern 1")

    DeviceAddrOptions_1 = (stc.get( Project_1, 'children-DeviceAddrOptions' )).split(' ')[0]
    stc.config(DeviceAddrOptions_1, \
    NextIpv4="192.85.1.7", \
    Ipv4Increment="0.0.0.1", \
    DefaultIpv4Prefix="24", \
    NextIpv6="2001::2", \
    Ipv6Increment="::1", \
    DefaultIpv6Prefix="64", \
    NextMac="00:10:94:00:00:05", \
    MacIncrement="00:00:00:00:00:01", \
    NextRouterId="192.0.0.5", \
    RouterIdIncrement="0.0.0.1", \
    NextIpv6RouterId="2000::5", \
    Ipv6RouterIdIncrement="::1", \
    NextWwn="20:00:10:85:00:00:00:01", \
    WwnIncrement="00:00:00:00:00:00:00:01", \
    UseForDeviceGenConfigExpand="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceAddrOptions 1")

    Ieee80211PhyOptions_1 = (stc.get( Project_1, 'children-Ieee80211PhyOptions' )).split(' ')[0]
    stc.config(Ieee80211PhyOptions_1, \
    SelectedRegion="USA", \
    AutoConnect="FALSE", \
    ScanDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee80211PhyOptions 1")

    PhyOptions_1 = (stc.get( Project_1, 'children-PhyOptions' )).split(' ')[0]
    stc.config(PhyOptions_1, \
    EnableCompensationMode="FALSE", \
    Enable8023brSwitch="FALSE", \
    EnableL1RegisterAccess="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhyOptions 1")

    TestResultSetting_1 = (stc.get( Project_1, 'children-TestResultSetting' )).split(' ')[0]
    stc.config(TestResultSetting_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestResultSetting 1")

    PortOptions_1 = (stc.get( Project_1, 'children-PortOptions' )).split(' ')[0]
    stc.config(PortOptions_1, \
    ReleaseMode="FULL_RESET", \
    AggregatorResult="AGGREGATED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Port Options 1")

    RealismOptions_1 = (stc.get( Project_1, 'children-RealismOptions' )).split(' ')[0]
    stc.config(RealismOptions_1, \
    RealismMode="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Realism Options 1")

    EventPublisherConfig_1 = (stc.get( Project_1, 'children-EventPublisherConfig' )).split(' ')[0]
    stc.config(EventPublisherConfig_1, \
    IsEnabled="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EventPublisherConfig 1")

    TrafficOptions_1 = (stc.get( Project_1, 'children-TrafficOptions' )).split(' ')[0]
    stc.config(TrafficOptions_1, \
    TrafficStartMode="ASYNCHRONOUS", \
    TrafficStartInterval="0", \
    TrafficStartIntervalUnit="UNITOF64US", \
    TrafficStreamIDStartIndex="1", \
    DeleteInactiveStreamsFromMemory="FALSE", \
    EnableGlobalAnalyzerPreload="FALSE", \
    TSharkPath="None", \
    ExcludeEthernetFcs="TRUE", \
    SmoothenRandomLength="FALSE", \
    UniqueRandomLengthSeedPerPort="FALSE", \
    EnableTxQueueFullRetryMode="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TrafficOptions 1")

    GroupHistogram_1 = (stc.get( Project_1, 'children-GroupHistogram' )).split(' ')[0]
    stc.config(GroupHistogram_1, \
    ActiveGroupHistogramMode="DISABLED_MODE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Group Histogram 1")

    ResultOptions_1 = (stc.get( Project_1, 'children-ResultOptions' )).split(' ')[0]
    stc.config(ResultOptions_1, \
    ResultViewMode="BASIC", \
    ColumnFilterMode="BASIC", \
    ShowWarningMessage="TRUE", \
    StopTrafficBeforeClearingResults="FALSE", \
    StopAnalyzerBeforeClearingResults="FALSE", \
    SyncClearResults="FALSE", \
    TimedRefreshResultViewMode="PERIODIC", \
    TimedRefreshInterval="1", \
    CollectStrayFrame="FALSE", \
    PreambleByteLength="8", \
    IfgByteLength="12", \
    JitterMode="RFC3393ABSOLUTEVALUE", \
    DeleteAllAnalyzerStreams="FALSE", \
    SaveAtEotProperties="", \
    TxPortExpectMCastTrafficSentFromSelf="FALSE", \
    SaveOnlyCountersFromResultViewMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultOptions 1")

    LabelBindingGlobalConfig_1 = (stc.get( Project_1, 'children-LabelBindingGlobalConfig' )).split(' ')[0]
    stc.config(LabelBindingGlobalConfig_1, \
    SubscriptionInterval="5", \
    LabelResolutionMode="PER_SESSION_LABEL_RESOLUTION", \
    SelectDeactivedTunnelForData="TRUE", \
    EnableTransmitUnresolvedStream="TRUE", \
    EnableStaticPwAttachmentGroupId="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LabelBindingGlobalConfig 1")

    MplsTpGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpGlobalConfig_1, \
    FMChannelType="88", \
    PWChannelType="34", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpGlobalConfig 1")

    L2LearningConfig_1 = (stc.get( Project_1, 'children-L2LearningConfig' )).split(' ')[0]
    stc.config(L2LearningConfig_1, \
    Rate="1000", \
    RepeatCount="3", \
    LearningStartDelay="1", \
    L2FrameSize="SAME_AS_STREAM", \
    L2FrameSizeFixed="128", \
    EncapOption="USE_TX_ENCAP", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2LearningConfig 1")

    ArpNdConfig_1 = (stc.get( Project_1, 'children-ArpNdConfig' )).split(' ')[0]
    stc.config(ArpNdConfig_1, \
    LearningRate="250", \
    MaxBurst="16", \
    EnableCyclicArp="TRUE", \
    DuplicateGatewayDetection="TRUE", \
    RetryCount="3", \
    TimeOut="1000", \
    EnableUniqueMacAddrInReply="FALSE", \
    EnableUniqueMacPattern="2222", \
    ProcessGratuitousArpRequests="TRUE", \
    UpdateDestMacUponNonGratuitousArpRequestsReceived="FALSE", \
    ProcessUnsolicitedArpReplies="TRUE", \
    EnableAutoArp="FALSE", \
    ApplyConfiguredGatewayMac="FALSE", \
    SetArpNdNoExpire="FALSE", \
    IgnoreFailures="TRUE", \
    UseLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseConfiguredLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseLinklayerCacheInStack="FALSE", \
    UseGatewayForTarget="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdConfig 1")

    BgpGlobalConfig_1 = (stc.get( Project_1, 'children-BgpGlobalConfig' )).split(' ')[0]
    stc.config(BgpGlobalConfig_1, \
    SequentialStartup="DISABLE", \
    StaggerOpen="100", \
    StaggerClose="100", \
    ConnectionRetryInterval="30", \
    ConnectionRetryCount="100", \
    UpdateCount="2000", \
    UpdateDelay="1", \
    VplsDraftVersion="VERSION_VPLS_4761", \
    ScalabilityMode="NORMAL", \
    EnableTcpNoDelay="FALSE", \
    EnablePackUpdates="TRUE", \
    TxTcpBufferSize="TCPBUFFER_32KB", \
    RxTcpBufferSize="TCPBUFFER_32KB", \
    TcpMaxSegmentSize="1460", \
    EnableStraightforwardUpdate="FALSE", \
    IgnoreAttributeErrors="FALSE", \
    MvpnAutoAdvertiseDelay="1000", \
    IsEvpnIRB="FALSE", \
    EvpnIRBMode="ASYMMETRIC", \
    NextHopFilterMode="DISABLED", \
    EnableDiscardUpdates="FALSE", \
    DisablePathMtuDiscovery="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpGlobalConfig 1")

    BgpSrGlobalConfig_1 = (stc.get( BgpGlobalConfig_1, 'children-BgpSrGlobalConfig' )).split(' ')[0]
    stc.config(BgpSrGlobalConfig_1, \
    SrDraftVersion="VERSION_00", \
    Srv6DraftVersion="VERSION_05", \
    PrefixSidAttrType="40", \
    Srv6TlvType="5", \
    Srv6L2ServiceTlvType="6", \
    SrVpnTrafficBindingKey="RD", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalConfig 1")

    BgpSrGlobalBlock_1 = (stc.get( BgpSrGlobalConfig_1, 'children-BgpSrGlobalBlock' )).split(' ')[0]
    stc.config(BgpSrGlobalBlock_1, \
    BlockBase="16000", \
    BlockRange="1000", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalBlock 1")

    PimGlobalConfig_1 = (stc.get( Project_1, 'children-PimGlobalConfig' )).split(' ')[0]
    stc.config(PimGlobalConfig_1, \
    TriggerHelloDelay="5", \
    EnablingPruningDelayOption="FALSE", \
    Tbit="FALSE", \
    LanPruneDelay="500", \
    OverrideInterval="2500", \
    EnablePackGroupRecord="TRUE", \
    EnableMsgRate="FALSE", \
    MsgRate="100", \
    MsgInterval="1", \
    DisableHelloExpireTimer="FALSE", \
    DisableHelloRxInNeighborState="FALSE", \
    DisableIncomingMsgProcessing="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PimGlobalConfig 1")

    IsisGlobalConfig_1 = (stc.get( Project_1, 'children-IsisGlobalConfig' )).split(' ')[0]
    stc.config(IsisGlobalConfig_1, \
    ScalabilityMode="NORMAL", \
    UseSameSrgb="FALSE", \
    SrmsPreferenceSubTlvType="24", \
    Srv6CapabilitySubTlvType="25", \
    Srv6LocatorTlvType="27", \
    Srv6EndSidSubTlvType="5", \
    Srv6EndXSidSubTlvType="43", \
    Srv6LanEndXSidSubTlvType="44", \
    SrNodeMsdSubTlvType="23", \
    SrLinkMsdSubTlvType="15", \
    FapmSubTlvType="5", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisGlobalConfig 1")

    IsisPlsbGlobalConfig_1 = (stc.get( Project_1, 'children-IsisPlsbGlobalConfig' )).split(' ')[0]
    stc.config(IsisPlsbGlobalConfig_1, \
    PlsbNlpid="143", \
    PlsbInstanceTlvType="180", \
    PlsbIsidAddrTlvType="181", \
    PlsbLinkMetricSubTlvType="17", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisPlsbGlobalConfig 1")

    OtvOptions_1 = (stc.get( Project_1, 'children-OtvOptions' )).split(' ')[0]
    stc.config(OtvOptions_1, \
    UnicastOnlyTransport="FALSE", \
    OverlayEncapMode="MPLS_GRE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OTV Project-Level Options 1")

    VxlanGlobalConfig_1 = (stc.get( Project_1, 'children-VxlanGlobalConfig' )).split(' ')[0]
    stc.config(VxlanGlobalConfig_1, \
    EnableVxlanScale="TRUE", \
    EnableTrafficScaleForEvpnLearning="FALSE", \
    EnableVxlanFlowBasedTraffic="FALSE", \
    EnableEvpnOverlayIRB="FALSE", \
    EvpnOverlayIRBMode="ASYMMETRIC", \
    DiscardEvpnLearning="FALSE", \
    EnableDRVForVxlanBindings="FALSE", \
    EnableEvpnType5VA="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VxlanGlobalConfig 1")

    PcepGlobalConfig_1 = (stc.get( Project_1, 'children-PcepGlobalConfig' )).split(' ')[0]
    stc.config(PcepGlobalConfig_1, \
    SessionOutStanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    LSPPerMessage="100", \
    TCPInterval="500", \
    PacketAlignToMTU="FALSE", \
    EnableTCPNoDelay="FALSE", \
    UseSRDraft5="FALSE", \
    AssociationTypeListTlvType="200", \
    PpagAssociationType="100", \
    PpagTlvType="100", \
    PathSegmentTlvType="80", \
    PathBindingTlvType="81", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PcepGlobalConfig 1")

    Ieee8021asGlobalConfig_1 = (stc.get( Project_1, 'children-Ieee8021asGlobalConfig' )).split(' ')[0]
    stc.config(Ieee8021asGlobalConfig_1, \
    ManagementId="12292", \
    TlvType="32772", \
    SlaveInfoSetCount="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee8021asGlobalConfig 1")

    Dhcpv4Options_1 = (stc.get( Project_1, 'children-Dhcpv4Options' )).split(' ')[0]
    stc.config(Dhcpv4Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4Options 1")

    Dhcpv6Options_1 = (stc.get( Project_1, 'children-Dhcpv6Options' )).split(' ')[0]
    stc.config(Dhcpv6Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6Options 1")

    PppoxOptions_1 = (stc.get( Project_1, 'children-PppoxOptions' )).split(' ')[0]
    stc.config(PppoxOptions_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_CONNECTED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxOptions 1")

    CuspGlobalConfig_1 = (stc.get( Project_1, 'children-CuspGlobalConfig' )).split(' ')[0]
    stc.config(CuspGlobalConfig_1, \
    SessionRetryCount="10", \
    SessionRetryInterval="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CuspGlobalConfig 1")

    MplsTpOamGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpOamGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpOamGlobalConfig_1, \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    TstOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"MPLSTPOAMTLV:TestTLV\"><Length>0040</Length></pdu></pdus></config></frame>", \
    ChannelType="8902", \
    EchoTlvsInLmr="FALSE", \
    EchoTlvsInDmr="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpOamGlobalConfig 1")

    EoamGlobalConfig_1 = (stc.get( Project_1, 'children-EoamGlobalConfig' )).split(' ')[0]
    stc.config(EoamGlobalConfig_1, \
    DmCommonTimeSource="FALSE", \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    SlrTxFCbStart="1", \
    SlrTxFCbStep="1", \
    SlmTxFCfOffset="0", \
    SlrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LtmOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTMEgrID\"><Length>0000</Length></pdu></pdus></config></frame>", \
    LtrOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTREgrID\"><Length>0000</Length></pdu><pdu name=\"RplyEgr_1\" pdu=\"EOAMTLV:RplyEgr\"><Length>0000</Length></pdu></pdus></config></frame>", \
    DmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    DmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    ResultTimeUnit="MILLISECONDS", \
    TestModeType="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamGlobalConfig 1")

    VqAnalyzerOptions_1 = (stc.get( Project_1, 'children-VqAnalyzerOptions' )).split(' ')[0]
    stc.config(VqAnalyzerOptions_1, \
    SamplingPeriod="10", \
    DatabaseFileName="vqAnalyzerTest.db", \
    AppendDateTime="TRUE", \
    EnableEotDatabase="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzerOptions 1")

    ExternalDeviceOption_1 = (stc.get( Project_1, 'children-ExternalDeviceOption' )).split(' ')[0]
    stc.config(ExternalDeviceOption_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ExternalDeviceOption 1")

    Dot1xOptions_1 = (stc.get( Project_1, 'children-Dot1xOptions' )).split(' ')[0]
    stc.config(Dot1xOptions_1, \
    TrafficStartOption="REQUIRE_ALL_SUPPLICANT_AUTH", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dot1xOptions 1")

    VicGlobalConfig_1 = (stc.get( Project_1, 'children-VicGlobalConfig' )).split(' ')[0]
    stc.config(VicGlobalConfig_1, \
    OpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    CreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"><Type>12</Type><Length>0</Length><ProvisioningInfoTypeSpace>00000C</ProvisioningInfoTypeSpace><Info><ProvList name=\"ProvList_0\"><Fixed><NumOfTlvs>0</NumOfTlvs><SubTlvs><FixedSubTlvList name=\"FixedSubTlvList_0\"><ProfileNameTlv><Type>1</Type><Length>0</Length></ProfileNameTlv></FixedSubTlvList><FixedSubTlvList name=\"FixedSubTlvList_1\"><vNicUuidTlv><Type>2</Type><Length>0</Length></vNicUuidTlv></FixedSubTlvList></SubTlvs></Fixed></ProvList></Info></pdu></pdus></config></frame>", \
    EnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    SpirentOpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    SpirentCreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"></pdu></pdus></config></frame>", \
    SpirentEnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VIC 1")

    MsdpGlobalConfig_1 = (stc.get( Project_1, 'children-MsdpGlobalConfig' )).split(' ')[0]
    stc.config(MsdpGlobalConfig_1, \
    SessionOutstanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    SourceActiveAdvertisementTimer="60", \
    SourceActiveStateTimer="100", \
    PacketAlignToMTU="FALSE", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MsdpGlobalConfig 1")

    OamFlexeGlobalConfig_1 = (stc.get( Project_1, 'children-OamFlexeGlobalConfig' )).split(' ')[0]
    stc.config(OamFlexeGlobalConfig_1, \
    CodeO="75", \
    CodeC="12", \
    BasType="1", \
    ApsType="2", \
    CvType="17", \
    DmType="18", \
    DmmType="19", \
    DmmrType="20", \
    CsType="21", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OamFlexeGlobalConfig 1")

    ResultDataSet_1 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="Port", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="100", \
    NotifyInterval="1000", \
    Identifier="Port Traffic\\Basic Traffic Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/Port", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Basic Traffic Results")

    ResultQuery_1 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="generator", \
    ResultClassId="generatorportresults", \
    PropertyIdArray="generatorportresults.totalframecount generatorportresults.totaloctetcount generatorportresults.generatorframecount generatorportresults.generatoroctetcount generatorportresults.generatorsigframecount generatorportresults.generatorundersizeframecount generatorportresults.generatoroversizeframecount generatorportresults.generatorjumboframecount generatorportresults.totalframerate generatorportresults.totaloctetrate generatorportresults.generatorframerate generatorportresults.generatoroctetrate generatorportresults.generatorsigframerate generatorportresults.generatorundersizeframerate generatorportresults.generatoroversizeframerate generatorportresults.generatorjumboframerate generatorportresults.generatorcrcerrorframecount generatorportresults.generatorl3checksumerrorcount generatorportresults.generatorl4checksumerrorcount generatorportresults.generatorcrcerrorframerate generatorportresults.generatorl3checksumerrorrate generatorportresults.generatorl4checksumerrorrate generatorportresults.totalipv4framecount generatorportresults.totalipv6framecount generatorportresults.totalmplsframecount generatorportresults.generatoripv4framecount generatorportresults.generatoripv6framecount generatorportresults.generatorvlanframecount generatorportresults.generatormplsframecount generatorportresults.totalipv4framerate generatorportresults.totalipv6framerate generatorportresults.totalmplsframerate generatorportresults.generatoripv4framerate generatorportresults.generatoripv6framerate generatorportresults.generatorvlanframerate generatorportresults.generatormplsframerate generatorportresults.totalbitrate generatorportresults.generatorbitrate generatorportresults.l1bitcount generatorportresults.l1bitrate generatorportresults.pfcframecount generatorportresults.pfcpri0framecount generatorportresults.pfcpri1framecount generatorportresults.pfcpri2framecount generatorportresults.pfcpri3framecount generatorportresults.pfcpri4framecount generatorportresults.pfcpri5framecount generatorportresults.pfcpri6framecount generatorportresults.pfcpri7framecount generatorportresults.txqueuefulldropcount generatorportresults.txqueuefullretrycount generatorportresults.l1bitratepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 32")

    ResultQuery_2 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="analyzer", \
    ResultClassId="analyzerportresults", \
    PropertyIdArray="analyzerportresults.totalframecount analyzerportresults.totaloctetcount analyzerportresults.sigframecount analyzerportresults.undersizeframecount analyzerportresults.oversizeframecount analyzerportresults.jumboframecount analyzerportresults.minframelength analyzerportresults.maxframelength analyzerportresults.pauseframecount analyzerportresults.totalframerate analyzerportresults.totaloctetrate analyzerportresults.sigframerate analyzerportresults.undersizeframerate analyzerportresults.oversizeframerate analyzerportresults.jumboframerate analyzerportresults.pauseframerate analyzerportresults.fcserrorframecount analyzerportresults.ipv4checksumerrorcount analyzerportresults.tcpchecksumerrorcount analyzerportresults.udpchecksumerrorcount analyzerportresults.prbsfilloctetcount analyzerportresults.prbsbiterrorcount analyzerportresults.fcserrorframerate analyzerportresults.ipv4checksumerrorrate analyzerportresults.tcpchecksumerrorrate analyzerportresults.udpchecksumerrorrate analyzerportresults.prbsfilloctetrate analyzerportresults.prbsbiterrorrate analyzerportresults.ipv4framecount analyzerportresults.ipv6framecount analyzerportresults.ipv6overipv4framecount analyzerportresults.tcpframecount analyzerportresults.udpframecount analyzerportresults.mplsframecount analyzerportresults.icmpframecount analyzerportresults.vlanframecount analyzerportresults.ipv4framerate analyzerportresults.ipv6framerate analyzerportresults.ipv6overipv4framerate analyzerportresults.tcpframerate analyzerportresults.udpframerate analyzerportresults.mplsframerate analyzerportresults.icmpframerate analyzerportresults.vlanframerate analyzerportresults.trigger1count analyzerportresults.trigger1rate analyzerportresults.trigger2count analyzerportresults.trigger2rate analyzerportresults.trigger3count analyzerportresults.trigger3rate analyzerportresults.trigger4count analyzerportresults.trigger4rate analyzerportresults.trigger5count analyzerportresults.trigger5rate analyzerportresults.trigger6count analyzerportresults.trigger6rate analyzerportresults.trigger7count analyzerportresults.trigger7rate analyzerportresults.trigger8count analyzerportresults.trigger8rate analyzerportresults.combotriggercount analyzerportresults.combotriggerrate analyzerportresults.totalbitrate analyzerportresults.prbsbiterrorratio analyzerportresults.vlanframerate analyzerportresults.l1bitcount analyzerportresults.l1bitrate analyzerportresults.pfcframecount analyzerportresults.fcoeframecount analyzerportresults.pfcframerate analyzerportresults.fcoeframerate analyzerportresults.pfcpri0framecount analyzerportresults.pfcpri1framecount analyzerportresults.pfcpri2framecount analyzerportresults.pfcpri3framecount analyzerportresults.pfcpri4framecount analyzerportresults.pfcpri5framecount analyzerportresults.pfcpri6framecount analyzerportresults.pfcpri7framecount analyzerportresults.pfcpri0quanta analyzerportresults.pfcpri1quanta analyzerportresults.pfcpri2quanta analyzerportresults.pfcpri3quanta analyzerportresults.pfcpri4quanta analyzerportresults.pfcpri5quanta analyzerportresults.pfcpri6quanta analyzerportresults.pfcpri7quanta analyzerportresults.prbserrorframecount analyzerportresults.prbserrorframerate analyzerportresults.userdefinedframecount1 analyzerportresults.userdefinedframerate1 analyzerportresults.userdefinedframecount2 analyzerportresults.userdefinedframerate2 analyzerportresults.userdefinedframecount3 analyzerportresults.userdefinedframerate3 analyzerportresults.userdefinedframecount4 analyzerportresults.userdefinedframerate4 analyzerportresults.userdefinedframecount5 analyzerportresults.userdefinedframerate5 analyzerportresults.userdefinedframecount6 analyzerportresults.userdefinedframerate6 analyzerportresults.avglatency analyzerportresults.minlatency analyzerportresults.maxlatency analyzerportresults.totallatency analyzerportresults.l1bitratepercent analyzerportresults.outseqframecount analyzerportresults.preambletotalbytes analyzerportresults.preambleminlength analyzerportresults.preamblemaxlength analyzerportresults.droppedframecount analyzerportresults.inorderframecount analyzerportresults.reorderedframecount analyzerportresults.duplicateframecount analyzerportresults.lateframecount analyzerportresults.firstarrivaltime analyzerportresults.lastarrivaltime analyzerportresults.correctedrsfecerrorcount analyzerportresults.uncorrectedrsfecerrorcount analyzerportresults.correctedbaserfecerrorcount analyzerportresults.uncorrectedbaserfecerrorcount analyzerportresults.correctedrsfecsymbols analyzerportresults.prersfecserrate analyzerportresults.postrsfecserrate analyzerportresults.prebaserfecserrate analyzerportresults.postbaserfecserrate", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 33")

    RealTimeResultColumnDefinition_1 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 671")

    RealTimeResultColumnDefinition_2 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 672")

    RealTimeResultColumnDefinition_3 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 673")

    RealTimeResultColumnDefinition_4 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 674")

    RealTimeResultColumnDefinition_5 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 675")

    RealTimeResultColumnDefinition_6 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 676")

    RealTimeResultColumnDefinition_7 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 677")

    RealTimeResultColumnDefinition_8 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 678")

    RealTimeResultColumnDefinition_9 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 679")

    RealTimeResultColumnDefinition_10 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_11 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_12 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_13 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_14 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 682")

    RealTimeResultColumnDefinition_15 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="167", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 683")

    RealTimeResultColumnDefinition_16 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="130", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 684")

    RealTimeResultColumnDefinition_17 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 685")

    RealTimeResultColumnDefinition_18 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 686")

    RealTimeResultColumnDefinition_19 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 687")

    RealTimeResultColumnDefinition_20 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOctetRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 688")

    RealTimeResultColumnDefinition_21 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="131", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 689")

    RealTimeResultColumnDefinition_22 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="139", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 690")

    RealTimeResultColumnDefinition_23 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="102", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 691")

    RealTimeResultColumnDefinition_24 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="197", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 692")

    RealTimeResultColumnDefinition_25 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="201", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 693")

    RealTimeResultColumnDefinition_26 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 694")

    RealTimeResultColumnDefinition_27 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 695")

    RealTimeResultColumnDefinition_28 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="171", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 696")

    RealTimeResultColumnDefinition_29 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="168", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 697")

    RealTimeResultColumnDefinition_30 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="170", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 698")

    RealTimeResultColumnDefinition_31 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsFillOctetCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 699")

    RealTimeResultColumnDefinition_32 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="137", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 700")

    RealTimeResultColumnDefinition_33 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRatio", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 701")

    RealTimeResultColumnDefinition_34 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="134", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 702")

    RealTimeResultColumnDefinition_35 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="172", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 703")

    RealTimeResultColumnDefinition_36 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 704")

    RealTimeResultColumnDefinition_37 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 705")

    RealTimeResultColumnDefinition_38 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="164", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 706")

    RealTimeResultColumnDefinition_39 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="162", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 707")

    RealTimeResultColumnDefinition_40 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="163", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 708")

    RealTimeResultColumnDefinition_41 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="169", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 709")

    RealTimeResultColumnDefinition_42 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 710")

    RealTimeResultColumnDefinition_43 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 711")

    RealTimeResultColumnDefinition_44 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 712")

    RealTimeResultColumnDefinition_45 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 713")

    RealTimeResultColumnDefinition_46 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 714")

    RealTimeResultColumnDefinition_47 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 715")

    RealTimeResultColumnDefinition_48 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 716")

    RealTimeResultColumnDefinition_49 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 717")

    RealTimeResultColumnDefinition_50 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="87", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 718")

    RealTimeResultColumnDefinition_51 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 719")

    RealTimeResultColumnDefinition_52 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 720")

    RealTimeResultColumnDefinition_53 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 721")

    RealTimeResultColumnDefinition_54 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 722")

    RealTimeResultColumnDefinition_55 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 723")

    RealTimeResultColumnDefinition_56 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 724")

    RealTimeResultColumnDefinition_57 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 725")

    RealTimeResultColumnDefinition_58 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 726")

    RealTimeResultColumnDefinition_59 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="114", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 727")

    RealTimeResultColumnDefinition_60 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="86", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 728")

    RealTimeResultColumnDefinition_61 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="88", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 729")

    RealTimeResultColumnDefinition_62 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="91", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 730")

    RealTimeResultColumnDefinition_63 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="129", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 731")

    RealTimeResultColumnDefinition_64 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 732")

    RealTimeResultColumnDefinition_65 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 733")

    RealTimeResultColumnDefinition_66 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="132", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 734")

    RealTimeResultColumnDefinition_67 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 735")

    RealTimeResultColumnDefinition_68 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="124", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 736")

    RealTimeResultColumnDefinition_69 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 737")

    RealTimeResultColumnDefinition_70 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 738")

    RealTimeResultColumnDefinition_71 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 739")

    RealTimeResultColumnDefinition_72 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 740")

    RealTimeResultColumnDefinition_73 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="113", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 741")

    RealTimeResultColumnDefinition_74 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="87", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 742")

    RealTimeResultColumnDefinition_75 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="96", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 743")

    RealTimeResultColumnDefinition_76 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="99", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 744")

    RealTimeResultGroupDefinition_1 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="All Groups", \
    GroupId="core://allgroups/", \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    CountQuery="", \
    SqlString="", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 37")

    RealTimeResultColumnDefinition_77 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="101", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 38")

    RealTimeResultGroupDefinition_2 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Basic Counters", \
    GroupId="object://customgroup/cded8621-5e71-4a39-afd4-71d9faf37273/Basic Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalBitCount TotalBitCount TotalBitRate TotalBitRate L1BitCount L1BitCount L1BitRate L1BitRate L1BitRatePercent L1BitRatePercent GeneratorFrameCount GeneratorSigFrameCount SigFrameCount TotalFrameRate TotalFrameRate GeneratorFrameRate GeneratorOctetRate GeneratorBitRate GeneratorSigFrameRate SigFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorFrameCount AS 'Generator Count (Frames)', GeneratorPortResults.GeneratorSigFrameCount AS 'Generator Sig Count (Frames)', AnalyzerPortResults.SigFrameCount AS 'Rx Sig Count (Frames)', (GeneratorPortResults.TotalOctetCount * 8) AS 'Total Tx  Count (bits)', (AnalyzerPortResults.TotalOctetCount * 8) AS 'Total Rx Count (bits)', GeneratorPortResults.L1BitCount AS 'Tx L1 Count (bits)', AnalyzerPortResults.L1BitCount AS 'Rx L1 Count (bits)', AnalyzerPortResults.MinFrameLength AS 'Rx Min FrameLength', AnalyzerPortResults.MaxFrameLength AS 'Rx Max FrameLength', GeneratorPortResults.TotalCellCount AS 'Total Tx Count (Cells)', AnalyzerPortResults.TotalCellCount AS 'Total Rx Count (Cells)', GeneratorPortResults.TxDuration AS 'Tx Duration (sec)' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_3 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Errors", \
    GroupId="object://customgroup/e26c15e5-fb73-46ad-a76b-45304a4e6303/Errors", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount FcsErrorFrameCount GeneratorCrcErrorFrameCount GeneratorL3ChecksumErrorCount GeneratorL4ChecksumErrorCount Ipv4ChecksumErrorCount TcpChecksumErrorCount UdpChecksumErrorCount PrbsFillOctetCount PrbsBitErrorCount PrbsBitErrorRatio PrbsErrorFrameCount FcsErrorFrameRate GeneratorCrcErrorFrameRate GeneratorL3ChecksumErrorRate GeneratorL4ChecksumErrorRate Ipv4ChecksumErrorRate TcpChecksumErrorRate UdpChecksumErrorRate PrbsBitErrorRate PrbsErrorFrameRate OutSeqFrameCount", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.FcsErrorFrameCount AS 'Rx FCS Error Count (Frames)', GeneratorPortResults.GeneratorCrcErrorFrameCount AS 'Generator CRC Error Count (Frames)', GeneratorPortResults.GeneratorL3ChecksumErrorCount AS 'Generator L3 Checksum Error Count', GeneratorPortResults.GeneratorL4ChecksumErrorCount AS 'Generator L4 Checksum Error Count', AnalyzerPortResults.Ipv4ChecksumErrorCount AS 'Rx IPv4 Checksum Error Count', AnalyzerPortResults.TcpChecksumErrorCount AS 'Rx TCP Checksum Error Count', AnalyzerPortResults.UdpChecksumErrorCount AS 'Rx UDP Checksum Error Count', AnalyzerPortResults.PrbsFillOctetCount AS 'Rx PRBS Fill Octet Count', AnalyzerPortResults.PrbsBitErrorCount AS 'Rx PRBS Bit Error Count', coalesce(round(cast(AnalyzerPortResults.PrbsBitErrorCount as double)/cast((AnalyzerPortResults.PrbsFillOctetCount * 8) as double), 3), 0.0) as 'PRBS Bit Error Ratio', AnalyzerPortResults.PrbsErrorFrameCount AS 'Rx PRBS Error Frame Count', AnalyzerPortResults.OutSeqFrameCount AS 'Rx Out of Sequence Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_4 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Triggers", \
    GroupId="object://customgroup/ddcfebff-9e2d-49e4-8d4a-1cde4792f3c1/Triggers", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount Trigger1Count Trigger2Count Trigger3Count Trigger4Count Trigger5Count Trigger6Count Trigger7Count Trigger8Count ComboTriggerCount Trigger1Rate Trigger2Rate Trigger3Rate Trigger4Rate Trigger5Rate Trigger6Rate Trigger7Rate Trigger8Rate ComboTriggerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 40")

    RealTimeResultGroupDefinition_5 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Protocols", \
    GroupId="object://customgroup/3e090a0e-d3c7-413f-ad01-ccb4a21de519/Protocols", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalIpv4FrameCount TotalIpv6FrameCount TotalMplsFrameCount GeneratorIpv4FrameCount GeneratorIpv6FrameCount GeneratorVlanFrameCount GeneratorMplsFrameCount Ipv4FrameCount Ipv6FrameCount TcpFrameCount UdpFrameCount MplsFrameCount IcmpFrameCount VlanFrameCount FcoeFrameCount TotalIpv4FrameRate TotalIpv6FrameRate TotalMplsFrameRate GeneratorIpv4FrameRate GeneratorIpv6FrameRate GeneratorVlanFrameRate GeneratorMplsFrameRate Ipv4FrameRate Ipv6FrameRate TcpFrameRate UdpFrameRate MplsFrameRate IcmpFrameRate VlanFrameRate FcoeFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Frame Count', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Frame Count', GeneratorPortResults.TotalIpv4FrameCount AS 'Total Tx IPv4 Frame', GeneratorPortResults.TotalIpv6FrameCount AS 'Total Tx IPv6 Frame', GeneratorPortResults.TotalMplsFrameCount AS 'Total Tx MPLS Frame', GeneratorPortResults.GeneratorIpv4FrameCount AS 'Generator IPv4 Frame Count', GeneratorPortResults.GeneratorIpv6FrameCount AS 'Generator IPv6 Frame Count', GeneratorPortResults.GeneratorVlanFrameCount AS 'Generator VLAN Frame Count', GeneratorPortResults.GeneratorMplsFrameCount AS 'Generator MPLS Frame Count', AnalyzerPortResults.Ipv4FrameCount AS 'Rx IPv4 Frame Count', AnalyzerPortResults.Ipv6FrameCount AS 'Rx IPv6 Frame Count', AnalyzerPortResults.TcpFrameCount AS 'Rx TCP Frame Count', AnalyzerPortResults.UdpFrameCount AS 'Rx UDP Frame Count', AnalyzerPortResults.MplsFrameCount AS 'Rx MPLS Frame Count', AnalyzerPortResults.IcmpFrameCount AS 'Rx ICMP Frame Count', AnalyzerPortResults.VlanFrameCount AS 'Rx VLAN Frame Count', AnalyzerPortResults.FcoeFrameCount AS 'Rx FCoE Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 41")

    RealTimeResultColumnDefinition_78 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="90", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 88")

    RealTimeResultColumnDefinition_79 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameRate", \
    ColumnDescription="", \
    ColumnWidth="115", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 89")

    RealTimeResultColumnDefinition_80 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 90")

    RealTimeResultColumnDefinition_81 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 91")

    RealTimeResultColumnDefinition_82 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 92")

    RealTimeResultColumnDefinition_83 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="114", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 93")

    RealTimeResultColumnDefinition_84 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 94")

    RealTimeResultColumnDefinition_85 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="77", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 95")

    RealTimeResultColumnDefinition_86 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="84", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 96")

    RealTimeResultColumnDefinition_87 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameRate", \
    ColumnDescription="", \
    ColumnWidth="86", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 97")

    RealTimeResultColumnDefinition_88 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="79", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 98")

    RealTimeResultColumnDefinition_89 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameRate", \
    ColumnDescription="", \
    ColumnWidth="113", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 99")

    RealTimeResultGroupDefinition_6 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Undersize/Oversize/Jumbo", \
    GroupId="object://customgroup/06ce5837-a7ee-427b-96e8-10cca3ff961a/Undersize/Oversize/Jumbo", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount GeneratorUndersizeFrameCount UndersizeFrameCount GeneratorOversizeFrameCount OversizeFrameCount GeneratorJumboFrameCount JumboFrameCount PauseFrameCount GeneratorUndersizeFrameRate UndersizeFrameRate GeneratorOversizeFrameRate OversizeFrameRate GeneratorJumboFrameRate JumboFrameRate PauseFrameRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 8")

    RealTimeResultColumnDefinition_90 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 100")

    RealTimeResultColumnDefinition_91 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 101")

    RealTimeResultColumnDefinition_92 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="200", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 102")

    RealTimeResultColumnDefinition_93 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 103")

    RealTimeResultColumnDefinition_94 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="194", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 104")

    RealTimeResultColumnDefinition_95 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="192", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 613")

    RealTimeResultColumnDefinition_96 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="185", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 614")

    RealTimeResultColumnDefinition_97 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="182", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 615")

    RealTimeResultColumnDefinition_98 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameCount", \
    ColumnDescription="", \
    ColumnWidth="179", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 616")

    RealTimeResultColumnDefinition_99 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="172", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 617")

    RealTimeResultColumnDefinition_100 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 618")

    RealTimeResultColumnDefinition_101 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="166", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 619")

    RealTimeResultColumnDefinition_102 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="129", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 127")

    RealTimeResultColumnDefinition_103 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="191", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 128")

    RealTimeResultColumnDefinition_104 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="119", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 129")

    RealTimeResultColumnDefinition_105 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameRate", \
    ColumnDescription="", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 130")

    RealTimeResultColumnDefinition_106 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="", \
    ColumnWidth="96", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 131")

    RealTimeResultColumnDefinition_107 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 132")

    RealTimeResultColumnDefinition_108 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 133")

    RealTimeResultColumnDefinition_109 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 134")

    RealTimeResultColumnDefinition_110 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 135")

    RealTimeResultColumnDefinition_111 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 136")

    RealTimeResultColumnDefinition_112 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 137")

    RealTimeResultColumnDefinition_113 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 138")

    RealTimeResultColumnDefinition_114 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_115 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_116 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_117 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_118 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_119 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_120 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_121 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_122 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_7 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="PFC Counters", \
    GroupId="object://customgroup/ce2848b9-5f04-419d-8809-030032c630e4/PFC Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount PfcFrameCount PfcFrameRate PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.PfcFrameCount AS 'Tx PFC Count (Frames)', AnalyzerPortResults.PfcFrameCount AS 'Rx PFC Count (Frames)', GeneratorPortResults.PfcPri0FrameCount AS 'Tx PFC Priority0 Count (Frames)', GeneratorPortResults.PfcPri1FrameCount AS 'Tx PFC Priority1 Count (Frames)', GeneratorPortResults.PfcPri2FrameCount AS 'Tx PFC Priority2 Count (Frames)', GeneratorPortResults.PfcPri3FrameCount AS 'Tx PFC Priority3 Count (Frames)', GeneratorPortResults.PfcPri4FrameCount AS 'Tx PFC Priority4 Count (Frames)', GeneratorPortResults.PfcPri5FrameCount AS 'Tx PFC Priority5 Count (Frames)', GeneratorPortResults.PfcPri6FrameCount AS 'Tx PFC Priority6 Count (Frames)', GeneratorPortResults.PfcPri7FrameCount AS 'Tx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0FrameCount AS 'Rx PFC Priority0 Count (Frames)', AnalyzerPortResults.PfcPri1FrameCount AS 'Rx PFC Priority1 Count (Frames)', AnalyzerPortResults.PfcPri2FrameCount AS 'Rx PFC Priority2 Count (Frames)', AnalyzerPortResults.PfcPri3FrameCount AS 'Rx PFC Priority3 Count (Frames)', AnalyzerPortResults.PfcPri4FrameCount AS 'Rx PFC Priority4 Count (Frames)', AnalyzerPortResults.PfcPri5FrameCount AS 'Rx PFC Priority5 Count (Frames)', AnalyzerPortResults.PfcPri6FrameCount AS 'Rx PFC Priority6 Count (Frames)', AnalyzerPortResults.PfcPri7FrameCount AS 'Rx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0Quanta AS 'Rx PFC Priority0 Quanta', AnalyzerPortResults.PfcPri1Quanta AS 'Rx PFC Priority1 Quanta', AnalyzerPortResults.PfcPri2Quanta AS 'Rx PFC Priority2 Quanta', AnalyzerPortResults.PfcPri3Quanta AS 'Rx PFC Priority3 Quanta', AnalyzerPortResults.PfcPri4Quanta AS 'Rx PFC Priority4 Quanta', AnalyzerPortResults.PfcPri5Quanta AS 'Rx PFC Priority5 Quanta', AnalyzerPortResults.PfcPri6Quanta AS 'Rx PFC Priority6 Quanta', AnalyzerPortResults.PfcPri7Quanta AS 'Rx PFC Priority7 Quanta' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_123 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_124 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OutSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_125 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_126 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_127 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_128 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_129 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_130 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_131 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_132 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_133 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_134 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_135 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_136 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_137 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_8 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="User Defined", \
    GroupId="object://customgroup/45684926-5012-4d7b-a560-70e552840cbb/User Defined", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1 UserDefinedFrameRate1 UserDefinedFrameCount2 UserDefinedFrameRate2 UserDefinedFrameCount3 UserDefinedFrameRate3 UserDefinedFrameCount4 UserDefinedFrameRate4 UserDefinedFrameCount5 UserDefinedFrameRate5 UserDefinedFrameCount6 UserDefinedFrameRate6", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.UserDefinedFrameCount1 AS 'User Defined Capture Frame Count 1 (Frames)', AnalyzerPortResults.UserDefinedFrameCount2 AS 'User Defined Capture Frame Count 2 (Frames)', AnalyzerPortResults.UserDefinedFrameCount3 AS 'User Defined Capture Frame Count 3 (Frames)', AnalyzerPortResults.UserDefinedFrameCount4 AS 'User Defined Capture Frame Count 4 (Frames)', AnalyzerPortResults.UserDefinedFrameCount5 AS 'User Defined Capture Frame Count 5 (Frames)', AnalyzerPortResults.UserDefinedFrameCount6 AS 'User Defined Capture Frame Count 6 (Frames)'  FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 14")

    RealTimeResultColumnDefinition_138 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="InOrderFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_139 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ReorderedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_140 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DroppedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_141 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DuplicateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_142 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="LateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_143 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TxQueueFullDropCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_144 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TxQueueFullRetryCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultGroupDefinition_9 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Advanced Sequencing", \
    GroupId="object://customgroup/d775c482-4220-4044-b3d8-d0980146f9dc/Advanced Sequencing", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults", \
    ColumnPropertyName="DroppedFrameCount InOrderFrameCount ReorderedFrameCount DuplicateFrameCount LateFrameCount TxQueueFullDropCount TxQueueFullRetryCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)', GeneratorPortResults.TxQueueFullDropCount AS 'Tx Queue Full Drop Count (Frames)', GeneratorPortResults.TxQueueFullRetryCount AS 'Tx Queue Full Retry Count (Frames)' FROM Port, AnalyzerPortResults, GeneratorPortResults, Analyzer, Generator WHERE ( Analyzer.ParentHnd = Port.Handle AND Generator.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)', GeneratorPortResults.TxQueueFullDropCount AS 'Tx Queue Full Drop Count (Frames)', GeneratorPortResults.TxQueueFullRetryCount AS 'Tx Queue Full Retry Count (Frames)' FROM ExternalDevicePort, AnalyzerPortResults, GeneratorPortResults, Port, Analyzer, Generator WHERE ( Analyzer.ParentHnd = Port.Handle AND Generator.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_145 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_146 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_147 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecSymbols", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_148 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_149 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 148")

    RealTimeResultColumnDefinition_150 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 149")

    RealTimeResultColumnDefinition_151 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 150")

    RealTimeResultColumnDefinition_152 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 151")

    RealTimeResultColumnDefinition_153 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 152")

    RealTimeResultGroupDefinition_10 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="FEC Counters", \
    GroupId="object://customgroup/bdefbcbd-7034-44a1-9d63-b5a6b6736efb/FEC Counters", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount UncorrectedRsFecErrorCount CorrectedRsFecSymbols CorrectedBaseRFecErrorCount UncorrectedBaseRFecErrorCount PreRsFecSerRate PostRsFecSerRate PreBaseRFecSerRate PostBaseRFecSerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (codewords)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Symbols', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (cwps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (cwps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (cwps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (cwps)' FROM Port, AnalyzerPortResults, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (codewords)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Symbols', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (cwps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (cwps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (cwps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (cwps)' FROM ExternalDevicePort, AnalyzerPortResults, Port, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 10")

    Perspective_1 = stc.create("Perspective",under = Project_1, \
    PerspectiveViewOwner="USER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Perspective 1")

    PerspectiveNode_1 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3", \
    Data="<NodeData Name=\"resultFrame.1\" FrameId=\"8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3\" Active=\"false\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData><NodeContentData FrameName=\"frame://l2l3/TxStreamResults/ResultQuery:(1, 0, 0)\" ResultDataSetId=\"Stream Results\\Detailed Stream Results\" Column=\"0\" Row=\"0\" DockPanelNumber=\"1\" /><NodeContentData FrameName=\"frame://core/DynamicResultView/ResultQuery:(1, 0, 1)\" ResultDataSetId=\"Port Traffic\\Summarized Basic Traffic Results\" Column=\"1\" Row=\"0\" DockPanelNumber=\"1\" /></ContentData>
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 7")

    PerspectiveNode_2 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="1F412EE6-760C-4937-9644-ACFA463EA44E", \
    Data="<NodeData Name=\"resultFrame.2\" FrameId=\"1F412EE6-760C-4937-9644-ACFA463EA44E\" Active=\"false\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData />
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 8")

    DynamicResultView_1 = stc.create("DynamicResultView",under = Project_1, \
    ResultSourceClass="Port", \
    SaveToConfig="TRUE", \
    Identifier="Port Traffic and Counters\\Aggregate Port L1 Tx Rate", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/DynamicResultView", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Aggregate Port L1 Tx Rate")

    PresentationResultQuery_1 = stc.create("PresentationResultQuery",under = DynamicResultView_1, \
    SelectProperties="Port.TxL1BitRate Port.TxMaxLineRate Project.Name", \
    WhereConditions="", \
    GroupByProperties="Project.Name", \
    LimitOffset="0", \
    LimitSize="2000", \
    SortBy="", \
    ArchivingOption="NONE", \
    ResultState="IDLE", \
    ArchivingInterval="10", \
    DatabaseFileName="", \
    DisableAutoGrouping="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PresentationResultQuery 1")

    ColumnDisplayProperties_1 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxL1BitRate", \
    ColumnCaption="Tx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 1")

    ColumnDisplayProperties_2 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxMaxLineRate", \
    ColumnCaption="Tx Max Line Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 2")

    ColumnDisplayProperties_3 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Project.Name", \
    ColumnCaption="Project Name", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 3")

    Host_1 = (stc.get( Port_1, 'children-Host' )).split(' ')[0]
    stc.config(Host_1, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    EthIIIf_1 = stc.create("EthIIIf",under = Host_1, \
    SourceMac="00:10:94:00:00:02", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 1")

    HdlcIf_1 = stc.create("HdlcIf",under = Host_1, \
    ProtocolType="HDLC_PROTOCOL_TYPE_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="HDLC 1")

    PppIf_1 = stc.create("PppIf",under = Host_1, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 1")

    PppIf_2 = stc.create("PppIf",under = Host_1, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 2")

    Ipv4If_1 = stc.create("Ipv4If",under = Host_1, \
    Address="192.85.1.3", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 1")

    Ipv6If_1 = stc.create("Ipv6If",under = Host_1, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 1")

    Ipv6If_2 = stc.create("Ipv6If",under = Host_1, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 2")

    SystemResourceManager_1 = (stc.get( Port_1, 'children-SystemResourceManager' )).split(' ')[0]
    stc.config(SystemResourceManager_1, \
    MemoryThreshold="80", \
    MemoryThresholdEnable="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Resource Manager 1")

    Generator_1 = (stc.get( Port_1, 'children-Generator' )).split(' ')[0]
    stc.config(Generator_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Generator 1")

    GeneratorConfig_1 = (stc.get( Generator_1, 'children-GeneratorConfig' )).split(' ')[0]
    stc.config(GeneratorConfig_1, \
    SchedulingMode="RATE_BASED", \
    AdvancedInterleaving="FALSE", \
    Duration="120", \
    DurationMode="CONTINUOUS", \
    StepSize="1", \
    TimestampLatchMode="START_OF_FRAME", \
    RandomLengthSeed="10900842", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    BurstSize="1", \
    LoadUnit="PERCENT_LINE_RATE", \
    LoadMode="FIXED", \
    FixedLoad="10", \
    RandomMaxLoad="100", \
    RandomMinLoad="10", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    SmoothenRandomLength="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Generator Configuration 1")

    Analyzer_1 = (stc.get( Port_1, 'children-Analyzer' )).split(' ')[0]
    stc.config(Analyzer_1, \
    FilterOnStreamId="TRUE", \
    FilterOnInnerIP="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Analyzer 1")

    AnalyzerConfig_1 = (stc.get( Analyzer_1, 'children-AnalyzerConfig' )).split(' ')[0]
    stc.config(AnalyzerConfig_1, \
    TimestampLatchMode="START_OF_FRAME", \
    SigMode="ENHANCED_DETECTION", \
    HistogramMode="LATENCY", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    AdvSeqCheckerLateThreshold="1000", \
    VlanAlternateTpid="34984", \
    AlternateSigOffset="0", \
    LatencyMode="PER_STREAM_RX_LATENCY_ON", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Advanced Analyzer Settings 1")

    InterarrivalTimeHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-InterarrivalTimeHistogram' )).split(' ')[0]
    stc.config(InterarrivalTimeHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    LatencyHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-LatencyHistogram' )).split(' ')[0]
    stc.config(LatencyHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    FrameLengthHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-FrameLengthHistogram' )).split(' ')[0]
    stc.config(FrameLengthHistogram_1, \
    Description="(in bytes)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    SeqRunLengthHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-SeqRunLengthHistogram' )).split(' ')[0]
    stc.config(SeqRunLengthHistogram_1, \
    Description="(in frames)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    SeqDiffCheckHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-SeqDiffCheckHistogram' )).split(' ')[0]
    stc.config(SeqDiffCheckHistogram_1, \
    Description="(in deltas)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    JitterHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-JitterHistogram' )).split(' ')[0]
    stc.config(JitterHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    DiffServConfig_1 = (stc.get( Analyzer_1, 'children-DiffServConfig' )).split(' ')[0]
    stc.config(DiffServConfig_1, \
    QualifyIpv6DstAddr="FALSE", \
    Ipv6DstAddr="ffff::ffff", \
    QualifyIpv4DstAddr="FALSE", \
    Ipv4DstAddr="0.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QoS Settings 1")

    HighResolutionSamplingPortConfig_1 = (stc.get( Analyzer_1, 'children-HighResolutionSamplingPortConfig' )).split(' ')[0]
    stc.config(HighResolutionSamplingPortConfig_1, \
    BaselineSampleCount="3", \
    EnableTrigger="TRUE", \
    TriggerCondition="LESS_THAN", \
    TriggerValueUnitMode="PERCENT_BASELINE", \
    TriggerStat="TotalFrameRate", \
    TriggerValue="95", \
    TriggerLocation="20", \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Port Sampling 1")

    HighResolutionStreamBlockOptions_1 = stc.create("HighResolutionStreamBlockOptions",under = Analyzer_1, \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Stream Block Options 2")

    Capture_1 = (stc.get( Port_1, 'children-Capture' )).split(' ')[0]
    stc.config(Capture_1, \
    ElapsedTime="0:00:00", \
    TabIndex="0", \
    Mode="REGULAR_MODE", \
    SrcMode="TX_RX_MODE", \
    RealTimeMode="REALTIME_DISABLE", \
    FlagMode="REGULAR_FLAG_MODE", \
    BufferMode="WRAP", \
    Start="16384", \
    Stop="0", \
    SliceMode="DISABLE", \
    SliceOffsetRef="PREAMBLE", \
    SliceOffset="0", \
    SliceCaptureSize="128", \
    RealTimeFramesBuffer="0", \
    RealTimeBufferStatus="FALSE", \
    CurrentTask="IDLE", \
    CurrentFiltersUsed="0", \
    CurrentFilterBytesUsed="0", \
    AbortSaveTask="FALSE", \
    PostStopTriggerBuffer="255", \
    CaptureFilterMode="FRAMECONTENT", \
    SaveBufferWithPreamble="FALSE", \
    IncreasedMemorySupport="FALSE", \
    Ieee80211FilterString="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture 1")

    CaptureFilter_1 = (stc.get( Capture_1, 'children-CaptureFilter' )).split(' ')[0]
    stc.config(CaptureFilter_1, \
    QualifyEvents="TRUE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Qualify Events 1")

    CaptureFilterStartEvent_1 = (stc.get( Capture_1, 'children-CaptureFilterStartEvent' )).split(' ')[0]
    stc.config(CaptureFilterStartEvent_1, \
    StartEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Events 1")

    CaptureFilterStopEvent_1 = (stc.get( Capture_1, 'children-CaptureFilterStopEvent' )).split(' ')[0]
    stc.config(CaptureFilterStopEvent_1, \
    StopEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Events 1")

    CaptureIeee80211_1 = (stc.get( Capture_1, 'children-CaptureIeee80211' )).split(' ')[0]
    stc.config(CaptureIeee80211_1, \
    ChannelWidth="CHANNEL_WIDTH_40M", \
    Channel="36", \
    SecondChannel="149", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture IEEE 802.11 1")

    CaptureRawPacketTagsInfo_1 = (stc.get( Capture_1, 'children-CaptureRawPacketTagsInfo' )).split(' ')[0]
    stc.config(CaptureRawPacketTagsInfo_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CaptureRawPacketTagsInfo 1")

    ArpCache_1 = (stc.get( Port_1, 'children-ArpCache' )).split(' ')[0]
    stc.config(ArpCache_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpCache 1")

    ArpNdReport_1 = (stc.get( Port_1, 'children-ArpNdReport' )).split(' ')[0]
    stc.config(ArpNdReport_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdReport 1")

    PingReport_1 = (stc.get( Port_1, 'children-PingReport' )).split(' ')[0]
    stc.config(PingReport_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PingReport 1")

    IgmpPortConfig_1 = (stc.get( Port_1, 'children-IgmpPortConfig' )).split(' ')[0]
    stc.config(IgmpPortConfig_1, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IgmpPortConfig 1")

    MldPortConfig_1 = (stc.get( Port_1, 'children-MldPortConfig' )).split(' ')[0]
    stc.config(MldPortConfig_1, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MldPortConfig 1")

    OsePortConfig_1 = (stc.get( Port_1, 'children-OsePortConfig' )).split(' ')[0]
    stc.config(OsePortConfig_1, \
    VirtualSwitch="OVS_2_1", \
    ManufacturerDescription="Spirent Communications", \
    HardwareDescription="Open vSwitch", \
    SerialNumber="None", \
    DatapathDescription="None", \
    ExposeOvsdb="FALSE", \
    OvsdbPortNumber="6640", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OsePortConfig 1")

    OvsdbPortConfig_1 = (stc.get( Port_1, 'children-OvsdbPortConfig' )).split(' ')[0]
    stc.config(OvsdbPortConfig_1, \
    ConnectionType="TCP", \
    PrivateKey="", \
    Certificate="", \
    CaCertificates="", \
    TlsConnectionOpen="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OVSDB Port Configuration 1")

    OpflexPortConfig_1 = (stc.get( Port_1, 'children-OpflexPortConfig' )).split(' ')[0]
    stc.config(OpflexPortConfig_1, \
    DomainName="Openstack", \
    AgentName="Agent1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Opflex Port Configuration 1")

    VxlanPortConfig_1 = (stc.get( Port_1, 'children-VxlanPortConfig' )).split(' ')[0]
    stc.config(VxlanPortConfig_1, \
    UdpDstPort="4789", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VXLAN Port Configuration 1")

    Ieee1588v2PortConfig_1 = (stc.get( Port_1, 'children-Ieee1588v2PortConfig' )).split(' ')[0]
    stc.config(Ieee1588v2PortConfig_1, \
    UpperOffsetThreshold="300", \
    LowerOffsetThreshold="-300", \
    BeforeAndAfterThresholdRowCount="0", \
    RxLogSyncInterval="0", \
    MeasureSeqIdErrors="FALSE", \
    EnableClockSyncFilteredResult="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee1588v2PortConfig 1")

    QbvStreamConfig_1 = (stc.get( Port_1, 'children-QbvStreamConfig' )).split(' ')[0]
    stc.config(QbvStreamConfig_1, \
    ConfigQbvParams="FALSE", \
    GptpBaseTime="0.0", \
    GateCycleTime="1000", \
    StartTimeWithinCycle="0", \
    TickGranularityOfDut="2.5", \
    StreamStartWaitTime="0", \
    DurationModeSecondsValue="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QbvStreamConfig 1")

    StpPortConfig_1 = (stc.get( Port_1, 'children-StpPortConfig' )).split(' ')[0]
    stc.config(StpPortConfig_1, \
    StpType="STP", \
    PortType="TRUNK", \
    EthernetType="8100", \
    NativeVlan="1", \
    EnablePt2PtLink="FALSE", \
    EnableMacAddrReduction="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StpPortConfig 1")

    Dhcpv4PortConfig_1 = (stc.get( Port_1, 'children-Dhcpv4PortConfig' )).split(' ')[0]
    stc.config(Dhcpv4PortConfig_1, \
    MaxMsgSize="576", \
    LeaseTime="60", \
    MsgTimeout="60", \
    RetryCount="4", \
    RequestRate="100", \
    ReleaseRate="100", \
    StartingXid="0", \
    OutstandingSessionCount="1000", \
    SeqType="SEQUENTIAL", \
    MaxDnav4RetryCount="0", \
    Dnav4Timeout="1000", \
    EnableAssignCustomOptionsForHosts="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4PortConfig 1")

    Dhcpv6PortConfig_1 = (stc.get( Port_1, 'children-Dhcpv6PortConfig' )).split(' ')[0]
    stc.config(Dhcpv6PortConfig_1, \
    RequestRate="100", \
    ReleaseRate="100", \
    RenewRate="100", \
    SessionAutoRetry="FALSE", \
    RetryAttempts="0", \
    NoWaitMultiAdv="FALSE", \
    EnableBlockRate="FALSE", \
    SolicitTimeout="1", \
    MaxSolicitRetryTimeout="120", \
    SolicitRetryCount="10", \
    IndefSolicitRetry="FALSE", \
    DisableSolicitRetry="FALSE", \
    RequestTimeout="1", \
    MaxRequestRetryTimeout="30", \
    RequestRetryCount="10", \
    IndefRequestRetry="FALSE", \
    DisableRequestRetry="FALSE", \
    ConfirmTimeout="1", \
    MaxConfirmTimeout="4", \
    MaxConfirmDuration="10", \
    RenewTimeout="10", \
    MaxRenewRetryTimeout="600", \
    RenewRetryCount="0", \
    IndefRenewRetry="TRUE", \
    DisableRenewRetry="FALSE", \
    RebindTimeout="10", \
    MaxRebindRetryTimeout="600", \
    RebindRetryCount="0", \
    IndefRebindRetry="TRUE", \
    DisableRebindRetry="FALSE", \
    ReleaseTimeout="1", \
    ReleaseRetryCount="5", \
    IndefReleaseRetry="FALSE", \
    DisableReleaseRetry="FALSE", \
    DeclineTimeout="1", \
    DeclineRetryCount="5", \
    IndefDeclineRetry="FALSE", \
    DisableDeclineRetry="FALSE", \
    OutstandingSessionCount="1000", \
    InfoRequestTimeout="1", \
    MaxInfoRequestTimeout="120", \
    InfoRequestRetryCount="0", \
    IndefInfoRequestRetry="TRUE", \
    DisableInfoRequestRetry="FALSE", \
    LeaseTime="86400", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6PortConfig 1")

    SaaPortConfig_1 = (stc.get( Port_1, 'children-SaaPortConfig' )).split(' ')[0]
    stc.config(SaaPortConfig_1, \
    RequestRate="300", \
    OutstandingSessionCount="1000", \
    SeqType="PARALLEL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="SaaPortConfig 1")

    RoEPortConfig_1 = (stc.get( Port_1, 'children-RoEPortConfig' )).split(' ')[0]
    stc.config(RoEPortConfig_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RoEPortConfig 1")

    L2tpPortConfig_1 = (stc.get( Port_1, 'children-L2tpPortConfig' )).split(' ')[0]
    stc.config(L2tpPortConfig_1, \
    L2tpVersion="L2TPV2", \
    L2tpNodeType="LAC", \
    TunnelConnectRate="100", \
    SeqType="SEQUENTIAL", \
    ConnectRateV3="100", \
    DisconnectRateV3="1000", \
    SessionOutstandingV3="100", \
    CsurqRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2tpPortConfig 1")

    PppoxPortConfig_1 = (stc.get( Port_1, 'children-PppoxPortConfig' )).split(' ')[0]
    stc.config(PppoxPortConfig_1, \
    EmulationType="CLIENT", \
    EnableBlockRate="FALSE", \
    ConnectRate="100", \
    DisconnectRate="1000", \
    SessionOutstanding="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxPortConfig 1")

    PppProtocolConfig_1 = (stc.get( Port_1, 'children-PppProtocolConfig' )).split(' ')[0]
    stc.config(PppProtocolConfig_1, \
    PapRequestTimeout="3", \
    MaxPapRequestAttempts="10", \
    ChapChalRequestTimeout="3", \
    ChapAckTimeout="3", \
    MaxChapRequestReplyAttempts="10", \
    AutoRetryCount="65535", \
    EnableAutoRetry="FALSE", \
    EnableSessionAutoRetry="FALSE", \
    Ipv4PeerAddr="0.0.0.0", \
    Ipv6PeerAddr="::", \
    IpcpEncap="IPV4", \
    Protocol="PPPOPOS", \
    EnableMruNegotiation="TRUE", \
    EnableMagicNum="TRUE", \
    EnableNcpTermination="FALSE", \
    Authentication="NONE", \
    IncludeTxChapId="TRUE", \
    EnableOsi="FALSE", \
    EnableMpls="FALSE", \
    MruSize="1492", \
    EnableEchoRequest="FALSE", \
    EchoRequestGenFreq="10", \
    MaxEchoRequestAttempts="1", \
    LcpConfigRequestTimeout="3", \
    LcpConfigRequestMaxAttempts="10", \
    LcpTermRequestTimeout="3", \
    LcpTermRequestMaxAttempts="10", \
    NcpConfigRequestTimeout="3", \
    NcpConfigRequestMaxAttempts="10", \
    MaxNaks="5", \
    Username="spirent", \
    Password="spirent", \
    UseAuthenticationList="FALSE", \
    AuthenticationFilePath="", \
    EnablePrimaryDns="TRUE", \
    PrimaryDns="null", \
    EnableSecondaryDns="TRUE", \
    SecondaryDns="null", \
    RAMOFlag="NODHCP", \
    ConnectRate="100", \
    DisconnectRate="100", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 1")

    AncpPortConfig_1 = (stc.get( Port_1, 'children-AncpPortConfig' )).split(' ')[0]
    stc.config(AncpPortConfig_1, \
    EstablishRate="100", \
    TerminateRate="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AncpPortConfig 1")

    CuspPortConfig_1 = (stc.get( Port_1, 'children-CuspPortConfig' )).split(' ')[0]
    stc.config(CuspPortConfig_1, \
    EstablishRate="100", \
    TerminateRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CuspPortConfig 1")

    EoamPortConfig_1 = (stc.get( Port_1, 'children-EoamPortConfig' )).split(' ')[0]
    stc.config(EoamPortConfig_1, \
    EtherType="8902", \
    MulticastMacType1="01:80:c2:00:00:30", \
    MulticastMacType2="01:80:c2:00:00:38", \
    EncodeMeLevel="TRUE", \
    DisableContChkRx="FALSE", \
    LinkTraceResponseRelayAction="DEFAULT", \
    ImmediateLinkTraceResponse="FALSE", \
    ImmediateLoopbackResponse="FALSE", \
    EchoTlvsInDelayMeasurementResponse="TRUE", \
    EchoTlvsInLossMeasurementResponse="TRUE", \
    EchoTlvsInSlr="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamPortConfig 1")

    AppPerfPortConfig_1 = (stc.get( Port_1, 'children-AppPerfPortConfig' )).split(' ')[0]
    stc.config(AppPerfPortConfig_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AppPerfPortConfig 1")

    VqAnalyzer_1 = (stc.get( Port_1, 'children-VqAnalyzer' )).split(' ')[0]
    stc.config(VqAnalyzer_1, \
    FrameLossConcealmentRobustness="4", \
    SlicesPerIframe="0", \
    NominalDelay="3", \
    MaxPktCount="65535", \
    MosVThreshold="1", \
    MosVNormalizedThreshold="1", \
    MosAvThreshold="1", \
    MosAThreshold="1", \
    PidInterval="1", \
    PatRepetition="0.5", \
    PmtRepetition="0.5", \
    PcrContinuity="0.1", \
    PcrRepetition="0.04", \
    PtsRepetition="0.7", \
    RtpTimestampThreshold="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzer 1")

    AutosarTimeSyncPortConfig_1 = (stc.get( Port_1, 'children-AutosarTimeSyncPortConfig' )).split(' ')[0]
    stc.config(AutosarTimeSyncPortConfig_1, \
    DevicesMode="RX", \
    Protocol="CAN", \
    CANId="1061", \
    PortNumber="1", \
    TimeDomain="0", \
    SgwBit="0", \
    OverflowOfSeconds="0", \
    SequenceCounterJump="1", \
    SyncInterval="500", \
    MinSyncInterval="-10", \
    MaxSyncInterval="50", \
    MinFollowUpInterval="0", \
    MaxFollowUpInterval="100", \
    RandomJump="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutosarTimeSyncPortConfig 1")

    CoapPortConfig_1 = (stc.get( Port_1, 'children-CoapPortConfig' )).split(' ')[0]
    stc.config(CoapPortConfig_1, \
    ServerStartRate="500", \
    ServerStopRate="500", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CoapPortConfig 1")

    EthernetCopper_1 = stc.create("EthernetCopper",under = Port_1, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 1")

    Mii_1 = (stc.get( EthernetCopper_1, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_1 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_1, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_2 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_2, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_3 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_3, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_4 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_4, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_5 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_5, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_6 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_6, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_7 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_7, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_8 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_8, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_9 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_9, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_10 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_10, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_11 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_11, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_12 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_12, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_13 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_13, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_14 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_14, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_15 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_15, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_16 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_16, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_17 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_17, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_18 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_18, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_19 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_19, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_20 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_20, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_21 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_21, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_22 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_22, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_23 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_23, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_24 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_24, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_25 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_25, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_26 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_26, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_27 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_27, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_28 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_28, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_29 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_29, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_30 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_30, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_31 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_31, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_32 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_32, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    Ethernet10GigFiber_1 = stc.create("Ethernet10GigFiber",under = Port_1, \
    PortMode="LAN", \
    DeficitIdleCount="FALSE", \
    CfpInterface="ACC_6068A", \
    PriorityFlowControlArray="FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE", \
    IsPfcNegotiated="FALSE", \
    TxDeEmphasisPreTap="0", \
    TxDeEmphasisPostTap="13", \
    TxMainTapSwing="15", \
    DetectionMode="AUTO_DETECT", \
    CableTypeLength="OPTICAL", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_10G", \
    AlternateSpeeds="SPEED_10G", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="ENABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mdio/ieee802_3ae45.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet 10G Fiber Phy 1")

    EthernetWan_1 = (stc.get( Ethernet10GigFiber_1, 'children-EthernetWan' )).split(' ')[0]
    stc.config(EthernetWan_1, \
    FramingMode="SONET_FRAMING", \
    SectionScramble="TRUE", \
    PathSignalLabel="ETHERNET_10G_WAN_PATH_SIGNAL_LABEL", \
    Crc32="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G Ethernet WAN 1")

    Mdio_1 = (stc.get( Ethernet10GigFiber_1, 'children-Mdio' )).split(' ')[0]
    stc.config(Mdio_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mdio 1")

    MdioPort_1 = (stc.get( Mdio_1, 'children-MdioPort' )).split(' ')[0]
    stc.config(MdioPort_1, \
    Clause="CLAUSE_45", \
    Address="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MdioPort 1")

    ManagementDevice_1 = (stc.get( MdioPort_1, 'children-ManagementDevice' )).split(' ')[0]
    stc.config(ManagementDevice_1, \
    Address="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD")

    MdioRegister_1 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_1, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD control 1")

    MdioRegister_2 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_2, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD status 1(RO)")

    MdioRegister_3 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_3, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_4 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_4, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_5 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_5, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD speed ability")

    MdioRegister_6 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_6, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_7 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_7, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_8 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_8, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD control 2")

    MdioRegister_9 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_9, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD status 2")

    MdioRegister_10 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_10, \
    Address="9", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD transmit disable")

    MdioRegister_11 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_11, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD receive signal detect")

    MdioRegister_12 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_12, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Extended ability")

    MdioRegister_13 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_13, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_14 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_14, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_15 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_15, \
    Address="129", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T status")

    MdioRegister_16 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_16, \
    Address="130", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T pair swap and polarity")

    MdioRegister_17 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_17, \
    Address="131", \
    RegValue="0", \
    WritableMask="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T TX power backoff setting")

    MdioRegister_18 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_18, \
    Address="132", \
    RegValue="1024", \
    WritableMask="64512", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T test mode")

    MdioRegister_19 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_19, \
    Address="133", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel A")

    MdioRegister_20 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_20, \
    Address="134", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel B")

    MdioRegister_21 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_21, \
    Address="135", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel C")

    MdioRegister_22 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_22, \
    Address="136", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel D")

    MdioRegister_23 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_23, \
    Address="137", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel A")

    MdioRegister_24 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_24, \
    Address="138", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel B")

    MdioRegister_25 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_25, \
    Address="139", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel C")

    MdioRegister_26 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_26, \
    Address="140", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel D")

    MdioRegister_27 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_27, \
    Address="141", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel A")

    MdioRegister_28 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_28, \
    Address="142", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel B")

    MdioRegister_29 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_29, \
    Address="143", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel C")

    MdioRegister_30 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_30, \
    Address="144", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel D")

    MdioRegister_31 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_31, \
    Address="145", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    MdioRegister_32 = (stc.get( ManagementDevice_1, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_32, \
    Address="146", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    ManagementDevice_2 = (stc.get( MdioPort_1, 'children-ManagementDevice' )).split(' ')[1]
    stc.config(ManagementDevice_2, \
    Address="2", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS")

    MdioRegister_33 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_33, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS control 1")

    MdioRegister_34 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_34, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS status 1")

    MdioRegister_35 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_35, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_36 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_36, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_37 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_37, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS speed ability")

    MdioRegister_38 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_38, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_39 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_39, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_40 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_40, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS control 2")

    MdioRegister_41 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_41, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 2")

    MdioRegister_42 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_42, \
    Address="9", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS test pattern error counter")

    MdioRegister_43 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_43, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_44 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_44, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_45 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_45, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 3")

    MdioRegister_46 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_46, \
    Address="37", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end path block error count")

    MdioRegister_47 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_47, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_48 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_48, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_49 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_49, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_50 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_50, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_51 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_51, \
    Address="43", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_52 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_52, \
    Address="44", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_53 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_53, \
    Address="45", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_54 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_54, \
    Address="46", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_55 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_55, \
    Address="47", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_56 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_56, \
    Address="48", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_57 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_57, \
    Address="49", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_58 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_58, \
    Address="50", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_59 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_59, \
    Address="51", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_60 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_60, \
    Address="52", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_61 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_61, \
    Address="53", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_62 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_62, \
    Address="54", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_63 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_63, \
    Address="55", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_64 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_64, \
    Address="56", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_65 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[32]
    stc.config(MdioRegister_65, \
    Address="57", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_66 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[33]
    stc.config(MdioRegister_66, \
    Address="58", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_67 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[34]
    stc.config(MdioRegister_67, \
    Address="59", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS path block error count")

    MdioRegister_68 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[35]
    stc.config(MdioRegister_68, \
    Address="60", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS section BIP error count")

    MdioRegister_69 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[36]
    stc.config(MdioRegister_69, \
    Address="64", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_70 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[37]
    stc.config(MdioRegister_70, \
    Address="65", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_71 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[38]
    stc.config(MdioRegister_71, \
    Address="66", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_72 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[39]
    stc.config(MdioRegister_72, \
    Address="67", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_73 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[40]
    stc.config(MdioRegister_73, \
    Address="68", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_74 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[41]
    stc.config(MdioRegister_74, \
    Address="69", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_75 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[42]
    stc.config(MdioRegister_75, \
    Address="70", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_76 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[43]
    stc.config(MdioRegister_76, \
    Address="71", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_77 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[44]
    stc.config(MdioRegister_77, \
    Address="72", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_78 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[45]
    stc.config(MdioRegister_78, \
    Address="73", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_79 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[46]
    stc.config(MdioRegister_79, \
    Address="74", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_80 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[47]
    stc.config(MdioRegister_80, \
    Address="75", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_81 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[48]
    stc.config(MdioRegister_81, \
    Address="76", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_82 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[49]
    stc.config(MdioRegister_82, \
    Address="77", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_83 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[50]
    stc.config(MdioRegister_83, \
    Address="78", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_84 = (stc.get( ManagementDevice_2, 'children-MdioRegister' )).split(' ')[51]
    stc.config(MdioRegister_84, \
    Address="79", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    ManagementDevice_3 = (stc.get( MdioPort_1, 'children-ManagementDevice' )).split(' ')[2]
    stc.config(ManagementDevice_3, \
    Address="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS")

    MdioRegister_85 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_85, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS control 1")

    MdioRegister_86 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_86, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS status 1")

    MdioRegister_87 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_87, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_88 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_88, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_89 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_89, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS speed ability")

    MdioRegister_90 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_90, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_91 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_91, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_92 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_92, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS control 2")

    MdioRegister_93 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_93, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS status 2")

    MdioRegister_94 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_94, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_95 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_95, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_96 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_96, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS status")

    MdioRegister_97 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_97, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS test control")

    MdioRegister_98 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_98, \
    Address="32", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 1")

    MdioRegister_99 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_99, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 2")

    MdioRegister_100 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_100, \
    Address="34", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_101 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_101, \
    Address="35", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_102 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_102, \
    Address="36", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_103 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_103, \
    Address="37", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_104 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_104, \
    Address="38", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_105 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_105, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_106 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_106, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_107 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_107, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_108 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_108, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern control")

    MdioRegister_109 = (stc.get( ManagementDevice_3, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_109, \
    Address="43", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern error counter")

    ManagementDevice_4 = (stc.get( MdioPort_1, 'children-ManagementDevice' )).split(' ')[3]
    stc.config(ManagementDevice_4, \
    Address="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS")

    MdioRegister_110 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_110, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS control 1")

    MdioRegister_111 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_111, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 1")

    MdioRegister_112 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_112, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_113 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_113, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_114 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_114, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS speed ability")

    MdioRegister_115 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_115, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_116 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_116, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_117 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_117, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 2")

    MdioRegister_118 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_118, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_119 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_119, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_120 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_120, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS lane status")

    MdioRegister_121 = (stc.get( ManagementDevice_4, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_121, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS test control")

    ManagementDevice_5 = (stc.get( MdioPort_1, 'children-ManagementDevice' )).split(' ')[4]
    stc.config(ManagementDevice_5, \
    Address="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto Negotiation")

    MdioRegister_122 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_122, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN control")

    MdioRegister_123 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_123, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN status")

    MdioRegister_124 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_124, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_125 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_125, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_126 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_126, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_127 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_127, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_128 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_128, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_129 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_129, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_130 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_130, \
    Address="16", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_131 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_131, \
    Address="17", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_132 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_132, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_133 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_133, \
    Address="19", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_134 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_134, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_135 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_135, \
    Address="21", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_136 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_136, \
    Address="22", \
    RegValue="0", \
    WritableMask="63487", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_137 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_137, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_138 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_138, \
    Address="24", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_139 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_139, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_140 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_140, \
    Address="26", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_141 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_141, \
    Address="27", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_142 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_142, \
    Address="32", \
    RegValue="0", \
    WritableMask="61447", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN control")

    MdioRegister_143 = (stc.get( ManagementDevice_5, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_143, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN status")

    StreamBlock_1 = stc.create("StreamBlock",under = Port_1, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1024", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Vxlan,Ancp,PppProtocol,PppoeProtocol,Openflow Protocol,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,AUTOSARTIMESYNC Protocol,CP traffic,Coap Protocol,OAM Protocol,Packet Channel,Dhcpv4,SyncE,Dhcpv6,IgmpMld,Cusp,AppPerf,Cifs,Iperf,Http,Ntp,RawTcp,Dpg,Sip,Video,CSMP,XMPPvJ,Ftp,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_10078\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>19481</checksum><sourceAddr>10.43.36.2</sourceAddr><destAddr>192.168.0.179</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>10.43.36.1</gateway><tosDiffserv name=\"anon_8608\"><tos name=\"anon_8609\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 14-6-1")

    TableModifier_1 = stc.create("TableModifier",under = StreamBlock_1, \
    RepeatCount="0", \
    Data="10.43.53.188", \
    DataType="NATIVE", \
    EnableStream="FALSE", \
    Offset="0", \
    OffsetReference="ipv4_10078.destAddr", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 Modifier")

    StreamBlock_2 = stc.create("StreamBlock",under = Port_1, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1024", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Vxlan,Ancp,PppProtocol,PppoeProtocol,Openflow Protocol,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,AUTOSARTIMESYNC Protocol,CP traffic,Coap Protocol,OAM Protocol,Packet Channel,Dhcpv4,SyncE,Dhcpv6,IgmpMld,Cusp,AppPerf,Cifs,Iperf,Http,Ntp,RawTcp,Dpg,Sip,Video,CSMP,XMPPvJ,Ftp,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_10078\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>19486</checksum><sourceAddr>10.43.36.2</sourceAddr><destAddr>172.16.0.2</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>10.43.36.1</gateway><tosDiffserv name=\"anon_8618\"><tos name=\"anon_8619\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 14-6-2")

    TableModifier_2 = stc.create("TableModifier",under = StreamBlock_2, \
    RepeatCount="0", \
    Data="10.43.53.183", \
    DataType="NATIVE", \
    EnableStream="FALSE", \
    Offset="0", \
    OffsetReference="ipv4_10078.destAddr", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 Modifier")

    Host_2 = (stc.get( Port_2, 'children-Host' )).split(' ')[0]
    stc.config(Host_2, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    EthIIIf_2 = stc.create("EthIIIf",under = Host_2, \
    SourceMac="00:10:94:00:00:02", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 3")

    HdlcIf_2 = stc.create("HdlcIf",under = Host_2, \
    ProtocolType="HDLC_PROTOCOL_TYPE_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="HDLC 3")

    PppIf_3 = stc.create("PppIf",under = Host_2, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 5")

    PppIf_4 = stc.create("PppIf",under = Host_2, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 6")

    Ipv4If_2 = stc.create("Ipv4If",under = Host_2, \
    Address="192.85.1.3", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 3")

    Ipv6If_3 = stc.create("Ipv6If",under = Host_2, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 5")

    Ipv6If_4 = stc.create("Ipv6If",under = Host_2, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 6")

    SystemResourceManager_2 = (stc.get( Port_2, 'children-SystemResourceManager' )).split(' ')[0]
    stc.config(SystemResourceManager_2, \
    MemoryThreshold="80", \
    MemoryThresholdEnable="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Resource Manager 3")

    Generator_2 = (stc.get( Port_2, 'children-Generator' )).split(' ')[0]
    stc.config(Generator_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Generator 3")

    GeneratorConfig_2 = (stc.get( Generator_2, 'children-GeneratorConfig' )).split(' ')[0]
    stc.config(GeneratorConfig_2, \
    SchedulingMode="RATE_BASED", \
    AdvancedInterleaving="FALSE", \
    Duration="120", \
    DurationMode="CONTINUOUS", \
    StepSize="1", \
    TimestampLatchMode="START_OF_FRAME", \
    RandomLengthSeed="10900842", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    BurstSize="1", \
    LoadUnit="PERCENT_LINE_RATE", \
    LoadMode="FIXED", \
    FixedLoad="10", \
    RandomMaxLoad="100", \
    RandomMinLoad="10", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    SmoothenRandomLength="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Generator Configuration 3")

    Analyzer_2 = (stc.get( Port_2, 'children-Analyzer' )).split(' ')[0]
    stc.config(Analyzer_2, \
    FilterOnStreamId="TRUE", \
    FilterOnInnerIP="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Analyzer 3")

    AnalyzerConfig_2 = (stc.get( Analyzer_2, 'children-AnalyzerConfig' )).split(' ')[0]
    stc.config(AnalyzerConfig_2, \
    TimestampLatchMode="START_OF_FRAME", \
    SigMode="ENHANCED_DETECTION", \
    HistogramMode="LATENCY", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    AdvSeqCheckerLateThreshold="1000", \
    VlanAlternateTpid="34984", \
    AlternateSigOffset="0", \
    LatencyMode="PER_STREAM_RX_LATENCY_ON", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Advanced Analyzer Settings 3")

    InterarrivalTimeHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-InterarrivalTimeHistogram' )).split(' ')[0]
    stc.config(InterarrivalTimeHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    LatencyHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-LatencyHistogram' )).split(' ')[0]
    stc.config(LatencyHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    FrameLengthHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-FrameLengthHistogram' )).split(' ')[0]
    stc.config(FrameLengthHistogram_2, \
    Description="(in bytes)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    SeqRunLengthHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-SeqRunLengthHistogram' )).split(' ')[0]
    stc.config(SeqRunLengthHistogram_2, \
    Description="(in frames)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    SeqDiffCheckHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-SeqDiffCheckHistogram' )).split(' ')[0]
    stc.config(SeqDiffCheckHistogram_2, \
    Description="(in deltas)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    JitterHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-JitterHistogram' )).split(' ')[0]
    stc.config(JitterHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    DiffServConfig_2 = (stc.get( Analyzer_2, 'children-DiffServConfig' )).split(' ')[0]
    stc.config(DiffServConfig_2, \
    QualifyIpv6DstAddr="FALSE", \
    Ipv6DstAddr="ffff::ffff", \
    QualifyIpv4DstAddr="FALSE", \
    Ipv4DstAddr="0.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QoS Settings 3")

    HighResolutionSamplingPortConfig_2 = (stc.get( Analyzer_2, 'children-HighResolutionSamplingPortConfig' )).split(' ')[0]
    stc.config(HighResolutionSamplingPortConfig_2, \
    BaselineSampleCount="3", \
    EnableTrigger="TRUE", \
    TriggerCondition="LESS_THAN", \
    TriggerValueUnitMode="PERCENT_BASELINE", \
    TriggerStat="TotalFrameRate", \
    TriggerValue="95", \
    TriggerLocation="20", \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Port Sampling 3")

    HighResolutionStreamBlockOptions_2 = stc.create("HighResolutionStreamBlockOptions",under = Analyzer_2, \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Stream Block Options 1")

    AnalyzerFrameConfigFilter_1 = stc.create("AnalyzerFrameConfigFilter",under = Analyzer_2, \
    Summary="", \
    ParsedField="", \
    FrameConfig="<frame><config><pdus><pdu name=\"eth1\" pdu=\"ethernet:EthernetII\"></pdu><pdu name=\"ip_1\" pdu=\"ipv4:IPv4\"></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Template Filter 1")

    Capture_2 = (stc.get( Port_2, 'children-Capture' )).split(' ')[0]
    stc.config(Capture_2, \
    ElapsedTime="0:00:00", \
    TabIndex="0", \
    Mode="REGULAR_MODE", \
    SrcMode="TX_RX_MODE", \
    RealTimeMode="REALTIME_DISABLE", \
    FlagMode="REGULAR_FLAG_MODE", \
    BufferMode="WRAP", \
    Start="16384", \
    Stop="0", \
    SliceMode="DISABLE", \
    SliceOffsetRef="PREAMBLE", \
    SliceOffset="0", \
    SliceCaptureSize="128", \
    RealTimeFramesBuffer="0", \
    RealTimeBufferStatus="FALSE", \
    CurrentTask="IDLE", \
    CurrentFiltersUsed="0", \
    CurrentFilterBytesUsed="0", \
    AbortSaveTask="FALSE", \
    PostStopTriggerBuffer="255", \
    CaptureFilterMode="FRAMECONTENT", \
    SaveBufferWithPreamble="FALSE", \
    IncreasedMemorySupport="FALSE", \
    Ieee80211FilterString="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture 3")

    CaptureFilter_2 = (stc.get( Capture_2, 'children-CaptureFilter' )).split(' ')[0]
    stc.config(CaptureFilter_2, \
    QualifyEvents="TRUE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Qualify Events 3")

    CaptureFilterStartEvent_2 = (stc.get( Capture_2, 'children-CaptureFilterStartEvent' )).split(' ')[0]
    stc.config(CaptureFilterStartEvent_2, \
    StartEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Events 3")

    CaptureFilterStopEvent_2 = (stc.get( Capture_2, 'children-CaptureFilterStopEvent' )).split(' ')[0]
    stc.config(CaptureFilterStopEvent_2, \
    StopEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Events 3")

    CaptureIeee80211_2 = (stc.get( Capture_2, 'children-CaptureIeee80211' )).split(' ')[0]
    stc.config(CaptureIeee80211_2, \
    ChannelWidth="CHANNEL_WIDTH_40M", \
    Channel="36", \
    SecondChannel="149", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture IEEE 802.11 3")

    CaptureRawPacketTagsInfo_2 = (stc.get( Capture_2, 'children-CaptureRawPacketTagsInfo' )).split(' ')[0]
    stc.config(CaptureRawPacketTagsInfo_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CaptureRawPacketTagsInfo 3")

    ArpCache_2 = (stc.get( Port_2, 'children-ArpCache' )).split(' ')[0]
    stc.config(ArpCache_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpCache 3")

    ArpNdReport_2 = (stc.get( Port_2, 'children-ArpNdReport' )).split(' ')[0]
    stc.config(ArpNdReport_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdReport 3")

    PingReport_2 = (stc.get( Port_2, 'children-PingReport' )).split(' ')[0]
    stc.config(PingReport_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PingReport 3")

    IgmpPortConfig_2 = (stc.get( Port_2, 'children-IgmpPortConfig' )).split(' ')[0]
    stc.config(IgmpPortConfig_2, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IgmpPortConfig 3")

    MldPortConfig_2 = (stc.get( Port_2, 'children-MldPortConfig' )).split(' ')[0]
    stc.config(MldPortConfig_2, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MldPortConfig 3")

    OsePortConfig_2 = (stc.get( Port_2, 'children-OsePortConfig' )).split(' ')[0]
    stc.config(OsePortConfig_2, \
    VirtualSwitch="OVS_2_1", \
    ManufacturerDescription="Spirent Communications", \
    HardwareDescription="Open vSwitch", \
    SerialNumber="None", \
    DatapathDescription="None", \
    ExposeOvsdb="FALSE", \
    OvsdbPortNumber="6640", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OsePortConfig 3")

    OvsdbPortConfig_2 = (stc.get( Port_2, 'children-OvsdbPortConfig' )).split(' ')[0]
    stc.config(OvsdbPortConfig_2, \
    ConnectionType="TCP", \
    PrivateKey="", \
    Certificate="", \
    CaCertificates="", \
    TlsConnectionOpen="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OVSDB Port Configuration 3")

    OpflexPortConfig_2 = (stc.get( Port_2, 'children-OpflexPortConfig' )).split(' ')[0]
    stc.config(OpflexPortConfig_2, \
    DomainName="Openstack", \
    AgentName="Agent1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Opflex Port Configuration 3")

    VxlanPortConfig_2 = (stc.get( Port_2, 'children-VxlanPortConfig' )).split(' ')[0]
    stc.config(VxlanPortConfig_2, \
    UdpDstPort="4789", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VXLAN Port Configuration 3")

    Ieee1588v2PortConfig_2 = (stc.get( Port_2, 'children-Ieee1588v2PortConfig' )).split(' ')[0]
    stc.config(Ieee1588v2PortConfig_2, \
    UpperOffsetThreshold="300", \
    LowerOffsetThreshold="-300", \
    BeforeAndAfterThresholdRowCount="0", \
    RxLogSyncInterval="0", \
    MeasureSeqIdErrors="FALSE", \
    EnableClockSyncFilteredResult="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee1588v2PortConfig 3")

    QbvStreamConfig_2 = (stc.get( Port_2, 'children-QbvStreamConfig' )).split(' ')[0]
    stc.config(QbvStreamConfig_2, \
    ConfigQbvParams="FALSE", \
    GptpBaseTime="0.0", \
    GateCycleTime="1000", \
    StartTimeWithinCycle="0", \
    TickGranularityOfDut="2.5", \
    StreamStartWaitTime="0", \
    DurationModeSecondsValue="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QbvStreamConfig 3")

    StpPortConfig_2 = (stc.get( Port_2, 'children-StpPortConfig' )).split(' ')[0]
    stc.config(StpPortConfig_2, \
    StpType="STP", \
    PortType="TRUNK", \
    EthernetType="8100", \
    NativeVlan="1", \
    EnablePt2PtLink="FALSE", \
    EnableMacAddrReduction="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StpPortConfig 3")

    Dhcpv4PortConfig_2 = (stc.get( Port_2, 'children-Dhcpv4PortConfig' )).split(' ')[0]
    stc.config(Dhcpv4PortConfig_2, \
    MaxMsgSize="576", \
    LeaseTime="60", \
    MsgTimeout="60", \
    RetryCount="4", \
    RequestRate="100", \
    ReleaseRate="100", \
    StartingXid="0", \
    OutstandingSessionCount="1000", \
    SeqType="SEQUENTIAL", \
    MaxDnav4RetryCount="0", \
    Dnav4Timeout="1000", \
    EnableAssignCustomOptionsForHosts="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4PortConfig 3")

    Dhcpv6PortConfig_2 = (stc.get( Port_2, 'children-Dhcpv6PortConfig' )).split(' ')[0]
    stc.config(Dhcpv6PortConfig_2, \
    RequestRate="100", \
    ReleaseRate="100", \
    RenewRate="100", \
    SessionAutoRetry="FALSE", \
    RetryAttempts="0", \
    NoWaitMultiAdv="FALSE", \
    EnableBlockRate="FALSE", \
    SolicitTimeout="1", \
    MaxSolicitRetryTimeout="120", \
    SolicitRetryCount="10", \
    IndefSolicitRetry="FALSE", \
    DisableSolicitRetry="FALSE", \
    RequestTimeout="1", \
    MaxRequestRetryTimeout="30", \
    RequestRetryCount="10", \
    IndefRequestRetry="FALSE", \
    DisableRequestRetry="FALSE", \
    ConfirmTimeout="1", \
    MaxConfirmTimeout="4", \
    MaxConfirmDuration="10", \
    RenewTimeout="10", \
    MaxRenewRetryTimeout="600", \
    RenewRetryCount="0", \
    IndefRenewRetry="TRUE", \
    DisableRenewRetry="FALSE", \
    RebindTimeout="10", \
    MaxRebindRetryTimeout="600", \
    RebindRetryCount="0", \
    IndefRebindRetry="TRUE", \
    DisableRebindRetry="FALSE", \
    ReleaseTimeout="1", \
    ReleaseRetryCount="5", \
    IndefReleaseRetry="FALSE", \
    DisableReleaseRetry="FALSE", \
    DeclineTimeout="1", \
    DeclineRetryCount="5", \
    IndefDeclineRetry="FALSE", \
    DisableDeclineRetry="FALSE", \
    OutstandingSessionCount="1000", \
    InfoRequestTimeout="1", \
    MaxInfoRequestTimeout="120", \
    InfoRequestRetryCount="0", \
    IndefInfoRequestRetry="TRUE", \
    DisableInfoRequestRetry="FALSE", \
    LeaseTime="86400", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6PortConfig 3")

    SaaPortConfig_2 = (stc.get( Port_2, 'children-SaaPortConfig' )).split(' ')[0]
    stc.config(SaaPortConfig_2, \
    RequestRate="300", \
    OutstandingSessionCount="1000", \
    SeqType="PARALLEL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="SaaPortConfig 3")

    RoEPortConfig_2 = (stc.get( Port_2, 'children-RoEPortConfig' )).split(' ')[0]
    stc.config(RoEPortConfig_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RoEPortConfig 3")

    L2tpPortConfig_2 = (stc.get( Port_2, 'children-L2tpPortConfig' )).split(' ')[0]
    stc.config(L2tpPortConfig_2, \
    L2tpVersion="L2TPV2", \
    L2tpNodeType="LAC", \
    TunnelConnectRate="100", \
    SeqType="SEQUENTIAL", \
    ConnectRateV3="100", \
    DisconnectRateV3="1000", \
    SessionOutstandingV3="100", \
    CsurqRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2tpPortConfig 3")

    PppoxPortConfig_2 = (stc.get( Port_2, 'children-PppoxPortConfig' )).split(' ')[0]
    stc.config(PppoxPortConfig_2, \
    EmulationType="CLIENT", \
    EnableBlockRate="FALSE", \
    ConnectRate="100", \
    DisconnectRate="1000", \
    SessionOutstanding="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxPortConfig 3")

    PppProtocolConfig_2 = (stc.get( Port_2, 'children-PppProtocolConfig' )).split(' ')[0]
    stc.config(PppProtocolConfig_2, \
    PapRequestTimeout="3", \
    MaxPapRequestAttempts="10", \
    ChapChalRequestTimeout="3", \
    ChapAckTimeout="3", \
    MaxChapRequestReplyAttempts="10", \
    AutoRetryCount="65535", \
    EnableAutoRetry="FALSE", \
    EnableSessionAutoRetry="FALSE", \
    Ipv4PeerAddr="0.0.0.0", \
    Ipv6PeerAddr="::", \
    IpcpEncap="IPV4", \
    Protocol="PPPOPOS", \
    EnableMruNegotiation="TRUE", \
    EnableMagicNum="TRUE", \
    EnableNcpTermination="FALSE", \
    Authentication="NONE", \
    IncludeTxChapId="TRUE", \
    EnableOsi="FALSE", \
    EnableMpls="FALSE", \
    MruSize="1492", \
    EnableEchoRequest="FALSE", \
    EchoRequestGenFreq="10", \
    MaxEchoRequestAttempts="1", \
    LcpConfigRequestTimeout="3", \
    LcpConfigRequestMaxAttempts="10", \
    LcpTermRequestTimeout="3", \
    LcpTermRequestMaxAttempts="10", \
    NcpConfigRequestTimeout="3", \
    NcpConfigRequestMaxAttempts="10", \
    MaxNaks="5", \
    Username="spirent", \
    Password="spirent", \
    UseAuthenticationList="FALSE", \
    AuthenticationFilePath="", \
    EnablePrimaryDns="TRUE", \
    PrimaryDns="null", \
    EnableSecondaryDns="TRUE", \
    SecondaryDns="null", \
    RAMOFlag="NODHCP", \
    ConnectRate="100", \
    DisconnectRate="100", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 3")

    AncpPortConfig_2 = (stc.get( Port_2, 'children-AncpPortConfig' )).split(' ')[0]
    stc.config(AncpPortConfig_2, \
    EstablishRate="100", \
    TerminateRate="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AncpPortConfig 3")

    CuspPortConfig_2 = (stc.get( Port_2, 'children-CuspPortConfig' )).split(' ')[0]
    stc.config(CuspPortConfig_2, \
    EstablishRate="100", \
    TerminateRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CuspPortConfig 3")

    EoamPortConfig_2 = (stc.get( Port_2, 'children-EoamPortConfig' )).split(' ')[0]
    stc.config(EoamPortConfig_2, \
    EtherType="8902", \
    MulticastMacType1="01:80:c2:00:00:30", \
    MulticastMacType2="01:80:c2:00:00:38", \
    EncodeMeLevel="TRUE", \
    DisableContChkRx="FALSE", \
    LinkTraceResponseRelayAction="DEFAULT", \
    ImmediateLinkTraceResponse="FALSE", \
    ImmediateLoopbackResponse="FALSE", \
    EchoTlvsInDelayMeasurementResponse="TRUE", \
    EchoTlvsInLossMeasurementResponse="TRUE", \
    EchoTlvsInSlr="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamPortConfig 3")

    AppPerfPortConfig_2 = (stc.get( Port_2, 'children-AppPerfPortConfig' )).split(' ')[0]
    stc.config(AppPerfPortConfig_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AppPerfPortConfig 3")

    VqAnalyzer_2 = (stc.get( Port_2, 'children-VqAnalyzer' )).split(' ')[0]
    stc.config(VqAnalyzer_2, \
    FrameLossConcealmentRobustness="4", \
    SlicesPerIframe="0", \
    NominalDelay="3", \
    MaxPktCount="65535", \
    MosVThreshold="1", \
    MosVNormalizedThreshold="1", \
    MosAvThreshold="1", \
    MosAThreshold="1", \
    PidInterval="1", \
    PatRepetition="0.5", \
    PmtRepetition="0.5", \
    PcrContinuity="0.1", \
    PcrRepetition="0.04", \
    PtsRepetition="0.7", \
    RtpTimestampThreshold="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzer 3")

    AutosarTimeSyncPortConfig_2 = (stc.get( Port_2, 'children-AutosarTimeSyncPortConfig' )).split(' ')[0]
    stc.config(AutosarTimeSyncPortConfig_2, \
    DevicesMode="RX", \
    Protocol="CAN", \
    CANId="1061", \
    PortNumber="1", \
    TimeDomain="0", \
    SgwBit="0", \
    OverflowOfSeconds="0", \
    SequenceCounterJump="1", \
    SyncInterval="500", \
    MinSyncInterval="-10", \
    MaxSyncInterval="50", \
    MinFollowUpInterval="0", \
    MaxFollowUpInterval="100", \
    RandomJump="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutosarTimeSyncPortConfig 3")

    CoapPortConfig_2 = (stc.get( Port_2, 'children-CoapPortConfig' )).split(' ')[0]
    stc.config(CoapPortConfig_2, \
    ServerStartRate="500", \
    ServerStopRate="500", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CoapPortConfig 3")

    EthernetCopper_2 = stc.create("EthernetCopper",under = Port_2, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 3")

    Mii_2 = (stc.get( EthernetCopper_2, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_33 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_33, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_34 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_34, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_35 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_35, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_36 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_36, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_37 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_37, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_38 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_38, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_39 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_39, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_40 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_40, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_41 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_41, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_42 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_42, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_43 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_43, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_44 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_44, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_45 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_45, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_46 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_46, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_47 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_47, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_48 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_48, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_49 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_49, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_50 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_50, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_51 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_51, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_52 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_52, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_53 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_53, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_54 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_54, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_55 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_55, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_56 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_56, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_57 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_57, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_58 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_58, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_59 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_59, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_60 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_60, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_61 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_61, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_62 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_62, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_63 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_63, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_64 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_64, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    Ethernet10GigFiber_2 = stc.create("Ethernet10GigFiber",under = Port_2, \
    PortMode="LAN", \
    DeficitIdleCount="TRUE", \
    CfpInterface="ACC_6069A", \
    PriorityFlowControlArray="FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE", \
    IsPfcNegotiated="FALSE", \
    TxDeEmphasisPreTap="0", \
    TxDeEmphasisPostTap="13", \
    TxMainTapSwing="15", \
    DetectionMode="AUTO_DETECT", \
    CableTypeLength="OPTICAL", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="SPEED_10G", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="ENABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mdio/ieee802_3ae45.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet 10G Fiber Phy 3")

    EthernetWan_2 = (stc.get( Ethernet10GigFiber_2, 'children-EthernetWan' )).split(' ')[0]
    stc.config(EthernetWan_2, \
    FramingMode="SONET_FRAMING", \
    SectionScramble="TRUE", \
    PathSignalLabel="ETHERNET_10G_WAN_PATH_SIGNAL_LABEL", \
    Crc32="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G Ethernet WAN 3")

    Mdio_2 = (stc.get( Ethernet10GigFiber_2, 'children-Mdio' )).split(' ')[0]
    stc.config(Mdio_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mdio 1")

    MdioPort_2 = (stc.get( Mdio_2, 'children-MdioPort' )).split(' ')[0]
    stc.config(MdioPort_2, \
    Clause="CLAUSE_45", \
    Address="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MdioPort 1")

    ManagementDevice_6 = (stc.get( MdioPort_2, 'children-ManagementDevice' )).split(' ')[0]
    stc.config(ManagementDevice_6, \
    Address="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD")

    MdioRegister_144 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_144, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD control 1")

    MdioRegister_145 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_145, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD status 1(RO)")

    MdioRegister_146 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_146, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_147 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_147, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_148 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_148, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD speed ability")

    MdioRegister_149 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_149, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_150 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_150, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_151 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_151, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD control 2")

    MdioRegister_152 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_152, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD status 2")

    MdioRegister_153 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_153, \
    Address="9", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD transmit disable")

    MdioRegister_154 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_154, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD receive signal detect")

    MdioRegister_155 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_155, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Extended ability")

    MdioRegister_156 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_156, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_157 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_157, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_158 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_158, \
    Address="129", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T status")

    MdioRegister_159 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_159, \
    Address="130", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T pair swap and polarity")

    MdioRegister_160 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_160, \
    Address="131", \
    RegValue="0", \
    WritableMask="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T TX power backoff setting")

    MdioRegister_161 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_161, \
    Address="132", \
    RegValue="1024", \
    WritableMask="64512", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T test mode")

    MdioRegister_162 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_162, \
    Address="133", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel A")

    MdioRegister_163 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_163, \
    Address="134", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel B")

    MdioRegister_164 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_164, \
    Address="135", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel C")

    MdioRegister_165 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_165, \
    Address="136", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel D")

    MdioRegister_166 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_166, \
    Address="137", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel A")

    MdioRegister_167 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_167, \
    Address="138", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel B")

    MdioRegister_168 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_168, \
    Address="139", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel C")

    MdioRegister_169 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_169, \
    Address="140", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel D")

    MdioRegister_170 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_170, \
    Address="141", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel A")

    MdioRegister_171 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_171, \
    Address="142", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel B")

    MdioRegister_172 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_172, \
    Address="143", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel C")

    MdioRegister_173 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_173, \
    Address="144", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel D")

    MdioRegister_174 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_174, \
    Address="145", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    MdioRegister_175 = (stc.get( ManagementDevice_6, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_175, \
    Address="146", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    ManagementDevice_7 = (stc.get( MdioPort_2, 'children-ManagementDevice' )).split(' ')[1]
    stc.config(ManagementDevice_7, \
    Address="2", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS")

    MdioRegister_176 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_176, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS control 1")

    MdioRegister_177 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_177, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS status 1")

    MdioRegister_178 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_178, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_179 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_179, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_180 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_180, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS speed ability")

    MdioRegister_181 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_181, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_182 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_182, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_183 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_183, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS control 2")

    MdioRegister_184 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_184, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 2")

    MdioRegister_185 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_185, \
    Address="9", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS test pattern error counter")

    MdioRegister_186 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_186, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_187 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_187, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_188 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_188, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 3")

    MdioRegister_189 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_189, \
    Address="37", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end path block error count")

    MdioRegister_190 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_190, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_191 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_191, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_192 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_192, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_193 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_193, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_194 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_194, \
    Address="43", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_195 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_195, \
    Address="44", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_196 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_196, \
    Address="45", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_197 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_197, \
    Address="46", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_198 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_198, \
    Address="47", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_199 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_199, \
    Address="48", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_200 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_200, \
    Address="49", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_201 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_201, \
    Address="50", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_202 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_202, \
    Address="51", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_203 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_203, \
    Address="52", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_204 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_204, \
    Address="53", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_205 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_205, \
    Address="54", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_206 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_206, \
    Address="55", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_207 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_207, \
    Address="56", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_208 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[32]
    stc.config(MdioRegister_208, \
    Address="57", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_209 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[33]
    stc.config(MdioRegister_209, \
    Address="58", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_210 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[34]
    stc.config(MdioRegister_210, \
    Address="59", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS path block error count")

    MdioRegister_211 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[35]
    stc.config(MdioRegister_211, \
    Address="60", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS section BIP error count")

    MdioRegister_212 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[36]
    stc.config(MdioRegister_212, \
    Address="64", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_213 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[37]
    stc.config(MdioRegister_213, \
    Address="65", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_214 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[38]
    stc.config(MdioRegister_214, \
    Address="66", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_215 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[39]
    stc.config(MdioRegister_215, \
    Address="67", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_216 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[40]
    stc.config(MdioRegister_216, \
    Address="68", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_217 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[41]
    stc.config(MdioRegister_217, \
    Address="69", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_218 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[42]
    stc.config(MdioRegister_218, \
    Address="70", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_219 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[43]
    stc.config(MdioRegister_219, \
    Address="71", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_220 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[44]
    stc.config(MdioRegister_220, \
    Address="72", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_221 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[45]
    stc.config(MdioRegister_221, \
    Address="73", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_222 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[46]
    stc.config(MdioRegister_222, \
    Address="74", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_223 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[47]
    stc.config(MdioRegister_223, \
    Address="75", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_224 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[48]
    stc.config(MdioRegister_224, \
    Address="76", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_225 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[49]
    stc.config(MdioRegister_225, \
    Address="77", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_226 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[50]
    stc.config(MdioRegister_226, \
    Address="78", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_227 = (stc.get( ManagementDevice_7, 'children-MdioRegister' )).split(' ')[51]
    stc.config(MdioRegister_227, \
    Address="79", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    ManagementDevice_8 = (stc.get( MdioPort_2, 'children-ManagementDevice' )).split(' ')[2]
    stc.config(ManagementDevice_8, \
    Address="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS")

    MdioRegister_228 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_228, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS control 1")

    MdioRegister_229 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_229, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS status 1")

    MdioRegister_230 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_230, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_231 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_231, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_232 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_232, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS speed ability")

    MdioRegister_233 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_233, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_234 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_234, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_235 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_235, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS control 2")

    MdioRegister_236 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_236, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS status 2")

    MdioRegister_237 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_237, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_238 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_238, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_239 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_239, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS status")

    MdioRegister_240 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_240, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS test control")

    MdioRegister_241 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_241, \
    Address="32", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 1")

    MdioRegister_242 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_242, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 2")

    MdioRegister_243 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_243, \
    Address="34", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_244 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_244, \
    Address="35", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_245 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_245, \
    Address="36", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_246 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_246, \
    Address="37", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_247 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_247, \
    Address="38", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_248 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_248, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_249 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_249, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_250 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_250, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_251 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_251, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern control")

    MdioRegister_252 = (stc.get( ManagementDevice_8, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_252, \
    Address="43", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern error counter")

    ManagementDevice_9 = (stc.get( MdioPort_2, 'children-ManagementDevice' )).split(' ')[3]
    stc.config(ManagementDevice_9, \
    Address="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS")

    MdioRegister_253 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_253, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS control 1")

    MdioRegister_254 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_254, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 1")

    MdioRegister_255 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_255, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_256 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_256, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_257 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_257, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS speed ability")

    MdioRegister_258 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_258, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_259 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_259, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_260 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_260, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 2")

    MdioRegister_261 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_261, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_262 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_262, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_263 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_263, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS lane status")

    MdioRegister_264 = (stc.get( ManagementDevice_9, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_264, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS test control")

    ManagementDevice_10 = (stc.get( MdioPort_2, 'children-ManagementDevice' )).split(' ')[4]
    stc.config(ManagementDevice_10, \
    Address="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto Negotiation")

    MdioRegister_265 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_265, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN control")

    MdioRegister_266 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_266, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN status")

    MdioRegister_267 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_267, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_268 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_268, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_269 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_269, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_270 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_270, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_271 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_271, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_272 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_272, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_273 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_273, \
    Address="16", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_274 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_274, \
    Address="17", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_275 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_275, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_276 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_276, \
    Address="19", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_277 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_277, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_278 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_278, \
    Address="21", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_279 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_279, \
    Address="22", \
    RegValue="0", \
    WritableMask="63487", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_280 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_280, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_281 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_281, \
    Address="24", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_282 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_282, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_283 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_283, \
    Address="26", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_284 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_284, \
    Address="27", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_285 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_285, \
    Address="32", \
    RegValue="0", \
    WritableMask="61447", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN control")

    MdioRegister_286 = (stc.get( ManagementDevice_10, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_286, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN status")

    StreamBlock_3 = stc.create("StreamBlock",under = Port_2, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1024", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Vxlan,Ancp,PppProtocol,PppoeProtocol,Openflow Protocol,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,AUTOSARTIMESYNC Protocol,CP traffic,Coap Protocol,OAM Protocol,Packet Channel,Dhcpv4,SyncE,Dhcpv6,IgmpMld,Cusp,AppPerf,Cifs,Iperf,Http,Ntp,RawTcp,Dpg,Sip,Video,CSMP,XMPPvJ,Ftp,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_10078\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>57325</checksum><sourceAddr>172.16.0.2</sourceAddr><destAddr>10.43.36.2</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>172.16.0.1</gateway><tosDiffserv name=\"anon_8638\"><tos name=\"anon_8639\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 14-4-1")

    EmulatedDevice_1 = stc.create("EmulatedDevice",under = Project_1, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Device 1")

    Ipv4If_3 = stc.create("Ipv4If",under = EmulatedDevice_1, \
    Address="10.43.36.2", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="10.43.36.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:1f:12:b4:73:8a", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 4")

    EthIIIf_3 = stc.create("EthIIIf",under = EmulatedDevice_1, \
    SourceMac="00:10:94:00:00:01", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="TRUE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 4")

    EmulatedDevice_2 = stc.create("EmulatedDevice",under = Project_1, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.3", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::3", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Device 3")

    Ipv4If_4 = stc.create("Ipv4If",under = EmulatedDevice_2, \
    Address="172.16.0.2", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="172.16.0.2", \
    AddrRepeatCount="0", \
    AddrResolver="Dhcpv4", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="172.16.0.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="172.16.0.1", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="38:70:0c:ba:10:0c", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="FALSE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 6")

    EthIIIf_4 = stc.create("EthIIIf",under = EmulatedDevice_2, \
    SourceMac="00:10:94:00:00:03", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="TRUE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 6")

    Dhcpv4BlockConfig_1 = stc.create("Dhcpv4BlockConfig",under = EmulatedDevice_2, \
    HostName="client_@p-@b-@s", \
    DefaultHostAddrPrefixLength="24", \
    OptionList="1 6 15 33 44", \
    EnableRouterOption="FALSE", \
    EnableArpServerId="FALSE", \
    UseBroadcastFlag="TRUE", \
    EnableRelayAgent="FALSE", \
    ClientRelayAgent="FALSE", \
    RelayAgentIpv4AddrMask="255.255.0.0", \
    RelayAgentIpv4Addr="192.85.1.5", \
    RelayAgentIpv4AddrStep="0.0.0.1", \
    RelayServerIpv4Addr="0.0.0.0", \
    RelayServerIpv4AddrStep="0.0.0.0", \
    RelayPoolIpv4Addr="0.0.0.0", \
    RelayPoolIpv4AddrStep="0.0.1.0", \
    EnableCircuitId="FALSE", \
    CircuitId="circuitId_@p", \
    EnableRemoteId="FALSE", \
    RemoteId="remoteId_@p-@b-@s", \
    RelayClientMacAddrStart="00:10:01:00:00:01", \
    RelayClientMacAddrStep="00:00:00:00:00:01", \
    RelayClientMacAddrMask="00:00:00:ff:ff:ff", \
    EnableRelayServerIdOverride="FALSE", \
    RelayServerIdOverride="192.85.1.1", \
    EnableRelayLinkSelection="FALSE", \
    RelayLinkSelection="192.85.1.1", \
    EnableRelayVPNID="FALSE", \
    VPNType="NVT_ASCII", \
    VPNId="spirent_@p", \
    EnableSessionAutoRetry="FALSE", \
    EnableAutoRetry="FALSE", \
    RetryAttempts="4", \
    ExportAddrToLinkedClients="FALSE", \
    UseClientMacAddrForDataplane="FALSE", \
    Ipv4Tos="192", \
    DNAv4DestIp="192.85.1.1", \
    DNAv4DestMac="00:10:01:00:00:01", \
    EnableGarp="FALSE", \
    GarpTransmits="1", \
    GarpTimeout="1", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DHCP 2")

    ResultDataSet_2 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="TxStreamResults", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="25", \
    NotifyInterval="1000", \
    Identifier="Stream Results\\Detailed Stream Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Stream Results", \
    ResultViewOwner="SYSTEM", \
    Description="object://l2l3/TxStreamResults", \
    CustomDisplayName="", \
    CustomDisplayPath="Streams", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Detailed Stream Results")

    RealTimeResultGroupDefinition_11 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="All Groups", \
    GroupId="core://allgroups/", \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="StreamInfo", \
    CountQuery="", \
    SqlString="", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 11")

    RealTimeResultGroupDefinition_12 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Basic Counters", \
    GroupId="object://customgroup/a7d38eca-b341-4d2f-9c5b-400e46180add/Basic Counters", \
    ColumnClassName="Port RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults TxStreamResults", \
    ColumnPropertyName="Name PortUiName AggregatedRxPortCount PortStrayFrames FrameCount FrameCount BitRate BitRate BitCount BitCount L1BitCount L1BitCount L1BitRate L1BitRate FrameRate FrameRate SigFrameCount SigFrameRate ShortTermAvgLatency AvgLatency MinLatency MaxLatency ShortTermAvgJitter AvgJitter MinJitter MaxJitter ShortTermAvgInterarrivalTime AvgInterarrivalTime MinInterarrivalTime MaxInterarrivalTime ExpectedRxFrameCount", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', (case when MIN(coalesce(IsExpectedPort,1)) = 0 then 'YES' else 'NO' end) as 'Port Stray Frames', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(SigFrameCount), 0) as 'Sig Count (Frames)', (TxOctetCount * 8) as 'Tx Count (bits)', coalesce(sum(OctetCount * 8), 0) as 'Rx Count (bits)', TxL1BitCount as 'Tx L1 Count (bits)', coalesce(sum(L1BitCount), 0) as 'Rx L1 Count (bits)', coalesce(round(sum(TotalLatency) / 100.0 / sum(SigFrameCount), 3), '') as 'Avg Latency (us)', coalesce(min(MinLatency), 0.0) as 'Min Latency (us)', coalesce(max(MaxLatency), 0.0) as 'Max Latency (us)', (case when (sum(TotalJitter) < 0.001 and coalesce(avg(AvgJitter), 0) > 0) then round(avg(AvgJitter), 3) when ((InJitterModeRfc3393 and ModInSeqFrameCount < 1) or (not InJitterModeRfc3393 and ModSigFrameCount < 1)) then '' when (InJitterModeRfc3393) then coalesce(round(sum(TotalJitter) / 100.0 / sum(ModInSeqFrameCount), 3), '') else coalesce(round(sum(TotalJitter) / 100.0 / sum(ModSigFrameCount), 3), '') end) as 'Avg Jitter (us)', coalesce(min(MinJitter), 0.0) as 'Min Jitter (us)', coalesce(max(MaxJitter), 0.0) as 'Max Jitter (us)', coalesce(round(sum(TotalInterarrivalTime) / 100.0 / sum(ModFrameCount), 3), '') as 'Avg Inter-arrival Time (us)', coalesce(min(MinInterarrivalTime), 0.0) as 'Min Inter-arrival Time (us)', coalesce(max(MaxInterarrivalTime), 0.0) as 'Max Inter-arrival Time (us)', TxCellCount as 'Tx Count (Cells)', coalesce(sum(CellCount), 0) as 'Rx Count (Cells)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 12")

    ResultQuery_3 = stc.create("ResultQuery",under = ResultDataSet_2, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.framecount rxbasicresults.sigframecount rxbasicresults.fcserrorframecount rxbasicresults.minlatency rxbasicresults.maxlatency rxbasicresults.droppedframecount rxbasicresults.droppedframepercent rxbasicresults.inorderframecount rxbasicresults.reorderedframecount rxbasicresults.duplicateframecount rxbasicresults.lateframecount rxbasicresults.prbsbiterrorcount rxbasicresults.prbsfilloctetcount rxbasicresults.ipv4checksumerrorcount rxbasicresults.tcpudpchecksumerrorcount rxbasicresults.framerate rxbasicresults.sigframerate rxbasicresults.fcserrorframerate rxbasicresults.droppedframerate rxbasicresults.droppedframepercentrate rxbasicresults.inorderframerate rxbasicresults.reorderedframerate rxbasicresults.duplicateframerate rxbasicresults.lateframerate rxbasicresults.prbsbiterrorrate rxbasicresults.prbsfilloctetrate rxbasicresults.ipv4checksumerrorrate rxbasicresults.tcpudpchecksumerrorrate rxbasicresults.bitrate rxbasicresults.shorttermavglatency rxbasicresults.avglatency rxbasicresults.prbsbiterrorratio rxbasicresults.l1bitcount rxbasicresults.l1bitrate rxbasicresults.prbserrorframecount rxbasicresults.prbserrorframerate rxstreamsummaryresults.aggregatedrxportcount rxbasicresults.portstrayframes rxbasicresults.bitcount rxbasicresults.shorttermavgjitter rxbasicresults.avgjitter rxbasicresults.minjitter rxbasicresults.maxjitter rxbasicresults.shorttermavginterarrivaltime rxbasicresults.avginterarrivaltime rxbasicresults.mininterarrivaltime rxbasicresults.maxinterarrivaltime rxbasicresults.inseqframecount rxbasicresults.outseqframecount rxbasicresults.inseqframerate rxbasicresults.outseqframerate rxbasicresults.histbin1count rxbasicresults.histbin2count rxbasicresults.histbin3count rxbasicresults.histbin4count rxbasicresults.histbin5count rxbasicresults.histbin6count rxbasicresults.histbin7count rxbasicresults.histbin8count rxbasicresults.histbin9count rxbasicresults.histbin10count rxbasicresults.histbin11count rxbasicresults.histbin12count rxbasicresults.histbin13count rxbasicresults.histbin14count rxbasicresults.histbin15count rxbasicresults.histbin16count", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 6")

    ResultQuery_4 = stc.create("ResultQuery",under = ResultDataSet_2, \
    ConfigClassId="streamblock", \
    ResultClassId="txstreamresults", \
    PropertyIdArray="txbasicresults.framecount txbasicresults.framerate txbasicresults.bitrate txstreamresults.expectedrxframecount txbasicresults.l1bitcount txbasicresults.l1bitrate txstreamresults.streaminfo txbasicresults.bitcount", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 7")

    RealTimeResultColumnDefinition_154 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="StreamInfo", \
    ColumnDescription="", \
    ColumnWidth="74", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 119")

    RealTimeResultColumnDefinition_155 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="Port", \
    ColumnPropertyName="Name", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 120")

    RealTimeResultColumnDefinition_156 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PortUiName", \
    ColumnDescription="", \
    ColumnWidth="65", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 121")

    RealTimeResultColumnDefinition_157 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AggregatedRxPortCount", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 122")

    RealTimeResultColumnDefinition_158 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PortStrayFrames", \
    ColumnDescription="", \
    ColumnWidth="75", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 123")

    RealTimeResultColumnDefinition_159 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="FrameCount", \
    ColumnDescription="", \
    ColumnWidth="97", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 124")

    RealTimeResultColumnDefinition_160 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FrameCount", \
    ColumnDescription="", \
    ColumnWidth="97", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 125")

    RealTimeResultColumnDefinition_161 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 126")

    RealTimeResultColumnDefinition_162 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 127")

    RealTimeResultColumnDefinition_163 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 128")

    RealTimeResultColumnDefinition_164 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 129")

    RealTimeResultColumnDefinition_165 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 130")

    RealTimeResultColumnDefinition_166 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 131")

    RealTimeResultColumnDefinition_167 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 132")

    RealTimeResultColumnDefinition_168 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 133")

    RealTimeResultColumnDefinition_169 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="FrameRate", \
    ColumnDescription="", \
    ColumnWidth="90", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 134")

    RealTimeResultColumnDefinition_170 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FrameRate", \
    ColumnDescription="", \
    ColumnWidth="91", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 247")

    RealTimeResultColumnDefinition_171 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="SigFrameCount", \
    ColumnDescription="", \
    ColumnWidth="116", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 248")

    RealTimeResultColumnDefinition_172 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="SigFrameRate", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 249")

    RealTimeResultColumnDefinition_173 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgLatency", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 250")

    RealTimeResultColumnDefinition_174 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgLatency", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 247")

    RealTimeResultColumnDefinition_175 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinLatency", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 248")

    RealTimeResultColumnDefinition_176 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxLatency", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 249")

    RealTimeResultColumnDefinition_177 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgJitter", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 250")

    RealTimeResultColumnDefinition_178 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgJitter", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 135")

    RealTimeResultColumnDefinition_179 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinJitter", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 136")

    RealTimeResultColumnDefinition_180 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxJitter", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 137")

    RealTimeResultColumnDefinition_181 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 138")

    RealTimeResultColumnDefinition_182 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_183 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_184 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_185 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="ExpectedRxFrameCount", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_186 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="Ipv4ChecksumErrorCount", \
    ColumnDescription="", \
    ColumnWidth="171", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_187 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="TcpUdpChecksumErrorCount", \
    ColumnDescription="", \
    ColumnWidth="194", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_188 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorCount", \
    ColumnDescription="", \
    ColumnWidth="121", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_189 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsFillOctetCount", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="12", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 148")

    RealTimeResultColumnDefinition_190 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorRatio", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 149")

    RealTimeResultColumnDefinition_191 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FcsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="148", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 150")

    RealTimeResultColumnDefinition_192 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="Ipv4ChecksumErrorRate", \
    ColumnDescription="", \
    ColumnWidth="164", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 151")

    RealTimeResultColumnDefinition_193 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="TcpUdpChecksumErrorRate", \
    ColumnDescription="", \
    ColumnWidth="187", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 152")

    RealTimeResultColumnDefinition_194 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorRate", \
    ColumnDescription="", \
    ColumnWidth="130", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 153")

    RealTimeResultColumnDefinition_195 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsFillOctetRate", \
    ColumnDescription="", \
    ColumnWidth="117", \
    ColumnUnits="18", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 154")

    RealTimeResultColumnDefinition_196 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FcsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="141", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 155")

    RealTimeResultColumnDefinition_197 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 156")

    RealTimeResultColumnDefinition_198 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 157")

    RealTimeResultColumnDefinition_199 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="147", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 158")

    RealTimeResultColumnDefinition_200 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="OutSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="170", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 159")

    RealTimeResultColumnDefinition_201 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InSeqFrameRate", \
    ColumnDescription="", \
    ColumnWidth="140", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 160")

    RealTimeResultColumnDefinition_202 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="OutSeqFrameRate", \
    ColumnDescription="", \
    ColumnWidth="161", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 161")

    RealTimeResultColumnDefinition_203 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="127", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 162")

    RealTimeResultColumnDefinition_204 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFramePercent", \
    ColumnDescription="", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 163")

    RealTimeResultColumnDefinition_205 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InOrderFrameCount", \
    ColumnDescription="", \
    ColumnWidth="126", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 164")

    RealTimeResultColumnDefinition_206 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ReorderedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="136", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 165")

    RealTimeResultColumnDefinition_207 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DuplicateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="131", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 166")

    RealTimeResultColumnDefinition_208 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="LateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="106", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 167")

    RealTimeResultColumnDefinition_209 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFrameRate", \
    ColumnDescription="", \
    ColumnWidth="121", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 168")

    RealTimeResultColumnDefinition_210 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFramePercentRate", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 169")

    RealTimeResultColumnDefinition_211 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InOrderFrameRate", \
    ColumnDescription="", \
    ColumnWidth="119", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 170")

    RealTimeResultColumnDefinition_212 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ReorderedFrameRate", \
    ColumnDescription="", \
    ColumnWidth="130", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 171")

    RealTimeResultColumnDefinition_213 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DuplicateFrameRate", \
    ColumnDescription="", \
    ColumnWidth="124", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 172")

    RealTimeResultColumnDefinition_214 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="LateFrameRate", \
    ColumnDescription="", \
    ColumnWidth="99", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 173")

    RealTimeResultColumnDefinition_215 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin1Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 174")

    RealTimeResultColumnDefinition_216 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin2Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 175")

    RealTimeResultColumnDefinition_217 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin3Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 176")

    RealTimeResultGroupDefinition_13 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Errors", \
    GroupId="object://customgroup/1334ba8f-a144-4069-8cb7-11633334149f/Errors", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount Ipv4ChecksumErrorCount TcpUdpChecksumErrorCount PrbsBitErrorCount PrbsFillOctetCount PrbsBitErrorRatio FcsErrorFrameCount Ipv4ChecksumErrorRate TcpUdpChecksumErrorRate PrbsBitErrorRate PrbsFillOctetRate FcsErrorFrameRate PrbsErrorFrameCount PrbsErrorFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)',  coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(Ipv4ChecksumErrorCount), 0) as 'Rx IPv4 Checksum Error Count', coalesce(sum(TcpUdpChecksumErrorCount), 0) as 'Rx TCP/UDP Checksum Error Count', coalesce(sum(PrbsBitErrorCount), 0) as 'PRBS Bit Error Count', coalesce(sum(PrbsFillOctetCount), 0) as 'PRBS Fill Octet Count', coalesce(round(cast(sum(PrbsBitErrorCount) as double)/(sum(PrbsFillOctetCount)*8), 3), 0.0) as 'PRBS Bit Error Ratio', coalesce(sum(FcsErrorFrameCount), 0) as 'Rx FCS Error Count (Frames)', coalesce(sum(PrbsErrorFrameCount), 0) as 'PRBS Error Frame Count' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 13")

    RealTimeResultGroupDefinition_14 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Basic Sequencing", \
    GroupId="object://customgroup/e652f0ae-e04e-4f5b-922e-f6a0a21e9347/Basic Sequencing", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount InSeqFrameCount OutSeqFrameCount InSeqFrameRate OutSeqFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(SeqRunLength), 0) as 'Sequence Run Length', coalesce(sum(InSeqFrameCount), 0) as 'In Seq Count (Frames)', coalesce(sum(OutSeqFrameCount), 0) as 'Out of Seq Count (Frames)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 14")

    RealTimeResultGroupDefinition_15 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Advanced Sequencing", \
    GroupId="object://customgroup/3d3639f4-a55b-4466-8e16-2e7c6a70afa7/Advanced Sequencing", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount DroppedFrameCount DroppedFramePercent InOrderFrameCount ReorderedFrameCount DuplicateFrameCount LateFrameCount DroppedFrameRate DroppedFramePercentRate InOrderFrameRate ReorderedFrameRate DuplicateFrameRate LateFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as  'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', ExpectedRxFrameCount as 'Expected Rx Count (Frames)', (case when (ExpectedRxFrameCount - coalesce(sum(FrameCount), 0)) < 0 then '' else ExpectedRxFrameCount - coalesce(sum(FrameCount),0) end) as 'Tx-Rx (Frames)', (case when (ExpectedRxFrameCount - coalesce(sum(FrameCount), 0)) < 0 then '' else round(cast(ExpectedRxFrameCount - coalesce(sum(FrameCount), 0) as double) * 100.0 / ExpectedRxFrameCount, 5) end) as 'Tx-Rx (%)', coalesce(sum(DroppedFrameCount), 0) as 'Dropped Frame Count', round(cast(coalesce(sum(DroppedFrameCount), 0) as double) * 100.0 / ExpectedRxFrameCount, 5) as 'Dropped Frame (%)', coalesce(sum(InOrderFrameCount), 0) as 'In-order Frame Count', coalesce(sum(ReorderedFrameCount), 0) as 'Reordered Frame Count', coalesce(sum(DuplicateFrameCount), 0) as 'Duplicate Count (Frames)', coalesce(sum(LateFrameCount), 0) as 'Late Count (Frames)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 15")

    RealTimeResultGroupDefinition_16 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Histograms", \
    GroupId="object://customgroup/a3fa4141-b6c7-4c1b-935b-df51d6118259/Histograms", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount HistBin1Count HistBin2Count HistBin3Count HistBin4Count HistBin5Count HistBin6Count HistBin7Count HistBin8Count HistBin9Count HistBin10Count HistBin11Count HistBin12Count HistBin13Count HistBin14Count HistBin15Count HistBin16Count", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(HistBin1Count), 0) as 'Bucket 1', coalesce(sum(HistBin2Count), 0) as 'Bucket 2', coalesce(sum(HistBin3Count), 0) as 'Bucket 3', coalesce(sum(HistBin4Count), 0) as 'Bucket 4', coalesce(sum(HistBin5Count), 0) as 'Bucket 5', coalesce(sum(HistBin6Count), 0) as 'Bucket 6', coalesce(sum(HistBin7Count), 0) as 'Bucket 7', coalesce(sum(HistBin8Count), 0) as 'Bucket 8', coalesce(sum(HistBin9Count), 0) as 'Bucket 9', coalesce(sum(HistBin10Count), 0) as 'Bucket 10', coalesce(sum(HistBin11Count), 0) as 'Bucket 11', coalesce(sum(HistBin12Count), 0) as 'Bucket 12', coalesce(sum(HistBin13Count), 0) as 'Bucket 13', coalesce(sum(HistBin14Count), 0) as 'Bucket 14', coalesce(sum(HistBin15Count), 0) as 'Bucket 15', coalesce(sum(HistBin16Count), 0) as 'Bucket 16' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 16")

    RealTimeResultColumnDefinition_218 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin4Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 177")

    RealTimeResultColumnDefinition_219 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin5Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 178")

    RealTimeResultColumnDefinition_220 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin6Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 179")

    RealTimeResultColumnDefinition_221 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin7Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 180")

    RealTimeResultColumnDefinition_222 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin8Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 181")

    RealTimeResultColumnDefinition_223 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin9Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 182")

    RealTimeResultColumnDefinition_224 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin10Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 183")

    RealTimeResultColumnDefinition_225 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin11Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 184")

    RealTimeResultColumnDefinition_226 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin12Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 184")

    RealTimeResultColumnDefinition_227 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin13Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 185")

    RealTimeResultColumnDefinition_228 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin14Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 186")

    RealTimeResultColumnDefinition_229 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin15Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 229")

    RealTimeResultColumnDefinition_230 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin16Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 230")

    RxPortResultFilter_1 = stc.create("RxPortResultFilter",under = Project_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RxPortResultFilter 1")

    ExposedConfig_1 = stc.create("ExposedConfig",under = Project_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ExposedConfig 1")

    ResultDataSet_3 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 854")

    ResultQuery_5 = stc.create("ResultQuery",under = ResultDataSet_3, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 1059")

    Host_3 = (stc.get( Port_3, 'children-Host' )).split(' ')[0]
    stc.config(Host_3, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    EthIIIf_5 = stc.create("EthIIIf",under = Host_3, \
    SourceMac="00:10:94:00:00:02", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 5")

    HdlcIf_3 = stc.create("HdlcIf",under = Host_3, \
    ProtocolType="HDLC_PROTOCOL_TYPE_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="HDLC 3")

    PppIf_5 = stc.create("PppIf",under = Host_3, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 5")

    PppIf_6 = stc.create("PppIf",under = Host_3, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 6")

    Ipv4If_5 = stc.create("Ipv4If",under = Host_3, \
    Address="192.85.1.3", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 5")

    Ipv6If_5 = stc.create("Ipv6If",under = Host_3, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 5")

    Ipv6If_6 = stc.create("Ipv6If",under = Host_3, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    ExtensionHeader="0", \
    SegmentsLeft="0", \
    LastEntry="0", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 6")

    SystemResourceManager_3 = (stc.get( Port_3, 'children-SystemResourceManager' )).split(' ')[0]
    stc.config(SystemResourceManager_3, \
    MemoryThreshold="80", \
    MemoryThresholdEnable="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Resource Manager 3")

    Generator_3 = (stc.get( Port_3, 'children-Generator' )).split(' ')[0]
    stc.config(Generator_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Generator 3")

    GeneratorConfig_3 = (stc.get( Generator_3, 'children-GeneratorConfig' )).split(' ')[0]
    stc.config(GeneratorConfig_3, \
    SchedulingMode="RATE_BASED", \
    AdvancedInterleaving="FALSE", \
    Duration="30", \
    DurationMode="CONTINUOUS", \
    StepSize="1", \
    TimestampLatchMode="START_OF_FRAME", \
    RandomLengthSeed="10900842", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    BurstSize="1", \
    LoadUnit="PERCENT_LINE_RATE", \
    LoadMode="FIXED", \
    FixedLoad="10", \
    RandomMaxLoad="100", \
    RandomMinLoad="10", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    SmoothenRandomLength="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Generator Configuration 3")

    Analyzer_3 = (stc.get( Port_3, 'children-Analyzer' )).split(' ')[0]
    stc.config(Analyzer_3, \
    FilterOnStreamId="TRUE", \
    FilterOnInnerIP="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Analyzer 3")

    AnalyzerConfig_3 = (stc.get( Analyzer_3, 'children-AnalyzerConfig' )).split(' ')[0]
    stc.config(AnalyzerConfig_3, \
    TimestampLatchMode="START_OF_FRAME", \
    SigMode="ENHANCED_DETECTION", \
    HistogramMode="LATENCY", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    AdvSeqCheckerLateThreshold="1000", \
    VlanAlternateTpid="34984", \
    AlternateSigOffset="0", \
    LatencyMode="PER_STREAM_RX_LATENCY_ON", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Advanced Analyzer Settings 3")

    InterarrivalTimeHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-InterarrivalTimeHistogram' )).split(' ')[0]
    stc.config(InterarrivalTimeHistogram_3, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    LatencyHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-LatencyHistogram' )).split(' ')[0]
    stc.config(LatencyHistogram_3, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    FrameLengthHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-FrameLengthHistogram' )).split(' ')[0]
    stc.config(FrameLengthHistogram_3, \
    Description="(in bytes)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    SeqRunLengthHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-SeqRunLengthHistogram' )).split(' ')[0]
    stc.config(SeqRunLengthHistogram_3, \
    Description="(in frames)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    SeqDiffCheckHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-SeqDiffCheckHistogram' )).split(' ')[0]
    stc.config(SeqDiffCheckHistogram_3, \
    Description="(in deltas)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    JitterHistogram_3 = (stc.get( AnalyzerConfig_3, 'children-JitterHistogram' )).split(' ')[0]
    stc.config(JitterHistogram_3, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 3")

    DiffServConfig_3 = (stc.get( Analyzer_3, 'children-DiffServConfig' )).split(' ')[0]
    stc.config(DiffServConfig_3, \
    QualifyIpv6DstAddr="FALSE", \
    Ipv6DstAddr="ffff::ffff", \
    QualifyIpv4DstAddr="FALSE", \
    Ipv4DstAddr="0.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QoS Settings 3")

    HighResolutionSamplingPortConfig_3 = (stc.get( Analyzer_3, 'children-HighResolutionSamplingPortConfig' )).split(' ')[0]
    stc.config(HighResolutionSamplingPortConfig_3, \
    BaselineSampleCount="3", \
    EnableTrigger="TRUE", \
    TriggerCondition="LESS_THAN", \
    TriggerValueUnitMode="PERCENT_BASELINE", \
    TriggerStat="TotalFrameRate", \
    TriggerValue="95", \
    TriggerLocation="20", \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Port Sampling 3")

    Capture_3 = (stc.get( Port_3, 'children-Capture' )).split(' ')[0]
    stc.config(Capture_3, \
    ElapsedTime="0:00:00", \
    TabIndex="0", \
    Mode="REGULAR_MODE", \
    SrcMode="TX_RX_MODE", \
    RealTimeMode="REALTIME_DISABLE", \
    FlagMode="REGULAR_FLAG_MODE", \
    BufferMode="WRAP", \
    Start="16384", \
    Stop="0", \
    SliceMode="DISABLE", \
    SliceOffsetRef="PREAMBLE", \
    SliceOffset="0", \
    SliceCaptureSize="128", \
    RealTimeFramesBuffer="0", \
    RealTimeBufferStatus="FALSE", \
    CurrentTask="IDLE", \
    CurrentFiltersUsed="0", \
    CurrentFilterBytesUsed="0", \
    AbortSaveTask="FALSE", \
    PostStopTriggerBuffer="255", \
    CaptureFilterMode="FRAMECONTENT", \
    SaveBufferWithPreamble="FALSE", \
    IncreasedMemorySupport="FALSE", \
    Ieee80211FilterString="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture 3")

    CaptureFilter_3 = (stc.get( Capture_3, 'children-CaptureFilter' )).split(' ')[0]
    stc.config(CaptureFilter_3, \
    QualifyEvents="TRUE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Qualify Events 3")

    CaptureFilterStartEvent_3 = (stc.get( Capture_3, 'children-CaptureFilterStartEvent' )).split(' ')[0]
    stc.config(CaptureFilterStartEvent_3, \
    StartEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Events 3")

    CaptureFilterStopEvent_3 = (stc.get( Capture_3, 'children-CaptureFilterStopEvent' )).split(' ')[0]
    stc.config(CaptureFilterStopEvent_3, \
    StopEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Events 3")

    CaptureIeee80211_3 = (stc.get( Capture_3, 'children-CaptureIeee80211' )).split(' ')[0]
    stc.config(CaptureIeee80211_3, \
    ChannelWidth="CHANNEL_WIDTH_40M", \
    Channel="36", \
    SecondChannel="149", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture IEEE 802.11 3")

    CaptureRawPacketTagsInfo_3 = (stc.get( Capture_3, 'children-CaptureRawPacketTagsInfo' )).split(' ')[0]
    stc.config(CaptureRawPacketTagsInfo_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CaptureRawPacketTagsInfo 3")

    ArpCache_3 = (stc.get( Port_3, 'children-ArpCache' )).split(' ')[0]
    stc.config(ArpCache_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpCache 3")

    ArpNdReport_3 = (stc.get( Port_3, 'children-ArpNdReport' )).split(' ')[0]
    stc.config(ArpNdReport_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdReport 3")

    PingReport_3 = (stc.get( Port_3, 'children-PingReport' )).split(' ')[0]
    stc.config(PingReport_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PingReport 3")

    IgmpPortConfig_3 = (stc.get( Port_3, 'children-IgmpPortConfig' )).split(' ')[0]
    stc.config(IgmpPortConfig_3, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IgmpPortConfig 3")

    MldPortConfig_3 = (stc.get( Port_3, 'children-MldPortConfig' )).split(' ')[0]
    stc.config(MldPortConfig_3, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MldPortConfig 3")

    OsePortConfig_3 = (stc.get( Port_3, 'children-OsePortConfig' )).split(' ')[0]
    stc.config(OsePortConfig_3, \
    VirtualSwitch="OVS_2_1", \
    ManufacturerDescription="Spirent Communications", \
    HardwareDescription="Open vSwitch", \
    SerialNumber="None", \
    DatapathDescription="None", \
    ExposeOvsdb="FALSE", \
    OvsdbPortNumber="6640", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OsePortConfig 3")

    OvsdbPortConfig_3 = (stc.get( Port_3, 'children-OvsdbPortConfig' )).split(' ')[0]
    stc.config(OvsdbPortConfig_3, \
    ConnectionType="TCP", \
    PrivateKey="", \
    Certificate="", \
    CaCertificates="", \
    TlsConnectionOpen="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OVSDB Port Configuration 3")

    OpflexPortConfig_3 = (stc.get( Port_3, 'children-OpflexPortConfig' )).split(' ')[0]
    stc.config(OpflexPortConfig_3, \
    DomainName="Openstack", \
    AgentName="Agent1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Opflex Port Configuration 3")

    VxlanPortConfig_3 = (stc.get( Port_3, 'children-VxlanPortConfig' )).split(' ')[0]
    stc.config(VxlanPortConfig_3, \
    UdpDstPort="4789", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VXLAN Port Configuration 3")

    Ieee1588v2PortConfig_3 = (stc.get( Port_3, 'children-Ieee1588v2PortConfig' )).split(' ')[0]
    stc.config(Ieee1588v2PortConfig_3, \
    UpperOffsetThreshold="300", \
    LowerOffsetThreshold="-300", \
    BeforeAndAfterThresholdRowCount="0", \
    RxLogSyncInterval="0", \
    MeasureSeqIdErrors="FALSE", \
    EnableClockSyncFilteredResult="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee1588v2PortConfig 3")

    QbvStreamConfig_3 = (stc.get( Port_3, 'children-QbvStreamConfig' )).split(' ')[0]
    stc.config(QbvStreamConfig_3, \
    ConfigQbvParams="FALSE", \
    GptpBaseTime="0.0", \
    GateCycleTime="1000", \
    StartTimeWithinCycle="0", \
    TickGranularityOfDut="2.5", \
    StreamStartWaitTime="0", \
    DurationModeSecondsValue="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QbvStreamConfig 3")

    StpPortConfig_3 = (stc.get( Port_3, 'children-StpPortConfig' )).split(' ')[0]
    stc.config(StpPortConfig_3, \
    StpType="STP", \
    PortType="TRUNK", \
    EthernetType="8100", \
    NativeVlan="1", \
    EnablePt2PtLink="FALSE", \
    EnableMacAddrReduction="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StpPortConfig 3")

    Dhcpv4PortConfig_3 = (stc.get( Port_3, 'children-Dhcpv4PortConfig' )).split(' ')[0]
    stc.config(Dhcpv4PortConfig_3, \
    MaxMsgSize="576", \
    LeaseTime="60", \
    MsgTimeout="60", \
    RetryCount="4", \
    RequestRate="100", \
    ReleaseRate="100", \
    StartingXid="0", \
    OutstandingSessionCount="1000", \
    SeqType="SEQUENTIAL", \
    MaxDnav4RetryCount="0", \
    Dnav4Timeout="1000", \
    EnableAssignCustomOptionsForHosts="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4PortConfig 3")

    Dhcpv6PortConfig_3 = (stc.get( Port_3, 'children-Dhcpv6PortConfig' )).split(' ')[0]
    stc.config(Dhcpv6PortConfig_3, \
    RequestRate="100", \
    ReleaseRate="100", \
    RenewRate="100", \
    SessionAutoRetry="FALSE", \
    RetryAttempts="0", \
    NoWaitMultiAdv="FALSE", \
    EnableBlockRate="FALSE", \
    SolicitTimeout="1", \
    MaxSolicitRetryTimeout="120", \
    SolicitRetryCount="10", \
    IndefSolicitRetry="FALSE", \
    DisableSolicitRetry="FALSE", \
    RequestTimeout="1", \
    MaxRequestRetryTimeout="30", \
    RequestRetryCount="10", \
    IndefRequestRetry="FALSE", \
    DisableRequestRetry="FALSE", \
    ConfirmTimeout="1", \
    MaxConfirmTimeout="4", \
    MaxConfirmDuration="10", \
    RenewTimeout="10", \
    MaxRenewRetryTimeout="600", \
    RenewRetryCount="0", \
    IndefRenewRetry="TRUE", \
    DisableRenewRetry="FALSE", \
    RebindTimeout="10", \
    MaxRebindRetryTimeout="600", \
    RebindRetryCount="0", \
    IndefRebindRetry="TRUE", \
    DisableRebindRetry="FALSE", \
    ReleaseTimeout="1", \
    ReleaseRetryCount="5", \
    IndefReleaseRetry="FALSE", \
    DisableReleaseRetry="FALSE", \
    DeclineTimeout="1", \
    DeclineRetryCount="5", \
    IndefDeclineRetry="FALSE", \
    DisableDeclineRetry="FALSE", \
    OutstandingSessionCount="1000", \
    InfoRequestTimeout="1", \
    MaxInfoRequestTimeout="120", \
    InfoRequestRetryCount="0", \
    IndefInfoRequestRetry="TRUE", \
    DisableInfoRequestRetry="FALSE", \
    LeaseTime="86400", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6PortConfig 3")

    SaaPortConfig_3 = (stc.get( Port_3, 'children-SaaPortConfig' )).split(' ')[0]
    stc.config(SaaPortConfig_3, \
    RequestRate="300", \
    OutstandingSessionCount="1000", \
    SeqType="PARALLEL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="SaaPortConfig 3")

    RoEPortConfig_3 = (stc.get( Port_3, 'children-RoEPortConfig' )).split(' ')[0]
    stc.config(RoEPortConfig_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RoEPortConfig 3")

    L2tpPortConfig_3 = (stc.get( Port_3, 'children-L2tpPortConfig' )).split(' ')[0]
    stc.config(L2tpPortConfig_3, \
    L2tpVersion="L2TPV2", \
    L2tpNodeType="LAC", \
    TunnelConnectRate="100", \
    SeqType="SEQUENTIAL", \
    ConnectRateV3="100", \
    DisconnectRateV3="1000", \
    SessionOutstandingV3="100", \
    CsurqRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2tpPortConfig 3")

    PppoxPortConfig_3 = (stc.get( Port_3, 'children-PppoxPortConfig' )).split(' ')[0]
    stc.config(PppoxPortConfig_3, \
    EmulationType="CLIENT", \
    EnableBlockRate="FALSE", \
    ConnectRate="100", \
    DisconnectRate="1000", \
    SessionOutstanding="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxPortConfig 3")

    PppProtocolConfig_3 = (stc.get( Port_3, 'children-PppProtocolConfig' )).split(' ')[0]
    stc.config(PppProtocolConfig_3, \
    PapRequestTimeout="3", \
    MaxPapRequestAttempts="10", \
    ChapChalRequestTimeout="3", \
    ChapAckTimeout="3", \
    MaxChapRequestReplyAttempts="10", \
    AutoRetryCount="65535", \
    EnableAutoRetry="FALSE", \
    EnableSessionAutoRetry="FALSE", \
    Ipv4PeerAddr="0.0.0.0", \
    Ipv6PeerAddr="::", \
    IpcpEncap="IPV4", \
    Protocol="PPPOPOS", \
    EnableMruNegotiation="TRUE", \
    EnableMagicNum="TRUE", \
    EnableNcpTermination="FALSE", \
    Authentication="NONE", \
    IncludeTxChapId="TRUE", \
    EnableOsi="FALSE", \
    EnableMpls="FALSE", \
    MruSize="1492", \
    EnableEchoRequest="FALSE", \
    EchoRequestGenFreq="10", \
    MaxEchoRequestAttempts="1", \
    LcpConfigRequestTimeout="3", \
    LcpConfigRequestMaxAttempts="10", \
    LcpTermRequestTimeout="3", \
    LcpTermRequestMaxAttempts="10", \
    NcpConfigRequestTimeout="3", \
    NcpConfigRequestMaxAttempts="10", \
    MaxNaks="5", \
    Username="spirent", \
    Password="spirent", \
    UseAuthenticationList="FALSE", \
    AuthenticationFilePath="", \
    EnablePrimaryDns="TRUE", \
    PrimaryDns="null", \
    EnableSecondaryDns="TRUE", \
    SecondaryDns="null", \
    RAMOFlag="NODHCP", \
    ConnectRate="100", \
    DisconnectRate="100", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 3")

    AncpPortConfig_3 = (stc.get( Port_3, 'children-AncpPortConfig' )).split(' ')[0]
    stc.config(AncpPortConfig_3, \
    EstablishRate="100", \
    TerminateRate="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AncpPortConfig 3")

    CuspPortConfig_3 = (stc.get( Port_3, 'children-CuspPortConfig' )).split(' ')[0]
    stc.config(CuspPortConfig_3, \
    EstablishRate="100", \
    TerminateRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CuspPortConfig 3")

    EoamPortConfig_3 = (stc.get( Port_3, 'children-EoamPortConfig' )).split(' ')[0]
    stc.config(EoamPortConfig_3, \
    EtherType="8902", \
    MulticastMacType1="01:80:c2:00:00:30", \
    MulticastMacType2="01:80:c2:00:00:38", \
    EncodeMeLevel="TRUE", \
    DisableContChkRx="FALSE", \
    LinkTraceResponseRelayAction="DEFAULT", \
    ImmediateLinkTraceResponse="FALSE", \
    ImmediateLoopbackResponse="FALSE", \
    EchoTlvsInDelayMeasurementResponse="TRUE", \
    EchoTlvsInLossMeasurementResponse="TRUE", \
    EchoTlvsInSlr="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamPortConfig 3")

    AppPerfPortConfig_3 = (stc.get( Port_3, 'children-AppPerfPortConfig' )).split(' ')[0]
    stc.config(AppPerfPortConfig_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AppPerfPortConfig 3")

    VqAnalyzer_3 = (stc.get( Port_3, 'children-VqAnalyzer' )).split(' ')[0]
    stc.config(VqAnalyzer_3, \
    FrameLossConcealmentRobustness="4", \
    SlicesPerIframe="0", \
    NominalDelay="3", \
    MaxPktCount="65535", \
    MosVThreshold="1", \
    MosVNormalizedThreshold="1", \
    MosAvThreshold="1", \
    MosAThreshold="1", \
    PidInterval="1", \
    PatRepetition="0.5", \
    PmtRepetition="0.5", \
    PcrContinuity="0.1", \
    PcrRepetition="0.04", \
    PtsRepetition="0.7", \
    RtpTimestampThreshold="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzer 3")

    AutosarTimeSyncPortConfig_3 = (stc.get( Port_3, 'children-AutosarTimeSyncPortConfig' )).split(' ')[0]
    stc.config(AutosarTimeSyncPortConfig_3, \
    DevicesMode="RX", \
    Protocol="CAN", \
    CANId="1061", \
    PortNumber="1", \
    TimeDomain="0", \
    SgwBit="0", \
    OverflowOfSeconds="0", \
    SequenceCounterJump="1", \
    SyncInterval="500", \
    MinSyncInterval="-10", \
    MaxSyncInterval="50", \
    MinFollowUpInterval="0", \
    MaxFollowUpInterval="100", \
    RandomJump="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutosarTimeSyncPortConfig 3")

    CoapPortConfig_3 = (stc.get( Port_3, 'children-CoapPortConfig' )).split(' ')[0]
    stc.config(CoapPortConfig_3, \
    ServerStartRate="500", \
    ServerStopRate="500", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CoapPortConfig 3")

    EthernetCopper_3 = stc.create("EthernetCopper",under = Port_3, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 3")

    Mii_3 = (stc.get( EthernetCopper_3, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_65 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_65, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_66 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_66, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_67 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_67, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_68 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_68, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_69 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_69, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_70 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_70, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_71 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_71, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_72 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_72, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_73 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_73, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_74 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_74, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_75 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_75, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_76 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_76, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_77 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_77, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_78 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_78, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_79 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_79, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_80 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_80, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_81 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_81, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_82 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_82, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_83 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_83, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_84 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_84, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_85 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_85, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_86 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_86, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_87 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_87, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_88 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_88, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_89 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_89, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_90 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_90, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_91 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_91, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_92 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_92, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_93 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_93, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_94 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_94, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_95 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_95, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_96 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_96, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    Ethernet10GigFiber_3 = stc.create("Ethernet10GigFiber",under = Port_3, \
    PortMode="LAN", \
    DeficitIdleCount="TRUE", \
    CfpInterface="ACC_6068A", \
    PriorityFlowControlArray="FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE", \
    IsPfcNegotiated="FALSE", \
    TxDeEmphasisPreTap="0", \
    TxDeEmphasisPostTap="13", \
    TxMainTapSwing="15", \
    DetectionMode="AUTO_DETECT", \
    CableTypeLength="OPTICAL", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="SPEED_10G", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    AnAdvMode="CONSORTIUM", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="ENABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mdio/ieee802_3ae45.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet 10G Fiber Phy 3")

    EthernetWan_3 = (stc.get( Ethernet10GigFiber_3, 'children-EthernetWan' )).split(' ')[0]
    stc.config(EthernetWan_3, \
    FramingMode="SONET_FRAMING", \
    SectionScramble="TRUE", \
    PathSignalLabel="ETHERNET_10G_WAN_PATH_SIGNAL_LABEL", \
    Crc32="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G Ethernet WAN 3")

    Mdio_3 = (stc.get( Ethernet10GigFiber_3, 'children-Mdio' )).split(' ')[0]
    stc.config(Mdio_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mdio 1")

    MdioPort_3 = (stc.get( Mdio_3, 'children-MdioPort' )).split(' ')[0]
    stc.config(MdioPort_3, \
    Clause="CLAUSE_45", \
    Address="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MdioPort 1")

    ManagementDevice_11 = (stc.get( MdioPort_3, 'children-ManagementDevice' )).split(' ')[0]
    stc.config(ManagementDevice_11, \
    Address="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD")

    MdioRegister_287 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_287, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD control 1")

    MdioRegister_288 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_288, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD status 1(RO)")

    MdioRegister_289 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_289, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_290 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_290, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Device ID")

    MdioRegister_291 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_291, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD speed ability")

    MdioRegister_292 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_292, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_293 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_293, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD devices in package")

    MdioRegister_294 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_294, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD control 2")

    MdioRegister_295 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_295, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMA/PMD status 2")

    MdioRegister_296 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_296, \
    Address="9", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD transmit disable")

    MdioRegister_297 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_297, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PMD receive signal detect")

    MdioRegister_298 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_298, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD Extended ability")

    MdioRegister_299 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_299, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_300 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_300, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PMA/PMD package identifier")

    MdioRegister_301 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_301, \
    Address="129", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T status")

    MdioRegister_302 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_302, \
    Address="130", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T pair swap and polarity")

    MdioRegister_303 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_303, \
    Address="131", \
    RegValue="0", \
    WritableMask="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T TX power backoff setting")

    MdioRegister_304 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_304, \
    Address="132", \
    RegValue="1024", \
    WritableMask="64512", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T test mode")

    MdioRegister_305 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_305, \
    Address="133", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel A")

    MdioRegister_306 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_306, \
    Address="134", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel B")

    MdioRegister_307 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_307, \
    Address="135", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel C")

    MdioRegister_308 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_308, \
    Address="136", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T SNR operating margin channel D")

    MdioRegister_309 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_309, \
    Address="137", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel A")

    MdioRegister_310 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_310, \
    Address="138", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel B")

    MdioRegister_311 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_311, \
    Address="139", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel C")

    MdioRegister_312 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_312, \
    Address="140", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T minimum margin channel D")

    MdioRegister_313 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_313, \
    Address="141", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel A")

    MdioRegister_314 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_314, \
    Address="142", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel B")

    MdioRegister_315 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_315, \
    Address="143", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel C")

    MdioRegister_316 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_316, \
    Address="144", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T RX signal power channel D")

    MdioRegister_317 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_317, \
    Address="145", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    MdioRegister_318 = (stc.get( ManagementDevice_11, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_318, \
    Address="146", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T skew delay")

    ManagementDevice_12 = (stc.get( MdioPort_3, 'children-ManagementDevice' )).split(' ')[1]
    stc.config(ManagementDevice_12, \
    Address="2", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS")

    MdioRegister_319 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_319, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS control 1")

    MdioRegister_320 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_320, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS status 1")

    MdioRegister_321 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_321, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_322 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_322, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS device identifier")

    MdioRegister_323 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_323, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS speed ability")

    MdioRegister_324 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_324, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_325 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_325, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS devices in package")

    MdioRegister_326 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_326, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS control 2")

    MdioRegister_327 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_327, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 2")

    MdioRegister_328 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_328, \
    Address="9", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS test pattern error counter")

    MdioRegister_329 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_329, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_330 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_330, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="WIS package identifier")

    MdioRegister_331 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_331, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS status 3")

    MdioRegister_332 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_332, \
    Address="37", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end path block error count")

    MdioRegister_333 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_333, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_334 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_334, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_335 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_335, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_336 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_336, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_337 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_337, \
    Address="43", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_338 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_338, \
    Address="44", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_339 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_339, \
    Address="45", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_340 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_340, \
    Address="46", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 transmit")

    MdioRegister_341 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_341, \
    Address="47", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_342 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_342, \
    Address="48", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_343 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_343, \
    Address="49", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_344 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[25]
    stc.config(MdioRegister_344, \
    Address="50", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_345 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[26]
    stc.config(MdioRegister_345, \
    Address="51", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_346 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[27]
    stc.config(MdioRegister_346, \
    Address="52", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_347 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[28]
    stc.config(MdioRegister_347, \
    Address="53", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_348 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[29]
    stc.config(MdioRegister_348, \
    Address="54", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J1 receive")

    MdioRegister_349 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[30]
    stc.config(MdioRegister_349, \
    Address="55", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_350 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[31]
    stc.config(MdioRegister_350, \
    Address="56", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS far end line BIP errors")

    MdioRegister_351 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[32]
    stc.config(MdioRegister_351, \
    Address="57", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_352 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[33]
    stc.config(MdioRegister_352, \
    Address="58", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS line BIP errors")

    MdioRegister_353 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[34]
    stc.config(MdioRegister_353, \
    Address="59", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS path block error count")

    MdioRegister_354 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[35]
    stc.config(MdioRegister_354, \
    Address="60", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS section BIP error count")

    MdioRegister_355 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[36]
    stc.config(MdioRegister_355, \
    Address="64", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_356 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[37]
    stc.config(MdioRegister_356, \
    Address="65", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_357 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[38]
    stc.config(MdioRegister_357, \
    Address="66", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_358 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[39]
    stc.config(MdioRegister_358, \
    Address="67", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_359 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[40]
    stc.config(MdioRegister_359, \
    Address="68", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_360 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[41]
    stc.config(MdioRegister_360, \
    Address="69", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_361 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[42]
    stc.config(MdioRegister_361, \
    Address="70", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_362 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[43]
    stc.config(MdioRegister_362, \
    Address="71", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 transmit")

    MdioRegister_363 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[44]
    stc.config(MdioRegister_363, \
    Address="72", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_364 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[45]
    stc.config(MdioRegister_364, \
    Address="73", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_365 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[46]
    stc.config(MdioRegister_365, \
    Address="74", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_366 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[47]
    stc.config(MdioRegister_366, \
    Address="75", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_367 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[48]
    stc.config(MdioRegister_367, \
    Address="76", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_368 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[49]
    stc.config(MdioRegister_368, \
    Address="77", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_369 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[50]
    stc.config(MdioRegister_369, \
    Address="78", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    MdioRegister_370 = (stc.get( ManagementDevice_12, 'children-MdioRegister' )).split(' ')[51]
    stc.config(MdioRegister_370, \
    Address="79", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G WIS J0 receive")

    ManagementDevice_13 = (stc.get( MdioPort_3, 'children-ManagementDevice' )).split(' ')[2]
    stc.config(ManagementDevice_13, \
    Address="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS")

    MdioRegister_371 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_371, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS control 1")

    MdioRegister_372 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_372, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS status 1")

    MdioRegister_373 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_373, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_374 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_374, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS device identifier")

    MdioRegister_375 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_375, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS speed ability")

    MdioRegister_376 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_376, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_377 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_377, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS devices in package")

    MdioRegister_378 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_378, \
    Address="7", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS control 2")

    MdioRegister_379 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_379, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PCS status 2")

    MdioRegister_380 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_380, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_381 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_381, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PCS package identifier")

    MdioRegister_382 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_382, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS status")

    MdioRegister_383 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_383, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-X PCS test control")

    MdioRegister_384 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_384, \
    Address="32", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 1")

    MdioRegister_385 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_385, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS status 2")

    MdioRegister_386 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_386, \
    Address="34", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_387 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_387, \
    Address="35", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_388 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_388, \
    Address="36", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_389 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_389, \
    Address="37", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed A")

    MdioRegister_390 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_390, \
    Address="38", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_391 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_391, \
    Address="39", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_392 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_392, \
    Address="40", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_393 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[22]
    stc.config(MdioRegister_393, \
    Address="41", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern seed B")

    MdioRegister_394 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[23]
    stc.config(MdioRegister_394, \
    Address="42", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern control")

    MdioRegister_395 = (stc.get( ManagementDevice_13, 'children-MdioRegister' )).split(' ')[24]
    stc.config(MdioRegister_395, \
    Address="43", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-R PCS test pattern error counter")

    ManagementDevice_14 = (stc.get( MdioPort_3, 'children-ManagementDevice' )).split(' ')[3]
    stc.config(ManagementDevice_14, \
    Address="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS")

    MdioRegister_396 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_396, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS control 1")

    MdioRegister_397 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_397, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 1")

    MdioRegister_398 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_398, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_399 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_399, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS device identifier")

    MdioRegister_400 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_400, \
    Address="4", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS speed ability")

    MdioRegister_401 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_401, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_402 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_402, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS devices in package")

    MdioRegister_403 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_403, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS status 2")

    MdioRegister_404 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_404, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_405 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_405, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY XS package identifier")

    MdioRegister_406 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_406, \
    Address="24", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS lane status")

    MdioRegister_407 = (stc.get( ManagementDevice_14, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_407, \
    Address="25", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10G PHY XGXS test control")

    ManagementDevice_15 = (stc.get( MdioPort_3, 'children-ManagementDevice' )).split(' ')[4]
    stc.config(ManagementDevice_15, \
    Address="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto Negotiation")

    MdioRegister_408 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[0]
    stc.config(MdioRegister_408, \
    Address="0", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN control")

    MdioRegister_409 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[1]
    stc.config(MdioRegister_409, \
    Address="1", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN status")

    MdioRegister_410 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[2]
    stc.config(MdioRegister_410, \
    Address="2", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_411 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[3]
    stc.config(MdioRegister_411, \
    Address="3", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN device identifier")

    MdioRegister_412 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[4]
    stc.config(MdioRegister_412, \
    Address="5", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_413 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[5]
    stc.config(MdioRegister_413, \
    Address="6", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN devices in package")

    MdioRegister_414 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[6]
    stc.config(MdioRegister_414, \
    Address="14", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_415 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[7]
    stc.config(MdioRegister_415, \
    Address="15", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN package identifier")

    MdioRegister_416 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[8]
    stc.config(MdioRegister_416, \
    Address="16", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_417 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[9]
    stc.config(MdioRegister_417, \
    Address="17", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_418 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[10]
    stc.config(MdioRegister_418, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN advertisement")

    MdioRegister_419 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[11]
    stc.config(MdioRegister_419, \
    Address="19", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_420 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[12]
    stc.config(MdioRegister_420, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_421 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[13]
    stc.config(MdioRegister_421, \
    Address="21", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP base page ability")

    MdioRegister_422 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[14]
    stc.config(MdioRegister_422, \
    Address="22", \
    RegValue="0", \
    WritableMask="63487", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_423 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[15]
    stc.config(MdioRegister_423, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_424 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[16]
    stc.config(MdioRegister_424, \
    Address="24", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN XNP transmit")

    MdioRegister_425 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[17]
    stc.config(MdioRegister_425, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_426 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[18]
    stc.config(MdioRegister_426, \
    Address="26", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_427 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[19]
    stc.config(MdioRegister_427, \
    Address="27", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AN LP XNP ability")

    MdioRegister_428 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[20]
    stc.config(MdioRegister_428, \
    Address="32", \
    RegValue="0", \
    WritableMask="61447", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN control")

    MdioRegister_429 = (stc.get( ManagementDevice_15, 'children-MdioRegister' )).split(' ')[21]
    stc.config(MdioRegister_429, \
    Address="33", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="10GBASE-T AN status")

    StreamBlock_4 = stc.create("StreamBlock",under = Port_3, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1024", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Vxlan,Ancp,PppProtocol,PppoeProtocol,Openflow Protocol,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,AUTOSARTIMESYNC Protocol,CP traffic,Coap Protocol,OAM Protocol,Packet Channel,Dhcpv4,SyncE,Dhcpv6,IgmpMld,Cusp,AppPerf,Cifs,Iperf,Http,Ntp,RawTcp,Dpg,Sip,Video,CSMP,XMPPvJ,Ftp,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_10078\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>57325</checksum><sourceAddr>192.168.0.179</sourceAddr><destAddr>10.43.36.2</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>192.168.0.1</gateway><tosDiffserv name=\"anon_8628\"><tos name=\"anon_8629\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 14-5-1")

    EmulatedDeviceGenParams_1 = stc.create("EmulatedDeviceGenParams",under = Project_1, \
    BlockMode="ONE_NETWORK_PER_BLOCK", \
    RouterId="192.0.0.5", \
    RouterIdStep="0.0.0.1", \
    RouterIdSrc="MANUAL", \
    Ipv6RouterId="2000::5", \
    Ipv6RouterIdStep="::1", \
    Ipv6RouterIdSrc="MANUAL", \
    Role="", \
    DeviceTags="", \
    DuplicateNameResolution="SKIP_BLOCK_INDEX", \
    DeviceName="Device $(BlockIndex)", \
    BlockIndex="1", \
    PortType="ETHERNET", \
    Count="1", \
    CountBlockPerPort="1", \
    CountPerBlock="1", \
    GroupAssignmentMode="GROUPS_PER_PORT", \
    StepOrder="", \
    PreviewMaxCount="1000", \
    PreviewMode="FULL", \
    PreviewMaxCountPerIncrementLevel="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EmulatedDeviceGenParams 1")

    DeviceGenIpv4IfParams_1 = stc.create("DeviceGenIpv4IfParams",under = EmulatedDeviceGenParams_1, \
    PrefixLength="24", \
    Addr="192.85.1.7", \
    AddrStep="0.0.0.1", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    TosType="TOS", \
    Tos="192", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenIpv4IfParams 1")

    DeviceGenLinkedStep_1 = stc.create("DeviceGenLinkedStep",under = DeviceGenIpv4IfParams_1, \
    PropertyId="Addr", \
    LinkToId="port", \
    Step="1.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenLinkedStep 1")

    DeviceGenLinkedStep_2 = stc.create("DeviceGenLinkedStep",under = DeviceGenIpv4IfParams_1, \
    PropertyId="Gateway", \
    LinkToId="port", \
    Step="1.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenLinkedStep 3")

    DeviceGenEthIIIfParams_1 = stc.create("DeviceGenEthIIIfParams",under = EmulatedDeviceGenParams_1, \
    SrcMac="00:10:94:00:00:05", \
    SrcMacStep="00:00:00:00:00:01", \
    UseDefaultPhyMac="TRUE", \
    EnableRfc4814Addresses="FALSE", \
    RandomSeedValue="4814", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenEthIIIfParams 1")

    Dhcpv4DeviceGenProtocolParams_1 = stc.create("Dhcpv4DeviceGenProtocolParams",under = EmulatedDeviceGenParams_1, \
    HostName="client_@p-@b-@s", \
    EnableRouterOption="FALSE", \
    EnableAutoRetry="FALSE", \
    RetryAttempts="4", \
    OptionList="1 6 15 33 44", \
    EnableRelayAgent="FALSE", \
    UseGatewayAsRelayServerIpv4Addr="TRUE", \
    RelayServerIpv4Addr="0.0.0.0", \
    RelayServerIpv4AddrStep="0.0.0.1", \
    RelayPoolIpv4Addr="0.0.0.0", \
    RelayPoolIpv4AddrStep="0.0.1.0", \
    EnableCircuitId="FALSE", \
    CircuitId="circuitId_@p", \
    EnableRemoteId="FALSE", \
    RemoteId="remoteId_@p-@b-@s", \
    ClientsPerRelayAgent="1", \
    RelayClientMacAddrStart="00:10:01:00:00:01", \
    RelayClientMacAddrStep="00:00:00:00:00:01", \
    RelayClientMacAddrMask="00:00:00:ff:ff:ff", \
    EnableRelayServerIdOverride="FALSE", \
    RelayServerIdOverride="192.85.1.1", \
    EnableRelayLinkSelection="FALSE", \
    RelayLinkSelection="192.85.1.1", \
    EnableRelayVPNID="FALSE", \
    VPNType="NVT_ASCII", \
    VPNId="spirent_@p", \
    ExportAddrToLinkedClients="FALSE", \
    UseClientMacAddrForDataplane="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4DeviceGenProtocolParams 1")

    EmulatedDevice_3 = stc.create("EmulatedDevice",under = Project_1, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.4", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::4", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Device 2")

    Ipv4If_6 = stc.create("Ipv4If",under = EmulatedDevice_3, \
    Address="192.168.0.179", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="192.168.0.179", \
    AddrRepeatCount="0", \
    AddrResolver="Dhcpv4", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.168.0.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="192.168.0.1", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="02:10:18:49:25:b6", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="FALSE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 6")

    EthIIIf_6 = stc.create("EthIIIf",under = EmulatedDevice_3, \
    SourceMac="00:10:94:00:00:04", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="TRUE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 6")

    Dhcpv4BlockConfig_2 = stc.create("Dhcpv4BlockConfig",under = EmulatedDevice_3, \
    HostName="client_@p-@b-@s", \
    DefaultHostAddrPrefixLength="24", \
    OptionList="1 6 15 33 44", \
    EnableRouterOption="FALSE", \
    EnableArpServerId="FALSE", \
    UseBroadcastFlag="TRUE", \
    EnableRelayAgent="FALSE", \
    ClientRelayAgent="FALSE", \
    RelayAgentIpv4AddrMask="255.255.0.0", \
    RelayAgentIpv4Addr="192.85.1.6", \
    RelayAgentIpv4AddrStep="0.0.0.1", \
    RelayServerIpv4Addr="0.0.0.0", \
    RelayServerIpv4AddrStep="0.0.0.0", \
    RelayPoolIpv4Addr="0.0.0.0", \
    RelayPoolIpv4AddrStep="0.0.1.0", \
    EnableCircuitId="FALSE", \
    CircuitId="circuitId_@p", \
    EnableRemoteId="FALSE", \
    RemoteId="remoteId_@p-@b-@s", \
    RelayClientMacAddrStart="00:10:01:00:00:01", \
    RelayClientMacAddrStep="00:00:00:00:00:01", \
    RelayClientMacAddrMask="00:00:00:ff:ff:ff", \
    EnableRelayServerIdOverride="FALSE", \
    RelayServerIdOverride="192.85.1.1", \
    EnableRelayLinkSelection="FALSE", \
    RelayLinkSelection="192.85.1.1", \
    EnableRelayVPNID="FALSE", \
    VPNType="NVT_ASCII", \
    VPNId="spirent_@p", \
    EnableSessionAutoRetry="FALSE", \
    EnableAutoRetry="FALSE", \
    RetryAttempts="4", \
    ExportAddrToLinkedClients="FALSE", \
    UseClientMacAddrForDataplane="FALSE", \
    Ipv4Tos="192", \
    DNAv4DestIp="192.85.1.1", \
    DNAv4DestMac="00:10:01:00:00:01", \
    EnableGarp="FALSE", \
    GarpTransmits="1", \
    GarpTimeout="1", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DHCP 2")

    StreamBlockLoadProfile_1 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="MEGABITS_PER_SECOND", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 21")

    StreamBlockLoadProfile_2 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="MEGABITS_PER_SECOND", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 22")

    StreamBlockLoadProfile_3 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="MEGABITS_PER_SECOND", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 23")

    StreamBlockLoadProfile_4 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="MEGABITS_PER_SECOND", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 24")

    ResultDataSet_4 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 439")

    ResultQuery_6 = stc.create("ResultQuery",under = ResultDataSet_4, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 544")

    ResultDataSet_5 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 441")

    ResultQuery_7 = stc.create("ResultQuery",under = ResultDataSet_5, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 547")

    ResultDataSet_6 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 443")

    ResultQuery_8 = stc.create("ResultQuery",under = ResultDataSet_6, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 550")

    ResultDataSet_7 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 445")

    ResultQuery_9 = stc.create("ResultQuery",under = ResultDataSet_7, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 553")

    ResultDataSet_8 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 447")

    ResultQuery_10 = stc.create("ResultQuery",under = ResultDataSet_8, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 556")

    ResultDataSet_9 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 441")

    ResultQuery_11 = stc.create("ResultQuery",under = ResultDataSet_9, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="RecordsPerPage:1,PageNumber:1,NotifyInterval:1000,", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 548")

    ResultDataSet_10 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 445")

    ResultQuery_12 = stc.create("ResultQuery",under = ResultDataSet_10, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="RecordsPerPage:1,PageNumber:1,NotifyInterval:1000,", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 554")

    ResultDataSet_11 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 447")

    ResultQuery_13 = stc.create("ResultQuery",under = ResultDataSet_11, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="RecordsPerPage:1,PageNumber:1,NotifyInterval:1000,", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 557")

    ResultDataSet_12 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="StreamBlock", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="1", \
    NotifyInterval="1000", \
    Identifier="", \
    Persistent="TRUE", \
    CreatorId="VerifyResultsValueCommand", \
    IsDeprecated="FALSE", \
    Path="", \
    ResultViewOwner="SYSTEM", \
    Description="", \
    CustomDisplayName="", \
    CustomDisplayPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultDataSet 443")

    ResultQuery_14 = stc.create("ResultQuery",under = ResultDataSet_12, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.droppedframepercent", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="RecordsPerPage:1,PageNumber:1,NotifyInterval:1000,", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 551")

    DynamicResultView_2 = stc.create("DynamicResultView",under = Project_1, \
    ResultSourceClass="Project", \
    SaveToConfig="TRUE", \
    Identifier="Port Traffic\\Summarized Basic Traffic Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/DynamicResultView", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Summarized Basic Traffic Results")

    PresentationResultQuery_2 = stc.create("PresentationResultQuery",under = DynamicResultView_2, \
    SelectProperties="Project.Name Port.Name Port.GeneratorSigFrameCount Port.RxSigFrameCount Port.TxL1BitRate Port.RxL1BitRate Port.MinLatency Port.MaxLatency Port.AvgLatency", \
    WhereConditions="", \
    GroupByProperties="Project.Name", \
    LimitOffset="0", \
    LimitSize="2000", \
    SortBy="", \
    ArchivingOption="NONE", \
    ResultState="AVAILABLE", \
    ArchivingInterval="10", \
    DatabaseFileName="", \
    DisableAutoGrouping="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PresentationResultQuery 3")

    ColumnDisplayProperties_4 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Project.Name", \
    ColumnCaption="Project Name", \
    ColumnWidth="0", \
    ColumnUnits="0", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 9")

    ColumnDisplayProperties_5 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.GeneratorSigFrameCount", \
    ColumnCaption="Generator Sig Count", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 10")

    ColumnDisplayProperties_6 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.RxSigFrameCount", \
    ColumnCaption="Rx Sig Count", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 11")

    ColumnDisplayProperties_7 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.TxL1BitRate", \
    ColumnCaption="Tx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 12")

    ColumnDisplayProperties_8 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.RxL1BitRate", \
    ColumnCaption="Rx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 13")

    ColumnDisplayProperties_9 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.MinLatency", \
    ColumnCaption="Min Latency", \
    ColumnWidth="0", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 14")

    ColumnDisplayProperties_10 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.MaxLatency", \
    ColumnCaption="Max Latency", \
    ColumnWidth="0", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 15")

    ColumnDisplayProperties_11 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.AvgLatency", \
    ColumnCaption="Avg Latency", \
    ColumnWidth="0", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 16")

    ColumnDisplayProperties_12 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.Name", \
    ColumnCaption="Port Name", \
    ColumnWidth="0", \
    ColumnUnits="0", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 17")

    AutomationOptions_1 = (stc.get( system1, 'children-AutomationOptions' )).split(' ')[0]
    stc.config(AutomationOptions_1, \
    CommandTimeout="3600", \
    LogLevel="WARN", \
    LogTo="stdout", \
    MaxBackup="0", \
    MaxFileSizeInMB="10", \
    SuppressTclErrors="FALSE", \
    AutoSubscribe="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutomationOptions 1")

    PhysicalChassisManager_1 = stc.create("PhysicalChassisManager",under = system1, \
    RawImageArchiveDir="", \
    FirmwareArchiveDir="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhysicalChassisManager 1")

    Sequencer_1 = stc.create("Sequencer",under = system1, \
    CurrentSubCommandName="TX S9P11 RX S9P1 Dropped Frame Percent Check", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Sequencer")

    SequencerIfCommand_1 = stc.create("SequencerIfCommand",under = Sequencer_1, \
    Condition="PASSED", \
    ExecutionMode="BACKGROUND", \
    GroupCategory="REGULAR_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="If")

    print("Verifying the ports links are up")
    PhyVerifyLinkUpCommand_1 = stc.create("PhyVerifyLinkUpCommand",under = Sequencer_1, \
    ErrorOnFailure="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Verify Link Status 1")

    SequencerIfCommand_2 = stc.create("SequencerIfCommand",under = Sequencer_1, \
    Condition="FAILED", \
    ExecutionMode="BACKGROUND", \
    GroupCategory="REGULAR_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="If")

    PhyVerifyLinkUpCommand_2 = stc.create("PhyVerifyLinkUpCommand",under = SequencerIfCommand_2, \
    ErrorOnFailure="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Basic: Verify Link Status")

    SequencerStopCommand_1 = stc.create("SequencerStopCommand",under = SequencerIfCommand_2, \
    SequencerTestState="CHANGE_TO_FAILED", \
    StoppedReason="ERROR: Port links are not up", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Command Sequencer 1")
    print("Ports links are up\n")

    print("Starting all devices\n")
    DevicesStartAllCommand_1 = stc.create("DevicesStartAllCommand",under = Sequencer_1, \
    ProtocolStartOrder="START_PROTOCOLS_SERIALLY", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start All Devices 3")

    WaitCommand_1 = stc.create("WaitCommand",under = Sequencer_1, \
    WaitTime="5", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Wait 1")

    print("ARPing all ports\n")
    ArpNdStartOnAllDevicesCommand_1 = stc.create("ArpNdStartOnAllDevicesCommand",under = Sequencer_1, \
    WaitForArpToFinish="TRUE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Learning: Start ArpNd On All Devices 1")

    WaitCommand_2 = stc.create("WaitCommand",under = Sequencer_1, \
    WaitTime="5", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Wait 1")

    ArpNdVerifyResolvedCommand_1 = stc.create("ArpNdVerifyResolvedCommand",under = Sequencer_1, \
    ErrorOnFailure="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Learning: Verify ArpNd Status 1")

    SequencerIfCommand_3 = stc.create("SequencerIfCommand",under = Sequencer_1, \
    Condition="FAILED", \
    ExecutionMode="BACKGROUND", \
    GroupCategory="REGULAR_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="If")

    ArpNdVerifyResolvedCommand_2 = stc.create("ArpNdVerifyResolvedCommand",under = SequencerIfCommand_3, \
    ErrorOnFailure="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Learning: Verify ArpNd Status")

    SequencerStopCommand_2 = stc.create("SequencerStopCommand",under = SequencerIfCommand_3, \
    SequencerTestState="CHANGE_TO_FAILED", \
    StoppedReason="ERROR: ARPs failed", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Command Sequencer 3")

    print("Priming the pump (Sending packets upstream)\n")
    StreamBlockStartCommand_1 = stc.create("StreamBlockStartCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Prime the Pump (Start StreamBlocks 1)")

    WaitCommand_3 = stc.create("WaitCommand",under = Sequencer_1, \
    WaitTime="5", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Wait 1")

    StreamBlockStopCommand_1 = stc.create("StreamBlockStopCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop StreamBlocks 1")

    ResultsClearAllCommand_1 = stc.create("ResultsClearAllCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Clear All Results 1")

    WaitCommand_4 = stc.create("WaitCommand",under = Sequencer_1, \
    WaitTime="10", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Wait 1")

    print("Starting the WAN-to-LAN and LAN-to-WAN traffic\n")
    StreamBlockStartCommand_2 = stc.create("StreamBlockStartCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BiDirectional Testing (Start StreamBlocks 7)")

    AnalyzerStartCommand_1 = stc.create("AnalyzerStartCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Analyzer 2")

    print("Running test for 10 minutes")
#    print("Running test for 60 seconds")
    print(datetime.datetime.now())
    WaitCommand_5 = stc.create("WaitCommand",under = Sequencer_1, \
    WaitTime="600", \
#    WaitTime="60", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Pass Traffic for 10 minutes")

    StreamBlockStopCommand_2 = stc.create("StreamBlockStopCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop StreamBlocks 1")

    AnalyzerStopCommand_1 = stc.create("AnalyzerStopCommand",under = Sequencer_1, \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Analyzer 2")

    EOTResultsWriteIterationCommand_1 = stc.create("EOTResultsWriteIterationCommand",under = Sequencer_1, \
    EnableDetailedResultsCollection="TRUE", \
    SaveTrafficResults="TRUE", \
    TestType="Standalone", \
    DurationSeconds="0", \
    IsThroughputTest="FALSE", \
    IsStepTest="FALSE", \
    EnableOOSasFrameloss="TRUE", \
    EnableSavePortPairLatencyResults="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Save Iteration Results 1")

    SaveResultsCommand_1 = stc.create("SaveResultsCommand",under = Sequencer_1, \
    ResultFileName="BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12.db", \
    SaveDetailedResults="TRUE", \
    ClearChartResultAfterSave="TRUE", \
    CollectResult="TRUE", \
    LoopMode="APPEND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Save Results 1")

    VerifyResultsValueCommand_1 = stc.create("VerifyResultsValueCommand",under = Sequencer_1, \
    WaitTimeout="1", \
    InvertComparison="FALSE", \
    ErrorOnFailure="TRUE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TX S9P12 RX S9P1 Dropped Frame Percent Check")

    VerifyResultsValueCondition_1 = stc.create("VerifyResultsValueCondition",under = VerifyResultsValueCommand_1, \
    IsSpecialCondition="TRUE", \
    PropertyOperand="DroppedFramePercent", \
    ValueOperand="0.5", \
    ComparisonOperator="LESS_THAN_OR_EQUAL", \
    MinValueOperand="0.5", \
    MaxValueOperand="0.5", \
    BooleanOperator="AND", \
    InvertComparison="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VerifyResultsValueCondition 7")

    VerifyResultsValueCommand_2 = stc.create("VerifyResultsValueCommand",under = Sequencer_1, \
    WaitTimeout="0", \
    InvertComparison="FALSE", \
    ErrorOnFailure="FALSE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TX S9P1 RX S9P11 Dropped Frame Percent Check")

    VerifyResultsValueCondition_2 = stc.create("VerifyResultsValueCondition",under = VerifyResultsValueCommand_2, \
    IsSpecialCondition="TRUE", \
    PropertyOperand="DroppedFramePercent", \
    ValueOperand="0.5", \
    ComparisonOperator="LESS_THAN_OR_EQUAL", \
    MinValueOperand="0.5", \
    MaxValueOperand="0.5", \
    BooleanOperator="AND", \
    InvertComparison="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VerifyResultsValueCondition 9")

    VerifyResultsValueCommand_3 = stc.create("VerifyResultsValueCommand",under = Sequencer_1, \
    WaitTimeout="0", \
    InvertComparison="FALSE", \
    ErrorOnFailure="TRUE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TX S9P1 RX S9P12 Dropped Frame Percent Check")

    VerifyResultsValueCondition_3 = stc.create("VerifyResultsValueCondition",under = VerifyResultsValueCommand_3, \
    IsSpecialCondition="TRUE", \
    PropertyOperand="DroppedFramePercent", \
    ValueOperand="0.5", \
    ComparisonOperator="LESS_THAN_OR_EQUAL", \
    MinValueOperand="0.5", \
    MaxValueOperand="0.5", \
    BooleanOperator="AND", \
    InvertComparison="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VerifyResultsValueCondition 11")

    VerifyResultsValueCommand_4 = stc.create("VerifyResultsValueCommand",under = Sequencer_1, \
    WaitTimeout="0", \
    InvertComparison="FALSE", \
    ErrorOnFailure="TRUE", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TX S9P11 RX S9P1 Dropped Frame Percent Check")

    VerifyResultsValueCondition_4 = stc.create("VerifyResultsValueCondition",under = VerifyResultsValueCommand_4, \
    IsSpecialCondition="TRUE", \
    PropertyOperand="DroppedFramePercent", \
    ValueOperand="0.5", \
    ComparisonOperator="LESS_THAN_OR_EQUAL", \
    MinValueOperand="0.5", \
    MaxValueOperand="0.5", \
    BooleanOperator="AND", \
    InvertComparison="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VerifyResultsValueCondition 13")

    IfManager_1 = stc.create("IfManager",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IfManager 1")

    LinkRegistry_1 = stc.create("LinkRegistry",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LinkRegistry 1")

    FeatureSupportedVersion_1 = (stc.get( system1, 'children-FeatureSupportedVersion' )).split(' ')[0]
    stc.config(FeatureSupportedVersion_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FeatureSupportedVersion 1")

    ActiveEventManager_1 = (stc.get( system1, 'children-ActiveEventManager' )).split(' ')[0]
    stc.config(ActiveEventManager_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ActiveEventManager 1")

    SequencerGroupCommand_1 = stc.create("SequencerGroupCommand",under = system1, \
    ExecutionMode="BACKGROUND", \
    GroupCategory="CLEANUP_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Cleanup Commands")

    spirent_results_EnhancedResultsSelectorProfile_1 = stc.create("spirent.results.EnhancedResultsSelectorProfile",under = system1, \
    SubscribeType="SELECTED", \
    ConfigSubscribeType="SELECTED", \
    EnableLiveDataRetention="TRUE", \
    LiveDataRetentionInterval="15", \
    StorageLimitInKB="-1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsSelectorProfile 1")

    spirent_results_EnhancedResultsGroupFilter_1 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="autosartimesync_can_stats", \
    LiveFacts="state rx_bad_crc_count rx_follow_up_count rx_lost_follow_up_count rx_lost_sync_count rx_ovs rx_sgw rx_sync_count rx_avg_time_between_syncs rx_current_time_between_syncs_and_followup rx_current_time_between_sync rx_long_avg_time_between_syncs rx_max_time_between_syncs rx_min_time_between_syncs rx_short_avg_time_between_syncs rx_time_domain time_of_day time_of_day_seconds tx_follow_up_count tx_sync_count rx_ovs_set_count rx_sgw_bit_count rx_avg_time_between_syncs_and_followup rx_max_time_between_syncs_and_followup rx_min_time_between_syncs_and_followup rx_invalid_follow_up_count rx_invalid_sync_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 10")

    spirent_results_EnhancedResultsGroupFilter_2 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_afi_safi_stats", \
    LiveFacts="rx_advertised_route_count rx_withdrawn_route_count session_count tx_advertised_route_count tx_withdrawn_route_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 11")

    spirent_results_EnhancedResultsGroupFilter_3 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_ls_scale_stats", \
    LiveFacts="tx_advertised_ls_scale_link_route_count tx_advertised_ls_scale_node_route_count tx_advertised_ls_scale_prefix_ipv4_route_count tx_withdrawn_ls_scale_node_route_count tx_withdrawn_ls_scale_link_route_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 12")

    spirent_results_EnhancedResultsGroupFilter_4 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_session_stats", \
    LiveFacts="last_rx_update_route_count outstanding_route_count state rx_advertised_evpn_ad_route_count rx_advertised_evpn_eth_segment_route_count rx_advertised_evpn_mcast_route_count rx_advertised_evpn_ip_prefix_route_count rx_advertised_evpn_join_synch_route_count rx_advertised_evpn_leave_synch_route_count rx_advertised_evpn_mac_route_count rx_advertised_evpn_selective_mcast_route_count rx_advertised_route_count rx_advertised_update_count rx_keepalive_count rx_notification_count rx_notify_code rx_notify_sub_code rx_open_count rx_route_refresh_count rx_rt_constraint_count rx_withdrawn_evpn_ad_route_count rx_withdrawn_evpn_eth_segment_route_count rx_withdrawn_evpn_mcast_route_count rx_withdrawn_evpn_ip_prefix_route_count rx_withdrawn_evpn_join_synch_route_count rx_withdrawn_evpn_leave_synch_route_count rx_withdrawn_evpn_mac_route_count rx_withdrawn_evpn_selective_mcast_route_count rx_withdrawn_route_count session_up_count tx_advertised_evpn_ad_route_count tx_advertised_evpn_eth_segment_route_count tx_advertised_evpn_mcast_route_count tx_advertised_evpn_ip_prefix_route_count tx_advertised_evpn_join_synch_route_count tx_advertised_evpn_leave_synch_route_count tx_advertised_evpn_mac_route_count tx_advertised_evpn_selective_mcast_route_count tx_advertised_route_count tx_advertised_update_count tx_keepalive_count tx_notification_count tx_notify_code tx_notify_sub_code tx_open_count tx_route_refresh_count tx_rt_constraint_count tx_withdrawn_evpn_ad_route_count tx_withdrawn_evpn_eth_segment_route_count tx_withdrawn_evpn_mcast_route_count tx_withdrawn_evpn_ip_prefix_route_count tx_withdrawn_evpn_join_synch_route_count tx_withdrawn_evpn_leave_synch_route_count tx_withdrawn_evpn_mac_route_count tx_withdrawn_evpn_selective_mcast_route_count tx_withdrawn_route_count tx_withdrawn_update_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 13")

    spirent_results_EnhancedResultsGroupFilter_5 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="dhcpv4_block_stats", \
    LiveFacts="currently_engaged currently_bound currently_idle state total_bound total_failed total_renewed ack_rx decline_tx discover_tx dna_failed_tx dna_reply_rx dna_req_tx dna_retry_tx force_renew_rx garp_rx garp_tx reboot_tx nak_rx offer_rx rebind_tx release_tx renew_tx request_retry_tx request_tx total_discover_retry_tx attempt_rate bind_rate connect_start_time current_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 14")

    spirent_results_EnhancedResultsGroupFilter_6 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="dhcpv6_block_stats", \
    LiveFacts="currently_engaged currently_bound currently_idle state total_bound total_declined total_failed total_rebound total_released total_renewed pd_state advertise_rx confirm_tx decline_tx info_request_tx rebind_tx release_tx renew_tx request_tx solicit_tx total_release_retry_tx total_renew_retry_tx total_solicit_retry_tx reconfigure_rx reply_rx attempt_rate bind_rate rebind_rate release_rate renew_rate connect_start_time current_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 15")

    spirent_results_EnhancedResultsGroupFilter_7 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ecpri_device_stats", \
    LiveFacts="state rx_followup_count rx_remote_request_count rx_remote_request_with_fu_count rx_request_count rx_request_with_fu_count rx_response_count tx_followup_count tx_remote_request_count tx_remote_request_with_fu_count tx_request_count tx_request_with_fu_count tx_response_count rx_remote_reset_request_count rx_remote_reset_response_count tx_remote_reset_request_count tx_remote_reset_response_count rx_type4_failure_read_response_count rx_type4_failure_write_response_count rx_type4_partial_read_response_count rx_type4_partial_write_response_count rx_type4_read_request_count rx_type4_read_response_count rx_type4_write_no_response_count rx_type4_write_request_count rx_type4_write_response_count tx_type4_failure_read_response_count tx_type4_failure_write_response_count tx_type4_partial_read_response_count tx_type4_partial_write_response_count tx_type4_read_request_count tx_type4_read_response_count tx_type4_write_no_response_count tx_type4_write_request_count tx_type4_write_response_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 16")

    spirent_results_EnhancedResultsGroupFilter_8 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee1588v2_clock_stats", \
    LiveFacts="clock_domain clock_state port_number rx_announce_count rx_delay_request_count rx_delay_response_count rx_follow_up_count rx_peer_delay_request_count rx_peer_delay_response_count rx_peer_delay_response_follow_up_count rx_signaling_count rx_sync_count tx_announce_count tx_delay_request_count tx_delay_response_count tx_follow_up_count tx_peer_delay_request_count tx_peer_delay_response_count tx_peer_delay_response_follow_up_count tx_signaling_count tx_sync_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 17")

    spirent_results_EnhancedResultsGroupFilter_9 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee1588v2_clock_sync_stats", \
    LiveFacts="follow_up_correction_field pdelay_response_correction_field pdelay_response_followup_correction_field sync_correction_field invalid_timestamp_count average_mean_path_delay current_mean_path_delay max_mean_path_delay min_mean_path_delay peer_mean_path_delay log_min_delay_request_interval step_removed average_offset_minus_deviation average_offset_plus_deviation current_offset negative_offset_peak offset_deviation offset_standard_deviation positive_offset_peak t1_in_nano_seconds t2_in_nano_seconds t3_in_nano_seconds t4_in_nano_seconds time_of_day time_of_day_in_nano_seconds", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 18")

    spirent_results_EnhancedResultsGroupFilter_10 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_client_stats", \
    LiveFacts="authentication_type channel_number channel_width state reason_code ft_ave_delay ft_delay ft_fail ft_max_delay ft_min_delay ft_success ft_type freq_band group_id wlan_mode mfp_status mimo_mode noise_floor rx_guard_interval rx_mcs_type rx_nss rx_rate signal_strength startup_time sta_state sumu tdls_peer_status time_in_association rx_bytes rx_packets tx_bytes tx_packets guard_interval mcs_type tx_nss tx_rate wmm_status per_chn_width_rx_pkts_3 per_chn_width_rx_pkts_0 per_chn_width_rx_pkts_1 per_chn_width_rx_pkts_2 per_chn_width_tx_pkts_3 per_chn_width_tx_pkts_0 per_chn_width_tx_pkts_1 per_chn_width_tx_pkts_2 per_gi_rx_pkts_1600ns_0 per_gi_rx_pkts_1600ns_1 per_gi_rx_pkts_1600ns_10 per_gi_rx_pkts_1600ns_11 per_gi_rx_pkts_1600ns_2 per_gi_rx_pkts_1600ns_3 per_gi_rx_pkts_1600ns_4 per_gi_rx_pkts_1600ns_5 per_gi_rx_pkts_1600ns_6 per_gi_rx_pkts_1600ns_7 per_gi_rx_pkts_1600ns_8 per_gi_rx_pkts_1600ns_9 per_gi_rx_pkts_3200ns_0 per_gi_rx_pkts_3200ns_1 per_gi_rx_pkts_3200ns_10 per_gi_rx_pkts_3200ns_11 per_gi_rx_pkts_3200ns_2 per_gi_rx_pkts_3200ns_3 per_gi_rx_pkts_3200ns_4 per_gi_rx_pkts_3200ns_5 per_gi_rx_pkts_3200ns_6 per_gi_rx_pkts_3200ns_7 per_gi_rx_pkts_3200ns_8 per_gi_rx_pkts_3200ns_9 per_gi_rx_pkts_400ns_0 per_gi_rx_pkts_400ns_1 per_gi_rx_pkts_400ns_10 per_gi_rx_pkts_400ns_11 per_gi_rx_pkts_400ns_2 per_gi_rx_pkts_400ns_3 per_gi_rx_pkts_400ns_4 per_gi_rx_pkts_400ns_5 per_gi_rx_pkts_400ns_6 per_gi_rx_pkts_400ns_7 per_gi_rx_pkts_400ns_8 per_gi_rx_pkts_400ns_9 per_gi_rx_pkts_800ns_0 per_gi_rx_pkts_800ns_1 per_gi_rx_pkts_800ns_10 per_gi_rx_pkts_800ns_11 per_gi_rx_pkts_800ns_2 per_gi_rx_pkts_800ns_3 per_gi_rx_pkts_800ns_4 per_gi_rx_pkts_800ns_5 per_gi_rx_pkts_800ns_6 per_gi_rx_pkts_800ns_7 per_gi_rx_pkts_800ns_8 per_gi_rx_pkts_800ns_9 per_gi_tx_pkts_1600ns_0 per_gi_tx_pkts_1600ns_1 per_gi_tx_pkts_1600ns_10 per_gi_tx_pkts_1600ns_11 per_gi_tx_pkts_1600ns_2 per_gi_tx_pkts_1600ns_3 per_gi_tx_pkts_1600ns_4 per_gi_tx_pkts_1600ns_5 per_gi_tx_pkts_1600ns_6 per_gi_tx_pkts_1600ns_7 per_gi_tx_pkts_1600ns_8 per_gi_tx_pkts_1600ns_9 per_gi_tx_pkts_3200ns_0 per_gi_tx_pkts_3200ns_1 per_gi_tx_pkts_3200ns_10 per_gi_tx_pkts_3200ns_11 per_gi_tx_pkts_3200ns_2 per_gi_tx_pkts_3200ns_3 per_gi_tx_pkts_3200ns_4 per_gi_tx_pkts_3200ns_5 per_gi_tx_pkts_3200ns_6 per_gi_tx_pkts_3200ns_7 per_gi_tx_pkts_3200ns_8 per_gi_tx_pkts_3200ns_9 per_gi_tx_pkts_400ns_0 per_gi_tx_pkts_400ns_1 per_gi_tx_pkts_400ns_10 per_gi_tx_pkts_400ns_11 per_gi_tx_pkts_400ns_2 per_gi_tx_pkts_400ns_3 per_gi_tx_pkts_400ns_4 per_gi_tx_pkts_400ns_5 per_gi_tx_pkts_400ns_6 per_gi_tx_pkts_400ns_7 per_gi_tx_pkts_400ns_8 per_gi_tx_pkts_400ns_9 per_gi_tx_pkts_800ns_0 per_gi_tx_pkts_800ns_1 per_gi_tx_pkts_800ns_10 per_gi_tx_pkts_800ns_11 per_gi_tx_pkts_800ns_2 per_gi_tx_pkts_800ns_3 per_gi_tx_pkts_800ns_4 per_gi_tx_pkts_800ns_5 per_gi_tx_pkts_800ns_6 per_gi_tx_pkts_800ns_7 per_gi_tx_pkts_800ns_8 per_gi_tx_pkts_800ns_9 per_mcs_rx_pkts_0 per_mcs_rx_pkts_1 per_mcs_rx_pkts_10 per_mcs_rx_pkts_11 per_mcs_rx_pkts_2 per_mcs_rx_pkts_3 per_mcs_rx_pkts_4 per_mcs_rx_pkts_5 per_mcs_rx_pkts_6 per_mcs_rx_pkts_7 per_mcs_rx_pkts_8 per_mcs_rx_pkts_9 per_mcs_rx_mu_pkts_0 per_mcs_rx_mu_pkts_1 per_mcs_rx_mu_pkts_10 per_mcs_rx_mu_pkts_11 per_mcs_rx_mu_pkts_2 per_mcs_rx_mu_pkts_3 per_mcs_rx_mu_pkts_4 per_mcs_rx_mu_pkts_5 per_mcs_rx_mu_pkts_6 per_mcs_rx_mu_pkts_7 per_mcs_rx_mu_pkts_8 per_mcs_rx_mu_pkts_9 per_mcs_rx_su_pkts_0 per_mcs_rx_su_pkts_1 per_mcs_rx_su_pkts_10 per_mcs_rx_su_pkts_11 per_mcs_rx_su_pkts_2 per_mcs_rx_su_pkts_3 per_mcs_rx_su_pkts_4 per_mcs_rx_su_pkts_5 per_mcs_rx_su_pkts_6 per_mcs_rx_su_pkts_7 per_mcs_rx_su_pkts_8 per_mcs_rx_su_pkts_9 per_mcs_tx_pkts_0 per_mcs_tx_pkts_1 per_mcs_tx_pkts_10 per_mcs_tx_pkts_11 per_mcs_tx_pkts_2 per_mcs_tx_pkts_3 per_mcs_tx_pkts_4 per_mcs_tx_pkts_5 per_mcs_tx_pkts_6 per_mcs_tx_pkts_7 per_mcs_tx_pkts_8 per_mcs_tx_pkts_9 per_mcs_tx_mu_pkts_0 per_mcs_tx_mu_pkts_1 per_mcs_tx_mu_pkts_10 per_mcs_tx_mu_pkts_11 per_mcs_tx_mu_pkts_2 per_mcs_tx_mu_pkts_3 per_mcs_tx_mu_pkts_4 per_mcs_tx_mu_pkts_5 per_mcs_tx_mu_pkts_6 per_mcs_tx_mu_pkts_7 per_mcs_tx_mu_pkts_8 per_mcs_tx_mu_pkts_9 per_mcs_tx_su_pkts_0 per_mcs_tx_su_pkts_1 per_mcs_tx_su_pkts_10 per_mcs_tx_su_pkts_11 per_mcs_tx_su_pkts_2 per_mcs_tx_su_pkts_3 per_mcs_tx_su_pkts_4 per_mcs_tx_su_pkts_5 per_mcs_tx_su_pkts_6 per_mcs_tx_su_pkts_7 per_mcs_tx_su_pkts_8 per_mcs_tx_su_pkts_9 per_stream_rssi_chw160m_0 per_stream_rssi_chw160m_1 per_stream_rssi_chw160m_2 per_stream_rssi_chw160m_3 per_stream_rssi_chw160m_4 per_stream_rssi_chw160m_5 per_stream_rssi_chw160m_6 per_stream_rssi_chw160m_7 per_stream_rssi_chw20m_0 per_stream_rssi_chw20m_1 per_stream_rssi_chw20m_2 per_stream_rssi_chw20m_3 per_stream_rssi_chw20m_4 per_stream_rssi_chw20m_5 per_stream_rssi_chw20m_6 per_stream_rssi_chw20m_7 per_stream_rssi_chw40m_0 per_stream_rssi_chw40m_1 per_stream_rssi_chw40m_2 per_stream_rssi_chw40m_3 per_stream_rssi_chw40m_4 per_stream_rssi_chw40m_5 per_stream_rssi_chw40m_6 per_stream_rssi_chw40m_7 per_stream_rssi_chw80m_0 per_stream_rssi_chw80m_1 per_stream_rssi_chw80m_2 per_stream_rssi_chw80m_3 per_stream_rssi_chw80m_4 per_stream_rssi_chw80m_5 per_stream_rssi_chw80m_6 per_stream_rssi_chw80m_7 per_stream_rx_pkts_0 per_stream_rx_pkts_1 per_stream_rx_pkts_2 per_stream_rx_pkts_3 per_stream_rx_pkts_4 per_stream_rx_pkts_5 per_stream_rx_pkts_6 per_stream_rx_pkts_7 per_stream_tx_pkts_0 per_stream_tx_pkts_1 per_stream_tx_pkts_2 per_stream_tx_pkts_3 per_stream_tx_pkts_4 per_stream_tx_pkts_5 per_stream_tx_pkts_6 per_stream_tx_pkts_7 rx_ofdma_mode tx_ofdma_mode rx_ru_high_index rx_ru_low_index rx_ofdma_pkts rx_ru_index rx_ru_type tx_ru_high_index tx_ru_low_index tx_ofdma_pkts tx_ru_index tx_ru_type", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 19")

    spirent_results_EnhancedResultsGroupFilter_11 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee8021as_clock_sync_stats", \
    LiveFacts="as_capable as_capable_across_domain follow_up_correction_field pdelay_response_correction_field pdelay_response_followup_correction_field sync_correction_field invalid_timestamp_count average_mean_path_delay current_mean_path_delay max_mean_path_delay min_mean_path_delay peer_mean_path_delay log_min_delay_request_interval log_min_pdelay_request_interval step_removed average_offset_minus_deviation average_offset_plus_deviation current_offset negative_offset_peak offset_deviation offset_standard_deviation positive_offset_peak time_of_day time_of_day_in_seconds", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 20")

    spirent_results_EnhancedResultsGroupFilter_12 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="igmp_device_stats", \
    LiveFacts="host_state rx_frame_count rx_unknown_type_count tx_frame_count rx_checksum_error_count rx_length_error_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 21")

    spirent_results_EnhancedResultsGroupFilter_13 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="igmp_host_group_stats", \
    LiveFacts="duplicate_join join_fail join_latency join_timestamp leave_latency leave_timestamp state state_change_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 22")

    spirent_results_EnhancedResultsGroupFilter_14 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="isis_router_stats", \
    LiveFacts="adjacency_level adjacency_three_way_state l1_broadcast_adjacency_state l2_broadcast_adjacency_state state rx_adj_sid_tlv_count rx_backup_adj_sid_tlv_count rx_backup_lan_adj_sid_tlv_count rx_l1_csnp_count rx_l1_lan_hello_count rx_l1_lsp_count rx_l1_psnp_count rx_l2_bundle_adj_sid_tlv_count rx_l2_bundle_lan_adj_sid_tlv_count rx_l2_csnp_count rx_l2_lan_hello_count rx_l2_lsp_count rx_l2_psnp_count rx_lan_adj_sid_tlv_count rx_prefix_sid_tlv_count rx_ptp_hello_count rx_sid_label_binding_tlv_count rx_srlg_tlv_count rx_srv6_capabilities_tlv_count rx_srv6_endx_sid_tlv_count rx_srv6_lan_endx_sid_tlv_count rx_srv6_locator_tlv_count rx_unknown_sid_label_binding_tlv_count tx_adj_sid_tlv_count tx_backup_adj_sid_tlv_count tx_backup_lan_adj_sid_tlv_count tx_l1_csnp_count tx_l1_lan_hello_count tx_l1_lsp_count tx_l1_psnp_count tx_l2_bundle_adj_sid_tlv_count tx_l2_bundle_lan_adj_sid_tlv_count tx_l2_csnp_count tx_l2_lan_hello_count tx_l2_lsp_count tx_l2_psnp_count tx_lan_adj_sid_tlv_count tx_prefix_sid_tlv_count tx_ptp_hello_count tx_sid_label_binding_tlv_count tx_srlg_tlv_count tx_srv6_capabilities_tlv_count tx_srv6_endx_sid_tlv_count tx_srv6_lan_endx_sid_tlv_count tx_srv6_locator_tlv_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 23")

    spirent_results_EnhancedResultsGroupFilter_15 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_port_basic_stats", \
    LiveFacts="first_arrival_time last_arrival_time dropped_frame_count duplicate_frame_count in_order_frame_count late_frame_count out_seq_frame_count preamble_max_length preamble_min_length preamble_total_bytes reordered_frame_count hw_frame_count l1_bit_count l1_bit_rate pause_frame_count pause_frame_rate prbs_fill_octet_count prbs_fill_octet_rate sig_frame_count sig_frame_rate total_octet_count total_cell_count total_frame_count total_octet_rate total_cell_rate total_frame_rate corrected_base_rs_fec_error_count corrected_rs_fec_error_count fcs_error_frame_count fcs_error_frame_rate ipv4_checksum_error_count ipv4_checksum_error_rate jumbo_frame_count jumbo_frame_rate oversize_frame_count oversize_frame_rate prbs_bit_error_count prbs_bit_error_rate prbs_error_frame_count prbs_error_frame_rate tcp_checksum_error_count tcp_checksum_error_rate udp_checksum_error_count udp_checksum_error_rate undersize_frame_count undersize_frame_rate uncorrected_base_rs_fec_error_count uncorrected_rs_fec_error_count corrected_rs_fec_symbols post_base_rs_fec_ser_rate post_rs_fec_ser_rate pre_base_rs_fec_ser_rate pre_rs_fec_ser_rate max_frame_length min_frame_length avg_latency max_latency min_latency pfc_frame_count pfc_pri0_frame_count pfc_pri0_quanta pfc_pri0_frame_rate pfc_pri1_frame_count pfc_pri1_quanta pfc_pri1_frame_rate pfc_pri2_frame_count pfc_pri2_quanta pfc_pri2_frame_rate pfc_pri3_frame_count pfc_pri3_quanta pfc_pri3_frame_rate pfc_pri4_frame_count pfc_pri4_quanta pfc_pri4_frame_rate pfc_pri5_frame_count pfc_pri5_quanta pfc_pri5_frame_rate pfc_pri6_frame_count pfc_pri6_quanta pfc_pri6_frame_rate pfc_pri7_frame_count pfc_pri7_quanta pfc_pri7_frame_rate pfc_frame_rate fcoe_frame_count fcoe_frame_rate icmp_frame_count icmp_frame_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_over_ipv4_frame_count ipv6_over_ipv4_frame_rate ipv6_frame_rate mpls_frame_count mpls_frame_rate tcp_frame_count tcp_frame_rate udp_frame_count udp_frame_rate vlan_frame_count vlan_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 24")

    spirent_results_EnhancedResultsGroupFilter_16 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_port_basic_stats", \
    LiveFacts="generator_octet_count generator_frame_count generator_octet_rate generator_frame_rate generator_sig_frame_count generator_sig_frame_rate total_octet_count total_cell_count total_frame_count total_octet_rate total_cell_rate total_frame_rate hw_frame_count l1_bit_count l1_bit_rate generator_abort_frame_count generator_abort_frame_rate generator_crc_error_frame_count generator_crc_error_frame_rate generator_jumbo_frame_count generator_jumbo_frame_rate generator_l3_checksum_error_count generator_l3_checksum_error_rate generator_l4_checksum_error_count generator_l4_checksum_error_rate generator_oversize_frame_count generator_oversize_frame_rate generator_undersize_frame_count generator_undersize_frame_rate pfc_frame_count pfc_pri0_frame_count pfc_pri1_frame_count pfc_pri2_frame_count pfc_pri3_frame_count pfc_pri4_frame_count pfc_pri5_frame_count pfc_pri6_frame_count pfc_pri7_frame_count generator_ipv4_frame_count generator_ipv4_frame_rate generator_ipv6_frame_count generator_ipv6_frame_rate generator_mpls_frame_count generator_mpls_frame_rate generator_vlan_frame_count generator_vlan_frame_rate total_mpls_frame_rate total_ipv4_frame_count total_ipv4_frame_rate total_ipv6_frame_count total_ipv6_frame_rate total_mpls_frame_count queue_full_drop_count queue_full_retry_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 25")

    spirent_results_EnhancedResultsGroupFilter_17 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_port_cpu_stats", \
    LiveFacts="octet_count frame_count dropped_frame_count dropped_frame_rate neighbor_advertisement_count neighbor_advertisement_rate neighbor_solicitation_count neighbor_solicitation_rate octet_rate frame_rate arp_reply_count arp_reply_rate arp_request_count arp_request_rate icmp_echo_reply_count icmp_echo_reply_rate icmp_echo_request_count icmp_echo_request_rate icmpv6_echo_reply_count icmpv6_echo_reply_rate icmpv6_echo_request_count icmpv6_echo_request_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_frame_rate mpls_frame_count mpls_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 26")

    spirent_results_EnhancedResultsGroupFilter_18 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_port_cpu_stats", \
    LiveFacts="octet_count frame_count neighbor_advertisement_count neighbor_advertisement_rate neighbor_solicitation_count neighbor_solicitation_rate octet_rate frame_rate arp_reply_count arp_reply_rate arp_request_count arp_request_rate icmp_echo_reply_count icmp_echo_reply_rate icmp_echo_request_count icmp_echo_request_rate icmpv6_echo_reply_count icmpv6_echo_reply_rate icmpv6_echo_request_count icmpv6_echo_request_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_frame_rate mpls_frame_count mpls_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 27")

    spirent_results_EnhancedResultsGroupFilter_19 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_stream_stats", \
    LiveFacts="first_arrival_time last_arrival_time max_interarrival_time min_interarrival_time total_interarrival_time dropped_frame_count dropped_frame_rate duplicate_frame_count duplicate_frame_rate in_seq_frame_count in_seq_frame_rate in_order_frame_count in_order_frame_rate late_frame_count late_frame_rate out_seq_frame_count out_seq_frame_rate prbs_fill_octet_count prbs_fill_octet_rate reordered_frame_count reordered_frame_rate octet_count cell_count frame_count l1_bit_count l1_bit_rate octet_rate cell_rate frame_rate sig_frame_count sig_frame_rate prbs_bit_error_count prbs_error_frame_count prbs_error_frame_rate prbs_bit_error_rate fcs_error_frame_count fcs_error_frame_rate ipv4_checksum_error_count ipv4_checksum_error_rate tcp_udp_checksum_error_count tcp_udp_checksum_error_rate max_jitter min_jitter total_jitter total_jitter_rate max_latency min_latency total_latency expected_seq_num last_seq_num seq_run_length counter_timestamp avg_jitter avg_latency", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 28")

    spirent_results_EnhancedResultsGroupFilter_20 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_stream_stats", \
    LiveFacts="octet_count cell_count frame_count l1_bit_count l1_bit_rate octet_rate cell_rate frame_rate counter_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 29")

    spirent_results_EnhancedResultsGroupFilter_21 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pim_router_stats", \
    LiveFacts="mdt_join_count neighbor_count state rx_group_rp_count rx_group_starg_count rx_group_sg_count rx_group_sgrpt_count rx_assert_count rx_bootstrap_count rx_hello_count rx_joinprune_count rx_register_count rx_register_stop_count tx_group_rp_count tx_group_starg_count tx_group_sg_count tx_group_sgrpt_count tx_bootstrap_count tx_hello_count tx_joinprune_count tx_register_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 30")

    spirent_results_EnhancedResultsGroupFilter_22 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ppp_block_stats", \
    LiveFacts="block_state ipv4cp_block_state ipv6cp_block_state attempted sessions succ_disc failed_disc failed_conn succ_conn sessions_up retry avg_succ_tx chap_rx chap_tx ipcp_rx ipcp_tx ipv6cp_rx ipv6cp_tx lcp_conf_ack_rx lcp_conf_ack_tx lcp_conf_nak_rx lcp_conf_nak_tx lcp_conf_rej_rx lcp_conf_rej_tx lcp_conf_req_rx lcp_conf_req_tx lcp_echo_rep_rx lcp_echo_rep_tx lcp_echo_req_rx lcp_echo_req_tx lcp_term_ack_rx lcp_term_ack_tx lcp_term_req_rx lcp_term_req_tx padi_rx padi_tx pado_rx pado_tx padr_rx padr_tx pads_rx pads_tx padt_rx padt_tx pap_rx pap_tx succ_setup_rate max_setup_time min_setup_time avg_setup_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 31")

    spirent_results_EnhancedResultsGroupFilter_23 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="roe_block_stats", \
    LiveFacts="state rx_cpri_port_tlv_count rx_demapper_container_tlv_count rx_demapper_fft_tlv_count rx_demapper_tlv_count rx_ethernet_link_tlv_count rx_frame_count rx_roe_19141_tlv_count rx_mapper_container_tlv_count rx_mapper_fft_tlv_count rx_mapper_prach_tlv_count rx_mapper_tlv_count rx_dropped_count rx_dropped_rate tx_cpri_port_tlv_count tx_demapper_container_tlv_count tx_demapper_fft_tlv_count tx_demapper_tlv_count tx_ethernet_link_tlv_count tx_frame_count tx_roe_19141_tlv_count tx_mapper_container_tlv_count tx_mapper_fft_tlv_count tx_mapper_prach_tlv_count tx_mapper_tlv_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 32")

    spirent_results_EnhancedResultsGroupFilter_24 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rsvp_te_stats", \
    LiveFacts="avg_lsp_setup_time egress_lsp_up_count last_rx_path_error_code last_rx_resv_error_code last_tx_path_error_code last_tx_resv_error_code lsp_connecting_count lsp_down_count lsp_up_count max_lsp_setup_time min_lsp_setup_time state rx_hello rx_notify rx_path rx_path_error rx_path_recovery rx_path_tear rx_resv rx_resv_confirm rx_resv_error rx_resv_tear tx_hello tx_notify tx_path tx_path_error tx_path_recovery tx_path_tear tx_resv tx_resv_confirm tx_resv_error tx_resv_tear", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 33")

    spirent_results_EnhancedResultsGroupFilter_25 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ecpri_type_5_message_stats", \
    LiveFacts="measurement_id avg_delay max_delay min_delay rx_follow_up_count rx_remote_request_count rx_remote_request_with_follow_up_count rx_request_count rx_request_with_follow_up_count rx_response_count tx_follow_up_count tx_remote_request_count tx_remote_request_with_follow_up_count tx_request_count tx_request_with_follow_up_count tx_response_count curr_delay", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 25")

    spirent_results_EnhancedResultsConfigSelection_1 = stc.create("spirent.results.EnhancedResultsConfigSelection",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    DimensionSetName="tx_stream_config", \
    PropertyList="frames_per_second", \
    EnableAuto="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsConfigSelection 1")

    spirent_results_EnhancedResultsGroupFilter_26 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bfd_session_stats", \
    LiveFacts="bfd_diagnostic_code flaps_detected last_bfd_diagnostic_error_rx my_discriminator state rx_bfd_packets sessions_down sessions_up timesouts_detected tx_bfd_packets your_discriminator", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 45")

    spirent_results_EnhancedResultsGroupFilter_27 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ospfv2_session_stats", \
    LiveFacts="adjacency_status area_id ipv4_src_address state session_up_count rx_ack rx_as_external_lsa rx_asbr_summary_lsa rx_dd rx_el_lsa rx_ep_lsa rx_hello rx_network_lsa rx_nssa_lsa rx_request rx_ri_lsa rx_router_lsa rx_summary_lsa rx_te_lsa tx_ack tx_as_external_lsa tx_asbr_summary_lsa tx_dd tx_el_lsa tx_ep_lsa tx_hello tx_network_lsa tx_nssa_lsa tx_request tx_ri_lsa tx_router_lsa tx_summary_lsa tx_te_lsa", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 46")

    spirent_results_EnhancedResultsGroupFilter_28 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ospfv3_router_stats", \
    LiveFacts="adjacency_status state rx_ack rx_as_external_lsa rx_dd rx_e_as_external_lsa rx_e_inter_area_pfx_lsa rx_e_inter_area_router_lsa rx_e_intra_area_pfx_lsa rx_e_link_lsa rx_e_network_lsa rx_e_nssa_lsa rx_e_router_lsa rx_hello rx_inter_area_pfx_lsa rx_inter_area_router_lsa rx_intra_area_pfx_lsa rx_link_lsa rx_network_lsa rx_nssa_lsa rx_request rx_router_info_lsa rx_router_lsa rx_srv6_locator_lsa rx_update tx_ack tx_as_external_lsa tx_dd tx_e_as_external_lsa tx_e_inter_area_pfx_lsa tx_e_inter_area_router_lsa tx_e_intra_area_pfx_lsa tx_e_link_lsa tx_e_network_lsa tx_e_nssa_lsa tx_e_router_lsa tx_hello tx_inter_area_pfx_lsa tx_inter_area_router_lsa tx_intra_area_pfx_lsa tx_link_lsa tx_network_lsa tx_nssa_lsa tx_request tx_router_info_lsa tx_router_lsa tx_srv6_locator_lsa tx_update", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 47")

    spirent_results_EnhancedResultsConfigSelection_2 = stc.create("spirent.results.EnhancedResultsConfigSelection",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    DimensionSetName="tx_stream_config", \
    PropertyList="frames_per_second", \
    EnableAuto="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsConfigSelection 1")

    spirent_results_EnhancedResultsGroupFilter_29 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_client_assoc_stats", \
    LiveFacts="abort attempt failed failure_rate incoming_bytes incoming_traffic outgoing_bytes outgoing_traffic reading_interval success_rate successful", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 51")

    spirent_results_EnhancedResultsGroupFilter_30 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_client_stats", \
    LiveFacts="avg_rx_packet_rate avg_tx_packet_rate max_rx_packet_rate max_tx_packet_rate reading_interval rx_bandwidth rx_byte_rate rx_packet_count rx_packet_rate tx_bandwidth tx_byte_rate tx_packet_count tx_packet_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 52")

    spirent_results_EnhancedResultsGroupFilter_31 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_server_stats", \
    LiveFacts="average_rx_bandwidth avg_rx_packet_rate average_tx_bandwidth avg_tx_packet_rate is_memory_limited link_map main_pool_size main_pool_used max_rx_packet_rate max_tx_packet_rate maximum_rx_bandwidth maximum_tx_bandwidth packet_memory_used reading_interval rcv_queue_length response_time rx_bandwidth rx_byte_rate rx_packet_count rx_packet_rate tx_bandwidth tx_byte_rate tx_packet_count tx_packet_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 53")

    spirent_results_EnhancedResultsGroupFilter_32 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_url_client_stats", \
    LiveFacts="average_resp_time_per_url average_resp_time_per_page maximum_resp_time_per_url url_sample_count_delta minimum_resp_time_per_url minimum_resp_time_per_page maximum_resp_time_per_page url_response_time_delta page_sample_count_delta", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 54")

    spirent_results_EnhancedResultsGroupFilter_33 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_load_spec_client_stats", \
    LiveFacts="desired_load_spec_count average_idle_time maximum_idle_time cpu_utilized minimum_idle_time current_load_spec_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 55")

    spirent_results_EnhancedResultsGroupFilter_34 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="cptraffic_device_stats", \
    LiveFacts="state tx_pause_frame_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 56")

    spirent_results_EnhancedResultsGroupFilter_35 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_block_stats", \
    LiveFacts="state role session_count session_up_count session_idle_count session_pending_count tx_open_count rx_open_count tx_keepalive_count rx_keepalive_count tx_pc_req_count rx_pc_req_count tx_pc_rep_count rx_pc_rep_count tx_notify_count rx_notify_count tx_error_count rx_error_count tx_close_count rx_close_count flap_count tx_pc_rpt_count rx_pc_rpt_count tx_pc_upd_count rx_pc_upd_count tx_pc_init_count rx_pc_init_count total_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 57")

    spirent_results_EnhancedResultsGroupFilter_36 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_device_stats", \
    LiveFacts="state role local_ip_address peer_ip_address total_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count local_path_setup_list peer_path_setup_list local_ass_type_list peer_ass_type_list tx_open_count rx_open_count tx_keepalive_count rx_keepalive_count tx_pc_req_count rx_pc_req_count tx_pc_rep_count rx_pc_rep_count tx_pc_rpt_count rx_pc_rpt_count tx_pc_upd_count rx_pc_upd_count tx_pc_init_count rx_pc_init_count tx_notify_count tx_notify_type tx_notify_value rx_notify_count rx_notify_type rx_notify_value tx_error_count tx_error_type tx_error_value rx_error_count rx_error_type rx_error_value tx_close_count tx_close_reason rx_close_count rx_close_reason flap_count db_version", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 58")

    spirent_results_EnhancedResultsGroupFilter_37 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_lsp_block_stats", \
    LiveFacts="role lsp_count delegated_lsp_count updated_lsp_count revoked_lsp_count returned_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count initiated_lsp_count requested_lsp_count replied_lsp_count error_lsp_count mbb_lsp_count lsp_block_local_ip_address lsp_block_peer_ip_address", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 59")

    spirent_results_EnhancedResultsGroupFilter_38 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_lsp_stats", \
    LiveFacts="role symbolic_name lsp_state plsp_state plsp_id srp_id src_ip_address dst_ip_address rp_id lsp_tx_error_type lsp_tx_error_value lsp_rx_error_type lsp_rx_error_value lsp_id tunnel_id ex_tunnel_id association_group ero lsp_local_ip_address lsp_peer_ip_address path_setup_type path_segment binding_sid", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 60")

    spirent_results_EnhancedResultsGroupFilter_39 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="cusp_block_stats", \
    LiveFacts="state session_count session_idle_count session_up_count retry_count tx_frame_count rx_frame_count tx_keepalive_count rx_keepalive_count tx_hello_count rx_hello_count rx_error_count tx_error_count rx_update_object_count tx_update_object_count tx_report_count tx_event_count rx_bras_access_ifsrvinfo_count rx_bras_user_basicinfo_count rx_bras_user_pppinfo_count rx_bras_user_ipv4info_count rx_bras_user_ipv6info_count rx_bras_user_authInfo_count rx_bras_routev4Info_count rx_bras_routev6Info_count rx_bras_static_user_ipv4_info_count rx_bras_user_l2tp_lac_info_count rx_bras_user_l2tp_lns_info_count rx_bras_l2tp_tunnel_lac_info_count rx_bras_l2tp_tunnel_lns_info_count tx_bras_resource_if_info_count tx_bras_resource_board_info_count tx_bras_user_traffic_Info_count tx_bras_user_detect_result_info_count tx_bras_user_nat_info_count tx_bras_user_tbl_result_count tx_cgn_addr_alloc_req_count rx_cgn_addr_alloc_ack_count tx_cgn_addr_renew_req_count rx_cgn_addr_renew_ack_count tx_cgn_addr_release_req_count rx_cgn_addr_release_ack_count tx_sync_request_count rx_sync_request_count tx_sync_begin_count rx_sync_begin_count tx_sync_data_count rx_sync_data_count tx_sync_end_count rx_sync_end_count tx_sync_ack_count rx_sync_ack_count user_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 61")

    spirent_results_EnhancedResultsGroupFilter_40 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="mld_device_stats", \
    LiveFacts="host_state tx_frame_count rx_frame_count rx_unknown_type_count rx_checksum_error_count rx_length_error_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 62")

    spirent_results_EnhancedResultsGroupFilter_41 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="mld_host_group_stats", \
    LiveFacts="duplicate_join join_fail join_latency join_timestamp leave_latency leave_timestamp state state_change_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 63")

    spirent_results_EnhancedResultsGroupFilter_42 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_client_stats", \
    LiveFacts="bas_tx_count bas_rx_count cv_tx_count cv_rx_count cs_tx_count cs_rx_count dm_tx_count dm_rx_count dmm_tx_count dmm_rx_count dmmr_tx_count dmmr_rx_count aps_tx_count aps_rx_count rx_dropped_packet_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 64")

    spirent_results_EnhancedResultsGroupFilter_43 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_bas_stats", \
    LiveFacts="bip8_error_count rdi_status rei_count cs_lpi_status cs_lf_status cs_rf_status period_status period_error_count sequence_error_count rdi_error_count rdi_restore_count cs_lpi_error_count cs_lpi_restore_count cs_lf_error_count cs_lf_restore_count cs_rf_error_count cs_rf_restore_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 65")

    spirent_results_EnhancedResultsGroupFilter_44 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_dm_stats", \
    LiveFacts="min_delay max_delay avg_delay dm_rx_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 66")

    spirent_results_EnhancedResultsGroupFilter_45 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_dmmr_stats", \
    LiveFacts="min_round_trip_time max_round_trip_time avg_round_trip_time dmmr_rx_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 67")

    spirent_results_EnhancedResultsGroupFilter_46 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_fec_sym_err_stats", \
    LiveFacts="num_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 68")

    spirent_results_EnhancedResultsGroupFilter_47 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_pcs_stats", \
    LiveFacts="delay lock symbol_errors_last_sec symbol_errors_err_sec pre_fec_lane_ser rx_skew_bits symbol_error symbol_errors_per_sec sync_header_error symbol_errors_total virtual_lane_num", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 69")

    spirent_results_EnhancedResultsGroupFilter_48 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_prbs_pam4_stats", \
    LiveFacts="bitswap unsync_sec bit_errors rx_pattern sync_sec", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 70")

    spirent_results_EnhancedResultsGroupFilter_49 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_txcvrs_stats", \
    LiveFacts="los_count signal", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 71")

    spirent_results_EnhancedResultsGroupFilter_50 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_eyescan_stats", \
    LiveFacts="num_samples", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 72")

    spirent_results_EnhancedResultsGroupFilter_51 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_port_stats", \
    LiveFacts="fpga_temp module_temp module_volt link_status rx_ppm_offset cw_count cw_per_bin code_violations_err_sec code_violations_total code_violations_per_sec corrected_cw_total corrected_cw_per_sec corrected_cw_last_sec code_violations_last_sec corrected_cw_err_sec symbol_errors_err_sec uncorrected_cw_last_sec all_lanes_aligned post_fec_ser pre_fec_ser rx_fifo_error rx_local_fault rx_remote_fault symbol_errors_per_sec symbol_errors_last_sec rx_high_ser symbol_errors_total tx_local_fault uncorrected_cw_total uncorrected_cw_per_sec uncorrected_cw_err_sec", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 73")

    EotResultNode_1 = stc.create("EotResultNode",under = system1, \
    Description="Custom Test Result Description 6980", \
    ResultState="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Standalone")

    EotResultNodeParam_1 = stc.create("EotResultNodeParam",under = EotResultNode_1, \
    ParamValue="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="@EndDataSetId")

# Set up relationships
    stc.config(Project_1,**{"DefaultSelection-targets" : [FrameLengthDistribution_1,CustomFillPattern_1]})
    stc.config(Port_1,**{"AffiliationPort-sources" : [EmulatedDevice_1]})
    stc.config(Port_1,**{"ActivePhy-targets" : [Ethernet10GigFiber_1]})
    stc.config(Port_2,**{"AffiliationPort-sources" : [EmulatedDevice_2]})
    stc.config(Port_2,**{"ActivePhy-targets" : [Ethernet10GigFiber_2]})
    stc.config(Port_3,**{"AffiliationPort-sources" : [EmulatedDevice_3]})
    stc.config(Port_3,**{"ActivePhy-targets" : [Ethernet10GigFiber_3]})
    stc.config(Tags_1,**{"DefaultTag-targets" : [Tag_1,Tag_2,Tag_3,Tag_4,Tag_5,Tag_6]})
    stc.config(PerspectiveNode_1,**{"PerspectiveChild-targets" : [DynamicResultView_2,ResultDataSet_2]})
    stc.config(PerspectiveNode_2,**{"PerspectiveChild-targets" : [DynamicResultView_2,ResultDataSet_2]})
    stc.config(Host_1,**{"TopLevelIf-targets" : [Ipv4If_1,Ipv6If_1,Ipv6If_2]})
    stc.config(Ipv4If_1,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(Ipv6If_1,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(Ipv6If_2,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(AnalyzerConfig_1,**{"ActiveHistogram-targets" : [LatencyHistogram_1]})
    stc.config(StreamBlock_1,**{"SrcBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_1,**{"DstBinding-targets" : [Ipv4If_6]})
    stc.config(StreamBlock_1,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_1,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_3]})
    stc.config(StreamBlock_2,**{"SrcBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_2,**{"DstBinding-targets" : [Ipv4If_4]})
    stc.config(StreamBlock_2,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_2,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_4]})
    stc.config(Host_2,**{"TopLevelIf-targets" : [Ipv4If_2,Ipv6If_3,Ipv6If_4]})
    stc.config(Ipv4If_2,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(Ipv6If_3,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(Ipv6If_4,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(AnalyzerConfig_2,**{"ActiveHistogram-targets" : [LatencyHistogram_2]})
    stc.config(StreamBlock_3,**{"SrcBinding-targets" : [Ipv4If_4]})
    stc.config(StreamBlock_3,**{"DstBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_3,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_3,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_1]})
    stc.config(EmulatedDevice_1,**{"TopLevelIf-targets" : [Ipv4If_3]})
    stc.config(EmulatedDevice_1,**{"PrimaryIf-targets" : [Ipv4If_3]})
    stc.config(Ipv4If_3,**{"StackedOnEndpoint-targets" : [EthIIIf_3]})
    stc.config(EmulatedDevice_2,**{"TopLevelIf-targets" : [Ipv4If_4]})
    stc.config(EmulatedDevice_2,**{"PrimaryIf-targets" : [Ipv4If_4]})
    stc.config(Ipv4If_4,**{"StackedOnEndpoint-targets" : [EthIIIf_4]})
    stc.config(Dhcpv4BlockConfig_1,**{"UsesIf-targets" : [Ipv4If_4]})
    stc.config(ResultQuery_3,**{"ResultFilters-targets" : [RxPortResultFilter_1]})
    stc.config(Host_3,**{"TopLevelIf-targets" : [Ipv4If_5,Ipv6If_5,Ipv6If_6]})
    stc.config(Ipv4If_5,**{"StackedOnEndpoint-targets" : [EthIIIf_5]})
    stc.config(Ipv6If_5,**{"StackedOnEndpoint-targets" : [EthIIIf_5]})
    stc.config(Ipv6If_6,**{"StackedOnEndpoint-targets" : [EthIIIf_5]})
    stc.config(AnalyzerConfig_3,**{"ActiveHistogram-targets" : [LatencyHistogram_3]})
    stc.config(StreamBlock_4,**{"SrcBinding-targets" : [Ipv4If_6]})
    stc.config(StreamBlock_4,**{"DstBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_4,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_4,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_2]})
    stc.config(EmulatedDeviceGenParams_1,**{"SelectedPort-targets" : [Port_3]})
    stc.config(EmulatedDeviceGenParams_1,**{"DeviceGenTopLevelIf-targets" : [DeviceGenIpv4IfParams_1]})
    stc.config(DeviceGenIpv4IfParams_1,**{"DeviceGenStackedOnIf-targets" : [DeviceGenEthIIIfParams_1]})
    stc.config(EmulatedDevice_3,**{"TopLevelIf-targets" : [Ipv4If_6]})
    stc.config(EmulatedDevice_3,**{"PrimaryIf-targets" : [Ipv4If_6]})
    stc.config(Ipv4If_6,**{"StackedOnEndpoint-targets" : [EthIIIf_6]})
    stc.config(Dhcpv4BlockConfig_2,**{"UsesIf-targets" : [Ipv4If_6]})
    stc.config(Sequencer_1,**{"SequencerFinalizeType-targets" : [SequencerGroupCommand_1]})
    stc.config(EOTResultsWriteIterationCommand_1,**{"RootEotResultNode-targets" : [EotResultNode_1]})

# Set up handles
    stc.config(ResultQuery_3,ResultRootList=Project_1)
    stc.config(ResultQuery_3,PropertyHandleArray="")
    stc.config(ResultQuery_4,ResultRootList=Project_1)
    stc.config(ResultQuery_4,PropertyHandleArray="")
    stc.config(ResultQuery_5,ResultRootList="")
    stc.config(ResultQuery_5,PropertyHandleArray="")
    stc.config(ResultQuery_6,ResultRootList=StreamBlock_2)
    stc.config(ResultQuery_6,PropertyHandleArray="")
    stc.config(ResultQuery_7,ResultRootList=StreamBlock_4)
    stc.config(ResultQuery_7,PropertyHandleArray="")
    stc.config(ResultQuery_10,ResultRootList=StreamBlock_3)
    stc.config(ResultQuery_10,PropertyHandleArray="")
    stc.config(ResultQuery_9,ResultRootList=StreamBlock_1)
    stc.config(ResultQuery_9,PropertyHandleArray="")
    stc.config(ResultQuery_8,ResultRootList=StreamBlock_2)
    stc.config(ResultQuery_8,PropertyHandleArray="")
    stc.config(ResultQuery_11,ResultRootList=StreamBlock_4)
    stc.config(ResultQuery_11,PropertyHandleArray="")
    stc.config(ResultQuery_13,ResultRootList=StreamBlock_3)
    stc.config(ResultQuery_13,PropertyHandleArray="")
    stc.config(SequencerIfCommand_1,CommandList="")
    stc.config(PhyVerifyLinkUpCommand_1,PortList=[Port_1,Port_2])
    stc.config(ArpNdVerifyResolvedCommand_1,HandleList=[Port_1,Port_2,Port_3])
    stc.config(SequencerIfCommand_3,ExpressionCommand=ArpNdVerifyResolvedCommand_2)
    stc.config(SequencerIfCommand_3,CommandList=SequencerStopCommand_2)
    stc.config(ResultQuery_12,ResultRootList=StreamBlock_1)
    stc.config(ResultQuery_12,PropertyHandleArray="")
    stc.config(DevicesStartAllCommand_1,Project=Project_1)
    stc.config(PresentationResultQuery_2,FromObjects=Project_1)
    stc.config(ArpNdStartOnAllDevicesCommand_1,PortList=[Port_1,Port_2,Port_3])
    stc.config(SequencerIfCommand_2,ExpressionCommand=PhyVerifyLinkUpCommand_2)
    stc.config(SequencerIfCommand_2,CommandList=SequencerStopCommand_1)
    stc.config(ResultQuery_14,ResultRootList=StreamBlock_2)
    stc.config(ResultQuery_14,PropertyHandleArray="")
    stc.config(AnalyzerStartCommand_1,AnalyzerList=[Analyzer_1,Analyzer_2,Analyzer_3])
    stc.config(StreamBlockStartCommand_1,StreamBlockList=[StreamBlock_3,StreamBlock_4])
    stc.config(AnalyzerStopCommand_1,AnalyzerList=[Analyzer_1,Analyzer_2,Analyzer_3])
    stc.config(EOTResultsWriteIterationCommand_1,StreamBlockList=Project_1)
    stc.config(PhyVerifyLinkUpCommand_2,PortList=[Port_1,Port_2])
    stc.config(ArpNdVerifyResolvedCommand_2,HandleList=[Port_1,Port_2])
    stc.config(ResultsClearAllCommand_1,PortList=Project_1)
    stc.config(StreamBlockStopCommand_1,StreamBlockList=[StreamBlock_1,StreamBlock_2,StreamBlock_3,StreamBlock_4])
    stc.config(StreamBlockStartCommand_2,StreamBlockList=[StreamBlock_1,StreamBlock_2,StreamBlock_3,StreamBlock_4])
    stc.config(StreamBlockStopCommand_2,StreamBlockList=[StreamBlock_1,StreamBlock_2,StreamBlock_3,StreamBlock_4])
    stc.config(VerifyResultsValueCondition_2,ResultQuery=ResultQuery_14)
    stc.config(VerifyResultsValueCondition_4,ResultQuery=ResultQuery_13)
    stc.config(VerifyResultsValueCondition_3,ResultQuery=ResultQuery_12)
    stc.config(VerifyResultsValueCondition_1,ResultQuery=ResultQuery_11)
    stc.config(SequencerGroupCommand_1,CommandList="")
    stc.config(Sequencer_1,CommandList=[PhyVerifyLinkUpCommand_1,SequencerIfCommand_2,DevicesStartAllCommand_1,WaitCommand_1,ArpNdStartOnAllDevicesCommand_1,WaitCommand_2,ArpNdVerifyResolvedCommand_1,SequencerIfCommand_3,StreamBlockStartCommand_1,WaitCommand_3,StreamBlockStopCommand_1,ResultsClearAllCommand_1,WaitCommand_4,StreamBlockStartCommand_2,AnalyzerStartCommand_1,WaitCommand_5,StreamBlockStopCommand_2,AnalyzerStopCommand_1,EOTResultsWriteIterationCommand_1,SaveResultsCommand_1,VerifyResultsValueCommand_1,VerifyResultsValueCommand_2,VerifyResultsValueCommand_3,VerifyResultsValueCommand_4])
    stc.config(Sequencer_1,BreakpointList="")
    stc.config(Sequencer_1,DisabledCommandList="")
    stc.config(Sequencer_1,CleanupCommand=SequencerGroupCommand_1)
    stc.config(RxPortResultFilter_1,RxPortList="")
    stc.config(ResultQuery_2,ResultRootList=Project_1)
    stc.config(ResultQuery_2,PropertyHandleArray="")
    stc.config(ResultQuery_1,ResultRootList=Project_1)
    stc.config(ResultQuery_1,PropertyHandleArray="")
    stc.config(PresentationResultQuery_1,FromObjects=Project_1)

    stc.config('system1',IsLoadingFromConfiguration='false')

    if len(portLocations) > 0:
        cmdResult = stc.perform('GetObjects', ClassName='Port', Condition='IsVirtual=false')
        ports = cmdResult['ObjectList'].split()
        idx = 0
        for port in ports:
            stc.config(port, location=portLocations[idx])
            idx+=1

    stc.config('project1.testResultSetting', saveResultsRelativeTo='NONE', resultsDirectory=resultsDir)
    stc.config('system1.sequencer', errorHandler='STOP_ON_ERROR')

#    connect - perform the logical to physical port mapping, connect to the 
#              chassis' and reserve the ports. This routine performs the connect,
#              reserve, and logical to physical port mappings directly.
#              The port list is retrieved from the in-memory configuration.
def connect():
    stc.perform('attachPorts')

#    apply - apply writes the logical information held in memory on the 
#            workstation to the ports in the STC chassis'.
def apply():
    stc.apply()

#    run - subscribe to any results views located in the in-memory configuration
#          and execute the sequencer and return the test status from the 
#          command sequence, if any. Test status is set by the Stopped Reason
#          in the Stop Command Sequence command. This is a string value and 
#          can be anything. If there is no sequence defined or no Stop 
#          Command Sequence command is executed, then the test state is 
#          returned. Test state can take the values: NONE, PASSED or FAILED.
def run():
    # Subscribe to results for result query BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12-0001-rxstreamsummaryresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='streamblock',
                  resultType='rxstreamsummaryresults',
                  filterList=(stc.get( 'system1', 'children-RxPortResultFilter' )).split(' ')[0] ,
                  viewAttributeList='framecount sigframecount fcserrorframecount minlatency maxlatency droppedframecount droppedframepercent inorderframecount reorderedframecount duplicateframecount lateframecount prbsbiterrorcount prbsfilloctetcount ipv4checksumerrorcount tcpudpchecksumerrorcount framerate sigframerate fcserrorframerate droppedframerate droppedframepercentrate inorderframerate reorderedframerate duplicateframerate lateframerate prbsbiterrorrate prbsfilloctetrate ipv4checksumerrorrate tcpudpchecksumerrorrate bitrate shorttermavglatency avglatency prbsbiterrorratio l1bitcount l1bitrate prbserrorframecount prbserrorframerate aggregatedrxportcount portstrayframes bitcount shorttermavgjitter avgjitter minjitter maxjitter shorttermavginterarrivaltime avginterarrivaltime mininterarrivaltime maxinterarrivaltime inseqframecount outseqframecount inseqframerate outseqframerate histbin1count histbin2count histbin3count histbin4count histbin5count histbin6count histbin7count histbin8count histbin9count histbin10count histbin11count histbin12count histbin13count histbin14count histbin15count histbin16count ',
                  interval='1', filenamePrefix='BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12-0001-rxstreamsummaryresults')

    # Subscribe to results for result query BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12-0002-txstreamresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='streamblock',
                  resultType='txstreamresults',
                  filterList='',
                  viewAttributeList='framecount framerate bitrate expectedrxframecount l1bitcount l1bitrate streaminfo bitcount ',
                  interval='1', filenamePrefix='BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12-0002-txstreamresults')

    # Start the sequencer
    stc.perform('sequencerStart')

    # Wait for sequencer to finish
    testState = stc.waitUntilComplete()
    return testState

#    cleanup - release the ports, disconnect from the chassis' and reset 
#              the in-memory configuration.
def cleanup():
    stc.perform('chassisDisconnectAll')
    stc.perform('resetConfig')
    print(datetime.datetime.now())
    print ("\nResults can be found in BasicIPv4_Traffic_BiDirect_S9P1_toandfrom_S9P11S9P12.db{_YYYY-MM-DD_HH-MM-SS}.db")
