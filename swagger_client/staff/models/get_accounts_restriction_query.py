# coding: utf-8

"""
    crush-staff 平台接口（职员管理平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAccountsRestrictionQuery(object):
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
        'start_at': 'str',
        'end_at': 'str',
        'account_id': 'str',
        'withdraw': 'bool',
        'otc': 'bool'
    }

    attribute_map = {
        'start_at': 'startAt',
        'end_at': 'endAt',
        'account_id': 'accountId',
        'withdraw': 'withdraw',
        'otc': 'otc'
    }

    def __init__(self, start_at=None, end_at=None, account_id=None, withdraw=None, otc=None):  # noqa: E501
        """GetAccountsRestrictionQuery - a model defined in Swagger"""  # noqa: E501

        self._start_at = None
        self._end_at = None
        self._account_id = None
        self._withdraw = None
        self._otc = None
        self.discriminator = None

        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if account_id is not None:
            self.account_id = account_id
        if withdraw is not None:
            self.withdraw = withdraw
        if otc is not None:
            self.otc = otc

    @property
    def start_at(self):
        """Gets the start_at of this GetAccountsRestrictionQuery.  # noqa: E501

        开始创建时间  # noqa: E501

        :return: The start_at of this GetAccountsRestrictionQuery.  # noqa: E501
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this GetAccountsRestrictionQuery.

        开始创建时间  # noqa: E501

        :param start_at: The start_at of this GetAccountsRestrictionQuery.  # noqa: E501
        :type: str
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this GetAccountsRestrictionQuery.  # noqa: E501

        结束创建时间  # noqa: E501

        :return: The end_at of this GetAccountsRestrictionQuery.  # noqa: E501
        :rtype: str
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this GetAccountsRestrictionQuery.

        结束创建时间  # noqa: E501

        :param end_at: The end_at of this GetAccountsRestrictionQuery.  # noqa: E501
        :type: str
        """

        self._end_at = end_at

    @property
    def account_id(self):
        """Gets the account_id of this GetAccountsRestrictionQuery.  # noqa: E501

        uid  # noqa: E501

        :return: The account_id of this GetAccountsRestrictionQuery.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetAccountsRestrictionQuery.

        uid  # noqa: E501

        :param account_id: The account_id of this GetAccountsRestrictionQuery.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def withdraw(self):
        """Gets the withdraw of this GetAccountsRestrictionQuery.  # noqa: E501

        提币限制  # noqa: E501

        :return: The withdraw of this GetAccountsRestrictionQuery.  # noqa: E501
        :rtype: bool
        """
        return self._withdraw

    @withdraw.setter
    def withdraw(self, withdraw):
        """Sets the withdraw of this GetAccountsRestrictionQuery.

        提币限制  # noqa: E501

        :param withdraw: The withdraw of this GetAccountsRestrictionQuery.  # noqa: E501
        :type: bool
        """

        self._withdraw = withdraw

    @property
    def otc(self):
        """Gets the otc of this GetAccountsRestrictionQuery.  # noqa: E501

        法币交易限制  # noqa: E501

        :return: The otc of this GetAccountsRestrictionQuery.  # noqa: E501
        :rtype: bool
        """
        return self._otc

    @otc.setter
    def otc(self, otc):
        """Sets the otc of this GetAccountsRestrictionQuery.

        法币交易限制  # noqa: E501

        :param otc: The otc of this GetAccountsRestrictionQuery.  # noqa: E501
        :type: bool
        """

        self._otc = otc

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
        if issubclass(GetAccountsRestrictionQuery, dict):
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
        if not isinstance(other, GetAccountsRestrictionQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
