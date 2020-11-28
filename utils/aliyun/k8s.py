from aliyunsdkcore.request import CommonRequest

from .base import AliyunCli


class AliyunK8s(AliyunCli):
    '''
    阿里云容器服务
    '''
    def get_k8ses(self):
        '''
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('cs.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('GET')
        request.set_protocol_type('https') # https | http
        request.set_version('2015-12-15')

        request.add_query_param('RegionId', self.region_id)
        request.set_uri_pattern('/clusters')

        data_list = self._request(request)
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data


    def get_k8s_nodes(self, instance_id, page_num=1, page_size=20):
        '''
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('cs.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('GET')
        request.set_protocol_type('https')
        request.set_version('2015-12-15')
        request.add_query_param('RegionId', self.region_id)
        request.add_query_param('pageSize', page_size)
        request.add_query_param('pageNumber', page_num)
        request.set_uri_pattern('/clusters/{}/nodes'.format(instance_id))
        data = self._request(request)
        total = data.get('page').get('total_count')
        data_list = data.get('nodes')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_templates(self):
        '''
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('cs.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('GET')
        request.set_protocol_type('https')
        request.set_version('2015-12-15')
        request.add_query_param('RegionId', self.region_id)
        request.set_uri_pattern('/templates')
        data = self._request(request)
        total = data.get('page_info').get('total_count')
        data_list = data.get('templates')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data
