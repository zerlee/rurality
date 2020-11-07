from django.db import models
from base.models import BaseModel


class SlbModel(BaseModel):
    '''
    SLB
    '''
    model_name = 'SLB'
    model_sign = 'slb'

    IP_TYP_INTERNET = 'internet'
    IP_TYP_INTRANET = 'intranet'
    IP_TYP_CHOICES = (
        (IP_TYP_INTERNET, '公网'),
        (IP_TYP_INTRANET, '内网'),
    )

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    ip = models.CharField('IP', max_length=128)
    ip_typ = models.CharField('IP类型', max_length=128, choices=IP_TYP_CHOICES)
    region_id = models.CharField('地域ID', max_length=128)
    zone_id = models.CharField('可用区ID', max_length=128)
    slave_zone_id = models.CharField('备可用区ID', max_length=128)
    create_dt = models.DateTimeField('实例创建时间')

    class Meta:
        db_table = 'slb'


class SlbServerGroupModel(BaseModel):
    '''
    SLB服务器组
    '''
    model_name = 'SLB服务器组'
    model_sign = 'slb_server_group'

    TYP_DEFAULT = 10
    TYP_V_SERVER = 20
    TYP_CHOICES = (
        (TYP_DEFAULT, '默认服务器组'),
        (TYP_V_SERVER, '虚拟服务器组'),
    )

    slb = models.ForeignKey(SlbModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES)

    class Meta:
        db_table = 'slb_server_group'


class SlbServerGroupEcsModel(BaseModel):
    '''
    SLB服务器组后端ECS
    '''
    model_name = 'SLB关联ECS'
    model_sign = 'slb_server_group_ecs'

    slb = models.ForeignKey(SlbModel, on_delete=models.CASCADE)
    server_group = models.ForeignKey(SlbServerGroupModel, on_delete=models.CASCADE, null=True)
    ecs = models.ForeignKey(EcsModel, on_delete=models.CASCADE)
    weight = models.IntegerField('权重')

    class Meta:
        db_table = 'slb_server_group_ecs'
