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
  environment {
    DATADOG_API_KEY = '2xxx'
    DATADOG_APP_KEY = 'xxx'
  }
}