node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        echo "BRANCHES = ${scm.branches}"
        git branch: "main", url: "${repoURL}"
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
