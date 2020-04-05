from graphviz import Digraph


class Process:

    def build(self, dot):
        dot.node('process', 'Process')

        dot.edge('process', 'continuous-integration')
        dot.edge('process', 'continuous-delivery')
    