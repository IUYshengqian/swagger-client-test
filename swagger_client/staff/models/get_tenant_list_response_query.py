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


class GetTenantListResponseQuery(object):
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
        'created_start_at': 'str',
        'created_end_at': 'str',
        'exchange_id': 'str',
        'exchange_name': 'str',
        'auth_type': 'str'
    }

    attribute_map = {
        'created_start_at': 'createdStartAt',
        'created_end_at': 'createdEndAt',
        'exchange_id': 'exchangeId',
        'exchange_name': 'exchangeName',
        'auth_type': 'authType'
    }

    def __init__(self, created_start_at=None, created_end_at=None, exchange_id=None, exchange_name=None, auth_type=None):  # noqa: E501
        """GetTenantListResponseQuery - a model defined in Swagger"""  # noqa: E501

        self._created_start_at = None
        self._created_end_at = None
        self._exchange_id = None
        self._exchange_name = None
        self._auth_type = None
        self.discriminator = None

        if created_start_at is not None:
            self.created_start_at = created_start_at
        if created_end_at is not None:
            self.created_end_at = created_end_at
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if auth_type is not None:
            self.auth_type = auth_type

    @property
    def created_start_at(self):
        """Gets the created_start_at of this GetTenantListResponseQuery.  # noqa: E501

        请求的成立起始时间  # noqa: E501

        :return: The created_start_at of this GetTenantListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._created_start_at

    @created_start_at.setter
    def created_start_at(self, created_start_at):
        """Sets the created_start_at of this GetTenantListResponseQuery.

        请求的成立起始时间  # noqa: E501

        :param created_start_at: The created_start_at of this GetTenantListResponseQuery.  # noqa: E501
        :type: str
        """

        self._created_start_at = created_start_at

    @property
    def created_end_at(self):
        """Gets the created_end_at of this GetTenantListResponseQuery.  # noqa: E501

        请求的成立结束时间  # noqa: E501

        :return: The created_end_at of this GetTenantListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._created_end_at

    @created_end_at.setter
    def created_end_at(self, created_end_at):
        """Sets the created_end_at of this GetTenantListResponseQuery.

        请求的成立结束时间  # noqa: E501

        :param created_end_at: The created_end_at of this GetTenantListResponseQuery.  # noqa: E501
        :type: str
        """

        self._created_end_at = created_end_at

    @property
    def exchange_id(self):
        """Gets the exchange_id of this GetTenantListResponseQuery.  # noqa: E501

        请求的交易所id  # noqa: E501

        :return: The exchange_id of this GetTenantListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this GetTenantListResponseQuery.

        请求的交易所id  # noqa: E501

        :param exchange_id: The exchange_id of this GetTenantListResponseQuery.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetTenantListResponseQuery.  # noqa: E501

        请求的交易所名称  # noqa: E501

        :return: The exchange_name of this GetTenantListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetTenantListResponseQuery.

        请求的交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetTenantListResponseQuery.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def auth_type(self):
        """Gets the auth_type of this GetTenantListResponseQuery.  # noqa: E501

        请求的认证类型  # noqa: E501

        :return: The auth_type of this GetTenantListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this GetTenantListResponseQuery.

        请求的认证类型  # noqa: E501

        :param auth_type: The auth_type of this GetTenantListResponseQuery.  # noqa: E501
        :type: str
        """

        self._auth_type = auth_type

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
        if issubclass(GetTenantListResponseQuery, dict):
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
        if not isinstance(other, GetTenantListResponseQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
