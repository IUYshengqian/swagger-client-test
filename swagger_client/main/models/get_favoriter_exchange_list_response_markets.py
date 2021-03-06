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


class GetFavoriterExchangeListResponseMarkets(object):
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
        'market_id': 'str',
        'seller_coin_id': 'str',
        'buyer_coin_id': 'str',
        'trading_pair': 'str',
        'trading_area_id': 'str',
        'latest_price': 'str',
        'cny_latest_price': 'str',
        'volume': 'str',
        'amount': 'str',
        'change_extent': 'str',
        'change_pct': 'str'
    }

    attribute_map = {
        'market_id': 'marketId',
        'seller_coin_id': 'sellerCoinId',
        'buyer_coin_id': 'buyerCoinId',
        'trading_pair': 'tradingPair',
        'trading_area_id': 'tradingAreaId',
        'latest_price': 'latestPrice',
        'cny_latest_price': 'cnyLatestPrice',
        'volume': 'volume',
        'amount': 'amount',
        'change_extent': 'changeExtent',
        'change_pct': 'changePct'
    }

    def __init__(self, market_id=None, seller_coin_id=None, buyer_coin_id=None, trading_pair=None, trading_area_id=None, latest_price=None, cny_latest_price=None, volume=None, amount=None, change_extent=None, change_pct=None):  # noqa: E501
        """GetFavoriterExchangeListResponseMarkets - a model defined in Swagger"""  # noqa: E501

        self._market_id = None
        self._seller_coin_id = None
        self._buyer_coin_id = None
        self._trading_pair = None
        self._trading_area_id = None
        self._latest_price = None
        self._cny_latest_price = None
        self._volume = None
        self._amount = None
        self._change_extent = None
        self._change_pct = None
        self.discriminator = None

        if market_id is not None:
            self.market_id = market_id
        if seller_coin_id is not None:
            self.seller_coin_id = seller_coin_id
        if buyer_coin_id is not None:
            self.buyer_coin_id = buyer_coin_id
        if trading_pair is not None:
            self.trading_pair = trading_pair
        if trading_area_id is not None:
            self.trading_area_id = trading_area_id
        if latest_price is not None:
            self.latest_price = latest_price
        if cny_latest_price is not None:
            self.cny_latest_price = cny_latest_price
        if volume is not None:
            self.volume = volume
        if amount is not None:
            self.amount = amount
        if change_extent is not None:
            self.change_extent = change_extent
        if change_pct is not None:
            self.change_pct = change_pct

    @property
    def market_id(self):
        """Gets the market_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        市场ID  # noqa: E501

        :return: The market_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._market_id

    @market_id.setter
    def market_id(self, market_id):
        """Sets the market_id of this GetFavoriterExchangeListResponseMarkets.

        市场ID  # noqa: E501

        :param market_id: The market_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._market_id = market_id

    @property
    def seller_coin_id(self):
        """Gets the seller_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        卖方币种ID  # noqa: E501

        :return: The seller_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._seller_coin_id

    @seller_coin_id.setter
    def seller_coin_id(self, seller_coin_id):
        """Sets the seller_coin_id of this GetFavoriterExchangeListResponseMarkets.

        卖方币种ID  # noqa: E501

        :param seller_coin_id: The seller_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._seller_coin_id = seller_coin_id

    @property
    def buyer_coin_id(self):
        """Gets the buyer_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        买方币种ID  # noqa: E501

        :return: The buyer_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._buyer_coin_id

    @buyer_coin_id.setter
    def buyer_coin_id(self, buyer_coin_id):
        """Sets the buyer_coin_id of this GetFavoriterExchangeListResponseMarkets.

        买方币种ID  # noqa: E501

        :param buyer_coin_id: The buyer_coin_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._buyer_coin_id = buyer_coin_id

    @property
    def trading_pair(self):
        """Gets the trading_pair of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        币对  # noqa: E501

        :return: The trading_pair of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this GetFavoriterExchangeListResponseMarkets.

        币对  # noqa: E501

        :param trading_pair: The trading_pair of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

    @property
    def trading_area_id(self):
        """Gets the trading_area_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        交易分区ID  # noqa: E501

        :return: The trading_area_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._trading_area_id

    @trading_area_id.setter
    def trading_area_id(self, trading_area_id):
        """Sets the trading_area_id of this GetFavoriterExchangeListResponseMarkets.

        交易分区ID  # noqa: E501

        :param trading_area_id: The trading_area_id of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._trading_area_id = trading_area_id

    @property
    def latest_price(self):
        """Gets the latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        最新成交价  # noqa: E501

        :return: The latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._latest_price

    @latest_price.setter
    def latest_price(self, latest_price):
        """Sets the latest_price of this GetFavoriterExchangeListResponseMarkets.

        最新成交价  # noqa: E501

        :param latest_price: The latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._latest_price = latest_price

    @property
    def cny_latest_price(self):
        """Gets the cny_latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        折合人名币最新成交价  # noqa: E501

        :return: The cny_latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._cny_latest_price

    @cny_latest_price.setter
    def cny_latest_price(self, cny_latest_price):
        """Sets the cny_latest_price of this GetFavoriterExchangeListResponseMarkets.

        折合人名币最新成交价  # noqa: E501

        :param cny_latest_price: The cny_latest_price of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._cny_latest_price = cny_latest_price

    @property
    def volume(self):
        """Gets the volume of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        成交量  # noqa: E501

        :return: The volume of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetFavoriterExchangeListResponseMarkets.

        成交量  # noqa: E501

        :param volume: The volume of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def amount(self):
        """Gets the amount of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        成交额  # noqa: E501

        :return: The amount of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetFavoriterExchangeListResponseMarkets.

        成交额  # noqa: E501

        :param amount: The amount of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def change_extent(self):
        """Gets the change_extent of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        日涨跌幅度  # noqa: E501

        :return: The change_extent of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._change_extent

    @change_extent.setter
    def change_extent(self, change_extent):
        """Sets the change_extent of this GetFavoriterExchangeListResponseMarkets.

        日涨跌幅度  # noqa: E501

        :param change_extent: The change_extent of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._change_extent = change_extent

    @property
    def change_pct(self):
        """Gets the change_pct of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501

        日涨跌百分比  # noqa: E501

        :return: The change_pct of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :rtype: str
        """
        return self._change_pct

    @change_pct.setter
    def change_pct(self, change_pct):
        """Sets the change_pct of this GetFavoriterExchangeListResponseMarkets.

        日涨跌百分比  # noqa: E501

        :param change_pct: The change_pct of this GetFavoriterExchangeListResponseMarkets.  # noqa: E501
        :type: str
        """

        self._change_pct = change_pct

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
        if issubclass(GetFavoriterExchangeListResponseMarkets, dict):
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
        if not isinstance(other, GetFavoriterExchangeListResponseMarkets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
