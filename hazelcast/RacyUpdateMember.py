import hazelcast
import logging
import time
from Value import Value

logging.basicConfig(level=logging.INFO)

class RacyUpdateMember:
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
        print("Start Racy")
        for k in range(1000):
            value = map.get(key)
            time.sleep( 1 )
            value.amount = value.amount + 1
            map.put(key, value)

        print("Finished RacyUpdateMember! Result = {}".format(map.get(key).amount))


member1 = RacyUpdateMember()

while (True):
    time.sleep(100)