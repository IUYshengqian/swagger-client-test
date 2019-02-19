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


class GetNoticesResponseItems(object):
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
        'title': 'str',
        'status': 'bool',
        'created_at': 'datetime',
        'language': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'status': 'status',
        'created_at': 'createdAt',
        'language': 'language'
    }

    def __init__(self, id=None, title=None, status=None, created_at=None, language=None):  # noqa: E501
        """GetNoticesResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._status = None
        self._created_at = None
        self._language = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if language is not None:
            self.language = language

    @property
    def id(self):
        """Gets the id of this GetNoticesResponseItems.  # noqa: E501

        公告ID  # noqa: E501

        :return: The id of this GetNoticesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNoticesResponseItems.

        公告ID  # noqa: E501

        :param id: The id of this GetNoticesResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this GetNoticesResponseItems.  # noqa: E501

        标题  # noqa: E501

        :return: The title of this GetNoticesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetNoticesResponseItems.

        标题  # noqa: E501

        :param title: The title of this GetNoticesResponseItems.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this GetNoticesResponseItems.  # noqa: E501

        状态 1发布  0禁用  # noqa: E501

        :return: The status of this GetNoticesResponseItems.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetNoticesResponseItems.

        状态 1发布  0禁用  # noqa: E501

        :param status: The status of this GetNoticesResponseItems.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this GetNoticesResponseItems.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this GetNoticesResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetNoticesResponseItems.

        创建时间  # noqa: E501

        :param created_at: The created_at of this GetNoticesResponseItems.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def language(self):
        """Gets the language of this GetNoticesResponseItems.  # noqa: E501

        语种：中文zh_cn 英文en_us 马来文ms_my 韩文ko_kr 柬埔寨文km_kh  # noqa: E501

        :return: The language of this GetNoticesResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GetNoticesResponseItems.

        语种：中文zh_cn 英文en_us 马来文ms_my 韩文ko_kr 柬埔寨文km_kh  # noqa: E501

        :param language: The language of this GetNoticesResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["zh_cn", "en_us", "ms_my", "ko_kr", "km_kh"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

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
        if issubclass(GetNoticesResponseItems, dict):
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
        if not isinstance(other, GetNoticesResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
