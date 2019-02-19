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


class GetSystemConfigResponseInner(object):
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
        'id': 'str',
        'config_key': 'str',
        'config_value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'config_key': 'configKey',
        'config_value': 'configValue',
        'description': 'description'
    }

    def __init__(self, id=None, config_key=None, config_value=None, description=None):  # noqa: E501
        """GetSystemConfigResponseInner - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._config_key = None
        self._config_value = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if config_key is not None:
            self.config_key = config_key
        if config_value is not None:
            self.config_value = config_value
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this GetSystemConfigResponseInner.  # noqa: E501

        id  # noqa: E501

        :return: The id of this GetSystemConfigResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSystemConfigResponseInner.

        id  # noqa: E501

        :param id: The id of this GetSystemConfigResponseInner.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def config_key(self):
        """Gets the config_key of this GetSystemConfigResponseInner.  # noqa: E501

        配置键  # noqa: E501

        :return: The config_key of this GetSystemConfigResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        """Sets the config_key of this GetSystemConfigResponseInner.

        配置键  # noqa: E501

        :param config_key: The config_key of this GetSystemConfigResponseInner.  # noqa: E501
        :type: str
        """

        self._config_key = config_key

    @property
    def config_value(self):
        """Gets the config_value of this GetSystemConfigResponseInner.  # noqa: E501

        配置值  # noqa: E501

        :return: The config_value of this GetSystemConfigResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this GetSystemConfigResponseInner.

        配置值  # noqa: E501

        :param config_value: The config_value of this GetSystemConfigResponseInner.  # noqa: E501
        :type: str
        """

        self._config_value = config_value

    @property
    def description(self):
        """Gets the description of this GetSystemConfigResponseInner.  # noqa: E501

        描述  # noqa: E501

        :return: The description of this GetSystemConfigResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetSystemConfigResponseInner.

        描述  # noqa: E501

        :param description: The description of this GetSystemConfigResponseInner.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(GetSystemConfigResponseInner, dict):
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
        if not isinstance(other, GetSystemConfigResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
