pipeline {
    agent any

    environment {
        APP_HOST = "10.0.9.6"
        APP_PATH = "/devnet-labs/lab-web-app"
        CRED_ID = "lab-devnet01-ssh"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kalebmohr/kmohr_lab_web_app.git'
            }
        }

        stage('Lint') {
            steps {
                sshagent(credentials: [env.CRED_ID]) {
                    sh "ssh root@${APP_HOST} 'cd ${APP_PATH} && pip install pylint && pylint src/app.py || true'"
                }
            }
        }

        stage('Unit Test') {
            steps {
                sshagent(credentials: [env.CRED_ID]) {
                    sh "ssh root@${APP_HOST} 'cd ${APP_PATH} && pip install -r src/requirements.txt && pytest src/tests/unit_test.py --maxfail=1 --disable-warnings -q'"
                }
            }
        }

        stage('System Test') {
            steps {
                sshagent(credentials: [env.CRED_ID]) {
                    sh """
                    ssh root@${APP_HOST} 'cd ${APP_PATH} && docker-compose up -d'
                    sleep 5
                    ssh root@${APP_HOST} 'curl -f http://localhost:5000 || (echo "System test failed!" && exit 1)'
                    ssh root@${APP_HOST} 'docker-compose down'
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                sshagent(credentials: [env.CRED_ID]) {
                    sh "ssh root@${APP_HOST} 'cd ${APP_PATH} && docker-compose up -d --build'"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded and deployed to ${APP_HOST}"
        }
        failure {
            echo "Pipeline failed. Check Jenkins logs for details."
        }
    }
}

