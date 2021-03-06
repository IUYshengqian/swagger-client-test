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


class GetIndividualAuditResponse(object):
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
        'created_at': 'datetime',
        'id': 'str',
        'account_id': 'str',
        'nationality_code': 'str',
        'name': 'str',
        'id_type': 'str',
        'number': 'str',
        'front_url': 'str',
        'back_url': 'str',
        'handheld_url': 'str',
        'certification_status': 'str',
        'reject_type': 'str',
        'rejected_reason': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'account_id': 'accountId',
        'nationality_code': 'nationalityCode',
        'name': 'name',
        'id_type': 'idType',
        'number': 'number',
        'front_url': 'frontUrl',
        'back_url': 'backUrl',
        'handheld_url': 'handheldUrl',
        'certification_status': 'certificationStatus',
        'reject_type': 'rejectType',
        'rejected_reason': 'rejectedReason'
    }

    def __init__(self, created_at=None, id=None, account_id=None, nationality_code=None, name=None, id_type=None, number=None, front_url=None, back_url=None, handheld_url=None, certification_status=None, reject_type=None, rejected_reason=None):  # noqa: E501
        """GetIndividualAuditResponse - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._id = None
        self._account_id = None
        self._nationality_code = None
        self._name = None
        self._id_type = None
        self._number = None
        self._front_url = None
        self._back_url = None
        self._handheld_url = None
        self._certification_status = None
        self._reject_type = None
        self._rejected_reason = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if nationality_code is not None:
            self.nationality_code = nationality_code
        if name is not None:
            self.name = name
        if id_type is not None:
            self.id_type = id_type
        if number is not None:
            self.number = number
        if front_url is not None:
            self.front_url = front_url
        if back_url is not None:
            self.back_url = back_url
        if handheld_url is not None:
            self.handheld_url = handheld_url
        if certification_status is not None:
            self.certification_status = certification_status
        if reject_type is not None:
            self.reject_type = reject_type
        if rejected_reason is not None:
            self.rejected_reason = rejected_reason

    @property
    def created_at(self):
        """Gets the created_at of this GetIndividualAuditResponse.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The created_at of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetIndividualAuditResponse.

        提交申请时间  # noqa: E501

        :param created_at: The created_at of this GetIndividualAuditResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this GetIndividualAuditResponse.  # noqa: E501

        工单编号  # noqa: E501

        :return: The id of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetIndividualAuditResponse.

        工单编号  # noqa: E501

        :param id: The id of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this GetIndividualAuditResponse.  # noqa: E501

        uid  # noqa: E501

        :return: The account_id of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetIndividualAuditResponse.

        uid  # noqa: E501

        :param account_id: The account_id of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def nationality_code(self):
        """Gets the nationality_code of this GetIndividualAuditResponse.  # noqa: E501

        国籍  # noqa: E501

        :return: The nationality_code of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._nationality_code

    @nationality_code.setter
    def nationality_code(self, nationality_code):
        """Sets the nationality_code of this GetIndividualAuditResponse.

        国籍  # noqa: E501

        :param nationality_code: The nationality_code of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._nationality_code = nationality_code

    @property
    def name(self):
        """Gets the name of this GetIndividualAuditResponse.  # noqa: E501

        用户姓名  # noqa: E501

        :return: The name of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetIndividualAuditResponse.

        用户姓名  # noqa: E501

        :param name: The name of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id_type(self):
        """Gets the id_type of this GetIndividualAuditResponse.  # noqa: E501

        证件类型[\"ID（身份证）、PASSPORT（护照）\"]  # noqa: E501

        :return: The id_type of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this GetIndividualAuditResponse.

        证件类型[\"ID（身份证）、PASSPORT（护照）\"]  # noqa: E501

        :param id_type: The id_type of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ID", "PASSPORT"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(id_type, allowed_values)
            )

        self._id_type = id_type

    @property
    def number(self):
        """Gets the number of this GetIndividualAuditResponse.  # noqa: E501

        证件号码  # noqa: E501

        :return: The number of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GetIndividualAuditResponse.

        证件号码  # noqa: E501

        :param number: The number of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def front_url(self):
        """Gets the front_url of this GetIndividualAuditResponse.  # noqa: E501

        证件正面照  # noqa: E501

        :return: The front_url of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._front_url

    @front_url.setter
    def front_url(self, front_url):
        """Sets the front_url of this GetIndividualAuditResponse.

        证件正面照  # noqa: E501

        :param front_url: The front_url of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._front_url = front_url

    @property
    def back_url(self):
        """Gets the back_url of this GetIndividualAuditResponse.  # noqa: E501

        证件反面照  # noqa: E501

        :return: The back_url of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._back_url

    @back_url.setter
    def back_url(self, back_url):
        """Sets the back_url of this GetIndividualAuditResponse.

        证件反面照  # noqa: E501

        :param back_url: The back_url of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._back_url = back_url

    @property
    def handheld_url(self):
        """Gets the handheld_url of this GetIndividualAuditResponse.  # noqa: E501

        手持证件照  # noqa: E501

        :return: The handheld_url of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._handheld_url

    @handheld_url.setter
    def handheld_url(self, handheld_url):
        """Sets the handheld_url of this GetIndividualAuditResponse.

        手持证件照  # noqa: E501

        :param handheld_url: The handheld_url of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._handheld_url = handheld_url

    @property
    def certification_status(self):
        """Gets the certification_status of this GetIndividualAuditResponse.  # noqa: E501

        状态[APPLIED（待审核）、ACCEPTED（通过）、REJECTED（未通过）\"]  # noqa: E501

        :return: The certification_status of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._certification_status

    @certification_status.setter
    def certification_status(self, certification_status):
        """Sets the certification_status of this GetIndividualAuditResponse.

        状态[APPLIED（待审核）、ACCEPTED（通过）、REJECTED（未通过）\"]  # noqa: E501

        :param certification_status: The certification_status of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPLIED", "ACCEPTED", "REJECTED"]  # noqa: E501
        if certification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `certification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(certification_status, allowed_values)
            )

        self._certification_status = certification_status

    @property
    def reject_type(self):
        """Gets the reject_type of this GetIndividualAuditResponse.  # noqa: E501

        失败类型  # noqa: E501

        :return: The reject_type of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._reject_type

    @reject_type.setter
    def reject_type(self, reject_type):
        """Sets the reject_type of this GetIndividualAuditResponse.

        失败类型  # noqa: E501

        :param reject_type: The reject_type of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["INDIVIDUAL_ID", "INDIVIDUAL_PASSPORT", "ENTERPRISE_LOGO", "ENTERPRISE_LICENSE", "INDIVIDUAL_ABNORMAL", "ENTERPRISE_ABNORMAL", "USER_REPORT_ABNORMAL"]  # noqa: E501
        if reject_type not in allowed_values:
            raise ValueError(
                "Invalid value for `reject_type` ({0}), must be one of {1}"  # noqa: E501
                .format(reject_type, allowed_values)
            )

        self._reject_type = reject_type

    @property
    def rejected_reason(self):
        """Gets the rejected_reason of this GetIndividualAuditResponse.  # noqa: E501

        拒绝原因  # noqa: E501

        :return: The rejected_reason of this GetIndividualAuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._rejected_reason

    @rejected_reason.setter
    def rejected_reason(self, rejected_reason):
        """Sets the rejected_reason of this GetIndividualAuditResponse.

        拒绝原因  # noqa: E501

        :param rejected_reason: The rejected_reason of this GetIndividualAuditResponse.  # noqa: E501
        :type: str
        """

        self._rejected_reason = rejected_reason

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
        if issubclass(GetIndividualAuditResponse, dict):
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
        if not isinstance(other, GetIndividualAuditResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
