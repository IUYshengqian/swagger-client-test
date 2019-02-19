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


class GetMarketResponse(object):
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
        'trading_pair': 'str',
        'total_rate': 'float',
        'fee_rate': 'float',
        'service_rate': 'float',
        'disabled_at': 'datetime',
        'buyer_coin_id': 'str',
        'seller_coin_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'trading_pair': 'tradingPair',
        'total_rate': 'totalRate',
        'fee_rate': 'feeRate',
        'service_rate': 'serviceRate',
        'disabled_at': 'disabledAt',
        'buyer_coin_id': 'buyerCoinId',
        'seller_coin_id': 'sellerCoinId'
    }

    def __init__(self, id=None, trading_pair=None, total_rate=None, fee_rate=None, service_rate=None, disabled_at=None, buyer_coin_id=None, seller_coin_id=None):  # noqa: E501
        """GetMarketResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._trading_pair = None
        self._total_rate = None
        self._fee_rate = None
        self._service_rate = None
        self._disabled_at = None
        self._buyer_coin_id = None
        self._seller_coin_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trading_pair is not None:
            self.trading_pair = trading_pair
        if total_rate is not None:
            self.total_rate = total_rate
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if service_rate is not None:
            self.service_rate = service_rate
        if disabled_at is not None:
            self.disabled_at = disabled_at
        if buyer_coin_id is not None:
            self.buyer_coin_id = buyer_coin_id
        if seller_coin_id is not None:
            self.seller_coin_id = seller_coin_id

    @property
    def id(self):
        """Gets the id of this GetMarketResponse.  # noqa: E501

        市场ID  # noqa: E501

        :return: The id of this GetMarketResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetMarketResponse.

        市场ID  # noqa: E501

        :param id: The id of this GetMarketResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trading_pair(self):
        """Gets the trading_pair of this GetMarketResponse.  # noqa: E501

        市场标识  # noqa: E501

        :return: The trading_pair of this GetMarketResponse.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this GetMarketResponse.

        市场标识  # noqa: E501

        :param trading_pair: The trading_pair of this GetMarketResponse.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

    @property
    def total_rate(self):
        """Gets the total_rate of this GetMarketResponse.  # noqa: E501

        总手续费率  # noqa: E501

        :return: The total_rate of this GetMarketResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_rate

    @total_rate.setter
    def total_rate(self, total_rate):
        """Sets the total_rate of this GetMarketResponse.

        总手续费率  # noqa: E501

        :param total_rate: The total_rate of this GetMarketResponse.  # noqa: E501
        :type: float
        """

        self._total_rate = total_rate

    @property
    def fee_rate(self):
        """Gets the fee_rate of this GetMarketResponse.  # noqa: E501

        手续费收益率  # noqa: E501

        :return: The fee_rate of this GetMarketResponse.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this GetMarketResponse.

        手续费收益率  # noqa: E501

        :param fee_rate: The fee_rate of this GetMarketResponse.  # noqa: E501
        :type: float
        """

        self._fee_rate = fee_rate

    @property
    def service_rate(self):
        """Gets the service_rate of this GetMarketResponse.  # noqa: E501

        交易服务费率  # noqa: E501

        :return: The service_rate of this GetMarketResponse.  # noqa: E501
        :rtype: float
        """
        return self._service_rate

    @service_rate.setter
    def service_rate(self, service_rate):
        """Sets the service_rate of this GetMarketResponse.

        交易服务费率  # noqa: E501

        :param service_rate: The service_rate of this GetMarketResponse.  # noqa: E501
        :type: float
        """

        self._service_rate = service_rate

    @property
    def disabled_at(self):
        """Gets the disabled_at of this GetMarketResponse.  # noqa: E501

        失效时间  # noqa: E501

        :return: The disabled_at of this GetMarketResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._disabled_at

    @disabled_at.setter
    def disabled_at(self, disabled_at):
        """Sets the disabled_at of this GetMarketResponse.

        失效时间  # noqa: E501

        :param disabled_at: The disabled_at of this GetMarketResponse.  # noqa: E501
        :type: datetime
        """

        self._disabled_at = disabled_at

    @property
    def buyer_coin_id(self):
        """Gets the buyer_coin_id of this GetMarketResponse.  # noqa: E501

        买方币种ID  # noqa: E501

        :return: The buyer_coin_id of this GetMarketResponse.  # noqa: E501
        :rtype: str
        """
        return self._buyer_coin_id

    @buyer_coin_id.setter
    def buyer_coin_id(self, buyer_coin_id):
        """Sets the buyer_coin_id of this GetMarketResponse.

        买方币种ID  # noqa: E501

        :param buyer_coin_id: The buyer_coin_id of this GetMarketResponse.  # noqa: E501
        :type: str
        """
        if buyer_coin_id is not None and len(buyer_coin_id) > 32:
            raise ValueError("Invalid value for `buyer_coin_id`, length must be less than or equal to `32`")  # noqa: E501
        if buyer_coin_id is not None and len(buyer_coin_id) < 1:
            raise ValueError("Invalid value for `buyer_coin_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._buyer_coin_id = buyer_coin_id

    @property
    def seller_coin_id(self):
        """Gets the seller_coin_id of this GetMarketResponse.  # noqa: E501

        卖方币种ID  # noqa: E501

        :return: The seller_coin_id of this GetMarketResponse.  # noqa: E501
        :rtype: str
        """
        return self._seller_coin_id

    @seller_coin_id.setter
    def seller_coin_id(self, seller_coin_id):
        """Sets the seller_coin_id of this GetMarketResponse.

        卖方币种ID  # noqa: E501

        :param seller_coin_id: The seller_coin_id of this GetMarketResponse.  # noqa: E501
        :type: str
        """
        if seller_coin_id is not None and len(seller_coin_id) > 32:
            raise ValueError("Invalid value for `seller_coin_id`, length must be less than or equal to `32`")  # noqa: E501
        if seller_coin_id is not None and len(seller_coin_id) < 1:
            raise ValueError("Invalid value for `seller_coin_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._seller_coin_id = seller_coin_id

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
        if issubclass(GetMarketResponse, dict):
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
        if not isinstance(other, GetMarketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
