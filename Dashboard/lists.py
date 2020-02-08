from kubernetes import client, config


class K8sList:

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


class BreadTask:
    group = 'core.run-linux.com'
    version = 'v1alpha1'

    def __init__(self):
        config.load_kube_config()
        self.api = client.CustomObjectsApi()

    def Creat_Bread(self, name, namespace, gpu, mem, level,
                    framework, version, task_type, path, command):
        body = {
            "apiVersion": "core.run-linux.com/v1alpha1",
            "kind": "Bread",
            "metadata": {
                "name": name,
                "namespace": namespace,
            },
            "spec": {
                "scv": {
                    "gpu": gpu,
                    "memory": mem,
                    "level": level,
                },
                "framework": {
                    "name": framework,
                    "version": version
                },
                "task": {
                    "type": task_type,
                    "path": path,
                    "command": command
                }
            }
        }
        self.api.create_namespaced_custom_object(
            group=self.group,
            version=self.version,
            namespace=namespace,
            plural="breads",
            body=body,
        )

    def Get_Bread(self, name, namespace):
        return self.api.get_namespaced_custom_object(
            group=self.group,
            version=self.version,
            namespace=namespace,
            plural="breads",
            name=name
        )

    def Get_Bread_Status(self, name, namespace):
        return self.api.get_namespaced_custom_object_status(
            group=self.group,
            version=self.version,
            namespace=namespace,
            plural="breads",
            name=name
        )["status"]

    def Delete_Bread(self, name, namespace):
        self.api.delete_namespaced_custom_object(
            group=self.group,
            version=self.version,
            namespace=namespace,
            plural="breads",
            name=name,
            body=client.V1DeleteOptions(),
        )

    def List_Bread(self, namespace):
        return self.api.list_namespaced_custom_object(
            group=self.group,
            version=self.version,
            namespace=namespace,
            plural="breads",
        )['items']

    def Get_Pod_Logs(self, name, namespace):
        return client.CoreV1Api().read_namespaced_pod_log(
            name=name,
            namespace=namespace,
        )

    def Get_Pod_Info(self, name, namespace):
        return client.CoreV1Api().read_namespaced_pod(
            name=name,
            namespace=namespace,
        )


if __name__ == '__main__':
    pass
