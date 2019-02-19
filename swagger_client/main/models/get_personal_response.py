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


class GetPersonalResponse(object):
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
        'nationality_code': 'str',
        'name': 'str',
        'type': 'str',
        'number': 'str'
    }

    attribute_map = {
        'nationality_code': 'nationalityCode',
        'name': 'name',
        'type': 'type',
        'number': 'number'
    }

    def __init__(self, nationality_code=None, name=None, type=None, number=None):  # noqa: E501
        """GetPersonalResponse - a model defined in Swagger"""  # noqa: E501

        self._nationality_code = None
        self._name = None
        self._type = None
        self._number = None
        self.discriminator = None

        if nationality_code is not None:
            self.nationality_code = nationality_code
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if number is not None:
            self.number = number

    @property
    def nationality_code(self):
        """Gets the nationality_code of this GetPersonalResponse.  # noqa: E501

        国籍（证件所在区域）  # noqa: E501

        :return: The nationality_code of this GetPersonalResponse.  # noqa: E501
        :rtype: str
        """
        return self._nationality_code

    @nationality_code.setter
    def nationality_code(self, nationality_code):
        """Sets the nationality_code of this GetPersonalResponse.

        国籍（证件所在区域）  # noqa: E501

        :param nationality_code: The nationality_code of this GetPersonalResponse.  # noqa: E501
        :type: str
        """

        self._nationality_code = nationality_code

    @property
    def name(self):
        """Gets the name of this GetPersonalResponse.  # noqa: E501

        姓名  # noqa: E501

        :return: The name of this GetPersonalResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetPersonalResponse.

        姓名  # noqa: E501

        :param name: The name of this GetPersonalResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GetPersonalResponse.  # noqa: E501

        证件类型  # noqa: E501

        :return: The type of this GetPersonalResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetPersonalResponse.

        证件类型  # noqa: E501

        :param type: The type of this GetPersonalResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def number(self):
        """Gets the number of this GetPersonalResponse.  # noqa: E501

        证件号码  # noqa: E501

        :return: The number of this GetPersonalResponse.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GetPersonalResponse.

        证件号码  # noqa: E501

        :param number: The number of this GetPersonalResponse.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(GetPersonalResponse, dict):
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
        if not isinstance(other, GetPersonalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
