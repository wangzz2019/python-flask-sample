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
            sh '''cd /root
npm run datadog-ci-synthetics'''
          }
        }

      }
    }

  }
}