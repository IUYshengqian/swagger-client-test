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


class GetAnnouncementsByAllExchangeResponseItems(object):
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
        'created_at': 'str',
        'exchange_id': 'str',
        'title': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'exchange_id': 'exchangeId',
        'title': 'title',
        'status': 'status'
    }

    def __init__(self, id=None, created_at=None, exchange_id=None, title=None, status=None):  # noqa: E501
        """GetAnnouncementsByAllExchangeResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._exchange_id = None
        self._title = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501

        id  # noqa: E501

        :return: The id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAnnouncementsByAllExchangeResponseItems.

        id  # noqa: E501

        :param id: The id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501

        创建时间  # noqa: E501

        :return: The created_at of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetAnnouncementsByAllExchangeResponseItems.

        创建时间  # noqa: E501

        :param created_at: The created_at of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def exchange_id(self):
        """Gets the exchange_id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501

        交易所ID  # noqa: E501

        :return: The exchange_id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this GetAnnouncementsByAllExchangeResponseItems.

        交易所ID  # noqa: E501

        :param exchange_id: The exchange_id of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def title(self):
        """Gets the title of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501

        标题  # noqa: E501

        :return: The title of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetAnnouncementsByAllExchangeResponseItems.

        标题  # noqa: E501

        :param title: The title of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501

        状态  # noqa: E501

        :return: The status of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetAnnouncementsByAllExchangeResponseItems.

        状态  # noqa: E501

        :param status: The status of this GetAnnouncementsByAllExchangeResponseItems.  # noqa: E501
        :type: bool
        """

        self._status = status

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
        if issubclass(GetAnnouncementsByAllExchangeResponseItems, dict):
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
        if not isinstance(other, GetAnnouncementsByAllExchangeResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
