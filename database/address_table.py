# coding=utf-8
from backend_common.models.address import Address


def migrate():
    if Address.table_exists():
        Address.drop_table()
    Address.create_table()
    from address import addresses
    records = []
    for (code, address) in addresses.iteritems():
        if code[4:6] != '00':
            province_code = code[0:2] + '0000'
            city_code = code[0:4] + '00'
            record = {'province_code': province_code, 'province': addresses.get(province_code), 'city_code': city_code, 'city': addresses.get(city_code), 'region_code': code, 'region': address}
            records.append(record)
    Address.insert_many(records).execute()
