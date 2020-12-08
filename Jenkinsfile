node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        def branches = "${scm.branches}"
        if (branches.contains("master")) {
            git "${repoURL}"
        if (branches.contains("main")) {
            git branch: "main", url: "${repoURL}"
        }
    }
    stage("Prepare Workspace") {
        sh """
            pwd
            ls -l
            printenv | grep master
            printenv | grep main
        """
    }
}
