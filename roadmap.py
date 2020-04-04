from graphviz import Digraph

dot = Digraph(comment='Microservices Roadmap', format='png')

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

dot.edge('application', 'monitoring')
dot.node('monitoring', 'Monitoring')
dot.node('health-check', 'Health Check')
dot.node('app-metrics', 'Metrics')
dot.edge('monitoring', 'health-check')
dot.edge('monitoring', 'app-metrics')


dot.edge('application', 'comunication')
dot.node('comunication', 'Comunication')
dot.node('synchronous', 'Synchronous')
dot.node('asynchronous', 'Asynchronous')
dot.edge('comunication', 'synchronous')
dot.edge('comunication', 'asynchronous')

dot.node('grpc', 'gRPC')
dot.node('http', 'HTTP')
dot.edge('synchronous', 'http')
dot.edge('synchronous', 'grpc')

dot.node('rest', 'Rest')
dot.node('graphql', 'GraphQL')
dot.edge('http', 'rest')
dot.edge('http', 'graphql')

dot.node('queue', 'Queue')
dot.node('pub-sub', 'Publish-Subscribe')
dot.edge('asynchronous', 'queue')
dot.edge('asynchronous', 'pub-sub')

dot.node('queue-transaction', 'Message Transaction')
dot.edge('queue', 'queue-transaction')

dot.node('idempotent', 'Idempotent Consumer')
dot.node('deduplicate', 'Deduplicate-message')
dot.edge('pub-sub', 'idempotent')
dot.edge('pub-sub', 'deduplicate')

dot.edge('application', 'fault-tolerance')
dot.node('fault-tolerance', 'Fault Tolerance')
dot.node('app-circuit-breaker', 'Circuit Breaker')
dot.node('dlq', 'Dead Letter Queues')
dot.edge('fault-tolerance', 'app-circuit-breaker')
dot.edge('fault-tolerance', 'dlq')

dot.node('infrastructure', 'Infrastructure')
dot.edge('microservices', 'infrastructure')
dot.node('application-environment', 'Application Environment')
dot.node('gateway', 'Gateway')
dot.node('service-discovery', 'Service Discovery')
dot.node('configuration', 'Configurations')
dot.edge('infrastructure', 'application-environment')
dot.edge('infrastructure', 'gateway')
dot.edge('infrastructure', 'service-discovery')
dot.edge('infrastructure', 'configuration')
dot.edge('infrastructure', 'auto-scaling')

dot.node('container', 'container')
dot.node('cloud-instance', 'Cloud Instance')
dot.node('on-premise', 'OnPremise')
dot.node('serveless', 'Serverless')
dot.edge('application-environment', 'container')
dot.edge('application-environment', 'cloud-instance')
dot.edge('application-environment', 'on-premise')
dot.edge('application-environment', 'serveless')

dot.node('environment', 'Environments')
dot.node('secrets', 'Secrets')
dot.edge('configuration', 'environment')
dot.edge('configuration', 'secrets')


dot.node('orchestration', 'orchestration')
dot.edge('container', 'orchestration')

dot.node('observability', 'Observability')
dot.edge('microservices', 'observability')
dot.node('log', 'Logs')
dot.node('metrics', 'Metrics')
dot.node('tracing', 'Tracing')
dot.edge('observability', 'log')
dot.edge('observability', 'metrics')
dot.edge('observability', 'tracing')

dot.node('process', 'Process')
dot.edge('microservices', 'process')
dot.node('continuous-integration', 'CI')
dot.node('continuous-delivery', 'CD')
dot.edge('process', 'continuous-integration')
dot.edge('process', 'continuous-delivery')

dot.render('images/roadmap.gv', view=True)  
