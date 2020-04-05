from graphviz import Digraph
from model.application import Application


dot = Digraph(comment='Microservices Application Roadmap', format='png')

application = Application()
application.build(dot)

dot.render('images/microservices-application-roadmap.gv')  
