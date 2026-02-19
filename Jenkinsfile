pipeline {
    agent any

    stages {
        stage('Build and Test Python') {
            steps {
                dir('Basic Python') {
                    script {
                        echo '--- Building and Testing Python ---'
                        // Ensure python and pip are available. You may need to use 'python3' or 'pip3'
                        sh 'pip install pytest'
                        // The --junitxml flag creates a report Jenkins can read
                        sh 'pytest --junitxml=../python-test-results.xml'
                    }
                }
            }
        }

        stage('Build and Test Java') {
            steps {
                dir('JavaProject') {
                    script {
                        echo '--- Building and Testing Java ---'
                        // This assumes you have a Maven tool configured in Jenkins
                        // Go to Manage Jenkins -> Global Tool Configuration to set it up
                        def mvnHome = tool 'Maven'  // Use the name you gave your Maven config
                        sh "${mvnHome}/bin/mvn clean install"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                echo '--- Archiving Test Results ---'
                junit 'python-test-results.xml'
                junit 'JavaProject/target/suref
