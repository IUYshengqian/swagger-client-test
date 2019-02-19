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


class GetAccountRestrictionResponse(object):
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
        'withdraw': 'bool',
        'otc': 'bool'
    }

    attribute_map = {
        'withdraw': 'withdraw',
        'otc': 'otc'
    }

    def __init__(self, withdraw=None, otc=None):  # noqa: E501
        """GetAccountRestrictionResponse - a model defined in Swagger"""  # noqa: E501

        self._withdraw = None
        self._otc = None
        self.discriminator = None

        if withdraw is not None:
            self.withdraw = withdraw
        if otc is not None:
            self.otc = otc

    @property
    def withdraw(self):
        """Gets the withdraw of this GetAccountRestrictionResponse.  # noqa: E501

        提币限制  # noqa: E501

        :return: The withdraw of this GetAccountRestrictionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._withdraw

    @withdraw.setter
    def withdraw(self, withdraw):
        """Sets the withdraw of this GetAccountRestrictionResponse.

        提币限制  # noqa: E501

        :param withdraw: The withdraw of this GetAccountRestrictionResponse.  # noqa: E501
        :type: bool
        """

        self._withdraw = withdraw

    @property
    def otc(self):
        """Gets the otc of this GetAccountRestrictionResponse.  # noqa: E501

        交易限制  # noqa: E501

        :return: The otc of this GetAccountRestrictionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._otc

    @otc.setter
    def otc(self, otc):
        """Sets the otc of this GetAccountRestrictionResponse.

        交易限制  # noqa: E501

        :param otc: The otc of this GetAccountRestrictionResponse.  # noqa: E501
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
        if issubclass(GetAccountRestrictionResponse, dict):
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
        if not isinstance(other, GetAccountRestrictionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
