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


class GetWithdrawAddressResponseItems(object):
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
        'coin_name': 'str',
        'address': 'str',
        'tag': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'coin_name': 'coinName',
        'address': 'address',
        'tag': 'tag',
        'remark': 'remark'
    }

    def __init__(self, id=None, coin_name=None, address=None, tag=None, remark=None):  # noqa: E501
        """GetWithdrawAddressResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._coin_name = None
        self._address = None
        self._tag = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if coin_name is not None:
            self.coin_name = coin_name
        if address is not None:
            self.address = address
        if tag is not None:
            self.tag = tag
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this GetWithdrawAddressResponseItems.  # noqa: E501

        id  # noqa: E501

        :return: The id of this GetWithdrawAddressResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetWithdrawAddressResponseItems.

        id  # noqa: E501

        :param id: The id of this GetWithdrawAddressResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def coin_name(self):
        """Gets the coin_name of this GetWithdrawAddressResponseItems.  # noqa: E501

        币简称  # noqa: E501

        :return: The coin_name of this GetWithdrawAddressResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._coin_name

    @coin_name.setter
    def coin_name(self, coin_name):
        """Sets the coin_name of this GetWithdrawAddressResponseItems.

        币简称  # noqa: E501

        :param coin_name: The coin_name of this GetWithdrawAddressResponseItems.  # noqa: E501
        :type: str
        """

        self._coin_name = coin_name

    @property
    def address(self):
        """Gets the address of this GetWithdrawAddressResponseItems.  # noqa: E501

        地址  # noqa: E501

        :return: The address of this GetWithdrawAddressResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetWithdrawAddressResponseItems.

        地址  # noqa: E501

        :param address: The address of this GetWithdrawAddressResponseItems.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def tag(self):
        """Gets the tag of this GetWithdrawAddressResponseItems.  # noqa: E501

        标签  # noqa: E501

        :return: The tag of this GetWithdrawAddressResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GetWithdrawAddressResponseItems.

        标签  # noqa: E501

        :param tag: The tag of this GetWithdrawAddressResponseItems.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def remark(self):
        """Gets the remark of this GetWithdrawAddressResponseItems.  # noqa: E501

        地址备注  # noqa: E501

        :return: The remark of this GetWithdrawAddressResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this GetWithdrawAddressResponseItems.

        地址备注  # noqa: E501

        :param remark: The remark of this GetWithdrawAddressResponseItems.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if issubclass(GetWithdrawAddressResponseItems, dict):
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
        if not isinstance(other, GetWithdrawAddressResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other