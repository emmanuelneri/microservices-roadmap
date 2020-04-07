from graphviz import Digraph


class Infrastructure:

    def build(self, dot):
        dot.node('infrastructure', 'Infrastructure')

        dot.node('application-environment', 'Application Environment')
        dot.node('gateway', 'Gateway')
        dot.node('load-balance', 'Load Balance')
        dot.node('service-discovery', 'Service Discovery')
        dot.node('configuration', 'Configurations')

        dot.edge('infrastructure', 'application-environment')
        dot.edge('infrastructure', 'gateway')
        dot.edge('infrastructure', 'load-balance')
        dot.edge('infrastructure', 'service-discovery')
        dot.edge('infrastructure', 'configuration')
        dot.edge('infrastructure', 'auto-scaling')

        dot.edge('gateway', 'load-balance')
        dot.edge('load-balance', 'service-discovery')

        dot.node('container', 'container')
        dot.node('cloud-instance', 'Cloud Instance')
        dot.node('on-premise', 'OnPremise')
        dot.node('serveless', 'Serverless')
        dot.edge('application-environment', 'container')
        dot.edge('application-environment', 'cloud-instance')
        dot.edge('application-environment', 'on-premise')
        dot.edge('application-environment', 'serveless')

        dot.edge('container', 'orchestration')

        dot.node('environment', 'Environments')
        dot.node('secrets', 'Secrets')
        dot.edge('configuration', 'environment')
        dot.edge('configuration', 'secrets')

    