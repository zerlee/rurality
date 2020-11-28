from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerAttributeRequest import DescribeLoadBalancerAttributeRequest
from aliyunsdkslb.request.v20140515.SetBackendServersRequest import SetBackendServersRequest
from aliyunsdkslb.request.v20140515.AddBackendServersRequest import AddBackendServersRequest
from aliyunsdkslb.request.v20140515.RemoveBackendServersRequest import RemoveBackendServersRequest
from aliyunsdkslb.request.v20140515.DescribeRulesRequest import DescribeRulesRequest

from aliyunsdkslb.request.v20140515.DescribeVServerGroupsRequest import DescribeVServerGroupsRequest
from aliyunsdkslb.request.v20140515.DescribeVServerGroupAttributeRequest import DescribeVServerGroupAttributeRequest
from aliyunsdkslb.request.v20140515.SetVServerGroupAttributeRequest import SetVServerGroupAttributeRequest
from aliyunsdkslb.request.v20140515.AddVServerGroupBackendServersRequest import AddVServerGroupBackendServersRequest
from aliyunsdkslb.request.v20140515.RemoveVServerGroupBackendServersRequest import RemoveVServerGroupBackendServersRequest
# 监听
from aliyunsdkslb.request.v20140515.CreateLoadBalancerHTTPListenerRequest import CreateLoadBalancerHTTPListenerRequest
from aliyunsdkslb.request.v20140515.StartLoadBalancerListenerRequest import StartLoadBalancerListenerRequest
from aliyunsdkslb.request.v20140515.StopLoadBalancerListenerRequest import StopLoadBalancerListenerRequest
from aliyunsdkslb.request.v20140515.DeleteLoadBalancerListenerRequest import DeleteLoadBalancerListenerRequest
# 证书
from aliyunsdkslb.request.v20140515.DescribeServerCertificatesRequest import DescribeServerCertificatesRequest
# 扩展域名
from aliyunsdkslb.request.v20140515.CreateDomainExtensionRequest import CreateDomainExtensionRequest
# 转发策略
from aliyunsdkslb.request.v20140515.CreateRulesRequest import CreateRulesRequest
from aliyunsdkslb.request.v20140515.DeleteRulesRequest import DeleteRulesRequest

from .base import AliyunCli


class AliyunSLB(AliyunCli):
    '''
    阿里云SLB
    '''
    def get_slbs(self, page_num=1, page_size=20):
        '''
        '''
        request = DescribeLoadBalancersRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('LoadBalancers')
        data_list = data.get('LoadBalancer')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_slb_info(self, instance_id):
        '''
        获取SLB信息
        '''
        request = DescribeLoadBalancerAttributeRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(instance_id)
        data = self._request(request)

        listen_data = data.get('ListenerPortsAndProtocol')
        listens = listen_data.get('ListenerPortAndProtocol')

        backend_server_data = data.get('BackendServers')
        backend_servers = backend_server_data.get('BackendServer')
        data = {
            'backend_servers': backend_servers,
            'listens': listens,
        }
        return data

    def get_vserver_groups(self, instance_id):
        '''
        获取虚拟服务组
        '''
        request = DescribeVServerGroupsRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(instance_id)
        data = self._request(request)
        data= data.get('VServerGroups')
        data_list = data.get('VServerGroup')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_vserver_group_backend_servers(self, instance_id):
        '''
        获取虚拟服务组后端服务器
        '''
        request = DescribeVServerGroupAttributeRequest()
        request.set_accept_format('json')
        request.set_VServerGroupId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_rules(self, instance_id, port):
        request = DescribeRulesRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(instance_id)
        request.set_ListenerPort(port)
        data = self._request(request)
        data = data.get('Rules')
        data_list = data.get('Rule')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def _set_servers_weight(self, instance_id, ecs_instance_ids, weight):
        '''
        设置默认服务器服务器权重
        instance_id: SLB实例ID
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Type': 'ecs',
                'Weight': weight,
            }
            backend_servers.append(data)
        request = SetBackendServersRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(instance_id)
        request.set_BackendServers(backend_servers)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def down_servers(self, instance_id, ecs_instance_ids):
        '''
        默认服务器组下掉服务器流量(已验证)
        instance_id: SLB实例ID
        '''
        return self._set_servers_weight(instance_id, ecs_instance_ids, 0)

    def up_servers(self, instance_id, ecs_instance_ids):
        '''
        默认服务器组接入服务器流量(已验证)
        instance_id: SLB实例ID
        '''
        return self._set_servers_weight(instance_id, ecs_instance_ids, 100)

    def _set_vservers_weight(self, instance_id, ecs_instance_ids, port, weight):
        '''
        设置虚拟服务器组服务器权重
        instance_id: 虚拟服务器组ID
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Port': port,
                'Type': 'ecs',
                'Weight': weight,
            }
            backend_servers.append(data)
        request = SetVServerGroupAttributeRequest()
        request.set_accept_format('json')
        request.set_BackendServers(backend_servers)
        request.set_VServerGroupId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def down_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器组下掉服务器流量(已验证)
        instance_id：虚拟服务器组ID
        '''
        return self._set_vservers_weight(instance_id, ecs_instance_ids, port, 0)

    def up_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器组接入服务器流量(已验证)
        instance_id：虚拟服务器组ID
        '''
        return self._set_vservers_weight(instance_id, ecs_instance_ids, port, 100)

    def _add_servers(self, instance_id, ecs_instance_ids):
        '''
        slb中添加机器
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Type': 'ecs',
                'Weight': 100,
            }
            backend_servers.append(data)
        request = AddBackendServersRequest()
        request.set_accept_format('json')
        request.set_BackendServers(backend_servers)
        request.set_LoadBalancerId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def add_servers(self, instance_id, ecs_instance_ids):
        '''
        SLB默认服务器组增加机器(已验证)
        '''
        data = {
            'total': 0,
            'data_list': [],
        }
        for i in range(0, len(ecs_instance_ids), 20):
            result = self._add_servers(instance_id, ecs_instance_ids[i:i+20])
            data['total'] += result['total']
            data['data_list'] += result['data_list']
        return data

    def _remove_servers(self, instance_id, ecs_instance_ids):
        '''
        slb中删除机器
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Type': 'ecs',
                'Weight': 0,
            }
            backend_servers.append(data)
        request = RemoveBackendServersRequest()
        request.set_accept_format('json')
        request.set_BackendServers(backend_servers)
        request.set_LoadBalancerId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def remove_servers(self, instance_id, ecs_instance_ids):
        '''
        SLB默认服务器组删除机器(已验证)
        '''
        data = {
            'total': 0,
            'data_list': [],
        }
        for i in range(0, len(ecs_instance_ids), 20):
            result = self._remove_servers(instance_id, ecs_instance_ids[i:i+20])
            data['total'] += result['total']
            data['data_list'] += result['data_list']
        return data

    def _add_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器组中添加机器
        instance_id: 虚拟服务器组ID
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Port': port,
                'Type': 'ecs',
                'Weight': 100,
            }
            backend_servers.append(data)
        request = AddVServerGroupBackendServersRequest()
        request.set_accept_format('json')
        request.set_BackendServers(backend_servers)
        request.set_VServerGroupId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def add_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器级中添加机器(已验证)
        instance_id: 虚拟服务器组ID
        '''
        data = {
            'total': 0,
            'data_list': [],
        }
        for i in range(0, len(ecs_instance_ids), 20):
            result = self._add_vservers(instance_id, ecs_instance_ids[i:i+20], port)
            data['total'] += result['total']
            data['data_list'] += result['data_list']
        return data

    def _remove_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器组中删除机器
        instance_id: 虚拟服务器组ID
        '''
        backend_servers = []
        for  ecs_instance_id in ecs_instance_ids:
            data = {
                'ServerId': ecs_instance_id,
                'Port': port,
                'Type': 'ecs',
                'Weight': 0,
            }
            backend_servers.append(data)
        request = RemoveVServerGroupBackendServersRequest()
        request.set_accept_format('json')
        request.set_BackendServers(backend_servers)
        request.set_VServerGroupId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def remove_vservers(self, instance_id, ecs_instance_ids, port):
        '''
        虚拟服务器级中删除机器(已验证)
        instance_id: 虚拟服务器组ID
        '''
        data = {
            'total': 0,
            'data_list': [],
        }
        for i in range(0, len(ecs_instance_ids), 20):
            result = self._remove_vservers(instance_id, ecs_instance_ids[i:i+20], port)
            data['total'] += result['total']
            data['data_list'] += result['data_list']
        return data

    def create_http_listen(self, slb_instance_id, group_instance_id, port):
        '''
        创建http监听(已验证)
        创建完成后，需要通过start_listen开启
        '''
        request = CreateLoadBalancerHTTPListenerRequest()
        request.set_accept_format('json')
        request.set_ListenerPort(port)
        request.set_StickySession("off")
        request.set_HealthCheck("off")
        request.set_LoadBalancerId(slb_instance_id)
        request.set_VServerGroupId(group_instance_id)
        data = self._request(request)
        return data

    def start_listen(self, slb_instance_id, port, protocol):
        '''
        开启监听(已验证)
        此方法在上面create_http_listen后使用
        '''
        request = StartLoadBalancerListenerRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        request.set_ListenerPort(port)
        request.set_ListenerProtocol(protocol)
        data = self._request(request)
        return data

    def stop_listen(self, slb_instance_id, port, protocol):
        '''
        停止监听(已验证)
        '''
        request = StopLoadBalancerListenerRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        request.set_ListenerPort(port)
        request.set_ListenerProtocol(protocol)
        data = self._request(request)
        return data

    def delete_listen(self, slb_instance_id, port, protocol):
        '''
        删除监听(已验证)
        '''
        request = DeleteLoadBalancerListenerRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        request.set_ListenerPort(port)
        request.set_ListenerProtocol(protocol)
        data = self._request(request)
        return data

    def format_rule(self, name, domain, url, group_instance_id):
        '''
        格式化规则数据
        url必须是以斜线开头: /login
        '''
        data = {
            'RuleName': name,
            'Domain': domain,
            'Url': url,
            'VServerGroupId': group_instance_id,
        }
        return data

    def create_rules(self, slb_instance_id, port, protocol, rules):
        '''
        创建监听转发策略(已验证)
        '''
        request = CreateRulesRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        request.set_ListenerPort(port)
        request.set_RuleList(rules)
        request.set_ListenerProtocol(protocol)
        data = self._request(request)
        data = data.get('Rules')
        data_list = data.get('Rule')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def delete_rules(self, instance_ids):
        '''
        删除监听转发策略(已验证)
        '''
        request = DeleteRulesRequest()
        request.set_accept_format('json')
        request.set_RuleIds(instance_ids)
        data = self._request(request)
        return data

    def get_server_certificates(self):
        '''
        获取服务端证书
        需要根据地域来获取
        ServerCertificateId
        ServerCertificateName
        备注：证书名称都设置成二级域名名称
        '''
        request = DescribeServerCertificatesRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('ServerCertificates')
        data_list = data.get('ServerCertificate')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def create_extension_domain(self, slb_instance_id, port, domain, certificate_id):
        '''
        监听上增加扩展域名
        '''
        request = CreateDomainExtensionRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        request.set_ListenerPort(port)
        request.set_Domain(domain)
        request.set_ServerCertificateId(certificate_id)
        data = self._request(request)
        return data
