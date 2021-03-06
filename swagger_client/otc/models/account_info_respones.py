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

from swagger_client.otc.models.phone_number import PhoneNumber  # noqa: F401,E501


class AccountInfoRespones(object):
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
        'venture_id': 'str',
        'tenant_id': 'str',
        'investor_id': 'str',
        'nationality_code': 'str',
        'account_number': 'str',
        'account_id': 'str',
        'email': 'str',
        'phone_number': 'PhoneNumber',
        'created_at': 'datetime',
        'google_authenticator': 'bool',
        'area_code': 'str',
        'promotion_code': 'str',
        'exchange_id': 'str',
        'otc_id': 'str'
    }

    attribute_map = {
        'venture_id': 'ventureId',
        'tenant_id': 'tenantId',
        'investor_id': 'investorId',
        'nationality_code': 'nationalityCode',
        'account_number': 'accountNumber',
        'account_id': 'accountId',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'created_at': 'createdAt',
        'google_authenticator': 'googleAuthenticator',
        'area_code': 'areaCode',
        'promotion_code': 'promotionCode',
        'exchange_id': 'exchangeId',
        'otc_id': 'otcId'
    }

    def __init__(self, venture_id=None, tenant_id=None, investor_id=None, nationality_code=None, account_number=None, account_id=None, email=None, phone_number=None, created_at=None, google_authenticator=None, area_code=None, promotion_code=None, exchange_id=None, otc_id=None):  # noqa: E501
        """AccountInfoRespones - a model defined in Swagger"""  # noqa: E501

        self._venture_id = None
        self._tenant_id = None
        self._investor_id = None
        self._nationality_code = None
        self._account_number = None
        self._account_id = None
        self._email = None
        self._phone_number = None
        self._created_at = None
        self._google_authenticator = None
        self._area_code = None
        self._promotion_code = None
        self._exchange_id = None
        self._otc_id = None
        self.discriminator = None

        if venture_id is not None:
            self.venture_id = venture_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if investor_id is not None:
            self.investor_id = investor_id
        if nationality_code is not None:
            self.nationality_code = nationality_code
        if account_number is not None:
            self.account_number = account_number
        if account_id is not None:
            self.account_id = account_id
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if created_at is not None:
            self.created_at = created_at
        if google_authenticator is not None:
            self.google_authenticator = google_authenticator
        if area_code is not None:
            self.area_code = area_code
        if promotion_code is not None:
            self.promotion_code = promotion_code
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if otc_id is not None:
            self.otc_id = otc_id

    @property
    def venture_id(self):
        """Gets the venture_id of this AccountInfoRespones.  # noqa: E501

        项目方id  # noqa: E501

        :return: The venture_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._venture_id

    @venture_id.setter
    def venture_id(self, venture_id):
        """Sets the venture_id of this AccountInfoRespones.

        项目方id  # noqa: E501

        :param venture_id: The venture_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._venture_id = venture_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AccountInfoRespones.  # noqa: E501

        租户id  # noqa: E501

        :return: The tenant_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AccountInfoRespones.

        租户id  # noqa: E501

        :param tenant_id: The tenant_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def investor_id(self):
        """Gets the investor_id of this AccountInfoRespones.  # noqa: E501

        主平台id  # noqa: E501

        :return: The investor_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._investor_id

    @investor_id.setter
    def investor_id(self, investor_id):
        """Sets the investor_id of this AccountInfoRespones.

        主平台id  # noqa: E501

        :param investor_id: The investor_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._investor_id = investor_id

    @property
    def nationality_code(self):
        """Gets the nationality_code of this AccountInfoRespones.  # noqa: E501

        账号注册的国家  # noqa: E501

        :return: The nationality_code of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._nationality_code

    @nationality_code.setter
    def nationality_code(self, nationality_code):
        """Sets the nationality_code of this AccountInfoRespones.

        账号注册的国家  # noqa: E501

        :param nationality_code: The nationality_code of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._nationality_code = nationality_code

    @property
    def account_number(self):
        """Gets the account_number of this AccountInfoRespones.  # noqa: E501

        账号  # noqa: E501

        :return: The account_number of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountInfoRespones.

        账号  # noqa: E501

        :param account_number: The account_number of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_id(self):
        """Gets the account_id of this AccountInfoRespones.  # noqa: E501

        UID  # noqa: E501

        :return: The account_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountInfoRespones.

        UID  # noqa: E501

        :param account_id: The account_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def email(self):
        """Gets the email of this AccountInfoRespones.  # noqa: E501

        邮箱对象  # noqa: E501

        :return: The email of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountInfoRespones.

        邮箱对象  # noqa: E501

        :param email: The email of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this AccountInfoRespones.  # noqa: E501


        :return: The phone_number of this AccountInfoRespones.  # noqa: E501
        :rtype: PhoneNumber
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AccountInfoRespones.


        :param phone_number: The phone_number of this AccountInfoRespones.  # noqa: E501
        :type: PhoneNumber
        """

        self._phone_number = phone_number

    @property
    def created_at(self):
        """Gets the created_at of this AccountInfoRespones.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this AccountInfoRespones.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountInfoRespones.

        创建时间  # noqa: E501

        :param created_at: The created_at of this AccountInfoRespones.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def google_authenticator(self):
        """Gets the google_authenticator of this AccountInfoRespones.  # noqa: E501

        谷歌是否绑定(没绑定字段空;绑定为1)  # noqa: E501

        :return: The google_authenticator of this AccountInfoRespones.  # noqa: E501
        :rtype: bool
        """
        return self._google_authenticator

    @google_authenticator.setter
    def google_authenticator(self, google_authenticator):
        """Sets the google_authenticator of this AccountInfoRespones.

        谷歌是否绑定(没绑定字段空;绑定为1)  # noqa: E501

        :param google_authenticator: The google_authenticator of this AccountInfoRespones.  # noqa: E501
        :type: bool
        """

        self._google_authenticator = google_authenticator

    @property
    def area_code(self):
        """Gets the area_code of this AccountInfoRespones.  # noqa: E501

        国际码  # noqa: E501

        :return: The area_code of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this AccountInfoRespones.

        国际码  # noqa: E501

        :param area_code: The area_code of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def promotion_code(self):
        """Gets the promotion_code of this AccountInfoRespones.  # noqa: E501

        邀请码  # noqa: E501

        :return: The promotion_code of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._promotion_code

    @promotion_code.setter
    def promotion_code(self, promotion_code):
        """Sets the promotion_code of this AccountInfoRespones.

        邀请码  # noqa: E501

        :param promotion_code: The promotion_code of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._promotion_code = promotion_code

    @property
    def exchange_id(self):
        """Gets the exchange_id of this AccountInfoRespones.  # noqa: E501

        交易所id  # noqa: E501

        :return: The exchange_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this AccountInfoRespones.

        交易所id  # noqa: E501

        :param exchange_id: The exchange_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def otc_id(self):
        """Gets the otc_id of this AccountInfoRespones.  # noqa: E501

        法币id  # noqa: E501

        :return: The otc_id of this AccountInfoRespones.  # noqa: E501
        :rtype: str
        """
        return self._otc_id

    @otc_id.setter
    def otc_id(self, otc_id):
        """Sets the otc_id of this AccountInfoRespones.

        法币id  # noqa: E501

        :param otc_id: The otc_id of this AccountInfoRespones.  # noqa: E501
        :type: str
        """

        self._otc_id = otc_id

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
        if issubclass(AccountInfoRespones, dict):
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
        if not isinstance(other, AccountInfoRespones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
