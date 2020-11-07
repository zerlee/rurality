from django.db import models
from base.models import BaseModel


class RocketModel(BaseModel):
    '''
    RocketMQ
    '''
    model_name = 'Rocket'
    model_sign = 'rocket'

    instance_id = models.CharField('实例id', max_length=128)
    name = models.CharField('名称', max_length=128)

    class Meta:
        db_table = 'rocket'


class RocketTopicModel(BaseModel):
    '''
    RocketMQ Topic
    '''
    model_name = 'RocketMQ Topic'
    model_sign = 'rocket_topic'

    rocket = models.ForeignKey(RocketModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    desc = models.TextField('描述')

    class Meta:
        db_table = 'rocket_topic'
