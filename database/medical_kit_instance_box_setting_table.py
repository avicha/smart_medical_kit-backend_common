# coding=utf-8
from backend_common.models.medical_kit_instance_box_setting import MedicalKitInstanceBoxSetting


def migrate():
    if MedicalKitInstanceBoxSetting.table_exists():
        MedicalKitInstanceBoxSetting.drop_table()
    MedicalKitInstanceBoxSetting.create_table()
