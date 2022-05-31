# Homework 5
Team: Diana Hromyk

## Before starting services
Run Hazelcast and consul in the console.

Run ```consul_controller.py``` beforehead, as it contains some setups for consul


### Test code
1. POST 10 messages:

![image](https://user-images.githubusercontent.com/54356826/171204995-a5605b6e-ecba-4834-963b-c0b44c49c99b.png)

Facade service randomly chooses one logging service from services registred in consul:

![image](https://user-images.githubusercontent.com/54356826/171205176-151fe2a1-6402-4c94-ba64-337f30d7d40a.png)

2. GET messages:

![image](https://user-images.githubusercontent.com/54356826/171205512-deea08c2-f9c1-4395-9170-9902b472c63e.png)


Facade service randomly chooses one logging service and one message service from services registred in consul:

![image](https://user-images.githubusercontent.com/54356826/171205642-f18a481d-75e0-4750-90d4-1a3d6aab8418.png)

![image](https://user-images.githubusercontent.com/54356826/171205674-1f31f71f-785b-4ed7-bece-1d7438f756b0.png)

3. Shut down one message service and two logging services

![image](https://user-images.githubusercontent.com/54356826/171205864-0aeed95b-4f5d-4284-a13f-f696941f2f62.png)
