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


class GetInviterListResponseItems(object):
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
        'invite_at': 'str',
        'account_id': 'str',
        'invite_rebate': 'str'
    }

    attribute_map = {
        'id': 'id',
        'invite_at': 'inviteAt',
        'account_id': 'accountId',
        'invite_rebate': 'inviteRebate'
    }

    def __init__(self, id=None, invite_at=None, account_id=None, invite_rebate=None):  # noqa: E501
        """GetInviterListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._invite_at = None
        self._account_id = None
        self._invite_rebate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if invite_at is not None:
            self.invite_at = invite_at
        if account_id is not None:
            self.account_id = account_id
        if invite_rebate is not None:
            self.invite_rebate = invite_rebate

    @property
    def id(self):
        """Gets the id of this GetInviterListResponseItems.  # noqa: E501

        邀请记录ID  # noqa: E501

        :return: The id of this GetInviterListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetInviterListResponseItems.

        邀请记录ID  # noqa: E501

        :param id: The id of this GetInviterListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invite_at(self):
        """Gets the invite_at of this GetInviterListResponseItems.  # noqa: E501

        邀请时间  # noqa: E501

        :return: The invite_at of this GetInviterListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._invite_at

    @invite_at.setter
    def invite_at(self, invite_at):
        """Sets the invite_at of this GetInviterListResponseItems.

        邀请时间  # noqa: E501

        :param invite_at: The invite_at of this GetInviterListResponseItems.  # noqa: E501
        :type: str
        """

        self._invite_at = invite_at

    @property
    def account_id(self):
        """Gets the account_id of this GetInviterListResponseItems.  # noqa: E501

        用户ID  # noqa: E501

        :return: The account_id of this GetInviterListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetInviterListResponseItems.

        用户ID  # noqa: E501

        :param account_id: The account_id of this GetInviterListResponseItems.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def invite_rebate(self):
        """Gets the invite_rebate of this GetInviterListResponseItems.  # noqa: E501

        邀请返佣估值  # noqa: E501

        :return: The invite_rebate of this GetInviterListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._invite_rebate

    @invite_rebate.setter
    def invite_rebate(self, invite_rebate):
        """Sets the invite_rebate of this GetInviterListResponseItems.

        邀请返佣估值  # noqa: E501

        :param invite_rebate: The invite_rebate of this GetInviterListResponseItems.  # noqa: E501
        :type: str
        """

        self._invite_rebate = invite_rebate

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
        if issubclass(GetInviterListResponseItems, dict):
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
        if not isinstance(other, GetInviterListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
