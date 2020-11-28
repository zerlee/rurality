from aliyunsdkons.request.v20190214.OnsInstanceInServiceListRequest import OnsInstanceInServiceListRequest
from aliyunsdkons.request.v20190214.OnsTopicListRequest import OnsTopicListRequest

from .base import AliyunCli


class AliyunRocket(AliyunCli):
    '''
    阿里云消息队列RocketMQ
    '''
    def get_mqs(self):
        '''
        '''
        request = OnsInstanceInServiceListRequest()
        request.set_accept_format('json')

        data = self._request(request)
        data = data.get('Data')
        data_list = data.get('InstanceVO')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_mq_topics(self, instance_id):
        '''
        '''
        request = OnsTopicListRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)

        data = self._request(request)
        data = data.get('Data')
        data = data.get('PublishInfoDo')
        return data
