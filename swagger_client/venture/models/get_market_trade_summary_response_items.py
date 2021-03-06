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


class GetMarketTradeSummaryResponseItems(object):
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
        'latest_price': 'str',
        'volume': 'str',
        'change_pct': 'str',
        'price_trend': 'str'
    }

    attribute_map = {
        'latest_price': 'latestPrice',
        'volume': 'volume',
        'change_pct': 'changePct',
        'price_trend': 'priceTrend'
    }

    def __init__(self, latest_price=None, volume=None, change_pct=None, price_trend=None):  # noqa: E501
        """GetMarketTradeSummaryResponseItems - a model defined in Swagger"""  # noqa: E501

        self._latest_price = None
        self._volume = None
        self._change_pct = None
        self._price_trend = None
        self.discriminator = None

        if latest_price is not None:
            self.latest_price = latest_price
        if volume is not None:
            self.volume = volume
        if change_pct is not None:
            self.change_pct = change_pct
        if price_trend is not None:
            self.price_trend = price_trend

    @property
    def latest_price(self):
        """Gets the latest_price of this GetMarketTradeSummaryResponseItems.  # noqa: E501

        最新成交价  # noqa: E501

        :return: The latest_price of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._latest_price

    @latest_price.setter
    def latest_price(self, latest_price):
        """Sets the latest_price of this GetMarketTradeSummaryResponseItems.

        最新成交价  # noqa: E501

        :param latest_price: The latest_price of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :type: str
        """

        self._latest_price = latest_price

    @property
    def volume(self):
        """Gets the volume of this GetMarketTradeSummaryResponseItems.  # noqa: E501

        成交量  # noqa: E501

        :return: The volume of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetMarketTradeSummaryResponseItems.

        成交量  # noqa: E501

        :param volume: The volume of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def change_pct(self):
        """Gets the change_pct of this GetMarketTradeSummaryResponseItems.  # noqa: E501

        涨跌幅  # noqa: E501

        :return: The change_pct of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._change_pct

    @change_pct.setter
    def change_pct(self, change_pct):
        """Sets the change_pct of this GetMarketTradeSummaryResponseItems.

        涨跌幅  # noqa: E501

        :param change_pct: The change_pct of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :type: str
        """

        self._change_pct = change_pct

    @property
    def price_trend(self):
        """Gets the price_trend of this GetMarketTradeSummaryResponseItems.  # noqa: E501

        价格趋势  # noqa: E501

        :return: The price_trend of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._price_trend

    @price_trend.setter
    def price_trend(self, price_trend):
        """Sets the price_trend of this GetMarketTradeSummaryResponseItems.

        价格趋势  # noqa: E501

        :param price_trend: The price_trend of this GetMarketTradeSummaryResponseItems.  # noqa: E501
        :type: str
        """

        self._price_trend = price_trend

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
        if issubclass(GetMarketTradeSummaryResponseItems, dict):
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
        if not isinstance(other, GetMarketTradeSummaryResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
