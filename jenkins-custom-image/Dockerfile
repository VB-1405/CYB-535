# Start from the official Jenkins LTS controller image
FROM jenkins/jenkins:lts

# Switch to root user to install system packages
USER root

# Install common build tools, Python, Docker CLI, and Sonar Scanner
# Use -y --no-install-recommends to keep image size down
RUN apt-get update && 
    apt-get install -y --no-install-recommends 
    sudo 
    python3 
    python3-pip 
    python3-venv 
    wget 
    unzip 
    lsb-release 
    curl 
    docker.io && 
    rm -rf /var/lib/apt/lists/*

# Install SonarQube Scanner CLI
ARG SONAR_SCANNER_VERSION=5.0.1.3006
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip -P /opt && 
    unzip /opt/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip -d /opt/ && 
    mv /opt/sonar-scanner-${SONAR_SCANNER_VERSION}-linux /opt/sonar-scanner && 
    ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner && 
    rm /opt/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip

# Switch back to the default Jenkins user (jenkins)
USER jenkins
