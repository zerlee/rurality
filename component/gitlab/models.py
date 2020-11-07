from django.db import models
from base.models import BaseModel


class GitlabServerModel(BaseModel):
    '''
    Gitlab服务
    '''
    name = models.CharField('名称', max_length=128)
    web_url = models.CharField('访问地址', max_length=128)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    token = models.CharField('token', max_length=128)

    class Meta:
        db_table = 'gitlab_server'


class GitlabRepoModel(BaseModel):
    '''
    gitlab代码库
    '''
    name = models.CharField('名称', max_length=128)
    project_id = models.IntegerField('项目ID')
    web_url = models.CharField('访问地址', max_length=128)
    ssh_url = models.CharField('ssh地址', max_length=128)

    class Meta:
        db_table = 'gitlab_repo'
