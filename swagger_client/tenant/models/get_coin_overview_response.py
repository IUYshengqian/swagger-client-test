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


class GetCoinOverviewResponse(object):
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
        'project_name': 'str',
        'avg_usdprice': 'str',
        'avg_cny_price': 'str',
        'highest_price': 'str',
        'lowest_price': 'str',
        'usd_change_extent': 'str',
        'cny_change_extent': 'str',
        'change_pct': 'str',
        'volume': 'str',
        'listed_exchange_count': 'int',
        'usd_amount': 'str',
        'cny_amount': 'str',
        'usd_market_value': 'str',
        'cny_market_value': 'str'
    }

    attribute_map = {
        'project_name': 'projectName',
        'avg_usdprice': 'avgUsdprice',
        'avg_cny_price': 'avgCnyPrice',
        'highest_price': 'highestPrice',
        'lowest_price': 'lowestPrice',
        'usd_change_extent': 'usdChangeExtent',
        'cny_change_extent': 'cnyChangeExtent',
        'change_pct': 'changePct',
        'volume': 'volume',
        'listed_exchange_count': 'listedExchangeCount',
        'usd_amount': 'usdAmount',
        'cny_amount': 'cnyAmount',
        'usd_market_value': 'usdMarketValue',
        'cny_market_value': 'cnyMarketValue'
    }

    def __init__(self, project_name=None, avg_usdprice=None, avg_cny_price=None, highest_price=None, lowest_price=None, usd_change_extent=None, cny_change_extent=None, change_pct=None, volume=None, listed_exchange_count=None, usd_amount=None, cny_amount=None, usd_market_value=None, cny_market_value=None):  # noqa: E501
        """GetCoinOverviewResponse - a model defined in Swagger"""  # noqa: E501

        self._project_name = None
        self._avg_usdprice = None
        self._avg_cny_price = None
        self._highest_price = None
        self._lowest_price = None
        self._usd_change_extent = None
        self._cny_change_extent = None
        self._change_pct = None
        self._volume = None
        self._listed_exchange_count = None
        self._usd_amount = None
        self._cny_amount = None
        self._usd_market_value = None
        self._cny_market_value = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if avg_usdprice is not None:
            self.avg_usdprice = avg_usdprice
        if avg_cny_price is not None:
            self.avg_cny_price = avg_cny_price
        if highest_price is not None:
            self.highest_price = highest_price
        if lowest_price is not None:
            self.lowest_price = lowest_price
        if usd_change_extent is not None:
            self.usd_change_extent = usd_change_extent
        if cny_change_extent is not None:
            self.cny_change_extent = cny_change_extent
        if change_pct is not None:
            self.change_pct = change_pct
        if volume is not None:
            self.volume = volume
        if listed_exchange_count is not None:
            self.listed_exchange_count = listed_exchange_count
        if usd_amount is not None:
            self.usd_amount = usd_amount
        if cny_amount is not None:
            self.cny_amount = cny_amount
        if usd_market_value is not None:
            self.usd_market_value = usd_market_value
        if cny_market_value is not None:
            self.cny_market_value = cny_market_value

    @property
    def project_name(self):
        """Gets the project_name of this GetCoinOverviewResponse.  # noqa: E501

        币种名称  # noqa: E501

        :return: The project_name of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this GetCoinOverviewResponse.

        币种名称  # noqa: E501

        :param project_name: The project_name of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def avg_usdprice(self):
        """Gets the avg_usdprice of this GetCoinOverviewResponse.  # noqa: E501

        USD平均成交价  # noqa: E501

        :return: The avg_usdprice of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._avg_usdprice

    @avg_usdprice.setter
    def avg_usdprice(self, avg_usdprice):
        """Sets the avg_usdprice of this GetCoinOverviewResponse.

        USD平均成交价  # noqa: E501

        :param avg_usdprice: The avg_usdprice of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._avg_usdprice = avg_usdprice

    @property
    def avg_cny_price(self):
        """Gets the avg_cny_price of this GetCoinOverviewResponse.  # noqa: E501

        CNY平均成交价  # noqa: E501

        :return: The avg_cny_price of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._avg_cny_price

    @avg_cny_price.setter
    def avg_cny_price(self, avg_cny_price):
        """Sets the avg_cny_price of this GetCoinOverviewResponse.

        CNY平均成交价  # noqa: E501

        :param avg_cny_price: The avg_cny_price of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._avg_cny_price = avg_cny_price

    @property
    def highest_price(self):
        """Gets the highest_price of this GetCoinOverviewResponse.  # noqa: E501

        最高价  # noqa: E501

        :return: The highest_price of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._highest_price

    @highest_price.setter
    def highest_price(self, highest_price):
        """Sets the highest_price of this GetCoinOverviewResponse.

        最高价  # noqa: E501

        :param highest_price: The highest_price of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._highest_price = highest_price

    @property
    def lowest_price(self):
        """Gets the lowest_price of this GetCoinOverviewResponse.  # noqa: E501

        最低价  # noqa: E501

        :return: The lowest_price of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, lowest_price):
        """Sets the lowest_price of this GetCoinOverviewResponse.

        最低价  # noqa: E501

        :param lowest_price: The lowest_price of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._lowest_price = lowest_price

    @property
    def usd_change_extent(self):
        """Gets the usd_change_extent of this GetCoinOverviewResponse.  # noqa: E501

        usd日涨跌幅度  # noqa: E501

        :return: The usd_change_extent of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._usd_change_extent

    @usd_change_extent.setter
    def usd_change_extent(self, usd_change_extent):
        """Sets the usd_change_extent of this GetCoinOverviewResponse.

        usd日涨跌幅度  # noqa: E501

        :param usd_change_extent: The usd_change_extent of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._usd_change_extent = usd_change_extent

    @property
    def cny_change_extent(self):
        """Gets the cny_change_extent of this GetCoinOverviewResponse.  # noqa: E501

        cny日涨跌幅度  # noqa: E501

        :return: The cny_change_extent of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._cny_change_extent

    @cny_change_extent.setter
    def cny_change_extent(self, cny_change_extent):
        """Sets the cny_change_extent of this GetCoinOverviewResponse.

        cny日涨跌幅度  # noqa: E501

        :param cny_change_extent: The cny_change_extent of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._cny_change_extent = cny_change_extent

    @property
    def change_pct(self):
        """Gets the change_pct of this GetCoinOverviewResponse.  # noqa: E501

        日涨跌幅  # noqa: E501

        :return: The change_pct of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._change_pct

    @change_pct.setter
    def change_pct(self, change_pct):
        """Sets the change_pct of this GetCoinOverviewResponse.

        日涨跌幅  # noqa: E501

        :param change_pct: The change_pct of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._change_pct = change_pct

    @property
    def volume(self):
        """Gets the volume of this GetCoinOverviewResponse.  # noqa: E501

        整个平台成交量  # noqa: E501

        :return: The volume of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetCoinOverviewResponse.

        整个平台成交量  # noqa: E501

        :param volume: The volume of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def listed_exchange_count(self):
        """Gets the listed_exchange_count of this GetCoinOverviewResponse.  # noqa: E501

        已上线交易所数量  # noqa: E501

        :return: The listed_exchange_count of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: int
        """
        return self._listed_exchange_count

    @listed_exchange_count.setter
    def listed_exchange_count(self, listed_exchange_count):
        """Sets the listed_exchange_count of this GetCoinOverviewResponse.

        已上线交易所数量  # noqa: E501

        :param listed_exchange_count: The listed_exchange_count of this GetCoinOverviewResponse.  # noqa: E501
        :type: int
        """

        self._listed_exchange_count = listed_exchange_count

    @property
    def usd_amount(self):
        """Gets the usd_amount of this GetCoinOverviewResponse.  # noqa: E501

        折合USD交易额  # noqa: E501

        :return: The usd_amount of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._usd_amount

    @usd_amount.setter
    def usd_amount(self, usd_amount):
        """Sets the usd_amount of this GetCoinOverviewResponse.

        折合USD交易额  # noqa: E501

        :param usd_amount: The usd_amount of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._usd_amount = usd_amount

    @property
    def cny_amount(self):
        """Gets the cny_amount of this GetCoinOverviewResponse.  # noqa: E501

        折合CNY交易额  # noqa: E501

        :return: The cny_amount of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._cny_amount

    @cny_amount.setter
    def cny_amount(self, cny_amount):
        """Sets the cny_amount of this GetCoinOverviewResponse.

        折合CNY交易额  # noqa: E501

        :param cny_amount: The cny_amount of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._cny_amount = cny_amount

    @property
    def usd_market_value(self):
        """Gets the usd_market_value of this GetCoinOverviewResponse.  # noqa: E501

        折合USD市值  # noqa: E501

        :return: The usd_market_value of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._usd_market_value

    @usd_market_value.setter
    def usd_market_value(self, usd_market_value):
        """Sets the usd_market_value of this GetCoinOverviewResponse.

        折合USD市值  # noqa: E501

        :param usd_market_value: The usd_market_value of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._usd_market_value = usd_market_value

    @property
    def cny_market_value(self):
        """Gets the cny_market_value of this GetCoinOverviewResponse.  # noqa: E501

        折合CNY市值  # noqa: E501

        :return: The cny_market_value of this GetCoinOverviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._cny_market_value

    @cny_market_value.setter
    def cny_market_value(self, cny_market_value):
        """Sets the cny_market_value of this GetCoinOverviewResponse.

        折合CNY市值  # noqa: E501

        :param cny_market_value: The cny_market_value of this GetCoinOverviewResponse.  # noqa: E501
        :type: str
        """

        self._cny_market_value = cny_market_value

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
        if issubclass(GetCoinOverviewResponse, dict):
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
        if not isinstance(other, GetCoinOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
