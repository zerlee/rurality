from aliyunsdkr_kvstore.request.v20150101.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkr_kvstore.request.v20150101.DescribeSecurityIpsRequest import DescribeSecurityIpsRequest
from aliyunsdkr_kvstore.request.v20150101.DescribeAccountsRequest import DescribeAccountsRequest

from .base import AliyunCli


class AliyunRedis(AliyunCli):
    '''
    阿里云redis
    '''
    def get_redis_list(self, page_num=1, page_size=30):
        '''
        '''
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Instances')
        data_list = data.get('KVStoreInstance')

        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_redis_white_list(self, instance_id):
        '''
        获取Redis白名单
        '''
        request = DescribeSecurityIpsRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)
        data = self._request(request)
        data = data.get('SecurityIpGroups')
        data_list = data.get('SecurityIpGroup')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_redis_accounts(self, instance_id):
        '''
        获取Redis账户列表
        '''
        request = DescribeAccountsRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)
        data = self._request(request)
        data = data.get('Accounts')
        data_list = data.get('Account')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data
