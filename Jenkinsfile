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
            sh 'npm run datadog-ci-synthetics'
          }
        }

      }
    }

  }
}