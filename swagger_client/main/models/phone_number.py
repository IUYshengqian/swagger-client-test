# coding: utf-8

"""
    crush-main 平台接口（主平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PhoneNumber(object):
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
        'area_code': 'str',
        'full_phone_number': 'str',
        'short_phone_number': 'str'
    }

    attribute_map = {
        'area_code': 'areaCode',
        'full_phone_number': 'fullPhoneNumber',
        'short_phone_number': 'shortPhoneNumber'
    }

    def __init__(self, area_code=None, full_phone_number=None, short_phone_number=None):  # noqa: E501
        """PhoneNumber - a model defined in Swagger"""  # noqa: E501

        self._area_code = None
        self._full_phone_number = None
        self._short_phone_number = None
        self.discriminator = None

        if area_code is not None:
            self.area_code = area_code
        if full_phone_number is not None:
            self.full_phone_number = full_phone_number
        if short_phone_number is not None:
            self.short_phone_number = short_phone_number

    @property
    def area_code(self):
        """Gets the area_code of this PhoneNumber.  # noqa: E501

        区域码  # noqa: E501

        :return: The area_code of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this PhoneNumber.

        区域码  # noqa: E501

        :param area_code: The area_code of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def full_phone_number(self):
        """Gets the full_phone_number of this PhoneNumber.  # noqa: E501

        长手机号  # noqa: E501

        :return: The full_phone_number of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._full_phone_number

    @full_phone_number.setter
    def full_phone_number(self, full_phone_number):
        """Sets the full_phone_number of this PhoneNumber.

        长手机号  # noqa: E501

        :param full_phone_number: The full_phone_number of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._full_phone_number = full_phone_number

    @property
    def short_phone_number(self):
        """Gets the short_phone_number of this PhoneNumber.  # noqa: E501

        短手机号  # noqa: E501

        :return: The short_phone_number of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._short_phone_number

    @short_phone_number.setter
    def short_phone_number(self, short_phone_number):
        """Sets the short_phone_number of this PhoneNumber.

        短手机号  # noqa: E501

        :param short_phone_number: The short_phone_number of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._short_phone_number = short_phone_number

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
        if issubclass(PhoneNumber, dict):
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
        if not isinstance(other, PhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
