from kubernetes import client, config


class K8S:

    def __init__(self):
        config.load_kube_config()

    def pod_num(self):
        return len(client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items)

    def node_num(self):
        return len(client.CoreV1Api().list_node(watch=False).items)

    def namespace_num(self):
        return len(client.CoreV1Api().list_namespace().items)

    def job_num(self):
        return len(client.BatchV1Api().list_job_for_all_namespaces().items)


if __name__ == '__main__':
    k = K8S()
    print(k.pod_num(), k.node_num(), k.namespace_num(), k.job_num())
