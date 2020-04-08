from graphviz import Digraph


class Application:

    def build(self, dot):
        dot.node('application', 'Application')        

        dot.edge('application', 'stack')
        dot.edge('application', 'db')
        dot.edge('application', 'data-management')  
        dot.edge('application', 'monitoring')
        dot.edge('application', 'comunication')
        dot.edge('application', 'consistency')

        dot.node('stack', 'Stack')
        dot.node('linguagens', 'Linguagens')
        dot.node('framework', 'Frameworks')
        dot.node('lib', 'Libs')
        dot.edge('stack', 'linguagens')
        dot.edge('stack', 'framework')
        dot.edge('stack', 'lib')

        dot.node('db', 'Database')
        dot.node('sql', 'SQL')
        dot.node('nosql', 'NoSQL')
        dot.node('cache', 'Cache')
        dot.edge('db', 'sql')
        dot.edge('db', 'nosql')
        dot.edge('db', 'cache')

        dot.node('data-management', 'Datamanagement')
        dot.node('cqrs', 'CQRS')
        dot.node('event-sourcing', 'Event Sourcing')
        dot.edge('data-management', 'cqrs')
        dot.edge('data-management', 'event-sourcing')

        dot.node('monitoring', 'Monitoring')
        dot.node('health-check', 'Health Check')
        dot.node('app-metrics', 'Metrics')
        dot.edge('monitoring', 'health-check')
        dot.edge('monitoring', 'app-metrics')


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
        dot.node('tolerant-reader', 'tolerant-reader')
        dot.edge('pub-sub', 'idempotent')
        dot.edge('pub-sub', 'deduplicate')
        dot.edge('pub-sub', 'tolerant-reader')

        dot.edge('application', 'fault-tolerance')
        dot.node('fault-tolerance', 'Fault Tolerance')
        dot.node('app-circuit-breaker', 'Circuit Breaker')
        dot.node('dlq', 'Dead Letter Queues')
        dot.node('retry', 'Retry')

        dot.node('consistency', 'Consistency')
        dot.node('eventual-consistency', 'eventual consistency')
        dot.node('saga', 'SAGA')
        dot.edge('consistency', 'eventual-consistency')
        dot.edge('consistency', 'saga')

        dot.edge('fault-tolerance', 'app-circuit-breaker')
        dot.edge('fault-tolerance', 'dlq') 
        dot.edge('fault-tolerance', 'retry') 
    