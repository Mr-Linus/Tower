from kubernetes import client, config


class Service:
    def __init__(self):
        config.load_incluster_config()
        self.api = client.CustomObjectsApi()
        self.coreApi = client.CoreV1Api()

    def Create_Service(self, name, namespace, port):
        service = client.V1Service(
            kind="Service",
            api_version="v1",
            metadata=client.V1ObjectMeta(name=name,
                                         namespace=namespace),
            spec=client.V1ServiceSpec(
                selector={"bread": name},
                external_i_ps=["10.128.33.69"],
                ports=[client.V1ServicePort(name=name,
                                            protocol="TCP",
                                            port=22,
                                            target_port=port
                                            )]
            )
        )
        return self.coreApi.create_namespaced_service(namespace=namespace,
                                                      body=service)

    def Delete_Service(self, name, namespace):
        return self.coreApi.delete_namespaced_service(namespace=namespace,
                                                      name=name)

    def List_Service(self, namespace):
        return self.coreApi.list_namespaced_service(namespace).items

    def Number_Service(self, namespace):
        return len(self.coreApi.list_namespaced_service(namespace).items) == 0


if __name__ == '__main__':
    print(Service().Number_Service("root"))