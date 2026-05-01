**🚀 AI DevOps Mini Project**

📌 Overview

This project demonstrates an end-to-end DevSecOps pipeline that automates the build, deployment, and exposure of a Flask-based AI monitoring application using Jenkins, Docker, and Kubernetes.
The application simulates log generation and uses simple AI logic to detect system anomalies in real-time.

<img width="1726" height="778" alt="image" src="https://github.com/user-attachments/assets/66042956-e15f-4cf1-91f9-86f99b1351ab" />

⚙️ Architecture
GitHub
   ↓
Jenkins (CI/CD Pipeline)
   ↓
Docker Build
   ↓
Kubernetes Deployment
   ↓
Service (NodePort)
   ↓
Port Forward
   ↓
ngrok (Public URL)
   ↓
User Browser

🔄 CI/CD Workflow
	1.	Developer pushes code to GitHub
	2.	Jenkins pipeline is triggered
	3.	Docker image is built
	4.	Image is deployed to Kubernetes
	5.	Kubernetes creates/updates pods
	6.	Application exposed using Service
	7.	ngrok provides public access


🧠 Features
	•	🔍 AI-based log analysis (simulated)
	•	⚙️ Automated CI/CD pipeline
	•	📦 Dockerized application
	•	☸️ Kubernetes deployment with rolling updates
	•	🌐 Public access using ngrok
	•	🔁 Self-healing pods in Kubernetes

📂 Project Structure
ai-mini-app/
├── app/                # Flask application
├── docker/             # Dockerfile
├── k8s/                # Kubernetes manifests
├── Jenkinsfile         # CI/CD pipeline
├── README.md           # Documentation
└── .gitignore

▶️ How to Run Locally

1️⃣ Start Kubernetes Deployment
kubectl apply -f k8s/

2️⃣ Port Forward Service
kubectl port-forward service/ai-app-service 8081:80

3️⃣ Expose via ngrok
ngrok http 8081

4️⃣ Access Application

Open the ngrok URL in your browser.

📸 Sample Output
	•	Displays system status (Healthy / Warning / Error)
	•	Shows AI-based insights
	•	Displays real-time logs

⸻

⚠️ Challenges Faced
	•	Debugging Kubernetes pod failures (CrashLoopBackOff)
	•	Fixing Docker build and dependency issues
	•	Resolving Gunicorn configuration errors
	•	Handling port-forward instability
	•	Managing Minikube networking limitations

⸻

🚀 Future Improvements
	•	📊 Add Prometheus & Grafana monitoring
	•	🔐 Integrate Trivy for image security scanning
	•	🌍 Replace ngrok with Kubernetes Ingress
	•	📈 Add Horizontal Pod Autoscaler (HPA)
	•	📦 Use Helm charts for deployment

⸻

🏆 Key Learnings
	•	End-to-end CI/CD automation
	•	Docker image lifecycle
	•	Kubernetes deployment & debugging
	•	Service exposure techniques
	•	Production vs development server differences

⸻

👨‍💻 Author

**Bertram Russell**

⸻

⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to fork or contribute!
