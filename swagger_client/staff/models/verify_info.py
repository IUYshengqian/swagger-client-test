# coding: utf-8

"""
    crush-staff 平台接口（职员管理平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VerifyInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'challenge': 'str',
        'seccode': 'str',
        'validate': 'str',
        'account': 'str',
        'code': 'str',
        'base_token': 'str'
    }

    attribute_map = {
        'challenge': 'challenge',
        'seccode': 'seccode',
        'validate': 'validate',
        'account': 'account',
        'code': 'code',
        'base_token': 'baseToken'
    }

    def __init__(self, challenge=None, seccode=None, validate=None, account=None, code=None, base_token=None):  # noqa: E501
        """VerifyInfo - a model defined in Swagger"""  # noqa: E501

        self._challenge = None
        self._seccode = None
        self._validate = None
        self._account = None
        self._code = None
        self._base_token = None
        self.discriminator = None

        self.challenge = challenge
        self.seccode = seccode
        self.validate = validate
        self.account = account
        self.code = code
        self.base_token = base_token

    @property
    def challenge(self):
        """Gets the challenge of this VerifyInfo.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The challenge of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this VerifyInfo.

        极验服务端需要用到的参数  # noqa: E501

        :param challenge: The challenge of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def seccode(self):
        """Gets the seccode of this VerifyInfo.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The seccode of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._seccode

    @seccode.setter
    def seccode(self, seccode):
        """Sets the seccode of this VerifyInfo.

        极验服务端需要用到的参数  # noqa: E501

        :param seccode: The seccode of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if seccode is None:
            raise ValueError("Invalid value for `seccode`, must not be `None`")  # noqa: E501

        self._seccode = seccode

    @property
    def validate(self):
        """Gets the validate of this VerifyInfo.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The validate of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._validate

    @validate.setter
    def validate(self, validate):
        """Sets the validate of this VerifyInfo.

        极验服务端需要用到的参数  # noqa: E501

        :param validate: The validate of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if validate is None:
            raise ValueError("Invalid value for `validate`, must not be `None`")  # noqa: E501

        self._validate = validate

    @property
    def account(self):
        """Gets the account of this VerifyInfo.  # noqa: E501

        账号，邮箱不超过64个字符，手机不超过16  # noqa: E501

        :return: The account of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this VerifyInfo.

        账号，邮箱不超过64个字符，手机不超过16  # noqa: E501

        :param account: The account of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501
        if account is not None and len(account) > 64:
            raise ValueError("Invalid value for `account`, length must be less than or equal to `64`")  # noqa: E501
        if account is not None and len(account) < 16:
            raise ValueError("Invalid value for `account`, length must be greater than or equal to `16`")  # noqa: E501

        self._account = account

    @property
    def code(self):
        """Gets the code of this VerifyInfo.  # noqa: E501

        默认验证码若存在两个code，此为关闭手机的谷歌验证或者邮件验证  # noqa: E501

        :return: The code of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VerifyInfo.

        默认验证码若存在两个code，此为关闭手机的谷歌验证或者邮件验证  # noqa: E501

        :param code: The code of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 6:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `6`")  # noqa: E501
        if code is not None and len(code) < 6:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `6`")  # noqa: E501

        self._code = code

    @property
    def base_token(self):
        """Gets the base_token of this VerifyInfo.  # noqa: E501

        baseToken 第一个接口返回的参数  # noqa: E501

        :return: The base_token of this VerifyInfo.  # noqa: E501
        :rtype: str
        """
        return self._base_token

    @base_token.setter
    def base_token(self, base_token):
        """Sets the base_token of this VerifyInfo.

        baseToken 第一个接口返回的参数  # noqa: E501

        :param base_token: The base_token of this VerifyInfo.  # noqa: E501
        :type: str
        """
        if base_token is None:
            raise ValueError("Invalid value for `base_token`, must not be `None`")  # noqa: E501
        if base_token is not None and len(base_token) > 200:
            raise ValueError("Invalid value for `base_token`, length must be less than or equal to `200`")  # noqa: E501

        self._base_token = base_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VerifyInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VerifyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
