"""
Get & Filter Queries Start.
"""
from typing import Optional

from django.db.models import QuerySet
from django.db.models import Q


def db_get_single_record_by_filters(model, filters):
    return model.objects.get(**filters)


def db_get_records_by_filters(
        model,
        q_filters: Q = None,
        filters: any = None,
        count: int = None,
        order_by: str = 'id',
        distinct: bool = False
):
    if q_filters:
        query = model.objects.filter(q_filters)
    else:
        query = model.objects.filter(**filters)

    if distinct:
        query = query.distinct()
    return query.order_by(order_by)[:count]


def db_get_records_by_filters_with_foreign_keys_and_look_ups(
        model: any,
        q_filters: Q = None,
        filters: dict = None,
        foreign_keys: list = None,
        look_ups: list = None,
        distinct: bool = False
):
    if filters is None:
        filters = dict()
    if foreign_keys is None:
        foreign_keys = list()
    if look_ups is None:
        look_ups = list()

    if q_filters:
        query = model.objects.filter(q_filters)
    else:
        query = model.objects.filter(**filters)

    query = query.distinct() if distinct else query
    return query.select_related(*foreign_keys).prefetch_related(*look_ups)


def db_filter_query_set(
        query_set,
        filters: Optional = None,
        q_filters: Q = None,
        distinct: bool = False
):
    if filters:
        query_set = query_set.filter(**filters)
    if q_filters:
        query_set = query_set.filters(q_filters)
    if distinct:
        query_set = query_set.distinct()
    return query_set.all()


def db_get_values_list(instance, filters: str = ""):
    return list(instance.values_list(filters, flat=True))


"""
Get & Filter Queries End.
"""


"""
Create Queries Start.
"""


def db_create_record(model, data: dict):
    return model.objects.create(**data)


def db_get_or_create_record(
        model=None, **filter_and_create_data
):
    filter_and_create_data.setdefault('defaults', {})

    return model.objects.get_or_create(**filter_and_create_data)


def db_bulk_create_records(model, data_list: list):
    record_list = [model(**record) for record in data_list]
    model.objects.bulk_create(record_list)


def db_add_many_to_many_field_data(
        instance,
        field: str,
        id_list: list
):
    getattr(instance, field).add(*id_list)
    return instance


"""
Create Queries End.
"""


"""
Update Queries Start.
"""


def db_update_records_by_filters(
        model: any,
        filters: dict,
        data: dict
):
    return model.objects.filter(**filters).update(**data)


def db_update_instance(
        instance, data: dict = None,
        foreign_key_data: dict = None,
        many_to_many_field: str = None,
        id_list: list = None
) -> None:
    if data:
        instance.__dict__.update(**data)
    if foreign_key_data:
        for foreign_key in foreign_key_data:
            setattr(instance, foreign_key, foreign_key_data[foreign_key])
    instance.save()

    if many_to_many_field:
        getattr(instance, many_to_many_field).add(*id_list)


"""
Update Queries End.
"""

"""
Delete Queries Start.
"""


def db_delete_instance(instance):
    instance.delete()


"""
Delete Queries End.
"""
