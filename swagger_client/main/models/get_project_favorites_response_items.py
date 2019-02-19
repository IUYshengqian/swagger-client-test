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


class GetProjectFavoritesResponseItems(object):
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
        'account_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'project_poster_url': 'str',
        'coin_logo_url': 'str',
        'full_name': 'str',
        'short_name': 'str',
        'latest_price': 'str',
        'vol24_h': 'str',
        'chg_pct24_h': 'str',
        'listed_exchange': 'str',
        'market_value': 'str',
        'issued_volume': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'project_poster_url': 'projectPosterUrl',
        'coin_logo_url': 'coinLogoUrl',
        'full_name': 'fullName',
        'short_name': 'shortName',
        'latest_price': 'latestPrice',
        'vol24_h': 'vol24H',
        'chg_pct24_h': 'chgPct24H',
        'listed_exchange': 'listedExchange',
        'market_value': 'marketValue',
        'issued_volume': 'issuedVolume'
    }

    def __init__(self, id=None, account_id=None, project_id=None, project_name=None, project_poster_url=None, coin_logo_url=None, full_name=None, short_name=None, latest_price=None, vol24_h=None, chg_pct24_h=None, listed_exchange=None, market_value=None, issued_volume=None):  # noqa: E501
        """GetProjectFavoritesResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._project_id = None
        self._project_name = None
        self._project_poster_url = None
        self._coin_logo_url = None
        self._full_name = None
        self._short_name = None
        self._latest_price = None
        self._vol24_h = None
        self._chg_pct24_h = None
        self._listed_exchange = None
        self._market_value = None
        self._issued_volume = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if project_poster_url is not None:
            self.project_poster_url = project_poster_url
        if coin_logo_url is not None:
            self.coin_logo_url = coin_logo_url
        if full_name is not None:
            self.full_name = full_name
        if short_name is not None:
            self.short_name = short_name
        if latest_price is not None:
            self.latest_price = latest_price
        if vol24_h is not None:
            self.vol24_h = vol24_h
        if chg_pct24_h is not None:
            self.chg_pct24_h = chg_pct24_h
        if listed_exchange is not None:
            self.listed_exchange = listed_exchange
        if market_value is not None:
            self.market_value = market_value
        if issued_volume is not None:
            self.issued_volume = issued_volume

    @property
    def id(self):
        """Gets the id of this GetProjectFavoritesResponseItems.  # noqa: E501

        收藏记录ID  # noqa: E501

        :return: The id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProjectFavoritesResponseItems.

        收藏记录ID  # noqa: E501

        :param id: The id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this GetProjectFavoritesResponseItems.  # noqa: E501

        账户ID  # noqa: E501

        :return: The account_id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetProjectFavoritesResponseItems.

        账户ID  # noqa: E501

        :param account_id: The account_id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def project_id(self):
        """Gets the project_id of this GetProjectFavoritesResponseItems.  # noqa: E501

        项目ID  # noqa: E501

        :return: The project_id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GetProjectFavoritesResponseItems.

        项目ID  # noqa: E501

        :param project_id: The project_id of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this GetProjectFavoritesResponseItems.  # noqa: E501

        项目名  # noqa: E501

        :return: The project_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this GetProjectFavoritesResponseItems.

        项目名  # noqa: E501

        :param project_name: The project_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_poster_url(self):
        """Gets the project_poster_url of this GetProjectFavoritesResponseItems.  # noqa: E501

        项目广告图URL  # noqa: E501

        :return: The project_poster_url of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._project_poster_url

    @project_poster_url.setter
    def project_poster_url(self, project_poster_url):
        """Sets the project_poster_url of this GetProjectFavoritesResponseItems.

        项目广告图URL  # noqa: E501

        :param project_poster_url: The project_poster_url of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._project_poster_url = project_poster_url

    @property
    def coin_logo_url(self):
        """Gets the coin_logo_url of this GetProjectFavoritesResponseItems.  # noqa: E501

        币种图标URL  # noqa: E501

        :return: The coin_logo_url of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._coin_logo_url

    @coin_logo_url.setter
    def coin_logo_url(self, coin_logo_url):
        """Sets the coin_logo_url of this GetProjectFavoritesResponseItems.

        币种图标URL  # noqa: E501

        :param coin_logo_url: The coin_logo_url of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._coin_logo_url = coin_logo_url

    @property
    def full_name(self):
        """Gets the full_name of this GetProjectFavoritesResponseItems.  # noqa: E501

        币全称  # noqa: E501

        :return: The full_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GetProjectFavoritesResponseItems.

        币全称  # noqa: E501

        :param full_name: The full_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def short_name(self):
        """Gets the short_name of this GetProjectFavoritesResponseItems.  # noqa: E501

        币简称  # noqa: E501

        :return: The short_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetProjectFavoritesResponseItems.

        币简称  # noqa: E501

        :param short_name: The short_name of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def latest_price(self):
        """Gets the latest_price of this GetProjectFavoritesResponseItems.  # noqa: E501

        最新成交价  # noqa: E501

        :return: The latest_price of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._latest_price

    @latest_price.setter
    def latest_price(self, latest_price):
        """Sets the latest_price of this GetProjectFavoritesResponseItems.

        最新成交价  # noqa: E501

        :param latest_price: The latest_price of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._latest_price = latest_price

    @property
    def vol24_h(self):
        """Gets the vol24_h of this GetProjectFavoritesResponseItems.  # noqa: E501

        24H交易量  # noqa: E501

        :return: The vol24_h of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._vol24_h

    @vol24_h.setter
    def vol24_h(self, vol24_h):
        """Sets the vol24_h of this GetProjectFavoritesResponseItems.

        24H交易量  # noqa: E501

        :param vol24_h: The vol24_h of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._vol24_h = vol24_h

    @property
    def chg_pct24_h(self):
        """Gets the chg_pct24_h of this GetProjectFavoritesResponseItems.  # noqa: E501

        24H涨跌幅  # noqa: E501

        :return: The chg_pct24_h of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._chg_pct24_h

    @chg_pct24_h.setter
    def chg_pct24_h(self, chg_pct24_h):
        """Sets the chg_pct24_h of this GetProjectFavoritesResponseItems.

        24H涨跌幅  # noqa: E501

        :param chg_pct24_h: The chg_pct24_h of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._chg_pct24_h = chg_pct24_h

    @property
    def listed_exchange(self):
        """Gets the listed_exchange of this GetProjectFavoritesResponseItems.  # noqa: E501

        已上交易所数量  # noqa: E501

        :return: The listed_exchange of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._listed_exchange

    @listed_exchange.setter
    def listed_exchange(self, listed_exchange):
        """Sets the listed_exchange of this GetProjectFavoritesResponseItems.

        已上交易所数量  # noqa: E501

        :param listed_exchange: The listed_exchange of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._listed_exchange = listed_exchange

    @property
    def market_value(self):
        """Gets the market_value of this GetProjectFavoritesResponseItems.  # noqa: E501

        市值  # noqa: E501

        :return: The market_value of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this GetProjectFavoritesResponseItems.

        市值  # noqa: E501

        :param market_value: The market_value of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._market_value = market_value

    @property
    def issued_volume(self):
        """Gets the issued_volume of this GetProjectFavoritesResponseItems.  # noqa: E501

        发行总量  # noqa: E501

        :return: The issued_volume of this GetProjectFavoritesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._issued_volume

    @issued_volume.setter
    def issued_volume(self, issued_volume):
        """Sets the issued_volume of this GetProjectFavoritesResponseItems.

        发行总量  # noqa: E501

        :param issued_volume: The issued_volume of this GetProjectFavoritesResponseItems.  # noqa: E501
        :type: str
        """

        self._issued_volume = issued_volume

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
        if issubclass(GetProjectFavoritesResponseItems, dict):
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
        if not isinstance(other, GetProjectFavoritesResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
