from kubernetes import client, config

def restart_deployment(deployment_name: str, namespace="default"):
    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()

    api = client.AppsV1Api()

    deployment = api.read_namespaced_deployment(
        name=deployment_name,
        namespace=namespace
    )

    # Trigger rolling restart
    deployment.spec.template.metadata.annotations = {
        "kubectl.kubernetes.io/restartedAt": "now"
    }

    api.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=deployment
    )

    print(f"♻️ Restart triggered for deployment: {deployment_name}")
