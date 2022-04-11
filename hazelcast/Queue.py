import hazelcast
import logging
import time

logging.basicConfig(level=logging.INFO)

class Queue():
    def __init__(self):
        hz_client = hazelcast.HazelcastClient(
            cluster_members=[
                "127.0.0.1:5701",
            ]
        )
        queue_client = hz_client.get_queue("queue").blocking()

        hz_listener = hazelcast.HazelcastClient(
            cluster_members=[
                "127.0.0.1:5702",

                "127.0.0.1:5703",
            ]
        )

        queue_l = hz_listener.get_queue("queue").blocking()
        queue_client.clear()

        for i in range(100):
            queue_client.add(i)
            print(queue_l.take())


lim_queue = Queue()

while (True):
    time.sleep(100)

