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


class GetTenantAuditListResponseItems(object):
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
        'submitted_at': 'datetime',
        'uid': 'str',
        'certification_type': 'str',
        'exchange_name': 'str',
        'updated_at': 'datetime',
        'audit_user': 'str',
        'status': 'str',
        'failure_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'submitted_at': 'submittedAt',
        'uid': 'uid',
        'certification_type': 'certificationType',
        'exchange_name': 'exchangeName',
        'updated_at': 'updatedAt',
        'audit_user': 'auditUser',
        'status': 'status',
        'failure_type': 'failureType'
    }

    def __init__(self, id=None, submitted_at=None, uid=None, certification_type=None, exchange_name=None, updated_at=None, audit_user=None, status=None, failure_type=None):  # noqa: E501
        """GetTenantAuditListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._submitted_at = None
        self._uid = None
        self._certification_type = None
        self._exchange_name = None
        self._updated_at = None
        self._audit_user = None
        self._status = None
        self._failure_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if submitted_at is not None:
            self.submitted_at = submitted_at
        if uid is not None:
            self.uid = uid
        if certification_type is not None:
            self.certification_type = certification_type
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if updated_at is not None:
            self.updated_at = updated_at
        if audit_user is not None:
            self.audit_user = audit_user
        if status is not None:
            self.status = status
        if failure_type is not None:
            self.failure_type = failure_type

    @property
    def id(self):
        """Gets the id of this GetTenantAuditListResponseItems.  # noqa: E501

        id工单编号  # noqa: E501

        :return: The id of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetTenantAuditListResponseItems.

        id工单编号  # noqa: E501

        :param id: The id of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def submitted_at(self):
        """Gets the submitted_at of this GetTenantAuditListResponseItems.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The submitted_at of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this GetTenantAuditListResponseItems.

        提交申请时间  # noqa: E501

        :param submitted_at: The submitted_at of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def uid(self):
        """Gets the uid of this GetTenantAuditListResponseItems.  # noqa: E501

        uid  # noqa: E501

        :return: The uid of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetTenantAuditListResponseItems.

        uid  # noqa: E501

        :param uid: The uid of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def certification_type(self):
        """Gets the certification_type of this GetTenantAuditListResponseItems.  # noqa: E501

        认证类型[\"individual（个人）、company（企业）\"]  # noqa: E501

        :return: The certification_type of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._certification_type

    @certification_type.setter
    def certification_type(self, certification_type):
        """Sets the certification_type of this GetTenantAuditListResponseItems.

        认证类型[\"individual（个人）、company（企业）\"]  # noqa: E501

        :param certification_type: The certification_type of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["individual", "company"]  # noqa: E501
        if certification_type not in allowed_values:
            raise ValueError(
                "Invalid value for `certification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(certification_type, allowed_values)
            )

        self._certification_type = certification_type

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetTenantAuditListResponseItems.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The exchange_name of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetTenantAuditListResponseItems.

        交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def updated_at(self):
        """Gets the updated_at of this GetTenantAuditListResponseItems.  # noqa: E501

        更新时间  # noqa: E501

        :return: The updated_at of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GetTenantAuditListResponseItems.

        更新时间  # noqa: E501

        :param updated_at: The updated_at of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def audit_user(self):
        """Gets the audit_user of this GetTenantAuditListResponseItems.  # noqa: E501

        审核用户  # noqa: E501

        :return: The audit_user of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._audit_user

    @audit_user.setter
    def audit_user(self, audit_user):
        """Sets the audit_user of this GetTenantAuditListResponseItems.

        审核用户  # noqa: E501

        :param audit_user: The audit_user of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._audit_user = audit_user

    @property
    def status(self):
        """Gets the status of this GetTenantAuditListResponseItems.  # noqa: E501

        类型audit(初审)、re_audit(复审)、audit_return(初审驳回)、re_audit_return(复审驳回)、approved(通过)  # noqa: E501

        :return: The status of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetTenantAuditListResponseItems.

        类型audit(初审)、re_audit(复审)、audit_return(初审驳回)、re_audit_return(复审驳回)、approved(通过)  # noqa: E501

        :param status: The status of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["audit", "re_audit", "audit_return", "re_audit_return", "approved"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def failure_type(self):
        """Gets the failure_type of this GetTenantAuditListResponseItems.  # noqa: E501

        审核失败类型  # noqa: E501

        :return: The failure_type of this GetTenantAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type):
        """Sets the failure_type of this GetTenantAuditListResponseItems.

        审核失败类型  # noqa: E501

        :param failure_type: The failure_type of this GetTenantAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._failure_type = failure_type

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
        if issubclass(GetTenantAuditListResponseItems, dict):
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
        if not isinstance(other, GetTenantAuditListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other