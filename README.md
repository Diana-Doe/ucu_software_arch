# ucu_software_arch
## Homework 4
Team: Diana Hromyak


1. POST 10 messages, they should be distributed between 3 logging services(which put them into map) and put into queue by facade service

![image](https://user-images.githubusercontent.com/54356826/169817669-c6c0cd40-10f1-41a4-a313-b6d63883f832.png)

Just to make sure that different logging services worked:
![image](https://user-images.githubusercontent.com/54356826/169817978-0d9f1b42-26c7-46d9-ac46-bb0f9a5b3cc6.png)

![image](https://user-images.githubusercontent.com/54356826/169818271-3d80153b-8b20-489d-a54f-e0616005f77b.png)

2. GET this messages. We can see that messages which we get from logging service and which are saved in map - are randomly ordered. But messages which we get throught message service are sorted, as we get them from map.

![image](https://user-images.githubusercontent.com/54356826/169818348-58c47320-c582-4043-b704-d319beabce63.png)

To make sure that facade chose only one message service (port 5004): 

![image](https://user-images.githubusercontent.com/54356826/169818707-a527cf8a-902f-40b7-954f-8f4453b2bb35.png)


![image](https://user-images.githubusercontent.com/54356826/169818666-a1e80398-119f-46e0-9f82-0af669db30d8.png)

3. Turn off port 5004, try to get message again (before that POST messages again, as queue is empty now):
![image](https://user-images.githubusercontent.com/54356826/169818855-51ab1dbe-ee46-4429-8b25-c590de748fb3.png)

![image](https://user-images.githubusercontent.com/54356826/169819104-84dac587-b088-4540-8f34-27021d031824.png)

![image](https://user-images.githubusercontent.com/54356826/169818907-3e764968-be70-4dbd-90b4-4064fca29ffa.png)



