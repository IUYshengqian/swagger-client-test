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


class GetWithdrawableListsResponseInner(object):
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
        'coin_id': 'str',
        'logo': 'str',
        'short_name': 'str',
        'full_name': 'str',
        'confirmation_number': 'int',
        'min_withdraw': 'str',
        'max_withdraw': 'str',
        'withdraw_rate': 'str',
        'min_fee': 'str',
        'max_withdraw_one_day': 'str'
    }

    attribute_map = {
        'coin_id': 'coinId',
        'logo': 'logo',
        'short_name': 'shortName',
        'full_name': 'fullName',
        'confirmation_number': 'confirmationNumber',
        'min_withdraw': 'minWithdraw',
        'max_withdraw': 'maxWithdraw',
        'withdraw_rate': 'withdrawRate',
        'min_fee': 'minFee',
        'max_withdraw_one_day': 'maxWithdrawOneDay'
    }

    def __init__(self, coin_id=None, logo=None, short_name=None, full_name=None, confirmation_number=None, min_withdraw=None, max_withdraw=None, withdraw_rate=None, min_fee=None, max_withdraw_one_day=None):  # noqa: E501
        """GetWithdrawableListsResponseInner - a model defined in Swagger"""  # noqa: E501

        self._coin_id = None
        self._logo = None
        self._short_name = None
        self._full_name = None
        self._confirmation_number = None
        self._min_withdraw = None
        self._max_withdraw = None
        self._withdraw_rate = None
        self._min_fee = None
        self._max_withdraw_one_day = None
        self.discriminator = None

        if coin_id is not None:
            self.coin_id = coin_id
        if logo is not None:
            self.logo = logo
        if short_name is not None:
            self.short_name = short_name
        if full_name is not None:
            self.full_name = full_name
        if confirmation_number is not None:
            self.confirmation_number = confirmation_number
        if min_withdraw is not None:
            self.min_withdraw = min_withdraw
        if max_withdraw is not None:
            self.max_withdraw = max_withdraw
        if withdraw_rate is not None:
            self.withdraw_rate = withdraw_rate
        if min_fee is not None:
            self.min_fee = min_fee
        if max_withdraw_one_day is not None:
            self.max_withdraw_one_day = max_withdraw_one_day

    @property
    def coin_id(self):
        """Gets the coin_id of this GetWithdrawableListsResponseInner.  # noqa: E501

        币ID  # noqa: E501

        :return: The coin_id of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetWithdrawableListsResponseInner.

        币ID  # noqa: E501

        :param coin_id: The coin_id of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def logo(self):
        """Gets the logo of this GetWithdrawableListsResponseInner.  # noqa: E501

        币logo  # noqa: E501

        :return: The logo of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetWithdrawableListsResponseInner.

        币logo  # noqa: E501

        :param logo: The logo of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def short_name(self):
        """Gets the short_name of this GetWithdrawableListsResponseInner.  # noqa: E501

        币简称  # noqa: E501

        :return: The short_name of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetWithdrawableListsResponseInner.

        币简称  # noqa: E501

        :param short_name: The short_name of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def full_name(self):
        """Gets the full_name of this GetWithdrawableListsResponseInner.  # noqa: E501

        币全称  # noqa: E501

        :return: The full_name of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GetWithdrawableListsResponseInner.

        币全称  # noqa: E501

        :param full_name: The full_name of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def confirmation_number(self):
        """Gets the confirmation_number of this GetWithdrawableListsResponseInner.  # noqa: E501

        区块确认数量  # noqa: E501

        :return: The confirmation_number of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._confirmation_number

    @confirmation_number.setter
    def confirmation_number(self, confirmation_number):
        """Sets the confirmation_number of this GetWithdrawableListsResponseInner.

        区块确认数量  # noqa: E501

        :param confirmation_number: The confirmation_number of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: int
        """

        self._confirmation_number = confirmation_number

    @property
    def min_withdraw(self):
        """Gets the min_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501

        单笔最小提币数量  # noqa: E501

        :return: The min_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._min_withdraw

    @min_withdraw.setter
    def min_withdraw(self, min_withdraw):
        """Sets the min_withdraw of this GetWithdrawableListsResponseInner.

        单笔最小提币数量  # noqa: E501

        :param min_withdraw: The min_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._min_withdraw = min_withdraw

    @property
    def max_withdraw(self):
        """Gets the max_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501

        单笔最大提币数量  # noqa: E501

        :return: The max_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._max_withdraw

    @max_withdraw.setter
    def max_withdraw(self, max_withdraw):
        """Sets the max_withdraw of this GetWithdrawableListsResponseInner.

        单笔最大提币数量  # noqa: E501

        :param max_withdraw: The max_withdraw of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._max_withdraw = max_withdraw

    @property
    def withdraw_rate(self):
        """Gets the withdraw_rate of this GetWithdrawableListsResponseInner.  # noqa: E501

        提币手续费率  # noqa: E501

        :return: The withdraw_rate of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_rate

    @withdraw_rate.setter
    def withdraw_rate(self, withdraw_rate):
        """Sets the withdraw_rate of this GetWithdrawableListsResponseInner.

        提币手续费率  # noqa: E501

        :param withdraw_rate: The withdraw_rate of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._withdraw_rate = withdraw_rate

    @property
    def min_fee(self):
        """Gets the min_fee of this GetWithdrawableListsResponseInner.  # noqa: E501

        提币最小手续费  # noqa: E501

        :return: The min_fee of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._min_fee

    @min_fee.setter
    def min_fee(self, min_fee):
        """Sets the min_fee of this GetWithdrawableListsResponseInner.

        提币最小手续费  # noqa: E501

        :param min_fee: The min_fee of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._min_fee = min_fee

    @property
    def max_withdraw_one_day(self):
        """Gets the max_withdraw_one_day of this GetWithdrawableListsResponseInner.  # noqa: E501

        每日提币最大数量  # noqa: E501

        :return: The max_withdraw_one_day of this GetWithdrawableListsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._max_withdraw_one_day

    @max_withdraw_one_day.setter
    def max_withdraw_one_day(self, max_withdraw_one_day):
        """Sets the max_withdraw_one_day of this GetWithdrawableListsResponseInner.

        每日提币最大数量  # noqa: E501

        :param max_withdraw_one_day: The max_withdraw_one_day of this GetWithdrawableListsResponseInner.  # noqa: E501
        :type: str
        """

        self._max_withdraw_one_day = max_withdraw_one_day

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
        if issubclass(GetWithdrawableListsResponseInner, dict):
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
        if not isinstance(other, GetWithdrawableListsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
