from graphviz import Digraph


class Observability:

    def build(self, dot):
        dot.node('observability', 'Observability')
        
        dot.edge('observability', 'log')
        dot.edge('observability', 'metrics')
        dot.edge('observability', 'tracing')

        dot.node('log', 'Logs')
        dot.node('metrics', 'Metrics')
        dot.node('tracing', 'Tracing')
    

    