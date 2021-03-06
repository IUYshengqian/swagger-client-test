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

from swagger_client.otc.models.simple_paymode_info import SimplePaymodeInfo  # noqa: F401,E501


class AdvertisementListQueryInfo(object):
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
        'user_id': 'str',
        'nick_name': 'str',
        'real_name': 'str',
        'user_color': 'str',
        'status': 'int',
        'amount': 'str',
        'trade_type': 'int',
        'currency_id': 'str',
        'currency_code': 'str',
        'price': 'str',
        'min_limit': 'str',
        'max_limit': 'str',
        'remark': 'str',
        'create_time': 'str',
        'order_count': 'int',
        'paymode_list': 'list[SimplePaymodeInfo]'
    }

    attribute_map = {
        'ad_id': 'adId',
        'user_id': 'userId',
        'nick_name': 'nickName',
        'real_name': 'realName',
        'user_color': 'userColor',
        'status': 'status',
        'amount': 'amount',
        'trade_type': 'tradeType',
        'currency_id': 'currencyId',
        'currency_code': 'currencyCode',
        'price': 'price',
        'min_limit': 'minLimit',
        'max_limit': 'maxLimit',
        'remark': 'remark',
        'create_time': 'createTime',
        'order_count': 'orderCount',
        'paymode_list': 'paymodeList'
    }

    def __init__(self, ad_id=None, user_id=None, nick_name=None, real_name=None, user_color=None, status=None, amount=None, trade_type=None, currency_id=None, currency_code=None, price=None, min_limit=None, max_limit=None, remark=None, create_time=None, order_count=None, paymode_list=None):  # noqa: E501
        """AdvertisementListQueryInfo - a model defined in Swagger"""  # noqa: E501

        self._ad_id = None
        self._user_id = None
        self._nick_name = None
        self._real_name = None
        self._user_color = None
        self._status = None
        self._amount = None
        self._trade_type = None
        self._currency_id = None
        self._currency_code = None
        self._price = None
        self._min_limit = None
        self._max_limit = None
        self._remark = None
        self._create_time = None
        self._order_count = None
        self._paymode_list = None
        self.discriminator = None

        if ad_id is not None:
            self.ad_id = ad_id
        if user_id is not None:
            self.user_id = user_id
        if nick_name is not None:
            self.nick_name = nick_name
        if real_name is not None:
            self.real_name = real_name
        if user_color is not None:
            self.user_color = user_color
        if status is not None:
            self.status = status
        if amount is not None:
            self.amount = amount
        if trade_type is not None:
            self.trade_type = trade_type
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_code is not None:
            self.currency_code = currency_code
        if price is not None:
            self.price = price
        if min_limit is not None:
            self.min_limit = min_limit
        if max_limit is not None:
            self.max_limit = max_limit
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if order_count is not None:
            self.order_count = order_count
        if paymode_list is not None:
            self.paymode_list = paymode_list

    @property
    def ad_id(self):
        """Gets the ad_id of this AdvertisementListQueryInfo.  # noqa: E501

        广告Id  # noqa: E501

        :return: The ad_id of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this AdvertisementListQueryInfo.

        广告Id  # noqa: E501

        :param ad_id: The ad_id of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._ad_id = ad_id

    @property
    def user_id(self):
        """Gets the user_id of this AdvertisementListQueryInfo.  # noqa: E501

        用户Id  # noqa: E501

        :return: The user_id of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AdvertisementListQueryInfo.

        用户Id  # noqa: E501

        :param user_id: The user_id of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def nick_name(self):
        """Gets the nick_name of this AdvertisementListQueryInfo.  # noqa: E501

        用户昵称  # noqa: E501

        :return: The nick_name of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this AdvertisementListQueryInfo.

        用户昵称  # noqa: E501

        :param nick_name: The nick_name of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def real_name(self):
        """Gets the real_name of this AdvertisementListQueryInfo.  # noqa: E501

        用户实名  # noqa: E501

        :return: The real_name of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this AdvertisementListQueryInfo.

        用户实名  # noqa: E501

        :param real_name: The real_name of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

    @property
    def user_color(self):
        """Gets the user_color of this AdvertisementListQueryInfo.  # noqa: E501

        logo颜色  # noqa: E501

        :return: The user_color of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_color

    @user_color.setter
    def user_color(self, user_color):
        """Sets the user_color of this AdvertisementListQueryInfo.

        logo颜色  # noqa: E501

        :param user_color: The user_color of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._user_color = user_color

    @property
    def status(self):
        """Gets the status of this AdvertisementListQueryInfo.  # noqa: E501

        广告状态 1 已上线  2 已下线  # noqa: E501

        :return: The status of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AdvertisementListQueryInfo.

        广告状态 1 已上线  2 已下线  # noqa: E501

        :param status: The status of this AdvertisementListQueryInfo.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def amount(self):
        """Gets the amount of this AdvertisementListQueryInfo.  # noqa: E501

        交易数量  # noqa: E501

        :return: The amount of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdvertisementListQueryInfo.

        交易数量  # noqa: E501

        :param amount: The amount of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def trade_type(self):
        """Gets the trade_type of this AdvertisementListQueryInfo.  # noqa: E501

        交易类型 1 买币广告 2 卖币广告  # noqa: E501

        :return: The trade_type of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: int
        """
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        """Sets the trade_type of this AdvertisementListQueryInfo.

        交易类型 1 买币广告 2 卖币广告  # noqa: E501

        :param trade_type: The trade_type of this AdvertisementListQueryInfo.  # noqa: E501
        :type: int
        """

        self._trade_type = trade_type

    @property
    def currency_id(self):
        """Gets the currency_id of this AdvertisementListQueryInfo.  # noqa: E501

        数字币id  # noqa: E501

        :return: The currency_id of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this AdvertisementListQueryInfo.

        数字币id  # noqa: E501

        :param currency_id: The currency_id of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def currency_code(self):
        """Gets the currency_code of this AdvertisementListQueryInfo.  # noqa: E501

        数字币代码  # noqa: E501

        :return: The currency_code of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AdvertisementListQueryInfo.

        数字币代码  # noqa: E501

        :param currency_code: The currency_code of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def price(self):
        """Gets the price of this AdvertisementListQueryInfo.  # noqa: E501

        价格  # noqa: E501

        :return: The price of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AdvertisementListQueryInfo.

        价格  # noqa: E501

        :param price: The price of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def min_limit(self):
        """Gets the min_limit of this AdvertisementListQueryInfo.  # noqa: E501

        最小交易限额 单位元  # noqa: E501

        :return: The min_limit of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._min_limit

    @min_limit.setter
    def min_limit(self, min_limit):
        """Sets the min_limit of this AdvertisementListQueryInfo.

        最小交易限额 单位元  # noqa: E501

        :param min_limit: The min_limit of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._min_limit = min_limit

    @property
    def max_limit(self):
        """Gets the max_limit of this AdvertisementListQueryInfo.  # noqa: E501

        最大交易限额 单位元  # noqa: E501

        :return: The max_limit of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._max_limit

    @max_limit.setter
    def max_limit(self, max_limit):
        """Sets the max_limit of this AdvertisementListQueryInfo.

        最大交易限额 单位元  # noqa: E501

        :param max_limit: The max_limit of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._max_limit = max_limit

    @property
    def remark(self):
        """Gets the remark of this AdvertisementListQueryInfo.  # noqa: E501

        交易备注信息  # noqa: E501

        :return: The remark of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AdvertisementListQueryInfo.

        交易备注信息  # noqa: E501

        :param remark: The remark of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def create_time(self):
        """Gets the create_time of this AdvertisementListQueryInfo.  # noqa: E501

        创建时间  # noqa: E501

        :return: The create_time of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AdvertisementListQueryInfo.

        创建时间  # noqa: E501

        :param create_time: The create_time of this AdvertisementListQueryInfo.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def order_count(self):
        """Gets the order_count of this AdvertisementListQueryInfo.  # noqa: E501

        正在进行的订单数量  # noqa: E501

        :return: The order_count of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this AdvertisementListQueryInfo.

        正在进行的订单数量  # noqa: E501

        :param order_count: The order_count of this AdvertisementListQueryInfo.  # noqa: E501
        :type: int
        """

        self._order_count = order_count

    @property
    def paymode_list(self):
        """Gets the paymode_list of this AdvertisementListQueryInfo.  # noqa: E501

        商家的支付方式 只有类型和id  # noqa: E501

        :return: The paymode_list of this AdvertisementListQueryInfo.  # noqa: E501
        :rtype: list[SimplePaymodeInfo]
        """
        return self._paymode_list

    @paymode_list.setter
    def paymode_list(self, paymode_list):
        """Sets the paymode_list of this AdvertisementListQueryInfo.

        商家的支付方式 只有类型和id  # noqa: E501

        :param paymode_list: The paymode_list of this AdvertisementListQueryInfo.  # noqa: E501
        :type: list[SimplePaymodeInfo]
        """

        self._paymode_list = paymode_list

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
        if issubclass(AdvertisementListQueryInfo, dict):
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
        if not isinstance(other, AdvertisementListQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
