pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        echo 'Hello World'
        sh 'datadog-ci synthetics run-tests'
      }
    }

  }
}