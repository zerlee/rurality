from django.db import models
from base.models import BaseModel


class AssetModel(BaseModel):
    '''
    资产模块
    '''
    model_name = '资产模块'
    model_sign = 'asset'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值')
    remark = models.TextField('备注')

    class Meta:
        db_table = 'asset'


class RegionModel(BaseModel):
    '''
    地域
    '''
    model_name = '地域'
    model_sign = 'region'

    ST_ENABLE = 10
    ST_DISABLE = 20
    ST_CHOICES = (
        (ST_ENABLE, '启用'),
        (ST_DISABLE, '禁用'),
    )

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    endpoint = models.CharField('接入点', max_length=128)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_DISABLE)

    class Meta:
        db_table = 'region'


class ZoneModel(BaseModel):
    '''
    可用区
    '''
    model_name = '可用区'
    model_sign = 'zone'

    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, verbose_name='地域')
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)

    class Meta:
        db_table = 'zone'


class VpcModel(BaseModel):
    '''
    VPC
    '''
    model_name = 'VPC'
    model_sign = 'vpc'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    desc = models.TextField('描述')
    is_default = models.BooleanField('是否默认')
    cidr_block= models.CharField('网段', max_length=128)
    region_id = models.CharField('地区', max_length=128)
    vswitch_count = models.IntegerField('交换机数量')

    class Meta:
        db_table = 'vpc'


class VSwitchModel(BaseModel):
    '''
    VSwitch交换机
    '''
    model_name = '交换机'
    model_sign = 'vswitch'

    vpc = models.ForeignKey(VpcModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    is_default = models.BooleanField('是否默认')
    desc = models.TextField('描述')
    cidr_block= models.CharField('网段', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    ip_count = models.IntegerField('可用IP数')

    class Meta:
        db_table = 'vswitch'


class SecurityGroupModel(BaseModel):
    '''
    安全组
    '''
    model_name = '安全组'
    model_sign = 'security_group'

    vpc = models.ForeignKey(VpcModel, on_delete=models.CASCADE, null=True, verbose_name='VPC')
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    desc = models.TextField('描述')

    class Meta:
        db_table = 'security_group'


class ResourceGroupModel(BaseModel):
    '''
    资源组
    '''
    model_name = '资源组'
    model_sign = 'resource_group'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    status = models.CharField('状态', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    account_id = models.CharField('账户ID', max_length=128)

    class Meta:
        db_table = 'resource_group'


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

    base_fields = ['name', 'instance_id', 'hostname', 'inner_ip', 'outer_ip', 'cpu', 'memory', 'os',
            'region_id', 'zone_id', 'create_dt']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    hostname = models.CharField('主机名', max_length=128)
    inner_ip = models.CharField('内网IP', max_length=128)
    outer_ip = models.CharField('外网IP', max_length=128)
    cpu = models.IntegerField('CPU')
    os = models.CharField('操作系统', max_length=128)
    memory = models.IntegerField('内存')
    region_id = models.CharField('地域ID', max_length=128)
    zone_id = models.CharField('可用区ID', max_length=128)
    create_dt = models.DateTimeField('实例创建时间')
    jump_id = models.CharField('Jumpserver资产ID', max_length=128)

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

    base_fields = ['name', 'instance_id', 'ip', 'ip_typ', 'region_id', 'zone_id', 'slave_zone_id', 'create_dt']

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


class SlbEcsModel(BaseModel):
    '''
    SLB后端ECS
    '''
    model_name = 'SLB关联ECS'
    model_sign = 'slb_ecs'

    slb = models.ForeignKey(SlbModel, on_delete=models.CASCADE)
    server_group = models.ForeignKey(SlbServerGroupModel, on_delete=models.CASCADE, null=True)
    ecs = models.ForeignKey(EcsModel, on_delete=models.CASCADE)
    weight = models.IntegerField('权重')

    class Meta:
        db_table = 'slb_ecs'


class RdsModel(BaseModel):
    '''
    数据库实例
    '''
    model_name = 'RDS'
    model_sign = 'rds'

    base_fields = ['name', 'instance_id', 'typ', 'version', 'db_typ', 'region_id',
            'zone_id', 'db_net_typ', 'net_typ', 'connection', 'desc']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    typ = models.CharField('数据库类型', max_length=128)
    version = models.CharField('数据库版本', max_length=128)
    db_typ = models.CharField('主从类型', max_length=128)
    region_id = models.CharField('地域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    db_net_typ = models.CharField('内网/外网', max_length=128)
    net_typ = models.CharField('EIP/VPC', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)
    desc = models.TextField('备注')

    class Meta:
        db_table = 'rds'


class RdsAccountModel(BaseModel):
    '''
    数据库账号
    '''
    model_name = 'RDS账号'
    model_sign = 'rds_account'

    base_fields = ['username', 'password']

    rds = models.ForeignKey(RdsModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)

    class Meta:
        db_table = 'rds_account'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password and self.password:
            data['password'] = '********'
        return data


class RdsDatabaseModel(BaseModel):
    '''
    数据库实例下的库
    '''
    model_name = '数据库实例'
    model_sign = 'rds_database'

    base_fields = ['name', 'instance_id', 'desc']

    rds = models.ForeignKey(RdsModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    desc = models.TextField('描述')

    class Meta:
        db_table = 'rds_database'


class RdsDatabaseAccountModel(BaseModel):
    '''
    数据库实例账号
    '''
    model_name = '数据库实例账号'
    model_sign = 'rds_database_account'

    database = models.ForeignKey(RdsDatabaseModel, on_delete=models.CASCADE)
    account = models.ForeignKey(RdsAccountModel, on_delete=models.CASCADE)
    privilege = models.CharField('权限', max_length=128)

    class Meta:
        db_table = 'rds_database_account'


class DomainModel(BaseModel):
    '''
    域名
    '''
    model_name = '域名'
    model_sign = 'domain'

    base_fields = ['name', 'instance_id', 'record_count']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    record_count = models.IntegerField('解析记录数')

    class Meta:
        db_table = 'domain'


class DomainRecordModel(BaseModel):
    '''
    域名解析记录
    '''
    model_name = '域名解析记录'
    model_sign = 'domain_record'

    base_fields = ['fullname', 'instance_id', 'name', 'rr', 'value', 'typ', 'enabled']

    domain = models.ForeignKey(DomainModel, on_delete=models.CASCADE, verbose_name='域名')
    fullname = models.CharField('完整域名', max_length=256)
    instance_id = models.CharField('实例id', max_length=128)
    name = models.CharField('主域名', max_length=128)
    value = models.CharField('value', max_length=128)
    typ = models.CharField('类型', max_length=128)
    rr = models.CharField('RR', max_length=128)
    enabled = models.BooleanField('是否启用', default=False)

    class Meta:
        db_table = 'domain_record'


class DomainRecordObjModel(BaseModel):
    '''
    域名解析关联实体对象
    '''
    model_name = '域名解析记录关联实体'
    model_sign = 'domain_record_obj'

    TYP_ECS = 'ecs'
    TYP_SLB = 'slb'
    TYP_CHOICES = (
        (TYP_ECS, 'ECS实例'),
        (TYP_SLB, 'SLB实例'),
    )

    obj_id = models.IntegerField('实体对象ID')
    record = models.ForeignKey(DomainRecordModel, on_delete=models.CASCADE)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)

    class Meta:
        db_table = 'domain_record_obj'


class RedisModel(BaseModel):
    '''
    Redis
    '''
    model_name = 'Redis'
    model_sign = 'redis'

    DEPLOY_TYP_CLUSTER = 'cluster'
    DEPLOY_TYP_STANDARD = 'standard'
    DEPLOY_TYP_SPLIT_RW= 'rwsplit'
    DEPLOY_TYP_NULL = 'NULL'
    DEPLOY_TYP_CHOICES = (
        (DEPLOY_TYP_CLUSTER, '集群版'),
        (DEPLOY_TYP_STANDARD, '标准版'),
        (DEPLOY_TYP_SPLIT_RW, '读写分离版'),
        (DEPLOY_TYP_NULL, '默认'),
    )

    base_fields = ['name', 'instance_id', 'connection', 'port', 'version', 'inner_ip', 'region_id',
            'zone_id', 'deploy_typ']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    version = models.CharField('版本', max_length=128)
    port = models.IntegerField('端口号')
    inner_ip = models.CharField('内网IP', max_length=128)
    deploy_typ = models.CharField('部署类型', max_length=128, choices=DEPLOY_TYP_CHOICES)
    username = models.CharField('用户名', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)

    class Meta:
        db_table = 'redis'


class RedisAccountModel(BaseModel):
    '''
    Redis账号
    '''
    model_name = 'Redis账号'
    model_sign = 'redis_account'

    ST_AVAILABLE = 'Available'
    ST_UNAVAILABLE = 'Unavailable'
    ST_CHOICES = (
        (ST_AVAILABLE, '可用'),
        (ST_UNAVAILABLE, '不可用'),
    )

    TYP_NORMAL = 'Normal'
    TYP_SUPER = 'Super'
    TYP_CHOICES = (
        (TYP_NORMAL, '普通账号'),
        (TYP_SUPER, '超级账号'),
    )
    PRIVILEGE_ROLE_READ_ONLY = 'RoleReadOnly'
    PRIVILEGE_ROLE_READ_WRITE = 'RoleReadWrite'
    PRIVILEGE_ROLE_REPL = 'RoleRepl'
    PRIVILEGE_CHOICES = (
        (PRIVILEGE_ROLE_READ_ONLY, '只读'),
        (PRIVILEGE_ROLE_READ_WRITE, '读写'),
        (PRIVILEGE_ROLE_REPL, '复制'),
    )

    redis = models.ForeignKey(RedisModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    status = models.CharField('状态', max_length=128, choices=ST_CHOICES)
    privilege = models.CharField('权限', max_length=128, choices=PRIVILEGE_CHOICES)

    class Meta:
        db_table = 'redis_account'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password and self.password:
            data['password'] = '********'
        return data


class MongoModel(BaseModel):
    '''
    Mongo实例
    '''
    model_name = 'Mongo'
    model_sign = 'mongo'

    base_fields = ['name', 'instance_id', 'typ', 'version', 'region_id', 'zone_id',
            'db_typ', 'net_typ', 'connection', 'replica_count', 'desc']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    typ = models.CharField('数据库类型', max_length=128)
    version = models.CharField('数据库版本', max_length=128)
    db_typ = models.CharField('复制集/分片', max_length=128)
    net_typ = models.CharField('EIP/VPC', max_length=128)
    replica_count = models.IntegerField('复制集节点数')
    region_id = models.CharField('地域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)
    desc = models.TextField('描述', null=True)

    class Meta:
        db_table = 'mongo'


class MongoAccountModel(BaseModel):
    '''
    Mongo实例
    '''
    model_name = 'Mongo账号'
    model_sign = 'mongo_account'

    ST_AVAILABLE = 'Available'
    ST_UNAVAILABLE = 'Unavailable'
    ST_CHOICES = (
        (ST_AVAILABLE, '可用'),
        (ST_UNAVAILABLE, '不可用'),
    )

    TYP_MONGOS = 'mongos'
    TYP_SHARD = 'shard'
    TYP_CHOICES = (
        (TYP_MONGOS, 'mongos'),
        (TYP_SHARD, 'shard'),
    )

    mongo = models.ForeignKey(MongoModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    status = models.CharField('状态', max_length=128, choices=ST_CHOICES)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    desc = models.TextField('备注', null=True)

    class Meta:
        db_table = 'mongo_account'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password and self.password:
            data['password'] = '********'
        return data


class MongoReplicaModel(BaseModel):
    '''
    Mongo复制集
    '''
    model_name = 'Mongo复制集'
    model_sign = 'mongo_replica'

    mongo = models.ForeignKey(MongoModel, on_delete=models.CASCADE)
    instance_id = models.CharField('实例id', max_length=128)
    role = models.CharField('角色', max_length=128)
    port = models.IntegerField('端口号')
    connection = models.CharField('连接字符串', max_length=128)

    class Meta:
        db_table = 'mongo_replica'


class RocketModel(BaseModel):
    '''
    RocketMQ
    '''
    model_name = 'Rocket'
    model_sign = 'rocket'

    base_fields = ['name', 'instance_id']

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


class K8sModel(BaseModel):
    '''
    k8s
    '''
    model_name = 'k8s'
    model_sign = 'k8s'

    base_fields = ['name', 'instance_id', 'size', 'docker_version', 'region_id', 'zone_id', 'version', 'create_dt']

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    size = models.IntegerField('节点数')
    version = models.CharField('k8s版本', max_length=128)
    docker_version = models.CharField('Docker版本', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    create_dt = models.DateTimeField('实例创建时间')

    class Meta:
        db_table = 'k8s'


class K8sNodeModel(BaseModel):
    '''
    k8s中节点
    '''
    model_name = 'k8s_node'
    model_sign = 'k8s_node'

    k8s = models.ForeignKey(K8sModel, on_delete=models.CASCADE)
    ecs = models.ForeignKey(EcsModel, on_delete=models.CASCADE)
    instance_id = models.CharField('实例id', max_length=128)
    nodepool_id = models.CharField('节点池ID', max_length=128)
    source = models.CharField('节点由来', max_length=128)
    role = models.CharField('角色', max_length=128)

    class Meta:
        db_table = 'k8s_node'


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
