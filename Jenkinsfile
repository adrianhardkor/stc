node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        git pull origin main "${repoURL}"
    }
    stage("Prepare Workspace") {
        sh """
            pwd
            ls -l
        """
    }
}
