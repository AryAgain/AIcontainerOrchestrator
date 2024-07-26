import joblib
import requests
import time
from kubernetes import client, config

# Load the trained model
model = joblib.load('path/to/your/model.joblib')

# Initialize Kubernetes client
config.load_kube_config()
v1 = client.AppsV1Api()

# Function to fetch metrics from Prometheus
def fetch_metrics():
    response = requests.get('http://localhost:9090/api/v1/query', params={'query': 'container_memory_usage_bytes{pod=~"service-a.*"}'})
    results = response.json()['data']['result']
    # Aggregate or average the memory usage if there are multiple pods
    memory_usage = sum([float(result['value'][1]) for result in results]) / len(results)
    
    # Fetch CPU usage as well (adjust the Prometheus query as needed)
    response_cpu = requests.get('http://localhost:9090/api/v1/query', params={'query': 'container_cpu_usage_seconds_total{pod=~"service-a.*"}'})
    results_cpu = response_cpu.json()['data']['result']
    cpu_usage = sum([float(result['value'][1]) for result in results_cpu]) / len(results_cpu)
    
    return cpu_usage, memory_usage

# Function to get current number of replicas
def get_current_replicas(deployment_name):
    deployment = v1.read_namespaced_deployment(name=deployment_name, namespace='default')
    return deployment.spec.replicas

# Function to scale deployment
def scale_deployment(deployment_name, replicas):
    body = {'spec': {'replicas': replicas}}
    v1.patch_namespaced_deployment_scale(name=deployment_name, namespace='default', body=body)

# Function to predict and make scaling decision
def predict_and_scale(deployment_name):
    cpu_usage, memory_usage = fetch_metrics()
    prediction = model.predict([[cpu_usage, memory_usage]])[0]
    
    current_replicas = get_current_replicas(deployment_name)
    
    if prediction == 'H':
        new_replicas = current_replicas * 2
        print(f"High utilization detected. Scaling up to {new_replicas} replicas.")
        scale_deployment(deployment_name, new_replicas)
    elif prediction == 'L':
        new_replicas = max(1, current_replicas // 2)
        print(f"Low utilization detected. Scaling down to {new_replicas} replicas.")
        scale_deployment(deployment_name, new_replicas)
    else:
        print("Medium utilization detected. No scaling action needed.")

if __name__ == "__main__":
    deployment_name = 'service-a'  # Name of Kubernetes deployment
    
    while True:
        predict_and_scale(deployment_name)
        time.sleep(60)  # Fetch metrics and make scaling decisions every 60 seconds