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


class PostFavoriterMarketRequest(object):
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
        'exchange_id': 'str',
        'favorite_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'exchange_id': 'exchangeId',
        'favorite_id': 'favoriteId',
        'type': 'type'
    }

    def __init__(self, exchange_id=None, favorite_id=None, type=None):  # noqa: E501
        """PostFavoriterMarketRequest - a model defined in Swagger"""  # noqa: E501

        self._exchange_id = None
        self._favorite_id = None
        self._type = None
        self.discriminator = None

        if exchange_id is not None:
            self.exchange_id = exchange_id
        if favorite_id is not None:
            self.favorite_id = favorite_id
        if type is not None:
            self.type = type

    @property
    def exchange_id(self):
        """Gets the exchange_id of this PostFavoriterMarketRequest.  # noqa: E501

        交易所Id  # noqa: E501

        :return: The exchange_id of this PostFavoriterMarketRequest.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this PostFavoriterMarketRequest.

        交易所Id  # noqa: E501

        :param exchange_id: The exchange_id of this PostFavoriterMarketRequest.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def favorite_id(self):
        """Gets the favorite_id of this PostFavoriterMarketRequest.  # noqa: E501

        收藏目标Id（收藏项目时为项目id，收藏交易所时为交易所id，收藏市场时为市场id）  # noqa: E501

        :return: The favorite_id of this PostFavoriterMarketRequest.  # noqa: E501
        :rtype: str
        """
        return self._favorite_id

    @favorite_id.setter
    def favorite_id(self, favorite_id):
        """Sets the favorite_id of this PostFavoriterMarketRequest.

        收藏目标Id（收藏项目时为项目id，收藏交易所时为交易所id，收藏市场时为市场id）  # noqa: E501

        :param favorite_id: The favorite_id of this PostFavoriterMarketRequest.  # noqa: E501
        :type: str
        """

        self._favorite_id = favorite_id

    @property
    def type(self):
        """Gets the type of this PostFavoriterMarketRequest.  # noqa: E501

        收藏类型  # noqa: E501

        :return: The type of this PostFavoriterMarketRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostFavoriterMarketRequest.

        收藏类型  # noqa: E501

        :param type: The type of this PostFavoriterMarketRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["exchange", "market", "project"]  # noqa: E501
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
        if issubclass(PostFavoriterMarketRequest, dict):
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
        if not isinstance(other, PostFavoriterMarketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
