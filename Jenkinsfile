node() {
    def STC_INSTALL = "/opt/STC_CLIENT/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux64Client/"
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    def os = System.properties['os.name'].toLowerCase()
    env.WORKSPACE_LOCAL = sh(returnStdout: true, script: 'pwd').trim()
    passthruString = sh(script: "printenv", returnStdout: true)
    passthruString = passthruString.replaceAll('\n',' jenkins_')
    env.BUILD_TIME = "${BUILD_TIMESTAMP}"
    def HUDSON_URL = "${env.HUDSON_URL}"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        sh """
            rm -rf *
            ls -l
        """
        def branches = "${scm.branches}"
        if (branches.contains("master")) {
            git "${repoURL}"
        }
        if (branches.contains("main")) {
            git branch: "main", url: "${repoURL}"
        }
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
                    printenv | grep STC_PRIVATE_INSTALL_DIR
                    /usr/local/bin/behave --format json -o target/behave.json --junit
                    ./b2c_json.py target/behave.json target/cucumber.json
                    ls -l target/
               """
            } catch (error) {
                echo "\n\n\n FAILURE FOUND -- CONTINUING TO XRAY-IMPORT"
            } finally {
                junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
            } 
        }
    }
    stage('Import results to Xray') {
        echo "\n\n\n*** Entering the Import results to Xray Stage ***"
        def description = "[Jenkins_BUILD_URL|${env.BUILD_URL}]"
        def labels = '["regression","automated_regression"]'
        def environment = "DEV"
        def testExecutionFieldId = 10552
        def testEnvironmentFieldName = "customfield_10372"
        def projectKey = "Xray-Test"
        def pk = 'XT'
        def projectId = 10606
        def xrayConnectorId = "${xrayConnectorId}"
        def info = """{
    "fields": {
        "description": "${description}",
        "issuetype": {
            "id": "${testExecutionFieldId}"
        },
        "labels": ${labels},
        "project": {
            "id": "${projectId}"
        },
        "summary": "Sample Jenkins STC - Automated Regression Execution @ ${env.BUILD_TIME} ${environment} "
    }
}"""
            echo "*** THIS IS THE XRAY INFO ***"
            echo "${info}"
            echo "*** XrayImportBuilder ***"
            step([$class: 'XrayImportBuilder', projectKey: pk, description: description, endpointName: '/junit/multipart', importFilePath: 'reports/*.xml', importInfo: info, inputInfoSwitcher: 'fileContent', serverInstance: xrayConnectorId])
    }
    stage('cleanWs') {
        echo "\n\nCleanWs"
        cleanWs()
    }
}
