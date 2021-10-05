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
    DATADOG_API_KEY = '226393fdc9e4468c8a8b379fabd53578'
    DATADOG_APP_KEY = 'dfc86914a775a501273612ca67b7c21a456918e7'
  }
}