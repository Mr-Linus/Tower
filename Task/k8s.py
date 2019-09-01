from kubernetes import client, config


class K8sTask:

    def __init__(self):
        config.load_kube_config()

    def get_namespace(self):
        return client.CoreV1Api().list_namespace().items

    def create_namespace(self):
        return client.CoreV1Api().create_namespace()


if __name__ == '__main__':
    k = K8sTask()
    print(k.get_namespace())
