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


class GetRechargeRecordsResponseItems(object):
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
        'short_name': 'str',
        'full_name': 'str',
        'logo': 'str',
        'confirmation_number': 'int',
        'completed_at': 'datetime',
        'amount': 'str',
        'address': 'str',
        'txid': 'str',
        'status': 'str',
        'confirmed_times': 'int'
    }

    attribute_map = {
        'coin_id': 'coinId',
        'short_name': 'shortName',
        'full_name': 'fullName',
        'logo': 'logo',
        'confirmation_number': 'confirmationNumber',
        'completed_at': 'completedAt',
        'amount': 'amount',
        'address': 'address',
        'txid': 'txid',
        'status': 'status',
        'confirmed_times': 'confirmedTimes'
    }

    def __init__(self, coin_id=None, short_name=None, full_name=None, logo=None, confirmation_number=None, completed_at=None, amount=None, address=None, txid=None, status=None, confirmed_times=None):  # noqa: E501
        """GetRechargeRecordsResponseItems - a model defined in Swagger"""  # noqa: E501

        self._coin_id = None
        self._short_name = None
        self._full_name = None
        self._logo = None
        self._confirmation_number = None
        self._completed_at = None
        self._amount = None
        self._address = None
        self._txid = None
        self._status = None
        self._confirmed_times = None
        self.discriminator = None

        if coin_id is not None:
            self.coin_id = coin_id
        if short_name is not None:
            self.short_name = short_name
        if full_name is not None:
            self.full_name = full_name
        if logo is not None:
            self.logo = logo
        if confirmation_number is not None:
            self.confirmation_number = confirmation_number
        if completed_at is not None:
            self.completed_at = completed_at
        if amount is not None:
            self.amount = amount
        if address is not None:
            self.address = address
        if txid is not None:
            self.txid = txid
        if status is not None:
            self.status = status
        if confirmed_times is not None:
            self.confirmed_times = confirmed_times

    @property
    def coin_id(self):
        """Gets the coin_id of this GetRechargeRecordsResponseItems.  # noqa: E501

        币id  # noqa: E501

        :return: The coin_id of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetRechargeRecordsResponseItems.

        币id  # noqa: E501

        :param coin_id: The coin_id of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def short_name(self):
        """Gets the short_name of this GetRechargeRecordsResponseItems.  # noqa: E501

        币简称  # noqa: E501

        :return: The short_name of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetRechargeRecordsResponseItems.

        币简称  # noqa: E501

        :param short_name: The short_name of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def full_name(self):
        """Gets the full_name of this GetRechargeRecordsResponseItems.  # noqa: E501

        币全称  # noqa: E501

        :return: The full_name of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GetRechargeRecordsResponseItems.

        币全称  # noqa: E501

        :param full_name: The full_name of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def logo(self):
        """Gets the logo of this GetRechargeRecordsResponseItems.  # noqa: E501

        币Logo  # noqa: E501

        :return: The logo of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetRechargeRecordsResponseItems.

        币Logo  # noqa: E501

        :param logo: The logo of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def confirmation_number(self):
        """Gets the confirmation_number of this GetRechargeRecordsResponseItems.  # noqa: E501

        区块确认数  # noqa: E501

        :return: The confirmation_number of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: int
        """
        return self._confirmation_number

    @confirmation_number.setter
    def confirmation_number(self, confirmation_number):
        """Sets the confirmation_number of this GetRechargeRecordsResponseItems.

        区块确认数  # noqa: E501

        :param confirmation_number: The confirmation_number of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: int
        """

        self._confirmation_number = confirmation_number

    @property
    def completed_at(self):
        """Gets the completed_at of this GetRechargeRecordsResponseItems.  # noqa: E501

        完成时间  # noqa: E501

        :return: The completed_at of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this GetRechargeRecordsResponseItems.

        完成时间  # noqa: E501

        :param completed_at: The completed_at of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: datetime
        """

        self._completed_at = completed_at

    @property
    def amount(self):
        """Gets the amount of this GetRechargeRecordsResponseItems.  # noqa: E501

        充币数量  # noqa: E501

        :return: The amount of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetRechargeRecordsResponseItems.

        充币数量  # noqa: E501

        :param amount: The amount of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def address(self):
        """Gets the address of this GetRechargeRecordsResponseItems.  # noqa: E501

        充币地址  # noqa: E501

        :return: The address of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetRechargeRecordsResponseItems.

        充币地址  # noqa: E501

        :param address: The address of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def txid(self):
        """Gets the txid of this GetRechargeRecordsResponseItems.  # noqa: E501

        交易hash  # noqa: E501

        :return: The txid of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetRechargeRecordsResponseItems.

        交易hash  # noqa: E501

        :param txid: The txid of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def status(self):
        """Gets the status of this GetRechargeRecordsResponseItems.  # noqa: E501

        充币状态  # noqa: E501

        :return: The status of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetRechargeRecordsResponseItems.

        充币状态  # noqa: E501

        :param status: The status of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCEED", "FAILED", "CONFIRMING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def confirmed_times(self):
        """Gets the confirmed_times of this GetRechargeRecordsResponseItems.  # noqa: E501

        区块确认次数  # noqa: E501

        :return: The confirmed_times of this GetRechargeRecordsResponseItems.  # noqa: E501
        :rtype: int
        """
        return self._confirmed_times

    @confirmed_times.setter
    def confirmed_times(self, confirmed_times):
        """Sets the confirmed_times of this GetRechargeRecordsResponseItems.

        区块确认次数  # noqa: E501

        :param confirmed_times: The confirmed_times of this GetRechargeRecordsResponseItems.  # noqa: E501
        :type: int
        """

        self._confirmed_times = confirmed_times

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
        if issubclass(GetRechargeRecordsResponseItems, dict):
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
        if not isinstance(other, GetRechargeRecordsResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
