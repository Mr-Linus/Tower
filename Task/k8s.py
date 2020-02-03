from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint


class K8sTask:
    namespace = ''
    user = ''

    def __init__(self):
        config.load_kube_config()

    def get_user_namespace(self):
        namespace = []
        for ns in client.CoreV1Api().list_namespace().items:
            if ns.metadata.labels is not None:
                if {"user": self.user} == ns.metadata.labels:
                    namespace.append(ns)
        return namespace

    def find_namespace(self):
        namespace = []
        for ns in client.CoreV1Api().list_namespace().items:
            if self.namespace in ns.metadata.name:
                namespace.append(ns)
        return namespace

    def create_namespace(self):
        info = client.V1Namespace(
            api_version="v1",
            kind="Namespace",
            metadata=client.V1ObjectMeta(name=self.namespace, labels={"user": self.user})
        )
        return client.CoreV1Api().create_namespace(body=info)

    def delete_namespace(self):
        return client.CoreV1Api().delete_namespace(self.namespace)

    def list_namespace(self):
        return client.CoreV1Api().read_namespace(self.namespace)

    def list_job(self):
        return client.BatchV1Api().list_job_for_all_namespaces().items

    def delete_job(self, name):
        return client.BatchV1Api().delete_namespaced_job(name=name, namespace=self.namespace)

    def create_job(self, name, image, cmd, path):
        container = client.V1Container(
            name=name,
            image=image,
            env=[client.V1EnvVar(
                name='PYTHONUNBUFFERED',
                value='0'
            )],
            command=cmd,
            volume_mounts=[client.V1VolumeMount(
                name=name+"-volume",
                mount_path="/root",
            )]
        )
        volume = client.V1Volume(
            name=name+"-volume",
            host_path=client.V1HostPathVolumeSource(
                path=path,
            )
        )
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(name=name, labels={"user": self.user}),
            spec=client.V1PodSpec(
                # 重启策略
                restart_policy="Never",
                containers=[container],
                volumes=[volume],
            )
        )
        spec = client.V1JobSpec(
            template=template,
            # 并行数
            parallelism=1,
            # 失败重启数
            backoff_limit=0,
        )
        job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(name=name),
            spec=spec
        )
        client.BatchV1Api().create_namespaced_job(
            namespace=self.namespace,
            body=job
        )

    def get_pod_name_with_job(self, job_name):
        job_uid = client.BatchV1Api().read_namespaced_job_status(job_name, self.namespace).metadata.uid
        for pod in client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items:
            if pod.metadata.owner_references is not None:
                if job_uid == pod.metadata.owner_references[0].uid:
                    return pod.metadata.name
        return None

    def get_pod_with_job(self, job_name):
        job_uid = client.BatchV1Api().read_namespaced_job_status(job_name, self.namespace).metadata.uid
        for pod in client.CoreV1Api().list_pod_for_all_namespaces(watch=False).items:
            if pod.metadata.owner_references is not None:
                if job_uid == pod.metadata.owner_references[0].uid:
                    return pod
        return None

    def log_job(self, name):
        return client.CoreV1Api().read_namespaced_pod_log(
            name=self.get_pod_name_with_job(job_name=name),
            namespace=self.namespace,
        )

    def info_job(self, name):
        return client.BatchV1Api().read_namespaced_job(
            name=name,
            namespace=self.namespace
        )


if __name__ == '__main__':
    k = K8sTask()
    k.user = 'root'
    k.namespace = 'test'
    k.create_namespace()
    print()
    # try:
    #     api_response = k.log_job('test')
    #     pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling CoreV1Api->read_namespaced_pod_log: %s\n" % e)

    # for ns in k.get_user_namespace():
    #     print(ns.metadata.name)
