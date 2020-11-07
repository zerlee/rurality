from django.db import models
from base.models import BaseModel


class KafkaModel(BaseModel):
    '''
    Kafka
    '''
    model_name = 'Kafka'
    model_sign = 'kafka'

    base_fields = ['name', 'instance_id', 'version', 'region_id', 'zone_id', 'ssl_endpoint', 'endpoint']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    version = models.CharField('版本', max_length=128)
    endpoint = models.TextField('默认接入点')
    ssl_endpoint = models.TextField('SSL接入点')

    class Meta:
        db_table = 'kafka'


class KafkaTopicModel(BaseModel):
    '''
    Kafka Topic
    '''
    model_name = 'Kafka Topic'
    model_sign = 'kafka_topic'

    kafka = models.ForeignKey(KafkaModel, on_delete=models.CASCADE)
    instance_id = models.CharField('实例id', max_length=128)
    name = models.CharField('名称', max_length=128)
    desc = models.TextField('描述')

    class Meta:
        db_table = 'kafka_topic'
