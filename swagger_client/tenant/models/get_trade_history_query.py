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


class GetTradeHistoryQuery(object):
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
        'start_at': 'date',
        'end_at': 'date',
        'exchange_id': 'str',
        'exchange_name': 'str',
        'trade_history_id': 'str',
        'uid': 'str',
        'trding_pair': 'str'
    }

    attribute_map = {
        'start_at': 'startAt',
        'end_at': 'endAt',
        'exchange_id': 'exchangeId',
        'exchange_name': 'exchangeName',
        'trade_history_id': 'tradeHistoryId',
        'uid': 'uid',
        'trding_pair': 'trdingPair'
    }

    def __init__(self, start_at=None, end_at=None, exchange_id=None, exchange_name=None, trade_history_id=None, uid=None, trding_pair=None):  # noqa: E501
        """GetTradeHistoryQuery - a model defined in Swagger"""  # noqa: E501

        self._start_at = None
        self._end_at = None
        self._exchange_id = None
        self._exchange_name = None
        self._trade_history_id = None
        self._uid = None
        self._trding_pair = None
        self.discriminator = None

        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if trade_history_id is not None:
            self.trade_history_id = trade_history_id
        if uid is not None:
            self.uid = uid
        if trding_pair is not None:
            self.trding_pair = trding_pair

    @property
    def start_at(self):
        """Gets the start_at of this GetTradeHistoryQuery.  # noqa: E501

        开始时间  # noqa: E501

        :return: The start_at of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: date
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this GetTradeHistoryQuery.

        开始时间  # noqa: E501

        :param start_at: The start_at of this GetTradeHistoryQuery.  # noqa: E501
        :type: date
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this GetTradeHistoryQuery.  # noqa: E501

        结束时间  # noqa: E501

        :return: The end_at of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: date
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this GetTradeHistoryQuery.

        结束时间  # noqa: E501

        :param end_at: The end_at of this GetTradeHistoryQuery.  # noqa: E501
        :type: date
        """

        self._end_at = end_at

    @property
    def exchange_id(self):
        """Gets the exchange_id of this GetTradeHistoryQuery.  # noqa: E501

        交易所id  # noqa: E501

        :return: The exchange_id of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this GetTradeHistoryQuery.

        交易所id  # noqa: E501

        :param exchange_id: The exchange_id of this GetTradeHistoryQuery.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetTradeHistoryQuery.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The exchange_name of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetTradeHistoryQuery.

        交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetTradeHistoryQuery.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def trade_history_id(self):
        """Gets the trade_history_id of this GetTradeHistoryQuery.  # noqa: E501

        成交记录编号  # noqa: E501

        :return: The trade_history_id of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: str
        """
        return self._trade_history_id

    @trade_history_id.setter
    def trade_history_id(self, trade_history_id):
        """Sets the trade_history_id of this GetTradeHistoryQuery.

        成交记录编号  # noqa: E501

        :param trade_history_id: The trade_history_id of this GetTradeHistoryQuery.  # noqa: E501
        :type: str
        """

        self._trade_history_id = trade_history_id

    @property
    def uid(self):
        """Gets the uid of this GetTradeHistoryQuery.  # noqa: E501

        用户id  # noqa: E501

        :return: The uid of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetTradeHistoryQuery.

        用户id  # noqa: E501

        :param uid: The uid of this GetTradeHistoryQuery.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def trding_pair(self):
        """Gets the trding_pair of this GetTradeHistoryQuery.  # noqa: E501

        交易币对  # noqa: E501

        :return: The trding_pair of this GetTradeHistoryQuery.  # noqa: E501
        :rtype: str
        """
        return self._trding_pair

    @trding_pair.setter
    def trding_pair(self, trding_pair):
        """Sets the trding_pair of this GetTradeHistoryQuery.

        交易币对  # noqa: E501

        :param trding_pair: The trding_pair of this GetTradeHistoryQuery.  # noqa: E501
        :type: str
        """

        self._trding_pair = trding_pair

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
        if issubclass(GetTradeHistoryQuery, dict):
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
        if not isinstance(other, GetTradeHistoryQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
