pipeline {
  agent any

  options {
    timestamps()
    ansiColor('xterm')
  }

  environment {
    VENV_DIR = ".venv"
    PIP_DISABLE_PIP_VERSION_CHECK = "1"
    PYTHONDONTWRITEBYTECODE = "1"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Set up Python venv') {
      steps {
        sh '''
          set -euxo pipefail

          # Try common python executables
          if command -v python3 >/dev/null 2>&1; then
            PY=python3
          elif command -v python >/dev/null 2>&1; then
            PY=python
          else
            echo "Python not found on agent"
            exit 1
          fi

          $PY -m venv "${VENV_DIR}"

          . "${VENV_DIR}/bin/activate"
          python -m pip install --upgrade pip wheel setuptools
        '''
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          set -euxo pipefail
          . "${VENV_DIR}/bin/activate"

          # If you have requirements.txt, use it; otherwise just install pytest
          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          else
            pip install pytest
          fi

          # For JUnit XML output support (pytest already supports it, no extra needed)
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          set -euxo pipefail
          . "${VENV_DIR}/bin/activate"

          # Ensure project root is on PYTHONPATH so "from mathutils_py import MathUtils" works
          export PYTHONPATH="$PWD"

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
      sh 'rm -rf .venv || true'
    }
  }
}
