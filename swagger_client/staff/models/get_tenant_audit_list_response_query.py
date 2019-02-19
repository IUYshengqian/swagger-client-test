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


class GetTenantAuditListResponseQuery(object):
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
        'submitted_start_at': 'str',
        'submitted_end_at': 'str',
        'ticket_number': 'str',
        'uid': 'str',
        'exchange_name': 'str',
        'status': 'str',
        'failure_type': 'str'
    }

    attribute_map = {
        'submitted_start_at': 'submittedStartAt',
        'submitted_end_at': 'submittedEndAt',
        'ticket_number': 'ticketNumber',
        'uid': 'uid',
        'exchange_name': 'exchangeName',
        'status': 'status',
        'failure_type': 'failureType'
    }

    def __init__(self, submitted_start_at=None, submitted_end_at=None, ticket_number=None, uid=None, exchange_name=None, status=None, failure_type=None):  # noqa: E501
        """GetTenantAuditListResponseQuery - a model defined in Swagger"""  # noqa: E501

        self._submitted_start_at = None
        self._submitted_end_at = None
        self._ticket_number = None
        self._uid = None
        self._exchange_name = None
        self._status = None
        self._failure_type = None
        self.discriminator = None

        if submitted_start_at is not None:
            self.submitted_start_at = submitted_start_at
        if submitted_end_at is not None:
            self.submitted_end_at = submitted_end_at
        if ticket_number is not None:
            self.ticket_number = ticket_number
        if uid is not None:
            self.uid = uid
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if status is not None:
            self.status = status
        if failure_type is not None:
            self.failure_type = failure_type

    @property
    def submitted_start_at(self):
        """Gets the submitted_start_at of this GetTenantAuditListResponseQuery.  # noqa: E501

        提交申请开始时间  # noqa: E501

        :return: The submitted_start_at of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._submitted_start_at

    @submitted_start_at.setter
    def submitted_start_at(self, submitted_start_at):
        """Sets the submitted_start_at of this GetTenantAuditListResponseQuery.

        提交申请开始时间  # noqa: E501

        :param submitted_start_at: The submitted_start_at of this GetTenantAuditListResponseQuery.  # noqa: E501
        :type: str
        """

        self._submitted_start_at = submitted_start_at

    @property
    def submitted_end_at(self):
        """Gets the submitted_end_at of this GetTenantAuditListResponseQuery.  # noqa: E501

        提交申请结束时间  # noqa: E501

        :return: The submitted_end_at of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._submitted_end_at

    @submitted_end_at.setter
    def submitted_end_at(self, submitted_end_at):
        """Sets the submitted_end_at of this GetTenantAuditListResponseQuery.

        提交申请结束时间  # noqa: E501

        :param submitted_end_at: The submitted_end_at of this GetTenantAuditListResponseQuery.  # noqa: E501
        :type: str
        """

        self._submitted_end_at = submitted_end_at

    @property
    def ticket_number(self):
        """Gets the ticket_number of this GetTenantAuditListResponseQuery.  # noqa: E501

        工单编号  # noqa: E501

        :return: The ticket_number of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """Sets the ticket_number of this GetTenantAuditListResponseQuery.

        工单编号  # noqa: E501

        :param ticket_number: The ticket_number of this GetTenantAuditListResponseQuery.  # noqa: E501
        :type: str
        """

        self._ticket_number = ticket_number

    @property
    def uid(self):
        """Gets the uid of this GetTenantAuditListResponseQuery.  # noqa: E501

        请求的uid  # noqa: E501

        :return: The uid of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetTenantAuditListResponseQuery.

        请求的uid  # noqa: E501

        :param uid: The uid of this GetTenantAuditListResponseQuery.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def exchange_name(self):
        """Gets the exchange_name of this GetTenantAuditListResponseQuery.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The exchange_name of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this GetTenantAuditListResponseQuery.

        交易所名称  # noqa: E501

        :param exchange_name: The exchange_name of this GetTenantAuditListResponseQuery.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

    @property
    def status(self):
        """Gets the status of this GetTenantAuditListResponseQuery.  # noqa: E501

        类型audit(初审)、re_audit(复审)、audit_return(初审驳回)、re_audit_return(复审驳回)、approved(通过)  # noqa: E501

        :return: The status of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetTenantAuditListResponseQuery.

        类型audit(初审)、re_audit(复审)、audit_return(初审驳回)、re_audit_return(复审驳回)、approved(通过)  # noqa: E501

        :param status: The status of this GetTenantAuditListResponseQuery.  # noqa: E501
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
        """Gets the failure_type of this GetTenantAuditListResponseQuery.  # noqa: E501

        失败类型  # noqa: E501

        :return: The failure_type of this GetTenantAuditListResponseQuery.  # noqa: E501
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type):
        """Sets the failure_type of this GetTenantAuditListResponseQuery.

        失败类型  # noqa: E501

        :param failure_type: The failure_type of this GetTenantAuditListResponseQuery.  # noqa: E501
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
        if issubclass(GetTenantAuditListResponseQuery, dict):
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
        if not isinstance(other, GetTenantAuditListResponseQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other