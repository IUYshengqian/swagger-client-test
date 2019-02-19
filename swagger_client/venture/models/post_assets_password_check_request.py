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


class PostAssetsPasswordCheckRequest(object):
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
        'tra_password': 'str',
        'coin_id': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'tra_password': 'traPassword',
        'coin_id': 'coinId',
        'amount': 'amount'
    }

    def __init__(self, tra_password=None, coin_id=None, amount=None):  # noqa: E501
        """PostAssetsPasswordCheckRequest - a model defined in Swagger"""  # noqa: E501

        self._tra_password = None
        self._coin_id = None
        self._amount = None
        self.discriminator = None

        if tra_password is not None:
            self.tra_password = tra_password
        if coin_id is not None:
            self.coin_id = coin_id
        if amount is not None:
            self.amount = amount

    @property
    def tra_password(self):
        """Gets the tra_password of this PostAssetsPasswordCheckRequest.  # noqa: E501

        资产密码  # noqa: E501

        :return: The tra_password of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._tra_password

    @tra_password.setter
    def tra_password(self, tra_password):
        """Sets the tra_password of this PostAssetsPasswordCheckRequest.

        资产密码  # noqa: E501

        :param tra_password: The tra_password of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :type: str
        """
        if tra_password is not None and len(tra_password) > 16:
            raise ValueError("Invalid value for `tra_password`, length must be less than or equal to `16`")  # noqa: E501
        if tra_password is not None and len(tra_password) < 8:
            raise ValueError("Invalid value for `tra_password`, length must be greater than or equal to `8`")  # noqa: E501

        self._tra_password = tra_password

    @property
    def coin_id(self):
        """Gets the coin_id of this PostAssetsPasswordCheckRequest.  # noqa: E501

        币种  # noqa: E501

        :return: The coin_id of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this PostAssetsPasswordCheckRequest.

        币种  # noqa: E501

        :param coin_id: The coin_id of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

    @property
    def amount(self):
        """Gets the amount of this PostAssetsPasswordCheckRequest.  # noqa: E501

        数量  # noqa: E501

        :return: The amount of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PostAssetsPasswordCheckRequest.

        数量  # noqa: E501

        :param amount: The amount of this PostAssetsPasswordCheckRequest.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if issubclass(PostAssetsPasswordCheckRequest, dict):
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
        if not isinstance(other, PostAssetsPasswordCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
