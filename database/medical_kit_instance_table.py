# coding=utf-8
from backend_common.models.medical_kit_instance import MedicalKitInstance


def migrate():
    if MedicalKitInstance.table_exists():
        MedicalKitInstance.drop_table()
    MedicalKitInstance.create_table()
    MedicalKitInstance.create(id=136581, product_code=13658, purchase_channel=1)
    MedicalKitInstance.create(id=762431, product_code=76243, purchase_channel=1)
    MedicalKitInstance.create(id=169851, product_code=16985, purchase_channel=1)
