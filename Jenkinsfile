node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    def branches = ${scm.branches}
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        echo "BRANCHES = ${branches}[0]"
        git branch: "${scm.branches}[0]", url: "${repoURL}"
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
