from graphviz import Digraph

dot = Digraph(comment='Microservices Roadmap')

dot.node('microservices', 'Microservices')

dot.node('application', 'Application')
dot.edge('application', 'commons')
dot.node('commons', 'Commons')
dot.node('db', 'Database')
dot.edge('microservices', 'application')
dot.edge('application', 'Comunication')
dot.edge('application', 'db')



dot.node('infrastructure', 'Infrastructure')
dot.edge('microservices', 'infrastructure')
dot.node('gateway', 'Gateway')
dot.edge('infrastructure', 'gateway')

dot.node('observability', 'Observability')
dot.edge('microservices', 'observability')
dot.node('log', 'Logs')
dot.edge('observability', 'log')

dot.node('process', 'Process')
dot.edge('microservices', 'process')
dot.node('ci', 'Continuous Integration')
dot.node('cd', 'Continuous Delivery')
dot.edge('process', 'ci')
dot.edge('process', 'cd')









dot.render('images/roadmap.gv', view=True)  
'images/roadmap.gv.pdf'