class NacosServerModel(BaseModel):
    '''
    Nacos服务
    '''
    class Meta:
        db_table = 'nacos_server'


class NacosNamespaceModel(BaseModel):
    '''
    nacos命名空间
    '''
