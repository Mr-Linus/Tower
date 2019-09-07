from kubernetes import client, config


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

    def create_job(self, name, image, cmd, mount_path, path):
        container = client.V1Container(
            name=name,
            image=image,
            command=cmd,
            volume_mounts=client.V1VolumeMount(
                name=name+"volume",
                mount_path=mount_path,
            )
        )
        volume = client.V1Volume(
            name=name+"-volume",
            host_path=client.V1HostPathVolumeSource(
                path=path,
                type="Directory"
            )
        )
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(name=name, labels={"user": self.user}),
            spec=client.V1PodSpec(
                containers=[container],
                volumes=volume,
            )
        )
        spec = client.V1JobSpec(
            template=template
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


if __name__ == '__main__':
    k = K8sTask()
    k.user = 'root'
    k.namespace='test'
    # k.create_namespace()
    print(k.create_job("test_job", ))
    # for ns in k.get_user_namespace():
    #     print(ns.metadata.name)
