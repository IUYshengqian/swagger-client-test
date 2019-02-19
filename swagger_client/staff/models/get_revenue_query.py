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


class GetRevenueQuery(object):
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
        'created_at': 'str',
        'coin_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'coin_id': 'coinId',
        'type': 'type'
    }

    def __init__(self, created_at=None, coin_id=None, type=None):  # noqa: E501
        """GetRevenueQuery - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._coin_id = None
        self._type = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if coin_id is not None:
            self.coin_id = coin_id
        if type is not None:
            self.type = type

    @property
    def created_at(self):
        """Gets the created_at of this GetRevenueQuery.  # noqa: E501

        开始创建时间  # noqa: E501

        :return: The created_at of this GetRevenueQuery.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetRevenueQuery.

        开始创建时间  # noqa: E501

        :param created_at: The created_at of this GetRevenueQuery.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def coin_id(self):
        """Gets the coin_id of this GetRevenueQuery.  # noqa: E501

        币id  # noqa: E501

        :return: The coin_id of this GetRevenueQuery.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetRevenueQuery.

        币id  # noqa: E501

        :param coin_id: The coin_id of this GetRevenueQuery.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def type(self):
        """Gets the type of this GetRevenueQuery.  # noqa: E501

        类型  # noqa: E501

        :return: The type of this GetRevenueQuery.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetRevenueQuery.

        类型  # noqa: E501

        :param type: The type of this GetRevenueQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["WITHDRAW", "RECHARGE", "WITHDRAW_FEE", "SERVICE_ORDER", "TRADE_FEE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(GetRevenueQuery, dict):
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
        if not isinstance(other, GetRevenueQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
