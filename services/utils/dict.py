# coding=utf-8


def pick(source_dict, *fields, **opts):
    allow_field_not_exists = opts.get('allow_field_not_exists', True)
    target_dict = {}
    for field in fields:
        if source_dict.has_key(field) or allow_field_not_exists:
            target_dict[field] = source_dict.get(field)
    return target_dict
