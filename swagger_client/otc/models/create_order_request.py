# coding: utf-8

"""
    crush-otc 平台接口（法币交易）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateOrderRequest(object):
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
        'ad_id': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'ad_id': 'adId',
        'amount': 'amount'
    }

    def __init__(self, ad_id=None, amount=None):  # noqa: E501
        """CreateOrderRequest - a model defined in Swagger"""  # noqa: E501

        self._ad_id = None
        self._amount = None
        self.discriminator = None

        self.ad_id = ad_id
        self.amount = amount

    @property
    def ad_id(self):
        """Gets the ad_id of this CreateOrderRequest.  # noqa: E501

        广告id  # noqa: E501

        :return: The ad_id of this CreateOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this CreateOrderRequest.

        广告id  # noqa: E501

        :param ad_id: The ad_id of this CreateOrderRequest.  # noqa: E501
        :type: str
        """
        if ad_id is None:
            raise ValueError("Invalid value for `ad_id`, must not be `None`")  # noqa: E501

        self._ad_id = ad_id

    @property
    def amount(self):
        """Gets the amount of this CreateOrderRequest.  # noqa: E501

        数量  # noqa: E501

        :return: The amount of this CreateOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateOrderRequest.

        数量  # noqa: E501

        :param amount: The amount of this CreateOrderRequest.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(CreateOrderRequest, dict):
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
        if not isinstance(other, CreateOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
