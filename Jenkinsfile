node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage("Prepare Workspace") {
        sh """
            git pull ${repoURL}
            pwd
            ls -l
        """
    }
}
