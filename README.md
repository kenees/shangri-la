# shangri-la
博客服务端

## 1. 表结构
### 1.1 blog_config表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
system_id | int | 唯一 | 主键 博客系统id
visitors_number | int | 不允许为空 | 系统访问人数
authority | varchar(255) | 不允许为空 | 博客

### 1.2 system_user表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
user_id | int | 唯一  | 主键 用户id
user_name | varchar(50) | 不允许为空 | 用户名
user_avatar | varchar(255) | null | 用户头像
password | varchar(20) | 不允许为空 | 密码
create_at | datetime | 不允许为空 | 创建时间
update_at | datetime | 不允许为空 | 更新时间
authority | varchar(255) | 不允许为空 | 用户权限json串
is_valid | boolean | 不允许为空  | 用户是否有效


### 1.3 blog_tag表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
tag_id | int | 唯一 | 主键 标签id
tag_name | varchar(20) | 不允许重复 | 标签名
is_valid | boolen |  不允许为空 | 是否有效
create_at | datetime | 不允许为空 | 创建时间
update_at | datetime | 不允许为空 | 更新时间


### 1.4 article表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
article_id | int | 唯一 | 主键 文章id
article_name | varchar(255) | 不允许为空 | 博客标题
article_tag | varchar(255) | | 博客标签 关联到blog_tag上
create_at | datetime | 不允许为空 | 创建时间
update_at | datetime | 不允许为空 | 更新时间
reading_number | int | 不允许为空 | 阅读量
edit_user | varchar(50) | 不允许为空 | 编辑者
comment_number | int |    | 评论数量


```
参考： https://blog.csdn.net/weixin_43681537/article/details/86080074
```

### 1.5 comment表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
comment_id | int | 唯一 | 主键，评论id
topic_id | int | 唯一 | 评论博客id  (id = 0 为留言信息)
content | varchar(255) | 不允许为空 | 评论内容
from_uid | int | 不允许为空 | 评论用户id
comment_date | datetime | 不允许为空 | 评论时间

### 1.6 reply表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
reply_id | int | 主键 | 回复id
comment_id | int | 唯一 | 回复评论的id
content | varchar(255) | 不允许为空 | 评论内容
from_uid | int | 不允许为空 | 评论用户id
comment_date | datetime | 不允许为空 | 评论时间


### 1.7 blog_visit访问用户
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
uid | int | 主键 | 访问用户id
user_name | varchar(32) | 用户名
system | varchar(32) | 用户系统
browser | varchar(32) | 浏览器
ip| varchar(16) | 用户ip
visitors_number | int | 不允许为空 | 访问次数
last_time | datetime | 不允许为空 | 最后访问时间
access_rights | boolean | 不允许为空 | 访问权限




### 1.8 Statistics 统计表
名称 | 类型 | 约束条件 | 说明
-|:-:|:-:|-:
id | int | 主键 | id
pv_h | int | | 历史总浏览量
pv_n | int | | 今日总浏览量
uv_h | int | | 历史总独立访客
uv_n | int | | 今日总独立访客
ip_h | int | | 总ip数
ip_n | int | | 今日新增ip数
vv_h | int | | 总访问次数
vv_n | int | | 今日新增访问数











--------------------
网站概况
https://web.umeng.com/main.php?c=site&a=frame&siteid=1254552353#!/1600408387143/site/overview/1/1254552353/2020-09-17/2020-09-17


----------------------- 数据展示 tab ---------------
总浏览量（今日上涨） |  总独立访客（今日上涨） |  总IP数（今日上涨）| 总访问次数（今日上涨）


浏览量（pv）: 用户每打开一个页面便记录1次PV (今日新增 | 历史累计)
独立访客（uv）: 1天内相同访客多次访问网站，只计算为1个独立访客。(今日新增| 历史累计)
访问次数(vv): 记录所有访客1天内访问了多少次您的网站，相同的访客有可能多次访问您的网站。(今日新增| 历史累计)
独立IP(IP): 同一个ip不论访问多少个页面，都算1个 （今日新增|历史累计）




--------------------- 折线图 -----------------------
今日
昨日
最近7天
最近30天
最近1年
          次数
           y/x 时间  00:00   01:00  02:00  ... 23:00
pv, uv, vv, ip
