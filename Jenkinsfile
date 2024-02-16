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
          bat 'python3 -m pip install --upgrade pip'
          bat 'pip3 install -r requirements.txt'
        }
        bat 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python3 script.py'
      }
    }
  }
}
