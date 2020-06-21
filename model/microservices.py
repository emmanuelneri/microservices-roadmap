from graphviz import Digraph


class Microservices:

    def build(self, dot):
        dot.node('microservices', 'Microservices')
        
        dot.edge('microservices', 'application')
        dot.edge('microservices', 'infrastructure')
        dot.edge('microservices', 'observability')
        dot.edge('microservices', 'process')
        dot.edge('microservices', 'test')
    