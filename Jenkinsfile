  pipeline
{
  agent any
  stages {
    stage('version') {
      steps {
       echo '123123'
       bat 'py -3.8 -m --version'
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
