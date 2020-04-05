from graphviz import Digraph
from model.observability import Observability


dot = Digraph(comment='Microservices Observability Roadmap', format='png')

observability = Observability()
observability.build(dot)

dot.render('images/microservices-observability-roadmap.gv')  
