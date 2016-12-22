#### 数据表编号

表名|编号|意义
----|----|----
admins|001|管理员
users|002|用户
user_tokens|003|用户令牌
addresses|004|地址
user_addresses|005|用户地址
products|006|产品
skus|007|最小库存管理单元
orders|008|订单
order_skus|009|订单购买的sku
medical_kit|010|药盒
medical_kit_instance|011|药盒实例
medical_kit_instance_setting|012|药盒实例设置
medical_kit_instance_box_setting|013|药盒实例盒子设置

#### 错误码
错误码由HTTP状态码+数据表编号组成，代表哪个表出现什么类型错误，常见HTTP错误码如下：

错误码|意义
------|----
400|传递参数错误 
401|未授权访问或者修改资源
402|未付款
403|禁止访问或者修改资源
404|找不到资源
