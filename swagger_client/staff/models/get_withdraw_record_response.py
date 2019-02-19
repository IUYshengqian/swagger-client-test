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

from swagger_client.staff.models.get_withdraw_record_query import GetWithdrawRecordQuery  # noqa: F401,E501
from swagger_client.staff.models.get_withdraw_record_response_items import GetWithdrawRecordResponseItems  # noqa: F401,E501
from swagger_client.staff.models.pagination import Pagination  # noqa: F401,E501


class GetWithdrawRecordResponse(object):
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
        'meta': 'Pagination',
        'query': 'GetWithdrawRecordQuery',
        'items': 'list[GetWithdrawRecordResponseItems]'
    }

    attribute_map = {
        'meta': 'meta',
        'query': 'query',
        'items': 'items'
    }

    def __init__(self, meta=None, query=None, items=None):  # noqa: E501
        """GetWithdrawRecordResponse - a model defined in Swagger"""  # noqa: E501

        self._meta = None
        self._query = None
        self._items = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if query is not None:
            self.query = query
        if items is not None:
            self.items = items

    @property
    def meta(self):
        """Gets the meta of this GetWithdrawRecordResponse.  # noqa: E501


        :return: The meta of this GetWithdrawRecordResponse.  # noqa: E501
        :rtype: Pagination
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this GetWithdrawRecordResponse.


        :param meta: The meta of this GetWithdrawRecordResponse.  # noqa: E501
        :type: Pagination
        """

        self._meta = meta

    @property
    def query(self):
        """Gets the query of this GetWithdrawRecordResponse.  # noqa: E501


        :return: The query of this GetWithdrawRecordResponse.  # noqa: E501
        :rtype: GetWithdrawRecordQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this GetWithdrawRecordResponse.


        :param query: The query of this GetWithdrawRecordResponse.  # noqa: E501
        :type: GetWithdrawRecordQuery
        """

        self._query = query

    @property
    def items(self):
        """Gets the items of this GetWithdrawRecordResponse.  # noqa: E501

        提币记录列表  # noqa: E501

        :return: The items of this GetWithdrawRecordResponse.  # noqa: E501
        :rtype: list[GetWithdrawRecordResponseItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GetWithdrawRecordResponse.

        提币记录列表  # noqa: E501

        :param items: The items of this GetWithdrawRecordResponse.  # noqa: E501
        :type: list[GetWithdrawRecordResponseItems]
        """

        self._items = items

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
        if issubclass(GetWithdrawRecordResponse, dict):
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
        if not isinstance(other, GetWithdrawRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
