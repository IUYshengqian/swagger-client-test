#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 20:40
# @Author  : ZDK
# @Email    : zhengdengke@wanshare.com

# 前台项目方新建报告成功——（后台）获取项目方的所有项目列表——获取项目报告列表——修改项目报告状态——获取项目报告列表
from faker import Faker
import pytest
import random
import copy

from swagger_client.venture.api.project_api import ProjectApi
from swagger_client.sponsor.api.sponsors_project_api import SponsorsProjectApi
from common.certification_verify import individual_verify
from swagger_client.venture.api.sponsors_managerment_api import SponsorsManagermentApi as SMApi
from common.utils import (PlatformManager, random_get_country_ob,
                          get_random_id_number, get_random_name)
from common.account_sign import set_login_status
from swagger_client.staff.api.sponsors_managerment_api import SponsorsManagermentApi
from common.account_sign import get_admin_token, get_sponsor_token
from swagger_client.venture.models.application_request import ApplicationRequest
from swagger_client.staff.api.announcement_management_api import AnnouncementManagementApi
from swagger_client.venture.models.post_report_request import PostReportRequest
from swagger_client.venture.api.report_management_api import ReportManagementApi
from test.venture.scenario.config import payload
from test.venture.scenario.rand_email import random_email


class TestAnnouncementCase4(object):

    @pytest.mark.order1
    def test_announcement4(self):
        faker = Faker()
        manager = PlatformManager("venture")
        email = random_email()
        password = faker.password()
        country = random_get_country_ob()
        manager.register(email=email, password=password,
                         promotion_code=None, verification_code="666666",
                         nationality_code=country.get("k"))
        token = manager.login(account=email, password=password)
        # 个人实名认证
        individual_verify(platform="venture", id_number=get_random_id_number(), token=token)
        # 申请项目
        project_name = get_random_name(2, 16)
        short_name = "AB" + str(random.randint(100, 999))
        full_name = get_random_name(2, 16)
        project_api = ProjectApi()
        set_login_status(project_api, token)
        pay = copy.deepcopy(dict(payload))
        pay.update({'project_name': project_name,
                    'short_name': short_name,
                    'full_name': full_name})
        req = ApplicationRequest(**pay)
        res = project_api.applications_post(body=req)
        project_apply_id = res.id

        # 创建保健方账号
        staff_api = SponsorsManagermentApi()
        staff_token = get_admin_token()
        set_login_status(staff_api, staff_token)
        sponsor = {"account": get_random_name(6, 25), "password": faker.password(),
                   "name": faker.user_name(), "email": email,
                   "phone": faker.phone_number()}
        staff_api.staff_sponsors_post(post_sponsor=sponsor)
        # 项目方获取保健列表
        venture_api = SMApi()
        set_login_status(venture_api, token)
        res = venture_api.sponsors_get(page=1, name=sponsor.get("name"))
        item = res.items.pop()
        sponsor_id = item.id
        # 项目方设置保健方
        project_api.applications_id_set_sponsor_put(
            id=project_apply_id, sponsor_request={"sponsorId": sponsor_id})
        # 保健方登
        # 保健项目
        sponsor_api = SponsorsProjectApi()
        get_sponsor_token(account=sponsor.get("account"),
                          password=sponsor.get("password"),
                          email=sponsor.get("email"), api_list=[sponsor_api])
        sponsor_api.projects_sponsor_put(put_project_sponsor_request={
            "id": project_apply_id,
            "status": 1,
            "remark": "remark"
        }
        )
        # 获取项目列表
        res = project_api.projects_get(page=1)
        audit_project_id = ''
        for item in res.items:
            assert item.project_name == project_name
            assert item.full_name == full_name
            assert item.short_name == short_name
            audit_project_id = item.project_id
        # 发送报告
        report_api = ReportManagementApi()
        set_login_status(report_api, token)
        payload1 = {
                      "title": "项目报告" + str(random.randint(1000,9999)),
                      "type": "daily",
                      "report_url": "C:\pc\Desktop\wanshare.pdf",
                      "project_id": audit_project_id
                    }
        req = PostReportRequest(**payload1)
        report_api.reports_post(body=req)
        # 获取项目报告列表
        staff_am_api = AnnouncementManagementApi()
        set_login_status(staff_am_api, token)
        report_id = ''
        status = ''
        res = staff_am_api.reports_project_id_get(project_id=audit_project_id)
        assert res.meta.total_count == 1
        for item in res.items:
            assert item.title == payload1['title']
            assert item.type == payload1['type']
            assert item.status is True
            report_id = item.id
            status = item.status
        # 修改项目报告状态
        staff_am_api.reports_id_status_put(id=report_id, status=False)
        # 获取项目报告列表
        res = staff_am_api.reports_project_id_get(project_id=report_id)
        for item in res.items:
            assert item.title == payload1['title']
            assert item.type == payload1['type']
            assert item.status is False
            assert item.status != status
