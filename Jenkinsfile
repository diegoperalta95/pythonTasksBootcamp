pipeline {
    agent: any

    stages {
        stage('Source'){
            steps {
                git 'https://github.com/diegoperalta95/pythonTasksBootcamp'
            }
        }

        stage('Check Format') {
            steps {
                script {
                    sh 'pip install pep8'
                    sh 'pep8 agenda.py'
                }
            }
        }
    }
}