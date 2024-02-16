pipeline
{
  agent any
  stages {
    stage('version') {
      steps {
       'python --version'
      }
    }
     stage('build') {
      steps {
        script{
          sh 'python -m pip install --upgrade pip'
          sh 'pip install -r requirements.txt'
        }
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python script.py'
      }
    }
  }
}
