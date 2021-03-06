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


class GetContactsResponseItems(object):
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
        'volume24_h': 'str',
        'contact_id': 'str',
        'exchange_id': 'str',
        'exchange_name': 'str',
        'logo': 'str',
        'sented_at': 'str',
        'currency_quantity': 'str'
    }

    attribute_map = {
        'volume24_h': 'volume24H',
        'contact_id': 'contactId',
        'exchange_id': 'exchangeId',
        'exchange_name': 'exchangeName',
        'logo': 'logo',
        'sented_at': 'sentedAt',
        'currency_quantity': 'currencyQuantity'
    }

    def __init__(self, volume24_h=None, contact_id=None, exchange_id=None, exchange_name=None, logo=None, sented_at=None, currency_quantity=None):  # noqa: E501
        """GetContactsResponseItems - a model defined in Swagger"""  # noqa: E501

        self._volume24_h = None
        self._contact_id = None
        self._exchange_id = None
        self._exchange_name = None
        self._logo = None
        self._sented_at = None
        self._currency_quantity = None
        self.discriminator = None

        if volume24_h is not None:
            self.volume24_h = volume24_h
        if contact_id is not None:
            self.contact_id = contact_id
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if logo is not None:
            self.logo = logo
        if sented_at is not None:
            self.sented_at = sented_at
        if currency_quantity is not None:
            self.currency_quantity = currency_quantity

    @property
    def volume24_h(self):
        """Gets the volume24_h of this GetContactsResponseItems.  # noqa: E501

        24H交易量  # noqa: E501

        :return: The volume24_h of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._volume24_h

    @volume24_h.setter
    def volume24_h(self, volume24_h):
        """Sets the volume24_h of this GetContactsResponseItems.

        24H交易量  # noqa: E501

        :param volume24_h: The volume24_h of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._volume24_h = volume24_h

    @property
    def contact_id(self):
        """Gets the contact_id of this GetContactsResponseItems.  # noqa: E501

        对接ID  # noqa: E501

        :return: The contact_id of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this GetContactsResponseItems.

        对接ID  # noqa: E501

        :param contact_id: The contact_id of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def exchange_id(self):
        """Gets the exchange_id of this GetContactsResponseItems.  # noqa: E501

        交易所ID  # noqa: E501

        :return: The exchange_id of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this GetContactsResponseItems.

        交易所ID  # noqa: E501

        :param exchange_id: The exchange_id of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetContactsResponseItems.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The exchange_name of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetContactsResponseItems.

        交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def logo(self):
        """Gets the logo of this GetContactsResponseItems.  # noqa: E501

        交易所图标  # noqa: E501

        :return: The logo of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetContactsResponseItems.

        交易所图标  # noqa: E501

        :param logo: The logo of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def sented_at(self):
        """Gets the sented_at of this GetContactsResponseItems.  # noqa: E501

        发送时间  # noqa: E501

        :return: The sented_at of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._sented_at

    @sented_at.setter
    def sented_at(self, sented_at):
        """Sets the sented_at of this GetContactsResponseItems.

        发送时间  # noqa: E501

        :param sented_at: The sented_at of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._sented_at = sented_at

    @property
    def currency_quantity(self):
        """Gets the currency_quantity of this GetContactsResponseItems.  # noqa: E501

        币种数量  # noqa: E501

        :return: The currency_quantity of this GetContactsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._currency_quantity

    @currency_quantity.setter
    def currency_quantity(self, currency_quantity):
        """Sets the currency_quantity of this GetContactsResponseItems.

        币种数量  # noqa: E501

        :param currency_quantity: The currency_quantity of this GetContactsResponseItems.  # noqa: E501
        :type: str
        """

        self._currency_quantity = currency_quantity

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
        if issubclass(GetContactsResponseItems, dict):
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
        if not isinstance(other, GetContactsResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
