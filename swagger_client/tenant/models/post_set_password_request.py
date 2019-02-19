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


class PostSetPasswordRequest(object):
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
        'old_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'old_password': 'oldPassword',
        'new_password': 'newPassword'
    }

    def __init__(self, old_password=None, new_password=None):  # noqa: E501
        """PostSetPasswordRequest - a model defined in Swagger"""  # noqa: E501

        self._old_password = None
        self._new_password = None
        self.discriminator = None

        self.old_password = old_password
        self.new_password = new_password

    @property
    def old_password(self):
        """Gets the old_password of this PostSetPasswordRequest.  # noqa: E501

        旧密码  # noqa: E501

        :return: The old_password of this PostSetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this PostSetPasswordRequest.

        旧密码  # noqa: E501

        :param old_password: The old_password of this PostSetPasswordRequest.  # noqa: E501
        :type: str
        """
        if old_password is None:
            raise ValueError("Invalid value for `old_password`, must not be `None`")  # noqa: E501
        if old_password is not None and len(old_password) > 16:
            raise ValueError("Invalid value for `old_password`, length must be less than or equal to `16`")  # noqa: E501
        if old_password is not None and len(old_password) < 8:
            raise ValueError("Invalid value for `old_password`, length must be greater than or equal to `8`")  # noqa: E501

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this PostSetPasswordRequest.  # noqa: E501


        :return: The new_password of this PostSetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this PostSetPasswordRequest.


        :param new_password: The new_password of this PostSetPasswordRequest.  # noqa: E501
        :type: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501
        if new_password is not None and len(new_password) > 16:
            raise ValueError("Invalid value for `new_password`, length must be less than or equal to `16`")  # noqa: E501
        if new_password is not None and len(new_password) < 8:
            raise ValueError("Invalid value for `new_password`, length must be greater than or equal to `8`")  # noqa: E501

        self._new_password = new_password

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
        if issubclass(PostSetPasswordRequest, dict):
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
        if not isinstance(other, PostSetPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
