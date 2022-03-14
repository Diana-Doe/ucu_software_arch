# ucu_software_arch

![image](https://user-images.githubusercontent.com/54356826/158179298-bfc65bd4-4bfa-4d79-b1ff-38e93db1477a.png)


#### You can use Requests.http to post or get messages
### POST
Add messages, facade service will generates POST requests to login service (returns success if POST succeeded):
![image](https://user-images.githubusercontent.com/54356826/158178391-1a83aa3f-1c65-46bc-a6d2-fa697402f60c.png)

### GET
Get messages (all messages in one string),facade service will generates GET requests to login service (returns string with messages) and to messages service (is not implemented yet). 
![image](https://user-images.githubusercontent.com/54356826/158178518-3c3ae4cb-66c8-47cd-bfd7-422c26376872.png)
