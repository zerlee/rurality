from aliyunsdkecs.request.v20140526.DescribeEipAddressesRequest import DescribeEipAddressesRequest
from aliyunsdkecs.request.v20140526.AssociateEipAddressRequest import AssociateEipAddressRequest
from aliyunsdkecs.request.v20140526.UnassociateEipAddressRequest import UnassociateEipAddressRequest
from aliyunsdkecs.request.v20140526.ReleaseEipAddressRequest import ReleaseEipAddressRequest

from .base import AliyunCli


class AliyunEIP(AliyunCli):
    '''
    阿里云EIP
    '''
    def get_eips(self, page_num=1, page_size=20):
        request = DescribeEipAddressesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('EipAddresses')
        data_list = data.get('EipAddress')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def related_eip(self, instance_id, related_id):
        '''
        实例关联EIP
        instance_id: EIP ID
        related_id: 要关联eip对象的实例ID，例如ecs实例ID、slb实例ID
        '''
        request = AssociateEipAddressRequest()
        request.set_InstanceId(related_id)
        request.set_AllocationId(instance_id)
        self._request(request)

    def unrelated_eip(self, instance_id, related_id):
        '''
        实例取消关联EIP
        instance_id: EIP ID
        related_id: 要取消关联eip对象的实例ID，例如ecs实例ID、slb实例ID
        '''
        request = UnassociateEipAddressRequest()
        request.set_InstanceId(related_id)
        request.set_AllocationId(instance_id)
        self._request(request)

    def delete_eip(self, instance_id):
        '''
        删除EIP
        instance_id: EIP ID
        '''
        request = DescribeEipAddressesRequest()
        request.set_PageSize(page_size)
        request.set_AllocationId(instance_id)
        self._request(request)
