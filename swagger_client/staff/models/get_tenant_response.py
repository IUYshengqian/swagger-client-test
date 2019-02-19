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


class GetTenantResponse(object):
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
        'name': 'str',
        'account_id': 'str',
        'exchange_id': 'str',
        'exchange_name': 'str',
        'nationality': 'str',
        'logo': 'str',
        'tags': 'str',
        'phone': 'str',
        'email': 'str',
        'certification_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'account_id': 'accountId',
        'exchange_id': 'exchangeId',
        'exchange_name': 'exchangeName',
        'nationality': 'nationality',
        'logo': 'logo',
        'tags': 'tags',
        'phone': 'phone',
        'email': 'email',
        'certification_type': 'certificationType'
    }

    def __init__(self, name=None, account_id=None, exchange_id=None, exchange_name=None, nationality=None, logo=None, tags=None, phone=None, email=None, certification_type=None):  # noqa: E501
        """GetTenantResponse - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._account_id = None
        self._exchange_id = None
        self._exchange_name = None
        self._nationality = None
        self._logo = None
        self._tags = None
        self._phone = None
        self._email = None
        self._certification_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if account_id is not None:
            self.account_id = account_id
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if nationality is not None:
            self.nationality = nationality
        if logo is not None:
            self.logo = logo
        if tags is not None:
            self.tags = tags
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if certification_type is not None:
            self.certification_type = certification_type

    @property
    def name(self):
        """Gets the name of this GetTenantResponse.  # noqa: E501

        姓名/企业名  # noqa: E501

        :return: The name of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetTenantResponse.

        姓名/企业名  # noqa: E501

        :param name: The name of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_id(self):
        """Gets the account_id of this GetTenantResponse.  # noqa: E501

        用户Id  # noqa: E501

        :return: The account_id of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetTenantResponse.

        用户Id  # noqa: E501

        :param account_id: The account_id of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def exchange_id(self):
        """Gets the exchange_id of this GetTenantResponse.  # noqa: E501

        交易所ID  # noqa: E501

        :return: The exchange_id of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this GetTenantResponse.

        交易所ID  # noqa: E501

        :param exchange_id: The exchange_id of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetTenantResponse.  # noqa: E501

        交易所名字  # noqa: E501

        :return: The exchange_name of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetTenantResponse.

        交易所名字  # noqa: E501

        :param exchange_name: The exchange_name of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def nationality(self):
        """Gets the nationality of this GetTenantResponse.  # noqa: E501

        交易所地区  # noqa: E501

        :return: The nationality of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this GetTenantResponse.

        交易所地区  # noqa: E501

        :param nationality: The nationality of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._nationality = nationality

    @property
    def logo(self):
        """Gets the logo of this GetTenantResponse.  # noqa: E501

        交易所logo  # noqa: E501

        :return: The logo of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetTenantResponse.

        交易所logo  # noqa: E501

        :param logo: The logo of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def tags(self):
        """Gets the tags of this GetTenantResponse.  # noqa: E501

        交易所标签  # noqa: E501

        :return: The tags of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetTenantResponse.

        交易所标签  # noqa: E501

        :param tags: The tags of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def phone(self):
        """Gets the phone of this GetTenantResponse.  # noqa: E501

        电话对象没有字段为空  # noqa: E501

        :return: The phone of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this GetTenantResponse.

        电话对象没有字段为空  # noqa: E501

        :param phone: The phone of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this GetTenantResponse.  # noqa: E501

        邮箱  # noqa: E501

        :return: The email of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetTenantResponse.

        邮箱  # noqa: E501

        :param email: The email of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def certification_type(self):
        """Gets the certification_type of this GetTenantResponse.  # noqa: E501

        认证类型  # noqa: E501

        :return: The certification_type of this GetTenantResponse.  # noqa: E501
        :rtype: str
        """
        return self._certification_type

    @certification_type.setter
    def certification_type(self, certification_type):
        """Sets the certification_type of this GetTenantResponse.

        认证类型  # noqa: E501

        :param certification_type: The certification_type of this GetTenantResponse.  # noqa: E501
        :type: str
        """

        self._certification_type = certification_type

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
        if issubclass(GetTenantResponse, dict):
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
        if not isinstance(other, GetTenantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
