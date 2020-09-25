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
- 輸出
    - 默认输出字典，可以直接进行序列化
    - 如果包含对象
        - 默认会抛出异常， 对象不可JSON序列化
    - 使用格式化工具
        - marshal 函数
        - marshal_with 装饰圈
        - 条件
            - 格式
                - 字典格式
                - 允许被嵌套
                - value是fields.xxx
            - 数据
                - 允许任何格式
            - 如果格式和格式完全对应，数据就是预期格式
            - 如果格式比数据中的字段多， 程序依然正常运行， 不存在的字段是默认值
            - 如果格式比数据中的字段少， 程序依然正常运行， 少的字段不会显示
            - 以格式的模版为主
            
         - 结论
            - 想要什么格式的返回
            - 格式工具（模板）就是什么打样的
            - 和传入的数据没什么直接关系
         - 格式和数据的映射
            - 格式中的字段名和数据中的字段名需要一致， 
              - 可通过attribute更改返回字段名
            - 也可以都对属性指定默认值
                - default
                - 指定默认值， 值传递使用传进来的值
                - 未传递， 则使用默认