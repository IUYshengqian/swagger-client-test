# coding: utf-8

"""
    crush-venture 平台接口（项目方平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body(object):
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
        'market_ids': 'str',
        'time_scope': 'int'
    }

    attribute_map = {
        'market_ids': 'marketIds',
        'time_scope': 'timeScope'
    }

    def __init__(self, market_ids=None, time_scope=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._market_ids = None
        self._time_scope = None
        self.discriminator = None

        if market_ids is not None:
            self.market_ids = market_ids
        if time_scope is not None:
            self.time_scope = time_scope

    @property
    def market_ids(self):
        """Gets the market_ids of this Body.  # noqa: E501

        市场ID  # noqa: E501

        :return: The market_ids of this Body.  # noqa: E501
        :rtype: str
        """
        return self._market_ids

    @market_ids.setter
    def market_ids(self, market_ids):
        """Sets the market_ids of this Body.

        市场ID  # noqa: E501

        :param market_ids: The market_ids of this Body.  # noqa: E501
        :type: str
        """

        self._market_ids = market_ids

    @property
    def time_scope(self):
        """Gets the time_scope of this Body.  # noqa: E501

        时间范围  # noqa: E501

        :return: The time_scope of this Body.  # noqa: E501
        :rtype: int
        """
        return self._time_scope

    @time_scope.setter
    def time_scope(self, time_scope):
        """Sets the time_scope of this Body.

        时间范围  # noqa: E501

        :param time_scope: The time_scope of this Body.  # noqa: E501
        :type: int
        """

        self._time_scope = time_scope

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
