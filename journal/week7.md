# Week 7 — Solving CORS with a Load Balancer and Custom Domain

## Homework Task Performed for Week 7

- **Created ALB for public accessibility and denying access to ECS from its public IPV4**
** **

![ALB   Rules](https://user-images.githubusercontent.com/125117631/230783261-91996c7b-0fd9-4b2d-a0c0-c7d288608f28.png)

- **Purchased domain on Route53 and issued public SSL certificate from ACM**
** **

![ACM](https://user-images.githubusercontent.com/125117631/230783323-30198ed9-6219-4cf8-8dec-bae29d334b70.png)

- **Setup record set as Alias for backend and frontend on Route53**
** **

![R53](https://user-images.githubusercontent.com/125117631/230783567-72ff31b7-46a1-48e2-a0d6-d0a178c079ae.png)

- **Created rules on ALB ensuring security via public issued SSL certificate**
** **

![ALB   Rules](https://user-images.githubusercontent.com/125117631/230783630-d6397589-c1f7-478d-b251-68535c82e0a7.png)

![ALB Rules 1](https://user-images.githubusercontent.com/125117631/230783590-a5201b0b-1b31-48ad-bc17-007db1687733.png)

![ALB Rules 2](https://user-images.githubusercontent.com/125117631/230783604-c7bcc7f1-07bc-40e2-89c1-0aff7be244fe.png)

- **Modified CORS by ensuring that traffic only comes from specific Route53 domain**
** **
