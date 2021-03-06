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


class PostSponsorRequest(object):
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
        'account': 'str',
        'name': 'str',
        'password': 'str',
        'phone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'account': 'account',
        'name': 'name',
        'password': 'password',
        'phone': 'phone',
        'email': 'email'
    }

    def __init__(self, account=None, name=None, password=None, phone=None, email=None):  # noqa: E501
        """PostSponsorRequest - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._name = None
        self._password = None
        self._phone = None
        self._email = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email

    @property
    def account(self):
        """Gets the account of this PostSponsorRequest.  # noqa: E501

        账号  # noqa: E501

        :return: The account of this PostSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this PostSponsorRequest.

        账号  # noqa: E501

        :param account: The account of this PostSponsorRequest.  # noqa: E501
        :type: str
        """
        if account is not None and len(account) > 50:
            raise ValueError("Invalid value for `account`, length must be less than or equal to `50`")  # noqa: E501
        if account is not None and len(account) < 6:
            raise ValueError("Invalid value for `account`, length must be greater than or equal to `6`")  # noqa: E501

        self._account = account

    @property
    def name(self):
        """Gets the name of this PostSponsorRequest.  # noqa: E501

        名称  # noqa: E501

        :return: The name of this PostSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostSponsorRequest.

        名称  # noqa: E501

        :param name: The name of this PostSponsorRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this PostSponsorRequest.  # noqa: E501

        密码  # noqa: E501

        :return: The password of this PostSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostSponsorRequest.

        密码  # noqa: E501

        :param password: The password of this PostSponsorRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this PostSponsorRequest.  # noqa: E501

        手机  # noqa: E501

        :return: The phone of this PostSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PostSponsorRequest.

        手机  # noqa: E501

        :param phone: The phone of this PostSponsorRequest.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this PostSponsorRequest.  # noqa: E501

        邮箱  # noqa: E501

        :return: The email of this PostSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostSponsorRequest.

        邮箱  # noqa: E501

        :param email: The email of this PostSponsorRequest.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(PostSponsorRequest, dict):
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
        if not isinstance(other, PostSponsorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
