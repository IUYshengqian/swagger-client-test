# coding: utf-8

"""
    crush-tenant 平台接口(租户平台)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAssetByCoinIdResponseEstimates(object):
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
        'usdt': 'str',
        'cny': 'str',
        'btc': 'str'
    }

    attribute_map = {
        'usdt': 'usdt',
        'cny': 'cny',
        'btc': 'btc'
    }

    def __init__(self, usdt=None, cny=None, btc=None):  # noqa: E501
        """GetAssetByCoinIdResponseEstimates - a model defined in Swagger"""  # noqa: E501

        self._usdt = None
        self._cny = None
        self._btc = None
        self.discriminator = None

        if usdt is not None:
            self.usdt = usdt
        if cny is not None:
            self.cny = cny
        if btc is not None:
            self.btc = btc

    @property
    def usdt(self):
        """Gets the usdt of this GetAssetByCoinIdResponseEstimates.  # noqa: E501

        折算usdt  # noqa: E501

        :return: The usdt of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :rtype: str
        """
        return self._usdt

    @usdt.setter
    def usdt(self, usdt):
        """Sets the usdt of this GetAssetByCoinIdResponseEstimates.

        折算usdt  # noqa: E501

        :param usdt: The usdt of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :type: str
        """

        self._usdt = usdt

    @property
    def cny(self):
        """Gets the cny of this GetAssetByCoinIdResponseEstimates.  # noqa: E501

        折算cny  # noqa: E501

        :return: The cny of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :rtype: str
        """
        return self._cny

    @cny.setter
    def cny(self, cny):
        """Sets the cny of this GetAssetByCoinIdResponseEstimates.

        折算cny  # noqa: E501

        :param cny: The cny of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :type: str
        """

        self._cny = cny

    @property
    def btc(self):
        """Gets the btc of this GetAssetByCoinIdResponseEstimates.  # noqa: E501

        折算btc  # noqa: E501

        :return: The btc of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :rtype: str
        """
        return self._btc

    @btc.setter
    def btc(self, btc):
        """Sets the btc of this GetAssetByCoinIdResponseEstimates.

        折算btc  # noqa: E501

        :param btc: The btc of this GetAssetByCoinIdResponseEstimates.  # noqa: E501
        :type: str
        """

        self._btc = btc

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
        if issubclass(GetAssetByCoinIdResponseEstimates, dict):
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
        if not isinstance(other, GetAssetByCoinIdResponseEstimates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
