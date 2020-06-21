from graphviz import Digraph


class Test:

    def build(self, dot):
        dot.node('test', 'Test')

        dot.edge('test', 'component-test')
        dot.edge('test', 'contract-test')
        dot.edge('test', 'end-to-end-test')

        dot.node('component-test', 'Component Test')
        dot.node('contract-test', 'Contract Test')
        dot.node('end-to-end-test', 'end-to-end Test')



    