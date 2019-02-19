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


class GetProjectsResponseQuery(object):
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
        'order_rule': 'str',
        'order': 'str'
    }

    attribute_map = {
        'order_rule': 'orderRule',
        'order': 'order'
    }

    def __init__(self, order_rule=None, order=None):  # noqa: E501
        """GetProjectsResponseQuery - a model defined in Swagger"""  # noqa: E501

        self._order_rule = None
        self._order = None
        self.discriminator = None

        if order_rule is not None:
            self.order_rule = order_rule
        if order is not None:
            self.order = order

    @property
    def order_rule(self):
        """Gets the order_rule of this GetProjectsResponseQuery.  # noqa: E501

        排序规则 appliedAt：申请时间  # noqa: E501

        :return: The order_rule of this GetProjectsResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._order_rule

    @order_rule.setter
    def order_rule(self, order_rule):
        """Sets the order_rule of this GetProjectsResponseQuery.

        排序规则 appliedAt：申请时间  # noqa: E501

        :param order_rule: The order_rule of this GetProjectsResponseQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["latestPrice", "chgPct24H", "amount24H", "marketValue"]  # noqa: E501
        if order_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `order_rule` ({0}), must be one of {1}"  # noqa: E501
                .format(order_rule, allowed_values)
            )

        self._order_rule = order_rule

    @property
    def order(self):
        """Gets the order of this GetProjectsResponseQuery.  # noqa: E501

        排序方式  # noqa: E501

        :return: The order of this GetProjectsResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this GetProjectsResponseQuery.

        排序方式  # noqa: E501

        :param order: The order of this GetProjectsResponseQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"  # noqa: E501
                .format(order, allowed_values)
            )

        self._order = order

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
        if issubclass(GetProjectsResponseQuery, dict):
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
        if not isinstance(other, GetProjectsResponseQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
