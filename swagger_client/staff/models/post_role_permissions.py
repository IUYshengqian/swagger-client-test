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


class PostRolePermissions(object):
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
        'role_id': 'str',
        'description': 'str',
        'ids': 'list[str]'
    }

    attribute_map = {
        'role_id': 'roleId',
        'description': 'description',
        'ids': 'ids'
    }

    def __init__(self, role_id=None, description=None, ids=None):  # noqa: E501
        """PostRolePermissions - a model defined in Swagger"""  # noqa: E501

        self._role_id = None
        self._description = None
        self._ids = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if description is not None:
            self.description = description
        if ids is not None:
            self.ids = ids

    @property
    def role_id(self):
        """Gets the role_id of this PostRolePermissions.  # noqa: E501

        角色id  # noqa: E501

        :return: The role_id of this PostRolePermissions.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this PostRolePermissions.

        角色id  # noqa: E501

        :param role_id: The role_id of this PostRolePermissions.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def description(self):
        """Gets the description of this PostRolePermissions.  # noqa: E501

        描述  # noqa: E501

        :return: The description of this PostRolePermissions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostRolePermissions.

        描述  # noqa: E501

        :param description: The description of this PostRolePermissions.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501

        self._description = description

    @property
    def ids(self):
        """Gets the ids of this PostRolePermissions.  # noqa: E501

        权限Id数组  # noqa: E501

        :return: The ids of this PostRolePermissions.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this PostRolePermissions.

        权限Id数组  # noqa: E501

        :param ids: The ids of this PostRolePermissions.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

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
        if issubclass(PostRolePermissions, dict):
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
        if not isinstance(other, PostRolePermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
