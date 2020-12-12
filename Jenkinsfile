node() {
	echo env.GIT_COMMIT
	echo env.GIT_BRANCH
	echo env.GIT_REVISION
	def repoURL = "https://github.com/adrianhardkor/stc.git"
	def STC_INSTALL = "/opt/STC_CLIENT/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux64Client/"
	def os = System.properties['os.name'].toLowerCase()
	def passthruString = sh(script: "printenv", returnStdout: true)
	passthruString = passthruString.replaceAll('\n',' jenkins_')
	env.WORKSPACE_LOCAL = sh(returnStdout: true, script: 'pwd').trim()
	env.BUILD_TIME = "${BUILD_TIMESTAMP}"
	def HUDSON_URL = "${env.HUDSON_URL}"
	stage("Prepare Workspace") {
		echo "\n\n*** Prepare Workspace ***"
		cleanWs()
		echo "Workspace set to: " + env.WORKSPACE_LOCAL
		echo "Build time: " + env.BUILD_TIME
		sh "ls -l"
		def branches = scm.branches[0].name
		if (branches.contains("master")) {
			git "${repoURL}"
		}
		if (branches.contains("main")) {
			git branch: "main", url: "${repoURL}"
		}
		echo "BRANCH = ${branch}"
	}
    stage("BDD-Behave") {
        if (HUDSON_URL.contains("10.88.48.21")) {
            echo "\n\n\nBDD-Behave FOR SANDBOX"
            sh """
                pwd
                ls -l
            """
            try {
               sh """
                    export STC_PRIVATE_INSTALL_DIR=${STC_INSTALL}
                    /var/lib/jenkins/.pyenv/shims/behave -f cucumber -o reports/cucumber.json --junit
               """
            } catch (error) {
                echo "\n\n\n FAILURE FOUND -- CONTINUING TO XRAY-IMPORT"
            } finally {
                echo "*** JUNIT ***"
				junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
            } 
        }
    }
	stage('Import results to Xray') {
		echo "*** Import Results to XRAY ***"

		def description = "[STC_BUILD_URL|${env.BUILD_URL}]"
		def labels = '["regression","automated_regression"]'
		def environment = "DEV"
		def testExecutionFieldId = 10552
		def testEnvironmentFieldName = "customfield_10372"
		def projectKey = "XT"
		def projectId = 10606
		def xrayConnectorId = "${xrayConnectorId}"
		def info = '''{
            "fields": {
                "project": {
                    "id": "''' + projectId + '''"
                },
                "labels":''' + labels + ''',
                "description":"''' + description + '''",
                "summary": "Testing Jenkins - Automated Regression Execution @ ''' + env.BUILD_TIME + ' ' + environment + ''' " ,
                "issuetype": {
                    "id": "''' + testExecutionFieldId + '''"
                }
            }
        }'''
		echo info
        	step([$class: 'XrayImportBuilder', endpointName: '/cucumber/multipart', importFilePath: 'reports/cucumber.json', importInfo: info, inputInfoSwitcher: 'fileContent', serverInstance: xrayConnectorId])
    }
}
