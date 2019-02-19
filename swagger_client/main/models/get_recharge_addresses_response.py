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


class GetRechargeAddressesResponse(object):
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
        'coin_address': 'str'
    }

    attribute_map = {
        'coin_id': 'coinId',
        'coin_address': 'coinAddress'
    }

    def __init__(self, coin_id=None, coin_address=None):  # noqa: E501
        """GetRechargeAddressesResponse - a model defined in Swagger"""  # noqa: E501

        self._coin_id = None
        self._coin_address = None
        self.discriminator = None

        if coin_id is not None:
            self.coin_id = coin_id
        if coin_address is not None:
            self.coin_address = coin_address

    @property
    def coin_id(self):
        """Gets the coin_id of this GetRechargeAddressesResponse.  # noqa: E501

        币id  # noqa: E501

        :return: The coin_id of this GetRechargeAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetRechargeAddressesResponse.

        币id  # noqa: E501

        :param coin_id: The coin_id of this GetRechargeAddressesResponse.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def coin_address(self):
        """Gets the coin_address of this GetRechargeAddressesResponse.  # noqa: E501

        充币地址  # noqa: E501

        :return: The coin_address of this GetRechargeAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._coin_address

    @coin_address.setter
    def coin_address(self, coin_address):
        """Sets the coin_address of this GetRechargeAddressesResponse.

        充币地址  # noqa: E501

        :param coin_address: The coin_address of this GetRechargeAddressesResponse.  # noqa: E501
        :type: str
        """

        self._coin_address = coin_address

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
        if issubclass(GetRechargeAddressesResponse, dict):
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
        if not isinstance(other, GetRechargeAddressesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
