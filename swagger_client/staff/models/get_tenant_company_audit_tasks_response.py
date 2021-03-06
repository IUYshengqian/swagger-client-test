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


class GetTenantCompanyAuditTasksResponse(object):
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
        'company_name': 'str',
        'social_number': 'str',
        'phone_number': 'str',
        'email': 'str',
        'tenant_name': 'str',
        'tenant_country': 'str',
        'tenant_logo': 'str',
        'tenant_label': 'str',
        'tenant_phone_number': 'str',
        'tenant_email': 'str'
    }

    attribute_map = {
        'submitted_at': 'submittedAt',
        'ticket_number': 'ticketNumber',
        'uid': 'uid',
        'company_name': 'companyName',
        'social_number': 'socialNumber',
        'phone_number': 'phoneNumber',
        'email': 'email',
        'tenant_name': 'tenantName',
        'tenant_country': 'tenantCountry',
        'tenant_logo': 'tenantLogo',
        'tenant_label': 'tenantLabel',
        'tenant_phone_number': 'tenantPhoneNumber',
        'tenant_email': 'tenantEmail'
    }

    def __init__(self, submitted_at=None, ticket_number=None, uid=None, company_name=None, social_number=None, phone_number=None, email=None, tenant_name=None, tenant_country=None, tenant_logo=None, tenant_label=None, tenant_phone_number=None, tenant_email=None):  # noqa: E501
        """GetTenantCompanyAuditTasksResponse - a model defined in Swagger"""  # noqa: E501

        self._submitted_at = None
        self._ticket_number = None
        self._uid = None
        self._company_name = None
        self._social_number = None
        self._phone_number = None
        self._email = None
        self._tenant_name = None
        self._tenant_country = None
        self._tenant_logo = None
        self._tenant_label = None
        self._tenant_phone_number = None
        self._tenant_email = None
        self.discriminator = None

        if submitted_at is not None:
            self.submitted_at = submitted_at
        if ticket_number is not None:
            self.ticket_number = ticket_number
        if uid is not None:
            self.uid = uid
        if company_name is not None:
            self.company_name = company_name
        if social_number is not None:
            self.social_number = social_number
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

    @property
    def submitted_at(self):
        """Gets the submitted_at of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The submitted_at of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this GetTenantCompanyAuditTasksResponse.

        提交申请时间  # noqa: E501

        :param submitted_at: The submitted_at of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def ticket_number(self):
        """Gets the ticket_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        工单编号  # noqa: E501

        :return: The ticket_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """Sets the ticket_number of this GetTenantCompanyAuditTasksResponse.

        工单编号  # noqa: E501

        :param ticket_number: The ticket_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._ticket_number = ticket_number

    @property
    def uid(self):
        """Gets the uid of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        uid  # noqa: E501

        :return: The uid of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetTenantCompanyAuditTasksResponse.

        uid  # noqa: E501

        :param uid: The uid of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def company_name(self):
        """Gets the company_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        企业名称  # noqa: E501

        :return: The company_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this GetTenantCompanyAuditTasksResponse.

        企业名称  # noqa: E501

        :param company_name: The company_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def social_number(self):
        """Gets the social_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        统一社会编号  # noqa: E501

        :return: The social_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._social_number

    @social_number.setter
    def social_number(self, social_number):
        """Sets the social_number of this GetTenantCompanyAuditTasksResponse.

        统一社会编号  # noqa: E501

        :param social_number: The social_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._social_number = social_number

    @property
    def phone_number(self):
        """Gets the phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        手机号码  # noqa: E501

        :return: The phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this GetTenantCompanyAuditTasksResponse.

        手机号码  # noqa: E501

        :param phone_number: The phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """Gets the email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        邮箱  # noqa: E501

        :return: The email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetTenantCompanyAuditTasksResponse.

        邮箱  # noqa: E501

        :param email: The email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def tenant_name(self):
        """Gets the tenant_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        交易所名称  # noqa: E501

        :return: The tenant_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this GetTenantCompanyAuditTasksResponse.

        交易所名称  # noqa: E501

        :param tenant_name: The tenant_name of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def tenant_country(self):
        """Gets the tenant_country of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        交易所国家  # noqa: E501

        :return: The tenant_country of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_country

    @tenant_country.setter
    def tenant_country(self, tenant_country):
        """Sets the tenant_country of this GetTenantCompanyAuditTasksResponse.

        交易所国家  # noqa: E501

        :param tenant_country: The tenant_country of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_country = tenant_country

    @property
    def tenant_logo(self):
        """Gets the tenant_logo of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        logo  # noqa: E501

        :return: The tenant_logo of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_logo

    @tenant_logo.setter
    def tenant_logo(self, tenant_logo):
        """Sets the tenant_logo of this GetTenantCompanyAuditTasksResponse.

        logo  # noqa: E501

        :param tenant_logo: The tenant_logo of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_logo = tenant_logo

    @property
    def tenant_label(self):
        """Gets the tenant_label of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        交易所标签  # noqa: E501

        :return: The tenant_label of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_label

    @tenant_label.setter
    def tenant_label(self, tenant_label):
        """Sets the tenant_label of this GetTenantCompanyAuditTasksResponse.

        交易所标签  # noqa: E501

        :param tenant_label: The tenant_label of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_label = tenant_label

    @property
    def tenant_phone_number(self):
        """Gets the tenant_phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        交易所电话  # noqa: E501

        :return: The tenant_phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_phone_number

    @tenant_phone_number.setter
    def tenant_phone_number(self, tenant_phone_number):
        """Sets the tenant_phone_number of this GetTenantCompanyAuditTasksResponse.

        交易所电话  # noqa: E501

        :param tenant_phone_number: The tenant_phone_number of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_phone_number = tenant_phone_number

    @property
    def tenant_email(self):
        """Gets the tenant_email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501

        交易所邮箱  # noqa: E501

        :return: The tenant_email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_email

    @tenant_email.setter
    def tenant_email(self, tenant_email):
        """Sets the tenant_email of this GetTenantCompanyAuditTasksResponse.

        交易所邮箱  # noqa: E501

        :param tenant_email: The tenant_email of this GetTenantCompanyAuditTasksResponse.  # noqa: E501
        :type: str
        """

        self._tenant_email = tenant_email

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
        if issubclass(GetTenantCompanyAuditTasksResponse, dict):
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
        if not isinstance(other, GetTenantCompanyAuditTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
