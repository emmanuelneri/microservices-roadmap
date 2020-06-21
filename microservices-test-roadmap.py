from graphviz import Digraph
from model.test import Test


dot = Digraph(comment='Microservices Test Roadmap', format='png')

test = Test()
test.build(dot)

dot.render('images/microservices-test-roadmap.gv')  
