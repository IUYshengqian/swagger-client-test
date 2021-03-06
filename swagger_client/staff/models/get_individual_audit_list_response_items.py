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


class GetIndividualAuditListResponseItems(object):
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
        'account_id': 'str',
        'name': 'str',
        'id_type': 'str',
        'number': 'str',
        'rejected_type': 'str',
        'rejected_reason': 'str',
        'fron_url': 'str',
        'back_url': 'str',
        'handheld_url': 'str',
        'created_at': 'str',
        'audited_at': 'str',
        'staff_id': 'str',
        'staff_name': 'str',
        'nationality_code': 'str',
        'certification_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'name': 'name',
        'id_type': 'idType',
        'number': 'number',
        'rejected_type': 'rejectedType',
        'rejected_reason': 'rejectedReason',
        'fron_url': 'fronUrl',
        'back_url': 'backUrl',
        'handheld_url': 'handheldUrl',
        'created_at': 'createdAt',
        'audited_at': 'auditedAt',
        'staff_id': 'staffId',
        'staff_name': 'staffName',
        'nationality_code': 'nationalityCode',
        'certification_status': 'certificationStatus'
    }

    def __init__(self, id=None, account_id=None, name=None, id_type=None, number=None, rejected_type=None, rejected_reason=None, fron_url=None, back_url=None, handheld_url=None, created_at=None, audited_at=None, staff_id=None, staff_name=None, nationality_code=None, certification_status=None):  # noqa: E501
        """GetIndividualAuditListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._name = None
        self._id_type = None
        self._number = None
        self._rejected_type = None
        self._rejected_reason = None
        self._fron_url = None
        self._back_url = None
        self._handheld_url = None
        self._created_at = None
        self._audited_at = None
        self._staff_id = None
        self._staff_name = None
        self._nationality_code = None
        self._certification_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if id_type is not None:
            self.id_type = id_type
        if number is not None:
            self.number = number
        if rejected_type is not None:
            self.rejected_type = rejected_type
        if rejected_reason is not None:
            self.rejected_reason = rejected_reason
        if fron_url is not None:
            self.fron_url = fron_url
        if back_url is not None:
            self.back_url = back_url
        if handheld_url is not None:
            self.handheld_url = handheld_url
        if created_at is not None:
            self.created_at = created_at
        if audited_at is not None:
            self.audited_at = audited_at
        if staff_id is not None:
            self.staff_id = staff_id
        if staff_name is not None:
            self.staff_name = staff_name
        if nationality_code is not None:
            self.nationality_code = nationality_code
        if certification_status is not None:
            self.certification_status = certification_status

    @property
    def id(self):
        """Gets the id of this GetIndividualAuditListResponseItems.  # noqa: E501

        工单编号  # noqa: E501

        :return: The id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetIndividualAuditListResponseItems.

        工单编号  # noqa: E501

        :param id: The id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this GetIndividualAuditListResponseItems.  # noqa: E501

        请求的uid  # noqa: E501

        :return: The account_id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetIndividualAuditListResponseItems.

        请求的uid  # noqa: E501

        :param account_id: The account_id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this GetIndividualAuditListResponseItems.  # noqa: E501

        用户姓名  # noqa: E501

        :return: The name of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetIndividualAuditListResponseItems.

        用户姓名  # noqa: E501

        :param name: The name of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id_type(self):
        """Gets the id_type of this GetIndividualAuditListResponseItems.  # noqa: E501

        状态[\"PASSPORT（护照）、ID（身份证）\"]  # noqa: E501

        :return: The id_type of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this GetIndividualAuditListResponseItems.

        状态[\"PASSPORT（护照）、ID（身份证）\"]  # noqa: E501

        :param id_type: The id_type of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASSPORT", "ID"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(id_type, allowed_values)
            )

        self._id_type = id_type

    @property
    def number(self):
        """Gets the number of this GetIndividualAuditListResponseItems.  # noqa: E501

        证件号码  # noqa: E501

        :return: The number of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GetIndividualAuditListResponseItems.

        证件号码  # noqa: E501

        :param number: The number of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def rejected_type(self):
        """Gets the rejected_type of this GetIndividualAuditListResponseItems.  # noqa: E501

        失败类型  # noqa: E501

        :return: The rejected_type of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._rejected_type

    @rejected_type.setter
    def rejected_type(self, rejected_type):
        """Sets the rejected_type of this GetIndividualAuditListResponseItems.

        失败类型  # noqa: E501

        :param rejected_type: The rejected_type of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["INDIVIDUAL_ID", "INDIVIDUAL_PASSPORT", "ENTERPRISE_LOGO", "ENTERPRISE_LICENSE", "INDIVIDUAL_ABNORMAL", "ENTERPRISE_ABNORMAL", "USER_REPORT_ABNORMAL"]  # noqa: E501
        if rejected_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rejected_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rejected_type, allowed_values)
            )

        self._rejected_type = rejected_type

    @property
    def rejected_reason(self):
        """Gets the rejected_reason of this GetIndividualAuditListResponseItems.  # noqa: E501

        拒绝原因  # noqa: E501

        :return: The rejected_reason of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._rejected_reason

    @rejected_reason.setter
    def rejected_reason(self, rejected_reason):
        """Sets the rejected_reason of this GetIndividualAuditListResponseItems.

        拒绝原因  # noqa: E501

        :param rejected_reason: The rejected_reason of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._rejected_reason = rejected_reason

    @property
    def fron_url(self):
        """Gets the fron_url of this GetIndividualAuditListResponseItems.  # noqa: E501

        正面图片  # noqa: E501

        :return: The fron_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._fron_url

    @fron_url.setter
    def fron_url(self, fron_url):
        """Sets the fron_url of this GetIndividualAuditListResponseItems.

        正面图片  # noqa: E501

        :param fron_url: The fron_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._fron_url = fron_url

    @property
    def back_url(self):
        """Gets the back_url of this GetIndividualAuditListResponseItems.  # noqa: E501

        背面图片  # noqa: E501

        :return: The back_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._back_url

    @back_url.setter
    def back_url(self, back_url):
        """Sets the back_url of this GetIndividualAuditListResponseItems.

        背面图片  # noqa: E501

        :param back_url: The back_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._back_url = back_url

    @property
    def handheld_url(self):
        """Gets the handheld_url of this GetIndividualAuditListResponseItems.  # noqa: E501

        正面图片  # noqa: E501

        :return: The handheld_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._handheld_url

    @handheld_url.setter
    def handheld_url(self, handheld_url):
        """Sets the handheld_url of this GetIndividualAuditListResponseItems.

        正面图片  # noqa: E501

        :param handheld_url: The handheld_url of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._handheld_url = handheld_url

    @property
    def created_at(self):
        """Gets the created_at of this GetIndividualAuditListResponseItems.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The created_at of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetIndividualAuditListResponseItems.

        提交申请时间  # noqa: E501

        :param created_at: The created_at of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def audited_at(self):
        """Gets the audited_at of this GetIndividualAuditListResponseItems.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The audited_at of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._audited_at

    @audited_at.setter
    def audited_at(self, audited_at):
        """Sets the audited_at of this GetIndividualAuditListResponseItems.

        提交申请时间  # noqa: E501

        :param audited_at: The audited_at of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._audited_at = audited_at

    @property
    def staff_id(self):
        """Gets the staff_id of this GetIndividualAuditListResponseItems.  # noqa: E501

        职员id  # noqa: E501

        :return: The staff_id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GetIndividualAuditListResponseItems.

        职员id  # noqa: E501

        :param staff_id: The staff_id of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._staff_id = staff_id

    @property
    def staff_name(self):
        """Gets the staff_name of this GetIndividualAuditListResponseItems.  # noqa: E501

        管理员姓名  # noqa: E501

        :return: The staff_name of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._staff_name

    @staff_name.setter
    def staff_name(self, staff_name):
        """Sets the staff_name of this GetIndividualAuditListResponseItems.

        管理员姓名  # noqa: E501

        :param staff_name: The staff_name of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._staff_name = staff_name

    @property
    def nationality_code(self):
        """Gets the nationality_code of this GetIndividualAuditListResponseItems.  # noqa: E501

        CN  # noqa: E501

        :return: The nationality_code of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._nationality_code

    @nationality_code.setter
    def nationality_code(self, nationality_code):
        """Sets the nationality_code of this GetIndividualAuditListResponseItems.

        CN  # noqa: E501

        :param nationality_code: The nationality_code of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """

        self._nationality_code = nationality_code

    @property
    def certification_status(self):
        """Gets the certification_status of this GetIndividualAuditListResponseItems.  # noqa: E501

        状态[APPLIED（待审核）、ACCEPTED（通过）、REJECTED（未通过）\"]  # noqa: E501

        :return: The certification_status of this GetIndividualAuditListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._certification_status

    @certification_status.setter
    def certification_status(self, certification_status):
        """Sets the certification_status of this GetIndividualAuditListResponseItems.

        状态[APPLIED（待审核）、ACCEPTED（通过）、REJECTED（未通过）\"]  # noqa: E501

        :param certification_status: The certification_status of this GetIndividualAuditListResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPLIED", "ACCEPTED", "REJECTED"]  # noqa: E501
        if certification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `certification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(certification_status, allowed_values)
            )

        self._certification_status = certification_status

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
        if issubclass(GetIndividualAuditListResponseItems, dict):
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
        if not isinstance(other, GetIndividualAuditListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
