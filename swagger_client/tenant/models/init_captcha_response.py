# coding: utf-8

"""
    crush-tenant 平台接口(租户平台)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InitCaptchaResponse(object):
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
        'success': 'str',
        'challenge': 'str',
        'gt': 'str',
        'new_captcha': 'str'
    }

    attribute_map = {
        'success': 'success',
        'challenge': 'challenge',
        'gt': 'gt',
        'new_captcha': 'newCaptcha'
    }

    def __init__(self, success=None, challenge=None, gt=None, new_captcha=None):  # noqa: E501
        """InitCaptchaResponse - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._challenge = None
        self._gt = None
        self._new_captcha = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if challenge is not None:
            self.challenge = challenge
        if gt is not None:
            self.gt = gt
        if new_captcha is not None:
            self.new_captcha = new_captcha

    @property
    def success(self):
        """Gets the success of this InitCaptchaResponse.  # noqa: E501

        是否成功，成功返回1  # noqa: E501

        :return: The success of this InitCaptchaResponse.  # noqa: E501
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InitCaptchaResponse.

        是否成功，成功返回1  # noqa: E501

        :param success: The success of this InitCaptchaResponse.  # noqa: E501
        :type: str
        """

        self._success = success

    @property
    def challenge(self):
        """Gets the challenge of this InitCaptchaResponse.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The challenge of this InitCaptchaResponse.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this InitCaptchaResponse.

        极验服务端需要用到的参数  # noqa: E501

        :param challenge: The challenge of this InitCaptchaResponse.  # noqa: E501
        :type: str
        """

        self._challenge = challenge

    @property
    def gt(self):
        """Gets the gt of this InitCaptchaResponse.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The gt of this InitCaptchaResponse.  # noqa: E501
        :rtype: str
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this InitCaptchaResponse.

        极验服务端需要用到的参数  # noqa: E501

        :param gt: The gt of this InitCaptchaResponse.  # noqa: E501
        :type: str
        """

        self._gt = gt

    @property
    def new_captcha(self):
        """Gets the new_captcha of this InitCaptchaResponse.  # noqa: E501

        极验服务端需要用到的参数  # noqa: E501

        :return: The new_captcha of this InitCaptchaResponse.  # noqa: E501
        :rtype: str
        """
        return self._new_captcha

    @new_captcha.setter
    def new_captcha(self, new_captcha):
        """Sets the new_captcha of this InitCaptchaResponse.

        极验服务端需要用到的参数  # noqa: E501

        :param new_captcha: The new_captcha of this InitCaptchaResponse.  # noqa: E501
        :type: str
        """

        self._new_captcha = new_captcha

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
        if issubclass(InitCaptchaResponse, dict):
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
        if not isinstance(other, InitCaptchaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
