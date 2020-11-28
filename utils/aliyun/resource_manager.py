from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkresourcemanager.request.v20200331.ListResourceGroupsRequest import ListResourceGroupsRequest
from aliyunsdkresourcemanager.request.v20200331.GetResourceGroupRequest import GetResourceGroupRequest
from aliyunsdkresourcemanager.request.v20200331.CreateResourceGroupRequest import CreateResourceGroupRequest

from .base import AliyunCli


class AliyunResourceManager(AliyunCli):
    '''
    阿里云资源管理
    调试接口地址：https://api.aliyun.com/#/?product=ResourceManager&version=2020-03-31
    '''

    def get_resource_groups(self, page_num=1, page_size=20):
        '''
        获取资源组列表
        '''
        request = ListResourceGroupsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('ResourceGroups')
        data_list = data.get('ResourceGroup')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_resource_group(self, instance_id):
        '''
        获取资源组信息
        '''
        request = GetResourceGroupRequest()
        request.set_accept_format('json')
        request.set_ResourceGroupId(instance_id)
        data = self._request(request)
        data = data.get('ResourceGroup')
        return data

    def create_resource_group(self, name, display_name):
        '''
        创建资源组
        name: 资源组唯一标识
        display_name: 用于展示的名称
        '''
        request = CreateResourceGroupRequest()
        request.set_accept_format('json')
        request.set_Name(name)
        request.set_DisplayName(display_name)
        data = self._request(request)
        data = data.get('ResourceGroup')
        return data
