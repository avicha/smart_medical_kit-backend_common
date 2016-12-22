# coding=utf-8
from backend_common.models.medical_kit_instance_setting import MedicalKitInstanceSetting


def migrate():
    if MedicalKitInstanceSetting.table_exists():
        MedicalKitInstanceSetting.drop_table()
    MedicalKitInstanceSetting.create_table()
