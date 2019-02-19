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

from swagger_client.staff.models.get_exchange_tags_response_other_language import GetExchangeTagsResponseOtherLanguage  # noqa: F401,E501


class GetExchangeTagsResponse(object):
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
        'name': 'str',
        'other_language': 'list[GetExchangeTagsResponseOtherLanguage]'
    }

    attribute_map = {
        'name': 'name',
        'other_language': 'otherLanguage'
    }

    def __init__(self, name=None, other_language=None):  # noqa: E501
        """GetExchangeTagsResponse - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._other_language = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if other_language is not None:
            self.other_language = other_language

    @property
    def name(self):
        """Gets the name of this GetExchangeTagsResponse.  # noqa: E501

        标签名称(中文)  # noqa: E501

        :return: The name of this GetExchangeTagsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetExchangeTagsResponse.

        标签名称(中文)  # noqa: E501

        :param name: The name of this GetExchangeTagsResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def other_language(self):
        """Gets the other_language of this GetExchangeTagsResponse.  # noqa: E501

        其他语言种类  # noqa: E501

        :return: The other_language of this GetExchangeTagsResponse.  # noqa: E501
        :rtype: list[GetExchangeTagsResponseOtherLanguage]
        """
        return self._other_language

    @other_language.setter
    def other_language(self, other_language):
        """Sets the other_language of this GetExchangeTagsResponse.

        其他语言种类  # noqa: E501

        :param other_language: The other_language of this GetExchangeTagsResponse.  # noqa: E501
        :type: list[GetExchangeTagsResponseOtherLanguage]
        """

        self._other_language = other_language

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
        if issubclass(GetExchangeTagsResponse, dict):
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
        if not isinstance(other, GetExchangeTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other