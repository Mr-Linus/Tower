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


if __name__ == '__main__':
    k = K8sTask()
    k.user='test'
    #k.create_namespace()
    print(k.get_user_namespace())
    # for ns in k.get_user_namespace():
    #     print(ns.metadata.name)
