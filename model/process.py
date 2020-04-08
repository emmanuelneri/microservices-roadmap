from graphviz import Digraph


class Process:

    def build(self, dot):
        dot.node('process', 'Process')

        dot.edge('process', 'continuous-integration')
        dot.edge('process', 'continuous-delivery')
        dot.edge('process', 'deploy')


        dot.node('deploy', 'deploy')

        dot.node('blue-green-deployment', 'Blue/Green Deployment')
        dot.node('canary-release', 'Canary release')

        dot.edge('deploy', 'blue-green-deployment')
        dot.edge('deploy', 'canary-release')





    