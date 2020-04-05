from graphviz import Digraph
from model.infrastructure import Infrastructure


dot = Digraph(comment='Microservices Infrastructure Roadmap', format='png')

infrastructure = Infrastructure()
infrastructure.build(dot)

dot.render('images/microservices-infrastructure-roadmap.gv')  
