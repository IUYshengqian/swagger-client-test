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


class GetJournalsQuery(object):
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
        'subject_type': 'str',
        'coin_id': 'str'
    }

    attribute_map = {
        'subject_type': 'subjectType',
        'coin_id': 'coinId'
    }

    def __init__(self, subject_type=None, coin_id=None):  # noqa: E501
        """GetJournalsQuery - a model defined in Swagger"""  # noqa: E501

        self._subject_type = None
        self._coin_id = None
        self.discriminator = None

        if subject_type is not None:
            self.subject_type = subject_type
        if coin_id is not None:
            self.coin_id = coin_id

    @property
    def subject_type(self):
        """Gets the subject_type of this GetJournalsQuery.  # noqa: E501

        科目类型,  # noqa: E501

        :return: The subject_type of this GetJournalsQuery.  # noqa: E501
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this GetJournalsQuery.

        科目类型,  # noqa: E501

        :param subject_type: The subject_type of this GetJournalsQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["C2C", "RECHARGE", "WITHDRAW", "ACTIVITY_IN", "ACTIVITY_OUT", "COMMISSION", "FEE", "BUY_COMMODITY", "SERVICE", "OTC_TRANSFER_IN", "OTC_TRANSFER_OUT"]  # noqa: E501
        if subject_type not in allowed_values:
            raise ValueError(
                "Invalid value for `subject_type` ({0}), must be one of {1}"  # noqa: E501
                .format(subject_type, allowed_values)
            )

        self._subject_type = subject_type

    @property
    def coin_id(self):
        """Gets the coin_id of this GetJournalsQuery.  # noqa: E501

        币种Id  # noqa: E501

        :return: The coin_id of this GetJournalsQuery.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetJournalsQuery.

        币种Id  # noqa: E501

        :param coin_id: The coin_id of this GetJournalsQuery.  # noqa: E501
        :type: str
        """

        self._coin_id = coin_id

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
        if issubclass(GetJournalsQuery, dict):
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
        if not isinstance(other, GetJournalsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
