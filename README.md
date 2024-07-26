# Container Orchestration using AI


## Overview

This project aims to develop an AI agent that orchestrates the containers of an application based on historical datasets such as CPU utilization and memory usage. The AI agent is trained using scikit-learn and Python, and it scales the Kubernetes pods dynamically to manage resources efficiently and reduce costs.

---

## Setting Up the Environment

### Prerequisites

1. **Python 3.x**
2. **Kubernetes cluster (Minikube)**
3. **Prometheus and Grafana for monitoring** (helm package manager can be used)

### Step-by-Step Setup

1. **Clone the repository:**

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set up a Python virtual environment:**

   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**

   ```sh
   pip install cachetools certifi charset-normalizer google-auth idna joblib kubernetes numpy oauthlib pandas pyasn1 pyasn1_modules python-dateutil pytz PyYAML requests requests-oauthlib rsa scikit-learn scipy six threadpoolctl tzdata urllib3 websocket-client
   ```

### Installed Packages

- cachetools 5.4.0
- certifi 2024.7.4
- charset-normalizer 3.3.2
- google-auth 2.32.0
- idna 3.7
- joblib 1.4.2
- kubernetes 30.1.0
- numpy 2.0.0
- oauthlib 3.2.2
- pandas 2.2.2
- pip 24.1.2
- pyasn1 0.6.0
- pyasn1_modules 0.4.0
- python-dateutil 2.9.0.post0
- pytz 2024.1
- PyYAML 6.0.1
- requests 2.32.3
- requests-oauthlib 2.0.0
- rsa 4.9
- scikit-learn 1.5.1
- scipy 1.14.0
- six 1.16.0
- threadpoolctl 3.5.0
- tzdata 2024.1
- urllib3 2.2.2
- websocket-client 1.8.0

---

## Running the AI Agent

### Step-by-Step Execution

1. **Deploy the dummy container:**

   ```sh
   kubectl apply -f memory_stress_container/memory-stress-deployment.yaml
   kubectl apply -f memory_stress_container/memory-stress-service.yaml
   ```

2. **Deploy the service:**

   ```sh
   kubectl apply -f serviceA/service_deployment.yaml
   ```

3. **Run the memory load job:**

   ```sh
   kubectl apply -f serviceA/memory-load-job.yaml
   ```

4. **Run the AI core script:**

   ```sh
   python ai_core.py
   ```

### Monitoring and Scaling

- **Fetch metrics:** The script periodically fetches metrics from Prometheus every 60 seconds.
- **Scaling Decision:** The AI model predicts the current state and scales the pods:
  - **High utilization:** Doubles the number of pods.
  - **Low utilization:** Halves the number of pods, maintaining a minimum of one pod.
  - **Medium utilization:** No scaling action is taken.
