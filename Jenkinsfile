pipeline
{
  agent any
  stages {
    stage('version') {
      steps {
       bat 'python --version'
      }
    }
     stage('build') {
      steps {
        script{
          bat 'python -m pip install --upgrade pip'
          bat 'pip install -r requirements.txt'
        }
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python script.py'
      }
    }
  }
}
