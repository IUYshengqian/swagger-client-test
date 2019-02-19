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


class GetHistoricalDataRequest(object):
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
        'coin_id': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'coin_id': 'coinId',
        'scope': 'scope'
    }

    def __init__(self, coin_id=None, scope=None):  # noqa: E501
        """GetHistoricalDataRequest - a model defined in Swagger"""  # noqa: E501

        self._coin_id = None
        self._scope = None
        self.discriminator = None

        if coin_id is not None:
            self.coin_id = coin_id
        if scope is not None:
            self.scope = scope

    @property
    def coin_id(self):
        """Gets the coin_id of this GetHistoricalDataRequest.  # noqa: E501

        币种id  # noqa: E501

        :return: The coin_id of this GetHistoricalDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetHistoricalDataRequest.

        币种id  # noqa: E501

        :param coin_id: The coin_id of this GetHistoricalDataRequest.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def scope(self):
        """Gets the scope of this GetHistoricalDataRequest.  # noqa: E501

        时间范围  # noqa: E501

        :return: The scope of this GetHistoricalDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GetHistoricalDataRequest.

        时间范围  # noqa: E501

        :param scope: The scope of this GetHistoricalDataRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["1w", "30d", "90d"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

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
        if issubclass(GetHistoricalDataRequest, dict):
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
        if not isinstance(other, GetHistoricalDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
