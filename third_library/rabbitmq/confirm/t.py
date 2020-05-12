import pika, sys
from pika import spec

# 在"/"虚拟主机vhost上通过用户guest建立channel通道
user_name = 'guest'
user_passwd = 'guest'
target_host = 'localhost'
vhost = '/'
cred = pika.PlainCredentials(user_name, user_passwd)
conn_params = pika.ConnectionParameters(target_host,
                                        virtual_host=vhost,
                                        credentials=cred)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()


# 定义消息发布后publisher接受到的确认信息处理函数
def confirm_handler(frame):
    if type(frame.method) == spec.Confirm.SelectOk:
        """生产者创建的channel处于‘publisher comfirms’模式"""
    elif type(frame.method) == spec.Basic.Nack:
        """生产者接受到消息发送失败并且消息丢失的消息"""
    elif type(frame.method) == spec.Basic.ack:
        if frame.method.delivery_tag in msg_ids:
            """生产者接受到成功发布的消息"""

            msg_ids.remove(frame.method.delivery_tag)

        # 将生产者创建的channel处于"publisher confirms"模式


channel.confirm_delivery(callback=confirm_handler)

# # 创建一个direct类型的、持久化的、没有consumer时队列是否自动删除的exchage交换机
# channel.exchange_declare(exchange='hello-exch',
#                          type='direct',
#                          passive=False,
#                          durable=True,
#                          auto_delete=False)
# # 使用接收到的信息创建消息
# # 使用接收到的信息创建消息
# msg = sys.argv[1]
# msg_props = pika.BasicProperties()
# msg_props.content_type = 'text/plain'
# # 持久化消息
# msg_props.delivery_mode = 2
msg_ids = []
#
#
# # 发布消息
# channel.basic_publish(body=msg,
#                       exchange='hello-exch',
#                       properties=msg_props,
#                       routing_key='hala')
#
# msg_ids.append(len(msg_ids) + 1)

channel.close()
conn_broker.close()