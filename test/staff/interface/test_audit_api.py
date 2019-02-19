# coding: utf-8

"""
    crush 平台接口（用户管理后台端）

    `crush` 平台接口（后台端）  当前接口为 `staff` 端  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: api@crush.team
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pytest
import json
import swagger_client.staff
from swagger_client.staff.api.audit_api import AuditApi  # noqa: E501
from swagger_client.staff.rest import ApiException
from conftest import verify, login, logout, register, BACK_DOOR_VERIFY_CODE, rand_password, rand_email, rand_phone, rand_indiv_cert


api = swagger_client.staff.api.audit_api.AuditApi()


def pytest_namespace():
    return {'email': "", "password": "", "base_token": "", "phone": ""}


class TestAuditApi:
    """AuditApi pytest stubs"""

    def test_register_and_login_prepare(self):
        country = "86"
        pytest.email = rand_email()
        pytest.password = rand_password()
        register(email=pytest.email, password=pytest.password, promotion_code="",
                 verification_code=BACK_DOOR_VERIFY_CODE,
                 country=country)

        pytest.base_token = login(api, pytest.email, pytest.password, challenge="", seccode=BACK_DOOR_VERIFY_CODE,
                                  validate="")
        print("register return base_token:%s" % pytest.base_token)

    def test_company_audits_get(self):
        """Test case for company_audits_get

        企业用户实名审核列表 - 李欣  # noqa: E501
        """
        pass

    def test_company_audits_id_get(self):
        """Test case for company_audits_id_get

        获取企业用户实名审核详情 - 李欣  # noqa: E501
        """
        pass

    def test_company_audits_post(self):
        """Test case for company_audits_post

        提交企业用户实名审核 - 李欣  # noqa: E501
        """
        pass

    def test_company_audits_tasks_audit_num_get(self):
        """Test case for company_audits_tasks_audit_num_get

        获取企业实名审核任务数量 - 李欣  # noqa: E501
        """
        pass

    def test_company_audits_tasks_receive_get(self):
        """Test case for company_audits_tasks_receive_get

        开始实名审核 - 李欣  # noqa: E501
        """
        pass

    def test_individual_audits_get(self):
        """Test case for individual_audits_get

        个人用户实名审核列表 - 李欣  # noqa: E501
        """
        pass

    def test_individual_audits_id_get(self):
        """Test case for individual_audits_id_get

        获取实名用户审核结果详情 - 李欣  # noqa: E501
        """
        pass

    def test_individual_audits_post(self):
        """Test case for individual_audits_post

        提交个人用户实名审核 - 李欣  # noqa: E501
        """
        pass

    def test_individual_audits_tasks_audit_pending_num_get(self):
        """Test case for individual_audits_tasks_audit_pending_num_get

        个人用户待审数 - 李欣  # noqa: E501
        """
        pass

    def test_individual_audits_tasks_receive_get(self):
        """Test case for individual_audits_tasks_receive_get

        开始实名审核 - 李欣  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_audit_post(self):
        """Test case for shutdown_market_audits_audit_post

        提交关闭交易市场审核-初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_get(self):
        """Test case for shutdown_market_audits_get

        关闭交易市场审核列表 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_id_audit_get(self):
        """Test case for shutdown_market_audits_id_audit_get

        关闭交易市场审核详情-初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_id_re_audit_get(self):
        """Test case for shutdown_market_audits_id_re_audit_get

        关闭交易市场审核详情-复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_id_tasks_audit_get(self):
        """Test case for shutdown_market_audits_id_tasks_audit_get

        关闭交易市场审核初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_id_tasks_re_audit_get(self):
        """Test case for shutdown_market_audits_id_tasks_re_audit_get

        关闭交易市场审核复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_shutdown_market_audits_re_audit_post(self):
        """Test case for shutdown_market_audits_re_audit_post

        提交关闭交易市场审核-复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_audit_post(self):
        """Test case for tenant_audits_audit_post

        提交交易所账号审核-初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_get(self):
        """Test case for tenant_audits_get

        交易所账号审核列表 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_re_audit_post(self):
        """Test case for tenant_audits_re_audit_post

        提交交易所账号审核-复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_results_id_company_audit_get(self):
        """Test case for tenant_audits_results_id_company_audit_get

        企业认证交易所账号审核详情-初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_results_id_company_re_audit_get(self):
        """Test case for tenant_audits_results_id_company_re_audit_get

        企业认证交易所账号审核详情-复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_results_id_individual_audit_get(self):
        """Test case for tenant_audits_results_id_individual_audit_get

        个人认证交易所账号审核详情-初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_results_id_individual_re_audit_get(self):
        """Test case for tenant_audits_results_id_individual_re_audit_get

        个人认证交易所账号审核详情-复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_tasks_id_company_audit_get(self):
        """Test case for tenant_audits_tasks_id_company_audit_get

        企业认证交易所账号初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_tasks_id_company_re_audit_get(self):
        """Test case for tenant_audits_tasks_id_company_re_audit_get

        企业认证交易所账号复审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_tasks_id_individual_audit_get(self):
        """Test case for tenant_audits_tasks_id_individual_audit_get

        个人认证交易所账号初审 - 邹凌威  # noqa: E501
        """
        pass

    def test_tenant_audits_tasks_id_individual_re_audit_get(self):
        """Test case for tenant_audits_tasks_id_individual_re_audit_get

        个人认证交易所账号复审 - 邹凌威  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
