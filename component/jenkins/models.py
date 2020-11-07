from django.db import models
from base.models import BaseModel


class JenkinsServerModel(BaseModel):
    '''
    Jenkins服务
    '''
    model_name = 'Jenkins服务'
    model_sign = 'jenkins_server'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('唯一标识', max_length=128)
    url = models.TextField('访问地址')
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    token = models.CharField('token', max_length=128)

    class Meta:
        db_table = 'jenkins_server'


class JenkinsJobModel(BaseModel):
    '''
    Jenkins Job
    '''
    model_name = 'Jenkins job'
    model_sign = 'jenkins_job'

    server = models.ForeignKey(JenkinsServerModel, on_delete=models.CASCADE, verbose_name='Jenkins服务')
    name = models.CharField('名称', max_length=128)
    url = models.TextField('访问地址')

    class Meta:
        db_table = 'jenkins_job'


class JenkinsJobBuildModel(BaseModel):
    '''
    Jenkins Job构建信息
    '''
    is_log = False

    ST_PENDING = 10
    ST_RUNNING = 20
    ST_SUCCESS = 30
    ST_FAILURE = 40
    ST_ABORTED = 50
    ST_CANCELLED = 60
    ST_CHOICES = (
        (ST_PENDING, '等待'),
        (ST_RUNNING, '执行中'),
        (ST_SUCCESS, '成功'),
        (ST_FAILURE, '失败'),
        (ST_ABORTED, '中止'),
        (ST_CANCELLED, '取消'),
    )
    # 代表结束的状态
    END_STATUS = (ST_SUCCESS, ST_FAILURE, ST_ABORTED, ST_CANCELLED,)

    jenkins_server = models.ForeignKey(JenkinsServerModel, on_delete=models.CASCADE)
    jenkins_job = models.ForeignKey(JenkinsJobModel, on_delete=models.CASCADE)
    status = models.IntegerField('状态', choices=ST_CHOICES)
    # queue_number的说明如下，job完成后保留五分钟
    # five minutes after the job completes
    queue_number = models.IntegerField('队列ID')
    build_number= models.IntegerField('构建ID', null=True)
    build_url = models.TextField('构建地址', null=True)
    build_output = models.TextField('构建信息', null=True)

    class Meta:
        db_table = 'jenkins_job_build'
