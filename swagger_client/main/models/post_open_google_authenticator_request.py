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


class PostOpenGoogleAuthenticatorRequest(object):
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
        'google_code': 'str'
    }

    attribute_map = {
        'google_code': 'googleCode'
    }

    def __init__(self, google_code=None):  # noqa: E501
        """PostOpenGoogleAuthenticatorRequest - a model defined in Swagger"""  # noqa: E501

        self._google_code = None
        self.discriminator = None

        self.google_code = google_code

    @property
    def google_code(self):
        """Gets the google_code of this PostOpenGoogleAuthenticatorRequest.  # noqa: E501

        谷歌验证码  # noqa: E501

        :return: The google_code of this PostOpenGoogleAuthenticatorRequest.  # noqa: E501
        :rtype: str
        """
        return self._google_code

    @google_code.setter
    def google_code(self, google_code):
        """Sets the google_code of this PostOpenGoogleAuthenticatorRequest.

        谷歌验证码  # noqa: E501

        :param google_code: The google_code of this PostOpenGoogleAuthenticatorRequest.  # noqa: E501
        :type: str
        """
        if google_code is None:
            raise ValueError("Invalid value for `google_code`, must not be `None`")  # noqa: E501
        if google_code is not None and len(google_code) > 6:
            raise ValueError("Invalid value for `google_code`, length must be less than or equal to `6`")  # noqa: E501
        if google_code is not None and len(google_code) < 6:
            raise ValueError("Invalid value for `google_code`, length must be greater than or equal to `6`")  # noqa: E501

        self._google_code = google_code

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
        if issubclass(PostOpenGoogleAuthenticatorRequest, dict):
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
        if not isinstance(other, PostOpenGoogleAuthenticatorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
