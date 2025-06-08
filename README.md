# Text Translator – Cloud Deployment using Docker, Jenkins & AWS

## Project Overview
This project showcases the complete DevOps lifecycle for a Flask-based multilingual text translator. The application is **containerized using Docker**, deployed on **AWS EC2**, and managed via a **CI/CD pipeline using Jenkins**.

## Prerequisites
Before you begin, ensure you have the following installed:

- Git: For version control.
- GitHub Account: To access and clone the repository.

## 1. Application Overview

**LangSha: Text Translator** is a web-based application built with the following tech stack:

- **Backend**: Flask  
- **Translation Engine**: `googletrans==4.0.0-rc1`  
- **Frontend**: HTML templates (Jinja2)  
- **GitHub Repo**: [LangSha--Text-Translator](https://github.com/Shristi-17/LangSha--Text-Translator)

The application detects the input text language and translates it into a user-selected target language.

## 2. Cloning the Repository

```bash
git clone https://github.com/Shristi-17/LangSha--Text-Translator.git
cd LangSha--Text-Translator
```

## 3. Docker Containerization

The application is containerized for portability and consistent deployment.

**Key Components**
- Dockerfile: Builds the container with Flask and dependencies.
- requirements.txt: Flask, googletrans==4.0.0-rc1

**Build the Docker Image**
```bash
docker build -t langsha-translator .
```

**Run the Docker Container**
```bash
docker run -d -p 5000:5000 langsha-translator
```

## 4. Deployment on AWS EC2

**Step 4.1: Launch EC2 Instance**
- AMI: Ubuntu 20.04
- Instance Type: t2.micro (Free tier eligible)
- Ports Opened:
  - `22: SSH (your IP only)`
  - `5000: App access (from anywhere)`

EC2 Instances created will look like this:

![Image](https://github.com/user-attachments/assets/ba2a7e5b-8801-4424-8e80-a621b91363d2)

**Step 4.2: Install Docker & Jenkins**
SSH into the instance:
```bash
ssh -i your-key.pem ubuntu@<EC2-IP>
```

Install Docker:
```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

Install Jenkins
```bash
sudo apt install -y openjdk-11-jdk
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
```
Access Jenkins at:
`http://<EC2-IP>:8080`

## 5. CI/CD with Jenkins
**Step 5.1: Plugin Setup**
Install the following plugins in Jenkins:
- Git Plugin
- Docker Pipeline
- Pipeline

**Step 5.2: Jenkinsfile**
Add a Jenkinsfile to the GitHub repo with the following structure:
```bash
pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Shristi-17/LangSha--Text-Translator.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('langsha-translator')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 langsha-translator'
            }
        }
    }
}
```

**Step 5.3: Create Jenkins Pipeline Job**
- Create a new pipeline job in Jenkins. Be careful when adding the file name, it is case sensitive.
- Point it to the GitHub repo containing the `Jenkinsfile`.
- After creation, build the pipeline. It will look like this:
  
![Image](https://github.com/user-attachments/assets/5d31d0cd-faf3-4419-bd4c-a897652cff06)

## 6. Testing the Deployment
Once the container is running:
- Open your browser
- Navigate to:
`http://<EC2-Public-IP>:5000`
You should see the LangSha Translator UI, ready to detect and translate text in real time.

## 7. Cleanup Resources (Only when needed)
To stop the running container:
```bash
docker ps
docker stop <container-id>
```
To remove AWS EC2 instance:
- Go to AWS EC2 Console → Instances → Terminate

---

Hope it helped :)
