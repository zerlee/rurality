from base.api import BaseApi
from business.service.controllers import asset_obj as asset_obj_ctl


class CreateServiceAssetObjApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'asset_id': ('资产模块ID', 'required int'),
        'asset_obj_id': ('资产实例ID', 'required int'),
    }
    def post(self, request, params):
        data = asset_obj_ctl.create_service_asset_obj(**params)
        return data


class DeleteServiceAssetObjApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'asset_id': ('资产模块ID', 'required int'),
        'asset_obj_id': ('资产实例ID', 'required int'),
    }
    def post(self, request, params):
        data = asset_obj_ctl.delete_service_asset_obj(**params)
        return data


class ListServiceAssetObjApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = asset_obj_ctl.get_service_asset_objs(**params)
        return data
