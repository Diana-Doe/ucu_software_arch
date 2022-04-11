# ucu_software_arch

### Task 3
Distributed Map distributes the elements almost equally between all nodes:
![Screenshot from 2022-04-05 16-30-25](https://user-images.githubusercontent.com/54356826/162747167-1f11c08a-41ad-456e-bf0b-e4ee53f04f80.png)

If you delete node, the items will be divided between the other two nodes:
![Screenshot from 2022-03-28 18-21-25](https://user-images.githubusercontent.com/54356826/162747128-5fe3b5c0-6a8e-4d46-b96d-a838e1ce1437.png)


### Task 4
OptimisticMember will stuck if you run it a bit later than others. PessimisticUpdateMember can be run a bit later, than it will return uncorrect result, but won't stuck.
![Screenshot from 2022-04-11 14-42-43](https://user-images.githubusercontent.com/54356826/162746569-f2ea8af2-cb3a-4d7e-bec6-c98f681fae6b.png)

### Task 5
When we try to add more than 10 items to a bounded queue (max 10), which doesn't have listeners, the error will be raised, but the queue will contain the first 10 items.
![Screenshot from 2022-04-11 15-06-38](https://user-images.githubusercontent.com/54356826/162746448-258ac7b5-8c2b-4350-b4df-4f06cf902c44.png)
