from django.db import models
from base.models import BaseModel


class BerryModel(BaseModel):
    '''
    Ferry是摆渡，Berry就是卜摆渡
    '''
    model_name = '任务'
    model_sign = 'berry'

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

    # 代表结束状态
    END_STATUS = (ST_SUCCESS, ST_FAILURE, ST_ABORTED, ST_CANCELLED,)

    TIME_MODE_NOW = 10
    TIME_MODE_CRONTAB = 20
    TIME_MODE_CHOICES = (
        (TIME_MODE_NOW, '立即执行'),
        (TIME_MODE_CRONTAB, '定时执行'),
    )

    TYP_DEPLOY = 10
    TYP_ROLLBACK = 11
    TYP_CHOICES = (
        (TYP_DEPLOY, '部署服务'),
        (TYP_ROLLBACK, '回滚服务'),
    )

    name = models.CharField('名称', max_length=128)
    task_id = models.CharField('任务ID', max_length=128)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES)
    typ = models.IntegerField('类型', choices=ST_CHOICES)
    time_mode = models.SmallIntegerField('时间模式', choices=TIME_MODE_CHOICES)
    # input_params、output_params一般存入json.dumps后的数据
    # 记录任务运行需要使用到的数据
    input_params = models.TextField('输入参数', null=True)
    # 记录任务结束后可以提供的数据
    output_params = models.TextField('输出参数', null=True)

    class Meta:
        db_table = 'berry'
