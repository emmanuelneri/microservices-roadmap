from graphviz import Digraph

dot = Digraph(comment='Microservices Roadmap')

dot.node('microservices', 'Microservices')

dot.node('application', 'Application')
dot.edge('microservices', 'application')
dot.node('db', 'Database')
dot.edge('application', 'db')

dot.node('stack', 'Stack')
dot.edge('application', 'stack')
dot.node('linguagens', 'Linguagens')
dot.node('framework', 'Frameworks')
dot.node('lib', 'Libs')
dot.edge('stack', 'linguagens')
dot.edge('stack', 'framework')
dot.edge('stack', 'lib')


dot.node('sql', 'SQL')
dot.node('nosql', 'NoSQL')
dot.node('cache', 'Cache')
dot.edge('db', 'sql')
dot.edge('db', 'nosql')
dot.edge('db', 'cache')


dot.edge('application', 'comunication')
dot.node('comunication', 'Comunication')
dot.node('synchronous', 'Synchronous')
dot.node('asynchronous', 'Asynchronous')
dot.edge('comunication', 'synchronous')
dot.edge('comunication', 'asynchronous')

dot.node('rest', 'Rest')
dot.node('graphql', 'GraphQL')
dot.node('grpc', 'gRPC')
dot.edge('synchronous', 'rest')
dot.edge('synchronous', 'graphql')
dot.edge('synchronous', 'grpc')

dot.node('queue', 'Queue')
dot.node('pub-sub', 'Publish-Subscribe')
dot.edge('asynchronous', 'queue')
dot.edge('asynchronous', 'pub-sub')

dot.node('infrastructure', 'Infrastructure')
dot.edge('microservices', 'infrastructure')
dot.node('provider', 'Provider')
dot.node('gateway', 'Gateway')
dot.node('service-discovery', 'Service Discovery')
dot.node('configuration', 'Configurations')
dot.edge('infrastructure', 'provider')
dot.edge('infrastructure', 'gateway')
dot.edge('infrastructure', 'service-discovery')
dot.edge('infrastructure', 'configuration')


dot.node('observability', 'Observability')
dot.edge('microservices', 'observability')
dot.node('log', 'Logs')
dot.node('metrics', 'Metrics')
dot.edge('observability', 'log')
dot.edge('observability', 'metrics')

dot.node('process', 'Process')
dot.edge('microservices', 'process')
dot.node('continuous-integration', 'CI')
dot.node('continuous-delivery', 'CD')
dot.edge('process', 'continuous-integration')
dot.edge('process', 'continuous-delivery')









dot.render('images/roadmap.gv', view=True)  
'images/roadmap.gv.pdf'