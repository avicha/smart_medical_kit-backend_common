# coding=utf-8
import backend_common.env as common_env
import database
import welink_sms
import weixin
import qiniu

# 环境变量
mode = common_env.APP_MODE
# 数据库配置
database = database.config(mode)
# welink短信配置
welink_sms = welink_sms.config(mode)
# 微信配置
weixin = weixin.config(mode)
# 七牛配置
qiniu = qiniu.config(mode)
