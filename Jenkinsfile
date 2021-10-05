pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            echo 'Hello World'
          }
        }

        stage('test') {
          steps {
            sh 'datadog-ci synthetics run-tests --config /root/datadog-ci.json'
          }
        }

      }
    }

  }
}