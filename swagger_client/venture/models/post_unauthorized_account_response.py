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


class PostUnauthorizedAccountResponse(object):
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
        'auth_message': 'str',
        'base_token': 'str',
        'type': 'str',
        'otc_id': 'str',
        'validation_restrict': 'str'
    }

    attribute_map = {
        'auth_message': 'authMessage',
        'base_token': 'baseToken',
        'type': 'type',
        'otc_id': 'otcId',
        'validation_restrict': 'validationRestrict'
    }

    def __init__(self, auth_message=None, base_token=None, type=None, otc_id=None, validation_restrict=None):  # noqa: E501
        """PostUnauthorizedAccountResponse - a model defined in Swagger"""  # noqa: E501

        self._auth_message = None
        self._base_token = None
        self._type = None
        self._otc_id = None
        self._validation_restrict = None
        self.discriminator = None

        if auth_message is not None:
            self.auth_message = auth_message
        if base_token is not None:
            self.base_token = base_token
        if type is not None:
            self.type = type
        if otc_id is not None:
            self.otc_id = otc_id
        if validation_restrict is not None:
            self.validation_restrict = validation_restrict

    @property
    def auth_message(self):
        """Gets the auth_message of this PostUnauthorizedAccountResponse.  # noqa: E501

        当前用户绑定的验证方式  # noqa: E501

        :return: The auth_message of this PostUnauthorizedAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth_message

    @auth_message.setter
    def auth_message(self, auth_message):
        """Sets the auth_message of this PostUnauthorizedAccountResponse.

        当前用户绑定的验证方式  # noqa: E501

        :param auth_message: The auth_message of this PostUnauthorizedAccountResponse.  # noqa: E501
        :type: str
        """

        self._auth_message = auth_message

    @property
    def base_token(self):
        """Gets the base_token of this PostUnauthorizedAccountResponse.  # noqa: E501

        账户ID  # noqa: E501

        :return: The base_token of this PostUnauthorizedAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_token

    @base_token.setter
    def base_token(self, base_token):
        """Sets the base_token of this PostUnauthorizedAccountResponse.

        账户ID  # noqa: E501

        :param base_token: The base_token of this PostUnauthorizedAccountResponse.  # noqa: E501
        :type: str
        """

        self._base_token = base_token

    @property
    def type(self):
        """Gets the type of this PostUnauthorizedAccountResponse.  # noqa: E501

        验证类型login  # noqa: E501

        :return: The type of this PostUnauthorizedAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostUnauthorizedAccountResponse.

        验证类型login  # noqa: E501

        :param type: The type of this PostUnauthorizedAccountResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def otc_id(self):
        """Gets the otc_id of this PostUnauthorizedAccountResponse.  # noqa: E501

        法币的id  # noqa: E501

        :return: The otc_id of this PostUnauthorizedAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._otc_id

    @otc_id.setter
    def otc_id(self, otc_id):
        """Sets the otc_id of this PostUnauthorizedAccountResponse.

        法币的id  # noqa: E501

        :param otc_id: The otc_id of this PostUnauthorizedAccountResponse.  # noqa: E501
        :type: str
        """

        self._otc_id = otc_id

    @property
    def validation_restrict(self):
        """Gets the validation_restrict of this PostUnauthorizedAccountResponse.  # noqa: E501

        当前开启的验证方式  # noqa: E501

        :return: The validation_restrict of this PostUnauthorizedAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._validation_restrict

    @validation_restrict.setter
    def validation_restrict(self, validation_restrict):
        """Sets the validation_restrict of this PostUnauthorizedAccountResponse.

        当前开启的验证方式  # noqa: E501

        :param validation_restrict: The validation_restrict of this PostUnauthorizedAccountResponse.  # noqa: E501
        :type: str
        """

        self._validation_restrict = validation_restrict

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
        if issubclass(PostUnauthorizedAccountResponse, dict):
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
        if not isinstance(other, PostUnauthorizedAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
