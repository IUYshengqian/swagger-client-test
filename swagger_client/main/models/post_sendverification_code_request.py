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


class PostSendverificationCodeRequest(object):
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
        'uri': 'str',
        'type': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type'
    }

    def __init__(self, uri=None, type=None):  # noqa: E501
        """PostSendverificationCodeRequest - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._type = None
        self.discriminator = None

        self.uri = uri
        self.type = type

    @property
    def uri(self):
        """Gets the uri of this PostSendverificationCodeRequest.  # noqa: E501

        电话或者邮箱, 例如：mailto:hello.world@email.com, number:18645511111, ...  # noqa: E501

        :return: The uri of this PostSendverificationCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this PostSendverificationCodeRequest.

        电话或者邮箱, 例如：mailto:hello.world@email.com, number:18645511111, ...  # noqa: E501

        :param uri: The uri of this PostSendverificationCodeRequest.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def type(self):
        """Gets the type of this PostSendverificationCodeRequest.  # noqa: E501

        LOGIN(\"login\"),REGISTER(\"register\"), FORGET_PWD(\"forget_pwd\"), EDIT_LOGIN_PWD(\"edit_login_pwd\"),EDIT_ASSET_PWD(\"edit_asset_pwd\"), BIND_EMAIL(\"bind_email\"),CLOSE_EMAIL(\"close_email\"),BIND_PHONE(\"bind_phone\"),ALTER_PHONE(\"alter_phone\"),CLOSE_PHONE(\"close_phone\"),ALTER_GOOGLE(\"alter_google\"),OPEN_PHONE(\"open_phone\"), WITHDRAW(\"withdraw\"),BIND_GOOGLE(\"bind_google\"), CLOSE_GOOGLE(\"close_google\"), CLOSE_MARKET(\"close_market\"), OPEN_GOOGLE(\"open_google\"),PAY(\"pay\")  # noqa: E501

        :return: The type of this PostSendverificationCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostSendverificationCodeRequest.

        LOGIN(\"login\"),REGISTER(\"register\"), FORGET_PWD(\"forget_pwd\"), EDIT_LOGIN_PWD(\"edit_login_pwd\"),EDIT_ASSET_PWD(\"edit_asset_pwd\"), BIND_EMAIL(\"bind_email\"),CLOSE_EMAIL(\"close_email\"),BIND_PHONE(\"bind_phone\"),ALTER_PHONE(\"alter_phone\"),CLOSE_PHONE(\"close_phone\"),ALTER_GOOGLE(\"alter_google\"),OPEN_PHONE(\"open_phone\"), WITHDRAW(\"withdraw\"),BIND_GOOGLE(\"bind_google\"), CLOSE_GOOGLE(\"close_google\"), CLOSE_MARKET(\"close_market\"), OPEN_GOOGLE(\"open_google\"),PAY(\"pay\")  # noqa: E501

        :param type: The type of this PostSendverificationCodeRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["login", "register", "forget_pwd", "edit_login_pwd", "edit_asset_pwd", "bind_phone", "alter_phone", "close_phone", "open_phone", "alter_google", "withdraw", "bind_google", "close_google", "open_google", "pay", "close_market"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(PostSendverificationCodeRequest, dict):
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
        if not isinstance(other, PostSendverificationCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
