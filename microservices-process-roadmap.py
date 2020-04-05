from graphviz import Digraph
from model.process import Process


dot = Digraph(comment='Microservices Process Roadmap', format='png')

process = Process()
process.build(dot)

dot.render('images/microservices-process-roadmap.gv')  
