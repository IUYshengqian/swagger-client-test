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


class GetMarketListResponseItems(object):
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
        'created_at': 'datetime',
        'disabled_at': 'datetime',
        'deep_sharing': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'trading_pair': 'tradingPair',
        'total_rate': 'totalRate',
        'fee_rate': 'feeRate',
        'created_at': 'createdAt',
        'disabled_at': 'disabledAt',
        'deep_sharing': 'deepSharing',
        'status': 'status'
    }

    def __init__(self, id=None, trading_pair=None, total_rate=None, fee_rate=None, created_at=None, disabled_at=None, deep_sharing=None, status=None):  # noqa: E501
        """GetMarketListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._trading_pair = None
        self._total_rate = None
        self._fee_rate = None
        self._created_at = None
        self._disabled_at = None
        self._deep_sharing = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trading_pair is not None:
            self.trading_pair = trading_pair
        if total_rate is not None:
            self.total_rate = total_rate
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if created_at is not None:
            self.created_at = created_at
        if disabled_at is not None:
            self.disabled_at = disabled_at
        if deep_sharing is not None:
            self.deep_sharing = deep_sharing
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this GetMarketListResponseItems.  # noqa: E501

        交易对市场ID  # noqa: E501

        :return: The id of this GetMarketListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetMarketListResponseItems.

        交易对市场ID  # noqa: E501

        :param id: The id of this GetMarketListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trading_pair(self):
        """Gets the trading_pair of this GetMarketListResponseItems.  # noqa: E501

        市场币对  # noqa: E501

        :return: The trading_pair of this GetMarketListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this GetMarketListResponseItems.

        市场币对  # noqa: E501

        :param trading_pair: The trading_pair of this GetMarketListResponseItems.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

    @property
    def total_rate(self):
        """Gets the total_rate of this GetMarketListResponseItems.  # noqa: E501

        总手续费率  # noqa: E501

        :return: The total_rate of this GetMarketListResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._total_rate

    @total_rate.setter
    def total_rate(self, total_rate):
        """Sets the total_rate of this GetMarketListResponseItems.

        总手续费率  # noqa: E501

        :param total_rate: The total_rate of this GetMarketListResponseItems.  # noqa: E501
        :type: float
        """

        self._total_rate = total_rate

    @property
    def fee_rate(self):
        """Gets the fee_rate of this GetMarketListResponseItems.  # noqa: E501

        手续费收益率  # noqa: E501

        :return: The fee_rate of this GetMarketListResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this GetMarketListResponseItems.

        手续费收益率  # noqa: E501

        :param fee_rate: The fee_rate of this GetMarketListResponseItems.  # noqa: E501
        :type: float
        """

        self._fee_rate = fee_rate

    @property
    def created_at(self):
        """Gets the created_at of this GetMarketListResponseItems.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this GetMarketListResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetMarketListResponseItems.

        创建时间  # noqa: E501

        :param created_at: The created_at of this GetMarketListResponseItems.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def disabled_at(self):
        """Gets the disabled_at of this GetMarketListResponseItems.  # noqa: E501

        失效时间  # noqa: E501

        :return: The disabled_at of this GetMarketListResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._disabled_at

    @disabled_at.setter
    def disabled_at(self, disabled_at):
        """Sets the disabled_at of this GetMarketListResponseItems.

        失效时间  # noqa: E501

        :param disabled_at: The disabled_at of this GetMarketListResponseItems.  # noqa: E501
        :type: datetime
        """

        self._disabled_at = disabled_at

    @property
    def deep_sharing(self):
        """Gets the deep_sharing of this GetMarketListResponseItems.  # noqa: E501

        是否深度共享  # noqa: E501

        :return: The deep_sharing of this GetMarketListResponseItems.  # noqa: E501
        :rtype: bool
        """
        return self._deep_sharing

    @deep_sharing.setter
    def deep_sharing(self, deep_sharing):
        """Sets the deep_sharing of this GetMarketListResponseItems.

        是否深度共享  # noqa: E501

        :param deep_sharing: The deep_sharing of this GetMarketListResponseItems.  # noqa: E501
        :type: bool
        """

        self._deep_sharing = deep_sharing

    @property
    def status(self):
        """Gets the status of this GetMarketListResponseItems.  # noqa: E501

        状态  # noqa: E501

        :return: The status of this GetMarketListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetMarketListResponseItems.

        状态  # noqa: E501

        :param status: The status of this GetMarketListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["in_review", "running", "wait_close", "wait_renew", " closed_in"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(GetMarketListResponseItems, dict):
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
        if not isinstance(other, GetMarketListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
