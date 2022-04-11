import hazelcast
import logging

logging.basicConfig(level=logging.INFO)



client = hazelcast.HazelcastClient(

    cluster_members=[

        "127.0.0.1:5701",

        "127.0.0.1:5702",

        "127.0.0.1:5703",

    ]

)

my_map = client.get_map("my_map").blocking()

for i in range(1000):
    my_map.lock(i)
    try:
        my_map.set(i, "val")
    finally:
        my_map.unlock(i)

for i in range(1000):
    print(my_map.get(i))
