from django.db import models
from base.models import BaseModel


class OsImageModel(BaseModel):
    '''
    操作系统镜像
    '''
    model_name = '操作系统镜像'
    model_sign = 'os_image'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    desc = models.TextField('描述')

    class Meta:
        db_table = 'os_image'


class EcsTemplateModel(BaseModel):
    '''
    ECS模板
    '''
    model_name = 'ECS模板'
    model_sign = 'ecs_template'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    version = models.CharField('默认版本', max_length=128)
    region_id = models.CharField('区域', max_length=128)

    class Meta:
        db_table = 'ecs_template'


class EcsModel(BaseModel):
    '''
    ECS
    '''
    model_name = 'ECS'
    model_sign = 'ecs'

    region_id = models.CharField('地域ID', max_length=128)
    zone_id = models.CharField('可用区ID', max_length=128)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    hostname = models.CharField('主机名', max_length=128)
    inner_ip = models.CharField('内网IP', max_length=128)
    outer_ip = models.CharField('外网IP', max_length=128)
    cpu = models.IntegerField('CPU')
    os = models.CharField('操作系统', max_length=128)
    memory = models.IntegerField('内存')
    dt_buy = models.DateTimeField('购买时间')

    class Meta:
        db_table = 'ecs'


class EipModel(BaseModel):
    '''
    EIP
    '''
    model_name = 'EIP'
    model_sign = 'eip'

    base_fields = ['name', 'instance_id', 'ip', 'bandwidth', 'create_dt', 'region_id', 'zone_id']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    ip = models.CharField('IP', max_length=128)
    bandwidth = models.IntegerField('带宽')
    status = models.CharField('状态', max_length=128)
    typ = models.CharField('关联实例类型', max_length=128)
    related_instance_id = models.CharField('关联实例ID', max_length=128)
    create_dt = models.DateTimeField('实例创建时间')
    region_id = models.CharField('地域ID', max_length=128)

    class Meta:
        db_table = 'eip'
