# ucu_software_arch
# 3 Homework
Team: Diana Hromyak

### Added multiple logging services. Logging_controller_threads.py is just an attemt to use threads, main code is in logging_controller
### Added hazelcast map to logging service

## Usage
1) Runned 3 logging services on ports 5001, 5002, 5003 with different nodes in hz map
![image](https://user-images.githubusercontent.com/54356826/167625349-c9dcfac9-ac3e-4705-8958-f0d9522dde20.png)

2) Post 10 messages 

![image](https://user-images.githubusercontent.com/54356826/167625884-c51883d4-1ddb-4b37-8db7-cb8430297c55.png)


(as you can see, the distribution is not very uniform)

![image](https://user-images.githubusercontent.com/54356826/167625937-35323907-e937-41d7-8488-947fc855b83d.png)
![image](https://user-images.githubusercontent.com/54356826/167625964-1d385755-ebd6-4567-af83-cbb6ecdf9f2b.png)
![image](https://user-images.githubusercontent.com/54356826/167625982-30e7d8be-5913-4ce6-8cfd-1c67eef4b1e4.png)

3) Get messages. You can see all 10 messages

![image](https://user-images.githubusercontent.com/54356826/167626117-e0c2a86f-75a4-4f24-a3b3-10b50f152e7c.png)


4) Remove member with the biggest number of entries. You can see that all entries were saved in other members.

![image](https://user-images.githubusercontent.com/54356826/167626269-c07e6616-a526-4652-aa65-12ac84bd0842.png)
![image](https://user-images.githubusercontent.com/54356826/167626359-8f6756ad-0ed3-4dc5-a3a7-65ac089666c6.png)


5) Left only one member

![image](https://user-images.githubusercontent.com/54356826/167626405-53b88d60-d937-4c8b-884b-1f7a063be1f1.png)
![image](https://user-images.githubusercontent.com/54356826/167626435-c2362cbd-508c-4fcb-b44a-044ed880e890.png)



