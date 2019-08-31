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

    def job_list(self):
        return client.BatchV1Api().list_job_for_all_namespaces().items

    def pod_list(self):
        return client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items

    def node_list(self):
        return client.CoreV1Api().list_node(watch=False).items

    def get_pod_name_with_job_uid(self, job_uid):
        for pod in client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items:
            if job_uid == pod.metadata.owner_references[0].uid:
                return pod.metadata.name

    def get_pod_name_with_job_name(self, job_name, job_namespace):
        job_uid = client.BatchV1Api().read_namespaced_job_status(job_name, job_namespace).metadata.uid
        for pod in client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items:
            if job_uid == pod.metadata.owner_references[0].uid:
                return pod.metadata.name
        return None



if __name__ == '__main__':
    k = K8S()
    print(k.node_list())