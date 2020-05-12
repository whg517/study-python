# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  export_to_pushgateway
@Date: 2019/2/15 14:21
@Description:
"""
import random
import time

__author__ = 'wanghuagang'

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Info, Summary, Counter, Histogram


# g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
# g.set_to_current_time()

# i = Info('my_build_version', 'Description of info', registry=registry)
# i.info({'version': '1.2.3', 'buildhost': 'foo@bar'})

def push(job, registry):
    """"""
    push_to_gateway('192.168.10.3:9091', job=job, registry=registry)


class Example(object):
    cls = None
    labelnames = ()

    def __init__(self, times=0):
        self.times = times

        self.registry = CollectorRegistry()
        self.obj = self.cls(f'test_{self.cls.__name__.lower()}', f'Description of {self.cls.__name__.lower()}',
                            labelnames=self.labelnames,
                            registry=self.registry)
        self.push()

    @property
    def random(self):
        return round(random.uniform(0, 10))

    def push(self):
        if self.times:
            for i in range(self.times):
                self._todo()
                print(f'executed {i + 1} times!')
                time.sleep(2)
        else:
            self._todo()
            print(f'executed !')

    def push_to_gateway(self):
        push_to_gateway('192.168.10.3:9091', job=self.cls.__name__.lower(), registry=self.registry)

    def _todo(self):
        self.todo()
        self.push_to_gateway()

    def todo(self):
        raise NotImplemented()


def counter_example():
    registry = CollectorRegistry()
    c = Counter('test_counter', 'Description of counter', registry=registry)
    c.inc(random.randint(0, 20))
    push_to_gateway('192.168.10.3:9091', job=Counter.__name__.lower(), registry=registry)


class CounterExample(Example):
    """
    一个计数器是代表一个累积指标单调递增计数器，它的值只能增加或在重新启动时重置为零。例如，您可以使用计数器来表示所服务的请求数，已完成的任务或错误。

    不要使用计数器来暴露可能减少的值。例如，不要使用计数器来处理当前正在运行的进程数; 而是使用仪表。

    """
    cls = Counter

    def todo(self):
        """"""
        self.obj.inc(self.random)


def summary_example():
    registry = CollectorRegistry()
    s = Summary('test_summary', 'Description of summary', registry=registry)
    s.observe(random.randint(0, 20))
    push_to_gateway('192.168.10.3:9091', job=Summary.__name__.lower(), registry=registry)


class SummaryExample(Example):
    """
    类似于直方图，summary(通常是请求持续时间和响应大小)。虽然它还提供了观察值的总数和所有观察值的和，
    但是它计算滑动时间窗口上的可配置分位数。
    基本度量名称为<basename>的summary在刮擦过程中暴露多个时间序列:
        - 流φ-quantiles(0≤φ≤1)观察到的事件,公开为< basename > {分位数= " <φ> " }
        - 所有观测值的总和，公开为<basename>_sum
        - 已观察到的事件的计数，公开为<basename>_count(与上面的<basename>_bucket{le=" Inf"}相同)
    """
    cls = Summary

    def todo(self):
        self.obj.observe(self.random)


def gauge_example():
    registry = CollectorRegistry()
    g = Gauge('test_gauge', 'Description of gauge', registry=registry)
    g.set(500)
    push_to_gateway('192.168.10.3:9091', job=Gauge.__name__.lower(), registry=registry)
    # g.inc(2)
    # push_to_gateway('192.168.10.3:9091', job=Gauge.__name__.lower(), registry=registry)
    # g.dec(1)
    # push_to_gateway('192.168.10.3:9091', job=Gauge.__name__.lower(), registry=registry)
    # # 5-2-1=6


class GaugeExample(Example):
    """
    gauge 是一个度量，它表示一个可以任意上下移动的数值。
    gauge 量规通常用于测量值，如温度或当前内存使用情况，但也用于“计数”，如并发请求的数量，可以上下浮动。
    """
    cls = Gauge

    def todo_set(self):
        """"""
        self.obj.inc(self.random)

    def todo_inc(self):
        """"""
        self.obj.set(self.random)

    def todo_dec(self):
        """"""
        self.obj.dec(self.random)

    def _todo(self):
        self.todo_inc()
        self.push_to_gateway()
        self.todo_dec()
        self.push_to_gateway()

    def push(self):
        """"""
        self.todo_set()
        super().push()


def histogram_example():
    registry = CollectorRegistry()
    h = Histogram('test_summary', 'Description of histogram', registry=registry)
    h.observe(2)
    push_to_gateway('192.168.10.3:9091', job=Histogram.__name__.lower(), registry=registry)


class HistogramExample(Example):
    """
    直方图对观察结果(通常是请求持续时间或响应大小)进行采样，并在可配置的bucket中对它们进行计数。它还提供了所有观测值的和。
    一个基本度量名称为<basename>的直方图在刮擦过程中暴露多个时间序列:
        - 观察桶的累积计数器，公开为<basename>_bucket{le="<上包界>"}
        - 所有观测值的总和，公开为<basename>_sum
        - 已观察到的事件的计数，公开为<basename>_count(与上面的<basename>_bucket{le=" Inf"}相同)

    使用histogram_quantile()函数从直方图甚至直方图的聚合中计算分位数。直方图也适用于计算Apdex评分。
    在bucket上操作时，请记住直方图是累积的。
    """
    cls = Histogram

    def todo(self):
        self.obj.observe(self.random)


def labels_example():
    registry = CollectorRegistry()
    g = Gauge('test_gauge', 'Description of gauge', labelnames=['label_name'], registry=registry)
    g.labels('label').set(5)
    push_to_gateway('192.168.10.3:9091', job=Gauge.__name__.lower(), registry=registry)


class LabelsExample(Example):
    cls = Gauge
    labelnames = ('label',)

    def todo(self):
        self.obj.labels('label_a').set(self.random)
        self.obj.labels('label_b').set(self.random)
        self.obj.labels('label_c').set(self.random)
        self.obj.labels('label_d').set(self.random)


def collector():
    registry = CollectorRegistry()
    g = Gauge('test_collector_gauge', 'Description of gauge', labelnames=['label_name'], registry=registry)
    g.labels('label').set(5)
    c = Counter('test_collector_counter', 'Description of counter', registry=registry)
    c.inc(random.randint(0, 20))
    push_to_gateway('192.168.10.3:9091', job='test_collector', registry=registry)


def test_character():
    registry = CollectorRegistry()
    g = Gauge('scheduler_enqueued', 'Description of gauge', labelnames=['label_name'], registry=registry)
    g.labels('label').set(5)
    push_to_gateway('192.168.10.3:9091', job='test_character', registry=registry)


def test_info():
    registry = CollectorRegistry()
    i = Info('test_info', 'desc', registry=registry)
    i.info({'version': '10'})
    push_to_gateway('192.168.10.3:9091', job='test_info', registry=registry)


if __name__ == "__main__":
    """"""
    # counter_example()
    # summary_example()
    # gauge_example()
    # histogram_example()
    # labels_example()

    # CounterExample(30)
    # SummaryExample(30)
    # GaugeExample(30)
    # HistogramExample(30)
    # LabelsExample(30)

    # collector()
    # test_character()

    test_info()
