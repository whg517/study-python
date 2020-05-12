import time

from prometheus_client import start_wsgi_server, Counter
from prometheus_client.metrics_core import CounterMetricFamily

counter = Counter('demo', 'demo')

if __name__ == '__main__':
    start_wsgi_server(8087, '0.0.0.0')
    i = 0
    while 1:
        i += 1
        time.sleep(1)
        print(f'i = {i}')
        CounterMetricFamily('demo', 'demo', i)
