node() {
    def String jenkinsenv
    stage('git clone') {
        git 'https://pl-acegit01.as12083.net/wopr/stc.git'
    }
    stage("Prepare Workspace") {
        def os = System.properties['os.name'].toLowerCase()
        echo "\n\n\n\nPrepare Workspace for '${os}'"
        if (os.contains("mac")) {
            env.WORKSPACE_LOCAL = sh(returnStdout: true, script: 'pwd').trim()
            passthruString = sh(script: "printenv", returnStdout: true)
            passthruString = passthruString.replaceAll('\n',' jenkins_')
            echo "${passthruString}"
            env.BUILD_TIME = "${BUILD_TIMESTAMP}"
            sh '''
                SUDO_ASKPASS=/usr/local/bin/pw.sh sudo -A python3 -m pip install --upgrade pip
                SUDO_ASKPASS=/usr/local/bin/pw.sh sudo -A python3 -m pip install -r requirements.txt
            '''
        }
        if (os.contains("windows")) {
            env.WORKSPACE_LOCAL = bat(returnStdout: true, script: 'echo %cd%').trim()
            passthruString = bat(script: "set", returnStdout: true)
            passthruString = passthruString.replaceAll('\n',' jenkins_')
            bat 'python -m pip install -q -r requirements.txt'
            env.BUILD_TIME = "${BUILD_TIMESTAMP}"
            echo "Workspace set to:" + env.WORKSPACE_LOCAL
            echo "Build time:" + env.BUILD_TIME
        }
    }
    stage('Behave-BDD.py') {
        def os = System.properties['os.name'].toLowerCase()
        echo "\n\nBehave-BDD for ${os}:"
        def WORKSPACE = "${env.WORKSPACE}"
        echo "env.WORKSPACE = ${env.WORKSPACE}"
        if (os.contains("linux")) {
            def xrayConnectorId = "${xrayConnectorId}"
            if (xrayConnectorId.contains("32cbc650-7dab-4522-9a52-336df2c2c24d")) {
                 echo "\n\n RUNNING BOB XRAYCONNECTORID = 32cbc650-7dab-4522-9a52-336df2c2c24d"
                 try {
                    sh """
                        export PYTHONPATH=.:/usr/lib/python3/dist-packages:${env.PWD}
                        export STC_PRIVATE_INSTALL_DIR=${STC_PRIVATE_INSTALL_DIR}
                        printenv | grep PYTHONPATH
                        ${behave_loc} --format=cucumber_jsonW:PrettyCucumberJSONFormatter -o target/cucumber.json --format=json -o target/behave.json --junit
                    """
                } catch (error) {
                    emailext attachLog: true, body: "Build failed (see ${env.BUILD_URL}): ${error}", subject: "[JENKINS] ${env.JOB_NAME} failed", to: 'adrian.krygowski@wowinc.com'
                } finally {
                    junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
                    echo "\n\t*** RAN JUNIT ***"
                }
            } else {
                try {
                    sh """
                        export STC_PRIVATE_INSTALL_DIR=${STC_PRIVATE_INSTALL_DIR}
                        export PYTHONPATH=.:/usr/lib/python3/dist-packages
                        printenv | grep PYTHONPATH
                        ${behave_loc} --format=cucumber_jsonW:PrettyCucumberJSONFormatter -o target/cucumber.json --format=json -o target/behave.json --junit
                    """
                } catch (error) {
                    emailext attachLog: true, body: "Build failed (see ${env.BUILD_URL}): ${error}", subject: "[JENKINS] ${env.JOB_NAME} failed", to: 'adrian.krygowski@wowinc.com'
                } finally {
                    junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
                    echo "\n\t*** RAN JUNIT ***"
                }
            }
        }
        if (os.contains("mac")) {
            if (WORKSPACE.contains("navid")) {
                try {
                    sh """
                        export PYTHONPATH=.
                        ${behave_loc} --format=cucumber_jsonW:PrettyCucumberJSONFormatter -o target/cucumber.json  --format=json -o target/behave.json --junit
                    """
                } catch (error) {
                    emailext attachLog: true, body: "Build failed (see ${env.BUILD_URL}): ${error}", subject: "[JENKINS] ${env.JOB_NAME} failed", to: 'adrian.krygowski@wowinc.com'
                } finally {
                    junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
                }
            } else {
                try {
                    sh """
                        export PYTHONPATH=.
                        ${behave_loc} --format=cucumber_jsonU:PrettyCucumberJSONFormatter -o target/cucumber.json  --format=json -o target/behave.json --junit
                    """
                } catch (error) {
                    emailext attachLog: true, body: "Build failed (see ${env.BUILD_URL}): ${error}", subject: "[JENKINS] ${env.JOB_NAME} failed", to: 'adrian.krygowski@wowinc.com'
                } finally {
                    junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
                    echo "\n\t*** RAN JUNIT ***"
                }
            }
        }
        if (os.contains("windows")) {
            try {
                bat """
                    set PYTHONPATH=.
                    set | findstr PYTHONPATH
                    ${behave_loc} --format=cucumber_jsonW:PrettyCucumberJSONFormatter -o target/cucumber.json  --format=json -o target/behave.json --junit
                """
            } catch (error) {
                emailext attachLog: true, body: "Build failed (see ${env.BUILD_URL}): ${error}", subject: "[JENKINS] ${env.JOB_NAME} failed", to: 'adrian.krygowski@wowinc.com'
            } finally {
                junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'reports/*.xml'
                echo "\n\t*** RAN JUNIT ***"
            }
        }
    }
    stage('Import results to Xray') {
        echo "\n\n\n*** Entering the Import results to Xray Stage ***"
        def description = "[TEST_BUILD_URL|${env.BUILD_URL}]"
        def labels = '["regression","automated_regression"]'
        def environment = "DEV"
        def testExecutionFieldId = 10552
        def testEnvironmentFieldName = "customfield_10372"
        def projectKey = "Xray-Test"
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
            echo "${info}"
            step([$class: 'XrayImportBuilder', endpointName: '/cucumber/multipart', importFilePath: 'target/cucumber.json', importInfo: info, inputInfoSwitcher: 'fileContent', serverInstance: xrayConnectorId])
        }
    stage('cleanWs') {
        echo "\n\nCleanWs"
        cleanWs()
    }
}
