node() {
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
        }
    }
}
