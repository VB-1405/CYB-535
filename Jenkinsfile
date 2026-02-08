pipeline {
    agent {
        docker {
            image 'my-jenkins-controller:latest' // Use your custom image with all tools pre-installed
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket for inner Docker commands
        }
    }
    tools {
        // This is not needed if sonar-scanner is installed in the custom image
        // and we are using `docker.image().inside()` for analysis.
        // Keeping it commented out for clarity if user expects it.
        // sonarScanner 'MySonarQube'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/VB-1405/Jenkins-Pipeline.git'
            }
        }

        stage('Run Python Tests') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv'
                    // Install build tools into the virtual environment
                    sh 'venv/bin/pip install pytest coverage'
                    // Run pytest with coverage and generate JUnit-compatible XML report
                    sh 'venv/bin/python -m coverage run -m pytest Basic_Python/test_math_utils.py --junitxml=report.xml'
                    sh 'venv/bin/python -m coverage xml -o coverage.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publish JUnit test results
                junit 'report.xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // We use withCredentials to securely pass the SonarQube token.
                    withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                        // Run sonar-scanner inside a Docker container
                        docker.image('sonarsource/sonar-scanner-cli').inside {
                            // Ensure sonar-project.properties is in the workspace
                            sh "sonar-scanner -Dsonar.host.url=http://172.17.0.3:9000 -Dsonar.login=$SONAR_TOKEN"
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') { // Set a reasonable timeout
                    // Pause the pipeline until quality gate status is retrieved
                    // This step requires the SonarQube plugin configured in Jenkins.
                    // The 'MySonarQube' here refers to the server name configured in Manage Jenkins -> Configure System
                    // waitForQualityGate is a step provided by the SonarQube Scanner for Jenkins plugin.
                    def qg = waitForQualityGate statusRecorders: [[credentialsId: 'sonarqube-token', sonarServerName: 'MySonarQube']]
                    if (qg.status != 'OK') {
                        error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    }
                }
            }
        }

        stage('Artifact Generation') {
            steps {
                script {
                    // Create a zip archive of the Basic_Python directory
                    sh 'zip -r PythonMathUtils.zip Basic_Python'
                }
            }
        }
    }
}
