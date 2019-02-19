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


class GetJournalsResponseItems(object):
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
        'amount': 'str',
        'order_id': 'str',
        'subject_type': 'str',
        'created_at': 'date',
        'style': 'str'
    }

    attribute_map = {
        'coin_id': 'coinId',
        'logo': 'logo',
        'short_name': 'shortName',
        'full_name': 'fullName',
        'amount': 'amount',
        'order_id': 'orderId',
        'subject_type': 'subjectType',
        'created_at': 'createdAt',
        'style': 'style'
    }

    def __init__(self, coin_id=None, logo=None, short_name=None, full_name=None, amount=None, order_id=None, subject_type=None, created_at=None, style=None):  # noqa: E501
        """GetJournalsResponseItems - a model defined in Swagger"""  # noqa: E501

        self._coin_id = None
        self._logo = None
        self._short_name = None
        self._full_name = None
        self._amount = None
        self._order_id = None
        self._subject_type = None
        self._created_at = None
        self._style = None
        self.discriminator = None

        if coin_id is not None:
            self.coin_id = coin_id
        if logo is not None:
            self.logo = logo
        if short_name is not None:
            self.short_name = short_name
        if full_name is not None:
            self.full_name = full_name
        if amount is not None:
            self.amount = amount
        if order_id is not None:
            self.order_id = order_id
        if subject_type is not None:
            self.subject_type = subject_type
        if created_at is not None:
            self.created_at = created_at
        if style is not None:
            self.style = style

    @property
    def coin_id(self):
        """Gets the coin_id of this GetJournalsResponseItems.  # noqa: E501

        币ID  # noqa: E501

        :return: The coin_id of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetJournalsResponseItems.

        币ID  # noqa: E501

        :param coin_id: The coin_id of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def logo(self):
        """Gets the logo of this GetJournalsResponseItems.  # noqa: E501

        币logo  # noqa: E501

        :return: The logo of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetJournalsResponseItems.

        币logo  # noqa: E501

        :param logo: The logo of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def short_name(self):
        """Gets the short_name of this GetJournalsResponseItems.  # noqa: E501

        币简称  # noqa: E501

        :return: The short_name of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetJournalsResponseItems.

        币简称  # noqa: E501

        :param short_name: The short_name of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def full_name(self):
        """Gets the full_name of this GetJournalsResponseItems.  # noqa: E501

        币全称  # noqa: E501

        :return: The full_name of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GetJournalsResponseItems.

        币全称  # noqa: E501

        :param full_name: The full_name of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def amount(self):
        """Gets the amount of this GetJournalsResponseItems.  # noqa: E501

        变动资产数量  # noqa: E501

        :return: The amount of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetJournalsResponseItems.

        变动资产数量  # noqa: E501

        :param amount: The amount of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def order_id(self):
        """Gets the order_id of this GetJournalsResponseItems.  # noqa: E501

        单号  # noqa: E501

        :return: The order_id of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this GetJournalsResponseItems.

        单号  # noqa: E501

        :param order_id: The order_id of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def subject_type(self):
        """Gets the subject_type of this GetJournalsResponseItems.  # noqa: E501

        科目类型  # noqa: E501

        :return: The subject_type of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this GetJournalsResponseItems.

        科目类型  # noqa: E501

        :param subject_type: The subject_type of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["C2C", "RECHARGE", "WITHDRAW", "ACTIVITY_IN", "ACTIVITY_OUT", "COMMISSION", "FEE", "BUY_COMMODITY", "SERVICE", "OTC_TRANSFER_IN", "OTC_TRANSFER_OUT"]  # noqa: E501
        if subject_type not in allowed_values:
            raise ValueError(
                "Invalid value for `subject_type` ({0}), must be one of {1}"  # noqa: E501
                .format(subject_type, allowed_values)
            )

        self._subject_type = subject_type

    @property
    def created_at(self):
        """Gets the created_at of this GetJournalsResponseItems.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this GetJournalsResponseItems.  # noqa: E501
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetJournalsResponseItems.

        创建时间  # noqa: E501

        :param created_at: The created_at of this GetJournalsResponseItems.  # noqa: E501
        :type: date
        """

        self._created_at = created_at

    @property
    def style(self):
        """Gets the style of this GetJournalsResponseItems.  # noqa: E501

        财务类型  # noqa: E501

        :return: The style of this GetJournalsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this GetJournalsResponseItems.

        财务类型  # noqa: E501

        :param style: The style of this GetJournalsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["INCREASE", "DECREASE"]  # noqa: E501
        if style not in allowed_values:
            raise ValueError(
                "Invalid value for `style` ({0}), must be one of {1}"  # noqa: E501
                .format(style, allowed_values)
            )

        self._style = style

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
        if issubclass(GetJournalsResponseItems, dict):
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
        if not isinstance(other, GetJournalsResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other