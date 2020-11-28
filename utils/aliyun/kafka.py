from aliyunsdkcore.request import CommonRequest

from .base import AliyunCli


class AliyunKafka(AliyunCli):
    '''
    阿里云Kafka
    '''
    def get_kafkas(self, page_num=1, page_size=30):
        '''
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('alikafka.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2019-09-16')
        request.set_action_name('GetInstanceList')
        request.add_query_param('RegionId', self.region_id)

        data = self._request(request)
        data = data.get('InstanceList')
        data_list = data.get('InstanceVO')
        total = len(data_list)
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data


    def get_kafka_topics(self, instance_id, page_num=1, page_size=30):
        '''
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('alikafka.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2019-09-16')
        request.set_action_name('GetTopicList')
        request.add_query_param('RegionId', self.region_id)
        request.add_query_param('CurrentPage', page_num)
        request.add_query_param('PageSize', page_size)
        request.add_query_param('InstanceId', instance_id)

        data = self._request(request)
        total = data.get('Total')
        data = data.get('TopicList')
        data_list = data.get('TopicVO')

        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_kafka_whites(self, instance_id):
        '''
        Kafka白名单
        '''
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('alikafka.{}.aliyuncs.com'.format(self.region_id))
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2019-09-16')
        request.set_action_name('GetAllowedIpList')
        request.add_query_param('RegionId', self.region_id)
        request.add_query_param('InstanceId', instance_id)

        data = self._request(request)
        data = data.get('AllowedList')
        data_list = data.get('VpcList')

        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data
