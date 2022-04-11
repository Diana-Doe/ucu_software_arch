import hazelcast
import logging
import time
from Value import Value

logging.basicConfig(level=logging.INFO)


class OptimisticMember:
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
        print("Started OptimisticMember")
        for k in range(1000):
            while True:
                old_value = map.get(key)
                new_value = Value(old_value)
                time.sleep( 1 )
                new_value.amount += 1
                if map.replace_if_same(key, old_value, new_value):
                    break
        print("Finished OptimisticMember! Result = {}".format(map.get(key).amount))


member3 = OptimisticMember()

while (True):
    time.sleep(100)
