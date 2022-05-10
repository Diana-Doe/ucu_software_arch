import hazelcast
import logging
import time
from Value import Value

logging.basicConfig(level=logging.INFO)


class PessimisticUpdateMember:
    def __init__(self):
        hz = hazelcast.HazelcastClient(
            cluster_members=[
                "127.0.0.1:5701",

                "127.0.0.1:5702",

                "127.0.0.1:5703",
            ]
        )
        map = hz.get_map("map").blocking()
        key = "1"
        map.put(key, Value())
        print("Start PessimisticUpdateMember")
        for k in range(1000):
            map.lock(key)
            try:
                value = map.get(key)
                time.sleep(1)
                value.amount += 1
                map.put(key, value)
            finally:
                map.unlock(key)
        print("Finished PessimisticUpdateMember! Result = {}".format(map.get(key).amount))


member2 = PessimisticUpdateMember()


while (True):
    time.sleep(100)
