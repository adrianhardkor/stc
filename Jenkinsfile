node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        def branches_raw = $scm.branches[0]
        def String[]branches = branches_raw.split("/")
        echo "BRANCHES = ${branches}"
        git branch: "${scm.branches}", url: "${repoURL}"
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
