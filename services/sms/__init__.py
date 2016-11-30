# coding=utf-8

from welink_sms_service import WelinkSMSService


def sendMessage(phone_number, message):
    import config.welink as config
    service = WelinkSMSService(config)
    return service.sendMessage(phone_number, message)
