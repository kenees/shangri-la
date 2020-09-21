# Model
## 常用约束
[] primary_key 主键
[] autoincrement 自动增量
[] unique  独特的
[] index 索引
[] nullable 可空的
[] default  默认
[] ForeignKey() 外键


## 字段类型
### 数字类型
Integer
Smilllnteger
Biginteger
Float
Numeric
### 字符类型，文本类型
String
Text
Unicode
Unicode Text
Boolean
时间类型
Date
Time
DateTime
Interval
LargeBinary


## 数据操作
db.create_all() 所有的表根据model 建立
db.drop_all() 把数据库的表全部删除
## 数据迁移
flask-migrate

### __tablename__ = 'config'   # 重新定义表名
### Model 继承
```
    class Animal(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        a_name = db.Column(db.String(16)


    class Dog(Animal):
        d_legs = db.Column(db.Integer, default=4)

    class Cat(Animal):
        c_cat = db.Column(db.String(32), default='fish')


    所有父类和子类都在一张表中 ， 即d_legs,c_cat 属性都加到Animal中， 
    往表中插入数据的时候，会导致数据错乱， 例如： dog的c_cat为fish(实际dog没有c_cat属性)

    解决方法： 抽象
    class Animal(db.Model):
        __abstract__ = True
        id = db.Column(db.Integer, primary_key=True)
        a_name = db.Column(db.String(16)
```

## 文档  sqlAlchemy,  flask-sqlAlchemy

## 数据库优化
    1. 怎么链接
    2. 连接多少个  mysql最多100个
    3. diango 和 flask 都有数据库连接池     
    
    
## 查询
    获取单个对象
        1. query.first()
        2. query.get()
        3. query.get_or_404
    获取结果集
        1. query.all()    列表  
        2. filter()       根据条件查询
            Dog.query.filter(Dog.id.__eq__(2))  # 查询id = 2的集
            Dog.query.filter(Dog.id < 2)  # 查询id < 2的集
            Dog.query.filter(Dog.name.contains('猫'))  # 查询name中包含猫的
            使用< > == 或者 __eq__,（等于） __lt__,（小于） __gt__(大于), __ge__（大于等于）, __le__,（小于等于） in_（在。。。中）, like（模糊查询）, endswith, startswith, contains（包含） 等魔术方法
             filter查询后获取的是 __str__输出的这个对象数据的sql
         注意： all（）获取的list没有filter方法， 要使用all，只能放在最后
        3. filter_by(),  筛选  
        4. offset()  # 偏移  offset 和 limit同时使用不区分顺序
        5. limit()  # 分页   offset 和 limit同时使用不区分顺序
        6. order_by()  # 排序   order_by比现在offset和limit前面使用
        7. get()   #
        8. first()
        9. paginate() # 分页 