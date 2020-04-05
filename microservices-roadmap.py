from graphviz import Digraph
from model.microservices import Microservices


dot = Digraph(comment='Microservices Roadmap', format='png')

root = Microservices()
root.build(dot)

dot.render('images/microservices-roadmap.gv')  
