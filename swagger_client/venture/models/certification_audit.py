# coding: utf-8

"""
    crush-venture 平台接口（项目方平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CertificationAudit(object):
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
        'certification_status': 'str',
        'certification_type': 'str',
        'rejected_type': 'str',
        'rejected_reason': 'str',
        'application_date': 'datetime',
        'certificat_name': 'str'
    }

    attribute_map = {
        'certification_status': 'certificationStatus',
        'certification_type': 'certificationType',
        'rejected_type': 'rejectedType',
        'rejected_reason': 'rejectedReason',
        'application_date': 'applicationDate',
        'certificat_name': 'certificatName'
    }

    def __init__(self, certification_status=None, certification_type=None, rejected_type=None, rejected_reason=None, application_date=None, certificat_name=None):  # noqa: E501
        """CertificationAudit - a model defined in Swagger"""  # noqa: E501

        self._certification_status = None
        self._certification_type = None
        self._rejected_type = None
        self._rejected_reason = None
        self._application_date = None
        self._certificat_name = None
        self.discriminator = None

        if certification_status is not None:
            self.certification_status = certification_status
        if certification_type is not None:
            self.certification_type = certification_type
        if rejected_type is not None:
            self.rejected_type = rejected_type
        if rejected_reason is not None:
            self.rejected_reason = rejected_reason
        if application_date is not None:
            self.application_date = application_date
        if certificat_name is not None:
            self.certificat_name = certificat_name

    @property
    def certification_status(self):
        """Gets the certification_status of this CertificationAudit.  # noqa: E501

        当前认证状态  # noqa: E501

        :return: The certification_status of this CertificationAudit.  # noqa: E501
        :rtype: str
        """
        return self._certification_status

    @certification_status.setter
    def certification_status(self, certification_status):
        """Sets the certification_status of this CertificationAudit.

        当前认证状态  # noqa: E501

        :param certification_status: The certification_status of this CertificationAudit.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "applied", "accepted", "rejected"]  # noqa: E501
        if certification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `certification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(certification_status, allowed_values)
            )

        self._certification_status = certification_status

    @property
    def certification_type(self):
        """Gets the certification_type of this CertificationAudit.  # noqa: E501

        认证类型，当前没有认证时忽略此字段  # noqa: E501

        :return: The certification_type of this CertificationAudit.  # noqa: E501
        :rtype: str
        """
        return self._certification_type

    @certification_type.setter
    def certification_type(self, certification_type):
        """Sets the certification_type of this CertificationAudit.

        认证类型，当前没有认证时忽略此字段  # noqa: E501

        :param certification_type: The certification_type of this CertificationAudit.  # noqa: E501
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
    def rejected_type(self):
        """Gets the rejected_type of this CertificationAudit.  # noqa: E501

        认证拒绝类型  # noqa: E501

        :return: The rejected_type of this CertificationAudit.  # noqa: E501
        :rtype: str
        """
        return self._rejected_type

    @rejected_type.setter
    def rejected_type(self, rejected_type):
        """Sets the rejected_type of this CertificationAudit.

        认证拒绝类型  # noqa: E501

        :param rejected_type: The rejected_type of this CertificationAudit.  # noqa: E501
        :type: str
        """

        self._rejected_type = rejected_type

    @property
    def rejected_reason(self):
        """Gets the rejected_reason of this CertificationAudit.  # noqa: E501

        认证拒绝的原因  # noqa: E501

        :return: The rejected_reason of this CertificationAudit.  # noqa: E501
        :rtype: str
        """
        return self._rejected_reason

    @rejected_reason.setter
    def rejected_reason(self, rejected_reason):
        """Sets the rejected_reason of this CertificationAudit.

        认证拒绝的原因  # noqa: E501

        :param rejected_reason: The rejected_reason of this CertificationAudit.  # noqa: E501
        :type: str
        """

        self._rejected_reason = rejected_reason

    @property
    def application_date(self):
        """Gets the application_date of this CertificationAudit.  # noqa: E501

        认证时间  # noqa: E501

        :return: The application_date of this CertificationAudit.  # noqa: E501
        :rtype: datetime
        """
        return self._application_date

    @application_date.setter
    def application_date(self, application_date):
        """Sets the application_date of this CertificationAudit.

        认证时间  # noqa: E501

        :param application_date: The application_date of this CertificationAudit.  # noqa: E501
        :type: datetime
        """

        self._application_date = application_date

    @property
    def certificat_name(self):
        """Gets the certificat_name of this CertificationAudit.  # noqa: E501

        认证名字  # noqa: E501

        :return: The certificat_name of this CertificationAudit.  # noqa: E501
        :rtype: str
        """
        return self._certificat_name

    @certificat_name.setter
    def certificat_name(self, certificat_name):
        """Sets the certificat_name of this CertificationAudit.

        认证名字  # noqa: E501

        :param certificat_name: The certificat_name of this CertificationAudit.  # noqa: E501
        :type: str
        """

        self._certificat_name = certificat_name

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
        if issubclass(CertificationAudit, dict):
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
        if not isinstance(other, CertificationAudit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
