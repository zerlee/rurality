from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeImagesRequest import DescribeImagesRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeLaunchTemplatesRequest import DescribeLaunchTemplatesRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupsRequest import DescribeSecurityGroupsRequest
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526.DescribeZonesRequest import DescribeZonesRequest
from aliyunsdkecs.request.v20140526.CreateImageRequest import CreateImageRequest
from aliyunsdkecs.request.v20140526.DescribeEipAddressesRequest import DescribeEipAddressesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceTypeFamiliesRequest import DescribeInstanceTypeFamiliesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceTypesRequest import DescribeInstanceTypesRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteInstancesRequest import DeleteInstancesRequest

from .base import AliyunCli


class AliyunECS(AliyunCli):
    '''
    阿里云ECS
    '''
    def get_ecses(self, instance_ids=[], page_num=1, page_size=20):
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        if instance_ids:
            request.set_InstanceIds(instance_ids)
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Instances')
        data_list = data.get('Instance')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def create_image_by_ecs(self, instance_id, name):
        '''
        通过ECS生成镜像
        '''
        request = CreateImageRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)
        request.set_ImageName(name)
        data = self._request(request)
        image_id = data.get('ImageId')
        return image_id

    def get_image_info(self, image_id):
        '''
        传入镜像id，查看镜像状态
        '''
        request = DescribeImagesRequest()
        request.set_accept_format('json')
        request.set_ImageId(image_id)
        data = self._request(request)
        total = data.get('TotalCount')
        image_info = None
        if total == 1:
            data = data.get('Images')
            data_list = data.get('Image')
            image_info = data_list[0]
        return image_info

    def get_images(self, page_num=1, page_size=20):
        '''
        获取镜像列表，只要自定义的镜像
        '''
        request = DescribeImagesRequest()
        request.set_accept_format('json')
        request.set_ImageOwnerAlias("self")
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Images')
        data_list = data.get('Image')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_ecs_templates(self, page_num=1, page_size=20):
        '''
        获取ECS模板列表
        '''
        request = DescribeLaunchTemplatesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('LaunchTemplateSets')
        data_list = data.get('LaunchTemplateSet')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def create_ecs_by_template(self, template_id, template_version, os_image_id,
            security_group_id, vswitch_id, instance_name, hostname, amount,
            auto_release_time=None, desc=None):
        '''
        使用模板创建ECS
        '''
        request = RunInstancesRequest()
        request.set_accept_format('json')
        # 启动模板ID
        request.set_LaunchTemplateId(template_id)
        # 启动模板版本
        request.set_LaunchTemplateVersion(template_version)
        # 镜像ID
        request.set_ImageId(os_image_id)
        # 安全组ID(必须和交换机在同一VPC下)
        request.set_SecurityGroupId(security_group_id)
        # 交换机
        request.set_VSwitchId(vswitch_id)
        # 实例名称
        # request.set_InstanceName(instance_name)
        # 实例Hostname
        # request.set_HostName(hostname)
        # 是否使用镜像预设的密码
        request.set_PasswordInherit(True)
        # 创建实例数量
        request.set_Amount(amount)
        # 包年包月计费方式的时长单位
        request.set_PeriodUnit("Month")
        # 购买资源的时长
        request.set_Period(1)
        # 自动续费
        request.set_AutoRenew(True)
        # 单次自动续费的续费时长
        request.set_AutoRenewPeriod(1)
        # 实例的付费方式: PrePaid：包年包月; PostPaid(默认)：按量付费
        request.set_InstanceChargeType("PrePaid")
        # 实例描述
        if desc:
            request.set_Description(desc)
        # 自动释放时间
        if auto_release_time:
            request.set_AutoReleaseTime(auto_release_time)

        data = self._request(request)
        data = data.get('InstanceIdSets')
        data_list = data.get('InstanceIdSet')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_security_groups(self, page_num=1, page_size=20):
        '''
        获取安全组列表
        '''
        request = DescribeSecurityGroupsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('SecurityGroups')
        data_list = data.get('SecurityGroup')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_eips(self, page_num=1, page_size=20):
        request = DescribeEipAddressesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('EipAddresses')
        data_list = data.get('EipAddress')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_regions(self):
        request = DescribeRegionsRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('Regions')
        data_list = data.get('Region')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data


    def get_zones(self, region_id):
        self.reset_region(region_id)
        request = DescribeZonesRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('Zones')
        data_list = data.get('Zone')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_ecs_type_families(self):
        request = DescribeInstanceTypeFamiliesRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('InstanceTypeFamilies')
        data_list = data.get('InstanceTypeFamily')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_ecs_types(self, family=None):
        request = DescribeInstanceTypesRequest()
        request.set_accept_format('json')
        if family:
            request.set_InstanceTypeFamily(family)
        data = self._request(request)
        data = data.get('InstanceTypes')
        data_list = data.get('InstanceType')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def delete_ecs(self, instance_id):
        '''
        删除单台ECS(已验证)
        刚创建成功的机器，立即调用接口会返回403，需要过一小段时间再调用(即使在控制台看到ecs已运行，也不可以)
        '''
        request = DeleteInstanceRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)
        request.set_Force(True)
        data = self._request(request)
        return data

    def delete_ecses(self, instance_ids):
        '''
        删除多台ECS(已验证)
        刚创建成功的机器，立即调用接口会返回403，需要过一小段时间再调用(即使在控制台看到ecs已运行，也不可以)
        注意：一次删除不超过100台
        文档：https://api.aliyun.com/?accounttraceid=538c9ab277ae440d862bf3f9f8d550f5fqxk#/?product=Ecs&version=2014-05-26&api=DeleteInstances&params={}&tab=DOC&lang=PYTHON
        '''
        # TODO: 这里需要做一下重试，生成一个clientToken，然后失败后使用此token继续调用
        request = DeleteInstancesRequest()
        request.set_accept_format('json')
        request.set_InstanceIds(instance_ids)
        request.set_Force(True)
        data = self._request(request)
        return data
