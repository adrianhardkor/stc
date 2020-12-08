node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        git "${repoURL}"
    }
    stage("Prepare Workspace") {
        sh """
            pwd
            ls -l
        """
    }
}
