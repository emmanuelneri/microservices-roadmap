from graphviz import Digraph
from model.microservices import Microservices
from model.process import Process
from model.application import Application
from model.infrastructure import Infrastructure
from model.observability import Observability


dot = Digraph(comment='Microservices Roadmap', format='png')

root = Microservices()
root.build(dot)

application = Application()
application.build(dot)

infrastructure = Infrastructure()
infrastructure.build(dot)

observability = Observability()
observability.build(dot)

process = Process()
process.build(dot)

dot.render('images/roadmap.gv', view=True)  
