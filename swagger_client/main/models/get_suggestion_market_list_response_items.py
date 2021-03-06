# coding: utf-8

"""
    crush-main 平台接口（主平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetSuggestionMarketListResponseItems(object):
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
        'id': 'str',
        'trading_pair': 'str'
    }

    attribute_map = {
        'id': 'id',
        'trading_pair': 'tradingPair'
    }

    def __init__(self, id=None, trading_pair=None):  # noqa: E501
        """GetSuggestionMarketListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._trading_pair = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trading_pair is not None:
            self.trading_pair = trading_pair

    @property
    def id(self):
        """Gets the id of this GetSuggestionMarketListResponseItems.  # noqa: E501

        交易对市场ID  # noqa: E501

        :return: The id of this GetSuggestionMarketListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSuggestionMarketListResponseItems.

        交易对市场ID  # noqa: E501

        :param id: The id of this GetSuggestionMarketListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trading_pair(self):
        """Gets the trading_pair of this GetSuggestionMarketListResponseItems.  # noqa: E501

        市场币对  # noqa: E501

        :return: The trading_pair of this GetSuggestionMarketListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this GetSuggestionMarketListResponseItems.

        市场币对  # noqa: E501

        :param trading_pair: The trading_pair of this GetSuggestionMarketListResponseItems.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

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
        if issubclass(GetSuggestionMarketListResponseItems, dict):
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
        if not isinstance(other, GetSuggestionMarketListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
