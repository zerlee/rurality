from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetModel
from business.service.models import ServiceAssetObjModel
from asset.manager.models import AssetModel
from utils.onlyone import onlyone


def create_service_asset_obj(obj_id, environment_id, asset_id, asset_obj_id, operator=None):
    '''
    创建服务关联资产实例
    '''
    query = {
        'service_id': obj_id,
        'asset_id': asset_id,
    }
    if not ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务需要先关联此资产模块')
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'asset_id': asset_id,
        'asset_obj_id': asset_obj_id,
    }
    if ServiceAssetObjModel.objects.filter(**query).exists():
        raise errors.CommonError('服务已关联此资产实例')
    data = query
    obj = base_ctl.create_obj(ServiceAssetObjModel, data, operator)
    data = obj.to_dict()
    return data


def delete_service_asset_obj(obj_id, environment_id, asset_id, asset_obj_id, operator=None):
    '''
    删除服务关联资产实例
    '''
    query = {
        'service_id': obj_id,
        'asset_id': asset_id,
    }
    if not ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务需要先关联此资产模块')
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'asset_id': asset_id,
        'asset_obj_id': asset_obj_id,
    }
    obj = ServiceAssetObjModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('服务未关联此资产实例')
    base_ctl.delete_obj(ServiceAssetObjModel, obj.id, operator)


def get_service_asset_objs(obj_id, environment_id, asset_id, page_num=None, page_size=None, operator=None):
    '''
    获取服务关联资产实例列表
    '''
    batch_ids = ServiceAssetObjModel.objects.filter(service_id=obj_id)\
            .values_list('asset_id', flat=True).all()

    base_query = AssetModel.objects.filter(id__in=batch_ids)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
