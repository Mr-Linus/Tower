from kubernetes import client, config


class Service:
    def __init__(self):
        config.load_kube_config()
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
                                            port=port,
                                            target_port=22
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

    def Max_Port(self):
        portMax = 0
        for s in self.coreApi.list_service_for_all_namespaces().items:
            if 11000 <= s.spec.ports[0].port <= 19000:
                if s.spec.ports[0].port > portMax:
                    portMax = s.spec.ports[0].port
        return portMax


if __name__ == '__main__':
    print(Service().Max_Port())
