# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKitInstance(BaseModel):
    product_code = IntegerField()
    purchase_channel = IntegerField()
    order_id = IntegerField(null=True)
    code = '011'

    class Meta:
        db_table = 'medical_kit_instances'

    def setting(self, fields=['id', 'prompt_sound']):
        from medical_kit_instance_setting import MedicalKitInstanceSetting as MedicalKitInstanceSettingModel
        setting = MedicalKitInstanceSettingModel.select().where(MedicalKitInstanceSettingModel.medical_kit_instance_id == self.id, MedicalKitInstanceSettingModel.deleted_at == None).first()
        return setting.format(fields) if setting else None

    def box_settings(self, box_count, fields=['id', 'box_index', 'medical_name', 'medical_barcode', 'schedule_times', 'piece_per_time', 'unit']):
        from medical_kit_instance_box_setting import MedicalKitInstanceBoxSetting as MedicalKitInstanceBoxSettingModel
        q = MedicalKitInstanceBoxSettingModel.select().where(MedicalKitInstanceBoxSettingModel.medical_kit_instance_id == self.id, MedicalKitInstanceBoxSettingModel.deleted_at == None)
        settings = []
        for x in q:
            settings.append(x.format(fields))
        result = []
        for i in range(0, box_count):
            try:
                box_setting = next(setting for setting in settings if setting.get('box_index') == i+1)
            except StopIteration, e:
                medical_kit_instance_box_setting = MedicalKitInstanceBoxSettingModel(medical_kit_instance_id=self.id, box_index=i+1)
                box_setting = medical_kit_instance_box_setting.format(fields)
            finally:
                box_setting['schedule_times'] = box_setting.get('schedule_times').split(',') if box_setting.get('schedule_times') else []
                result.append(box_setting)
        return result
