node() {
    def repoURL = "https://github.com/adrianhardkor/stc.git"
    stage('git clone') {
        echo "\n\n\n GIT CLONE STAGE"
        def branch = $scm.branches[0]
        echo "BRANCHES = ${branch}"
        git branch: "${branch}", url: "${repoURL}"
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
