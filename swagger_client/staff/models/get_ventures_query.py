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


class GetVenturesQuery(object):
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
        'created_start_at': 'str',
        'created_end_at': 'str',
        'venture_id': 'str',
        'email': 'str'
    }

    attribute_map = {
        'created_start_at': 'createdStartAt',
        'created_end_at': 'createdEndAt',
        'venture_id': 'ventureId',
        'email': 'email'
    }

    def __init__(self, created_start_at=None, created_end_at=None, venture_id=None, email=None):  # noqa: E501
        """GetVenturesQuery - a model defined in Swagger"""  # noqa: E501

        self._created_start_at = None
        self._created_end_at = None
        self._venture_id = None
        self._email = None
        self.discriminator = None

        if created_start_at is not None:
            self.created_start_at = created_start_at
        if created_end_at is not None:
            self.created_end_at = created_end_at
        if venture_id is not None:
            self.venture_id = venture_id
        if email is not None:
            self.email = email

    @property
    def created_start_at(self):
        """Gets the created_start_at of this GetVenturesQuery.  # noqa: E501

        开始创建时间  # noqa: E501

        :return: The created_start_at of this GetVenturesQuery.  # noqa: E501
        :rtype: str
        """
        return self._created_start_at

    @created_start_at.setter
    def created_start_at(self, created_start_at):
        """Sets the created_start_at of this GetVenturesQuery.

        开始创建时间  # noqa: E501

        :param created_start_at: The created_start_at of this GetVenturesQuery.  # noqa: E501
        :type: str
        """

        self._created_start_at = created_start_at

    @property
    def created_end_at(self):
        """Gets the created_end_at of this GetVenturesQuery.  # noqa: E501

        结束创建时间  # noqa: E501

        :return: The created_end_at of this GetVenturesQuery.  # noqa: E501
        :rtype: str
        """
        return self._created_end_at

    @created_end_at.setter
    def created_end_at(self, created_end_at):
        """Sets the created_end_at of this GetVenturesQuery.

        结束创建时间  # noqa: E501

        :param created_end_at: The created_end_at of this GetVenturesQuery.  # noqa: E501
        :type: str
        """

        self._created_end_at = created_end_at

    @property
    def venture_id(self):
        """Gets the venture_id of this GetVenturesQuery.  # noqa: E501

        项目方id  # noqa: E501

        :return: The venture_id of this GetVenturesQuery.  # noqa: E501
        :rtype: str
        """
        return self._venture_id

    @venture_id.setter
    def venture_id(self, venture_id):
        """Sets the venture_id of this GetVenturesQuery.

        项目方id  # noqa: E501

        :param venture_id: The venture_id of this GetVenturesQuery.  # noqa: E501
        :type: str
        """

        self._venture_id = venture_id

    @property
    def email(self):
        """Gets the email of this GetVenturesQuery.  # noqa: E501

        邮箱地址  # noqa: E501

        :return: The email of this GetVenturesQuery.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetVenturesQuery.

        邮箱地址  # noqa: E501

        :param email: The email of this GetVenturesQuery.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(GetVenturesQuery, dict):
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
        if not isinstance(other, GetVenturesQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
