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


class GetTenantAuditIndividualReAuditResponse(object):
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
        'submitted_at': 'datetime',
        'ticket_number': 'str',
        'uid': 'str',
        'user_name': 'str',
        'id_type': 'str',
        'id_number': 'str',
        'phone_number': 'str',
        'email': 'str',
        'tenant_name': 'str',
        'tenant_country': 'str',
        'tenant_logo': 'str',
        'tenant_label': 'str',
        'tenant_phone_number': 'str',
        'tenant_email': 'str',
        'audit_at': 'datetime',
        'audit_user': 'str',
        'is_data_received': 'bool',
        'audit_status': 'str',
        're_audit_at': 'datetime',
        're_audit_user': 'str',
        're_status': 'str',
        'failure_type': 'str'
    }

    attribute_map = {
        'submitted_at': 'submittedAt',
        'ticket_number': 'ticketNumber',
        'uid': 'uid',
        'user_name': 'userName',
        'id_type': 'idType',
        'id_number': 'idNumber',
        'phone_number': 'phoneNumber',
        'email': 'email',
        'tenant_name': 'tenantName',
        'tenant_country': 'tenantCountry',
        'tenant_logo': 'tenantLogo',
        'tenant_label': 'tenantLabel',
        'tenant_phone_number': 'tenantPhoneNumber',
        'tenant_email': 'tenantEmail',
        'audit_at': 'auditAt',
        'audit_user': 'auditUser',
        'is_data_received': 'isDataReceived',
        'audit_status': 'auditStatus',
        're_audit_at': 'reAuditAt',
        're_audit_user': 'reAuditUser',
        're_status': 'reStatus',
        'failure_type': 'failureType'
    }

    def __init__(self, submitted_at=None, ticket_number=None, uid=None, user_name=None, id_type=None, id_number=None, phone_number=None, email=None, tenant_name=None, tenant_country=None, tenant_logo=None, tenant_label=None, tenant_phone_number=None, tenant_email=None, audit_at=None, audit_user=None, is_data_received=None, audit_status=None, re_audit_at=None, re_audit_user=None, re_status=None, failure_type=None):  # noqa: E501
        """GetTenantAuditIndividualReAuditResponse - a model defined in Swagger"""  # noqa: E501

        self._submitted_at = None
        self._ticket_number = None
        self._uid = None
        self._user_name = None
        self._id_type = None
        self._id_number = None
        self._phone_number = None
        self._email = None
        self._tenant_name = None
        self._tenant_country = None
        self._tenant_logo = None
        self._tenant_label = None
        self._tenant_phone_number = None
        self._tenant_email = None
        self._audit_at = None
        self._audit_user = None
        self._is_data_received = None
        self._audit_status = None
        self._re_audit_at = None
        self._re_audit_user = None
        self._re_status = None
        self._failure_type = None
        self.discriminator = None

        if submitted_at is not None:
            self.submitted_at = submitted_at
        if ticket_number is not None:
            self.ticket_number = ticket_number
        if uid is not None:
            self.uid = uid
        if user_name is not None:
            self.user_name = user_name
        if id_type is not None:
            self.id_type = id_type
        if id_number is not None:
            self.id_number = id_number
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if tenant_country is not None:
            self.tenant_country = tenant_country
        if tenant_logo is not None:
            self.tenant_logo = tenant_logo
        if tenant_label is not None:
            self.tenant_label = tenant_label
        if tenant_phone_number is not None:
            self.tenant_phone_number = tenant_phone_number
        if tenant_email is not None:
            self.tenant_email = tenant_email
        if audit_at is not None:
            self.audit_at = audit_at
        if audit_user is not None:
            self.audit_user = audit_user
        if is_data_received is not None:
            self.is_data_received = is_data_received
        if audit_status is not None:
            self.audit_status = audit_status
        if re_audit_at is not None:
            self.re_audit_at = re_audit_at
        if re_audit_user is not None:
            self.re_audit_user = re_audit_user
        if re_status is not None:
            self.re_status = re_status
        if failure_type is not None:
            self.failure_type = failure_type

    @property
    def submitted_at(self):
        """Gets the submitted_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The submitted_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this GetTenantAuditIndividualReAuditResponse.

        提交申请时间  # noqa: E501

        :param submitted_at: The submitted_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def ticket_number(self):
        """Gets the ticket_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        工单编号  # noqa: E501

        :return: The ticket_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """Sets the ticket_number of this GetTenantAuditIndividualReAuditResponse.

        工单编号  # noqa: E501

        :param ticket_number: The ticket_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._ticket_number = ticket_number

    @property
    def uid(self):
        """Gets the uid of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        uid  # noqa: E501

        :return: The uid of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetTenantAuditIndividualReAuditResponse.

        uid  # noqa: E501

        :param uid: The uid of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def user_name(self):
        """Gets the user_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        用户姓名  # noqa: E501

        :return: The user_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GetTenantAuditIndividualReAuditResponse.

        用户姓名  # noqa: E501

        :param user_name: The user_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def id_type(self):
        """Gets the id_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        证件类型[\"id_card（身份证）、identification（护照）\"]  # noqa: E501

        :return: The id_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this GetTenantAuditIndividualReAuditResponse.

        证件类型[\"id_card（身份证）、identification（护照）\"]  # noqa: E501

        :param id_type: The id_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["id_card", "identification"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(id_type, allowed_values)
            )

        self._id_type = id_type

    @property
    def id_number(self):
        """Gets the id_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        证件号码  # noqa: E501

        :return: The id_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this GetTenantAuditIndividualReAuditResponse.

        证件号码  # noqa: E501

        :param id_number: The id_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._id_number = id_number

    @property
    def phone_number(self):
        """Gets the phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        手机号码  # noqa: E501

        :return: The phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this GetTenantAuditIndividualReAuditResponse.

        手机号码  # noqa: E501

        :param phone_number: The phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """Gets the email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        邮箱  # noqa: E501

        :return: The email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetTenantAuditIndividualReAuditResponse.

        邮箱  # noqa: E501

        :param email: The email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def tenant_name(self):
        """Gets the tenant_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The tenant_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this GetTenantAuditIndividualReAuditResponse.

        交易所名称  # noqa: E501

        :param tenant_name: The tenant_name of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def tenant_country(self):
        """Gets the tenant_country of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        交易所国家  # noqa: E501

        :return: The tenant_country of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_country

    @tenant_country.setter
    def tenant_country(self, tenant_country):
        """Sets the tenant_country of this GetTenantAuditIndividualReAuditResponse.

        交易所国家  # noqa: E501

        :param tenant_country: The tenant_country of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_country = tenant_country

    @property
    def tenant_logo(self):
        """Gets the tenant_logo of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        logo  # noqa: E501

        :return: The tenant_logo of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_logo

    @tenant_logo.setter
    def tenant_logo(self, tenant_logo):
        """Sets the tenant_logo of this GetTenantAuditIndividualReAuditResponse.

        logo  # noqa: E501

        :param tenant_logo: The tenant_logo of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_logo = tenant_logo

    @property
    def tenant_label(self):
        """Gets the tenant_label of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        交易所标签  # noqa: E501

        :return: The tenant_label of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_label

    @tenant_label.setter
    def tenant_label(self, tenant_label):
        """Sets the tenant_label of this GetTenantAuditIndividualReAuditResponse.

        交易所标签  # noqa: E501

        :param tenant_label: The tenant_label of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_label = tenant_label

    @property
    def tenant_phone_number(self):
        """Gets the tenant_phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        交易所电话  # noqa: E501

        :return: The tenant_phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_phone_number

    @tenant_phone_number.setter
    def tenant_phone_number(self, tenant_phone_number):
        """Sets the tenant_phone_number of this GetTenantAuditIndividualReAuditResponse.

        交易所电话  # noqa: E501

        :param tenant_phone_number: The tenant_phone_number of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_phone_number = tenant_phone_number

    @property
    def tenant_email(self):
        """Gets the tenant_email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        交易所邮箱  # noqa: E501

        :return: The tenant_email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_email

    @tenant_email.setter
    def tenant_email(self, tenant_email):
        """Sets the tenant_email of this GetTenantAuditIndividualReAuditResponse.

        交易所邮箱  # noqa: E501

        :param tenant_email: The tenant_email of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant_email = tenant_email

    @property
    def audit_at(self):
        """Gets the audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        初审时间  # noqa: E501

        :return: The audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._audit_at

    @audit_at.setter
    def audit_at(self, audit_at):
        """Sets the audit_at of this GetTenantAuditIndividualReAuditResponse.

        初审时间  # noqa: E501

        :param audit_at: The audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: datetime
        """

        self._audit_at = audit_at

    @property
    def audit_user(self):
        """Gets the audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        初审人员  # noqa: E501

        :return: The audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._audit_user

    @audit_user.setter
    def audit_user(self, audit_user):
        """Sets the audit_user of this GetTenantAuditIndividualReAuditResponse.

        初审人员  # noqa: E501

        :param audit_user: The audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._audit_user = audit_user

    @property
    def is_data_received(self):
        """Gets the is_data_received of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        资料接收状态  # noqa: E501

        :return: The is_data_received of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_data_received

    @is_data_received.setter
    def is_data_received(self, is_data_received):
        """Sets the is_data_received of this GetTenantAuditIndividualReAuditResponse.

        资料接收状态  # noqa: E501

        :param is_data_received: The is_data_received of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: bool
        """

        self._is_data_received = is_data_received

    @property
    def audit_status(self):
        """Gets the audit_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        初审状态[\"approved（通过）、disapproved（未通过）\"]  # noqa: E501

        :return: The audit_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._audit_status

    @audit_status.setter
    def audit_status(self, audit_status):
        """Sets the audit_status of this GetTenantAuditIndividualReAuditResponse.

        初审状态[\"approved（通过）、disapproved（未通过）\"]  # noqa: E501

        :param audit_status: The audit_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["approved", "disapproved"]  # noqa: E501
        if audit_status not in allowed_values:
            raise ValueError(
                "Invalid value for `audit_status` ({0}), must be one of {1}"  # noqa: E501
                .format(audit_status, allowed_values)
            )

        self._audit_status = audit_status

    @property
    def re_audit_at(self):
        """Gets the re_audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        复审时间  # noqa: E501

        :return: The re_audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._re_audit_at

    @re_audit_at.setter
    def re_audit_at(self, re_audit_at):
        """Sets the re_audit_at of this GetTenantAuditIndividualReAuditResponse.

        复审时间  # noqa: E501

        :param re_audit_at: The re_audit_at of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: datetime
        """

        self._re_audit_at = re_audit_at

    @property
    def re_audit_user(self):
        """Gets the re_audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        复审人员  # noqa: E501

        :return: The re_audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._re_audit_user

    @re_audit_user.setter
    def re_audit_user(self, re_audit_user):
        """Sets the re_audit_user of this GetTenantAuditIndividualReAuditResponse.

        复审人员  # noqa: E501

        :param re_audit_user: The re_audit_user of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """

        self._re_audit_user = re_audit_user

    @property
    def re_status(self):
        """Gets the re_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        状态[\"approved（通过）、disapproved（未通过）\"]  # noqa: E501

        :return: The re_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._re_status

    @re_status.setter
    def re_status(self, re_status):
        """Sets the re_status of this GetTenantAuditIndividualReAuditResponse.

        状态[\"approved（通过）、disapproved（未通过）\"]  # noqa: E501

        :param re_status: The re_status of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["approved", "disapproved"]  # noqa: E501
        if re_status not in allowed_values:
            raise ValueError(
                "Invalid value for `re_status` ({0}), must be one of {1}"  # noqa: E501
                .format(re_status, allowed_values)
            )

        self._re_status = re_status

    @property
    def failure_type(self):
        """Gets the failure_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501

        审核失败类型  # noqa: E501

        :return: The failure_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type):
        """Sets the failure_type of this GetTenantAuditIndividualReAuditResponse.

        审核失败类型  # noqa: E501

        :param failure_type: The failure_type of this GetTenantAuditIndividualReAuditResponse.  # noqa: E501
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
        if issubclass(GetTenantAuditIndividualReAuditResponse, dict):
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
        if not isinstance(other, GetTenantAuditIndividualReAuditResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
