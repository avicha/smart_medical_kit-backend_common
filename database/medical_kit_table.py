# coding=utf-8
from backend_common.models.medical_kit import MedicalKit


def migrate():
    if MedicalKit.table_exists():
        MedicalKit.drop_table()
    MedicalKit.create_table()
    MedicalKit.create(product_code=13658, name='智能药盒（纯白版）', image='', box_count=8)
    MedicalKit.create(product_code=76243, name='智能药盒（粉红版）', image='', box_count=8)
    MedicalKit.create(product_code=16985, name='智能药盒（天蓝版）', image='', box_count=8)
