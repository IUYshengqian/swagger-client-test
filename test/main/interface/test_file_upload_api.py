# coding: utf-8

"""
    crush 平台接口（主平台）

    `crush` 平台接口（主平台）  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: api@crush.team
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pytest
import json
import swagger_client.main
from swagger_client.main.api.file_upload_api import FileUploadApi  # noqa: E501
from swagger_client.main.rest import ApiException
from conftest import verify, login, logout, register, BACK_DOOR_VERIFY_CODE, rand_password, rand_email, rand_phone, rand_indiv_cert


api = swagger_client.main.api.file_upload_api.FileUploadApi()


def pytest_namespace():
    return {'email': "", "password": "", "base_token": "", "phone": ""}


class TestFileUploadApi:
    """FileUploadApi pytest stubs"""

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

    def test_file_key_get(self):
        """Test case for file_key_get

        由key来获取对应资源的URL  # noqa: E501
        """
        pass

    def test_file_key_zoom_zoom_get(self):
        """Test case for file_key_zoom_zoom_get

        由key来获取对应图片  # noqa: E501
        """
        pass

    def test_upload(self):
        """Test case for upload

        文件上传、图片上传  # noqa: E501
        """
        pass

