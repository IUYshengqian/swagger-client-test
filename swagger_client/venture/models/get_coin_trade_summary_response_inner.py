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


class GetCoinTradeSummaryResponseInner(object):
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
        'exchange_name': 'str',
        'volume_pct': 'str'
    }

    attribute_map = {
        'exchange_name': 'exchangeName',
        'volume_pct': 'volumePct'
    }

    def __init__(self, exchange_name=None, volume_pct=None):  # noqa: E501
        """GetCoinTradeSummaryResponseInner - a model defined in Swagger"""  # noqa: E501

        self._exchange_name = None
        self._volume_pct = None
        self.discriminator = None

        if exchange_name is not None:
            self.exchange_name = exchange_name
        if volume_pct is not None:
            self.volume_pct = volume_pct

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetCoinTradeSummaryResponseInner.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The exchange_name of this GetCoinTradeSummaryResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetCoinTradeSummaryResponseInner.

        交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetCoinTradeSummaryResponseInner.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def volume_pct(self):
        """Gets the volume_pct of this GetCoinTradeSummaryResponseInner.  # noqa: E501

        交易所内当前币种成交量在整个平台内成交量占比  # noqa: E501

        :return: The volume_pct of this GetCoinTradeSummaryResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._volume_pct

    @volume_pct.setter
    def volume_pct(self, volume_pct):
        """Sets the volume_pct of this GetCoinTradeSummaryResponseInner.

        交易所内当前币种成交量在整个平台内成交量占比  # noqa: E501

        :param volume_pct: The volume_pct of this GetCoinTradeSummaryResponseInner.  # noqa: E501
        :type: str
        """

        self._volume_pct = volume_pct

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
        if issubclass(GetCoinTradeSummaryResponseInner, dict):
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
        if not isinstance(other, GetCoinTradeSummaryResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
