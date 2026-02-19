pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args  '-u root:root'   // lets it write in workspace if needed
    }
  }

  options {
    timestamps()
  }

  environment {
    PIP_DISABLE_PIP_VERSION_CHECK = "1"
    PYTHONDONTWRITEBYTECODE = "1"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          set -euxo pipefail
          python -V
          pip install --upgrade pip wheel setuptools

          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          else
            pip install pytest
          fi
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          set -euxo pipefail
          export PYTHONPATH="$PWD"
          mkdir -p reports
          pytest -q --junitxml=reports/pytest-junit.xml
        '''
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/pytest-junit.xml'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
    }
  }
}
