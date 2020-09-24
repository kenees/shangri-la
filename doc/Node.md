## 钩子函数
- 面向切面编程
- 动态介入请求
- before_request
- after_request
- 可以做数据统计，判断是否登录..

## Django的请求流程
- client -> process_request[]
- 逐一进行process_request
- process_request -> urls
- urls -> process_view[]
- 逐一进行process_view
- process_view -> views
- views -> models
- models -> views
- views -> response
- response -> process_response[]
- 逐一进行process_response


## 四大内置对象
- g 全局变量，
    - 可以跨函数传递数据
    - 简介传递数据
- config:  
    - AppConfig里的值 ， 可以全局获取配置，在templates中可以直接获取， 
    - 在python中通过current_app.config获取
    - 一定是在项目启动之后调用
    
    
## 用户激活
- 邮箱
    - 异步发送邮件
    - 在邮件中包含激活地址
        - 激活地址接受一个一次性的token
        - token是用户注册的时候生产的， 存在了cache中
        - key-value
            - key： token
            - value 用户的唯一标识
            
- 短信
    - 同步操作


## flask-RESTful
 