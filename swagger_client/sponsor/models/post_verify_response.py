# coding: utf-8

"""
    crush-sponsor 平台接口（保荐方平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PostVerifyResponse(object):
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
        'base_token': 'str'
    }

    attribute_map = {
        'base_token': 'baseToken'
    }

    def __init__(self, base_token=None):  # noqa: E501
        """PostVerifyResponse - a model defined in Swagger"""  # noqa: E501

        self._base_token = None
        self.discriminator = None

        if base_token is not None:
            self.base_token = base_token

    @property
    def base_token(self):
        """Gets the base_token of this PostVerifyResponse.  # noqa: E501

        临时token  # noqa: E501

        :return: The base_token of this PostVerifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_token

    @base_token.setter
    def base_token(self, base_token):
        """Sets the base_token of this PostVerifyResponse.

        临时token  # noqa: E501

        :param base_token: The base_token of this PostVerifyResponse.  # noqa: E501
        :type: str
        """

        self._base_token = base_token

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
        if issubclass(PostVerifyResponse, dict):
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
        if not isinstance(other, PostVerifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
