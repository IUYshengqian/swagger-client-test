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


class GetBannerListResponseItems(object):
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
        'banner': 'str',
        'title': 'str',
        'created_at': 'str',
        'status': 'bool',
        'internal': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'banner': 'banner',
        'title': 'title',
        'created_at': 'createdAt',
        'status': 'status',
        'internal': 'internal'
    }

    def __init__(self, id=None, banner=None, title=None, created_at=None, status=None, internal=None):  # noqa: E501
        """GetBannerListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._banner = None
        self._title = None
        self._created_at = None
        self._status = None
        self._internal = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if banner is not None:
            self.banner = banner
        if title is not None:
            self.title = title
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if internal is not None:
            self.internal = internal

    @property
    def id(self):
        """Gets the id of this GetBannerListResponseItems.  # noqa: E501

        id  # noqa: E501

        :return: The id of this GetBannerListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetBannerListResponseItems.

        id  # noqa: E501

        :param id: The id of this GetBannerListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def banner(self):
        """Gets the banner of this GetBannerListResponseItems.  # noqa: E501

        轮播图  # noqa: E501

        :return: The banner of this GetBannerListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """Sets the banner of this GetBannerListResponseItems.

        轮播图  # noqa: E501

        :param banner: The banner of this GetBannerListResponseItems.  # noqa: E501
        :type: str
        """

        self._banner = banner

    @property
    def title(self):
        """Gets the title of this GetBannerListResponseItems.  # noqa: E501

        标题  # noqa: E501

        :return: The title of this GetBannerListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetBannerListResponseItems.

        标题  # noqa: E501

        :param title: The title of this GetBannerListResponseItems.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def created_at(self):
        """Gets the created_at of this GetBannerListResponseItems.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this GetBannerListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetBannerListResponseItems.

        创建时间  # noqa: E501

        :param created_at: The created_at of this GetBannerListResponseItems.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this GetBannerListResponseItems.  # noqa: E501

        状态  # noqa: E501

        :return: The status of this GetBannerListResponseItems.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetBannerListResponseItems.

        状态  # noqa: E501

        :param status: The status of this GetBannerListResponseItems.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def internal(self):
        """Gets the internal of this GetBannerListResponseItems.  # noqa: E501

        是否为内置  # noqa: E501

        :return: The internal of this GetBannerListResponseItems.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this GetBannerListResponseItems.

        是否为内置  # noqa: E501

        :param internal: The internal of this GetBannerListResponseItems.  # noqa: E501
        :type: bool
        """

        self._internal = internal

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
        if issubclass(GetBannerListResponseItems, dict):
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
        if not isinstance(other, GetBannerListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
