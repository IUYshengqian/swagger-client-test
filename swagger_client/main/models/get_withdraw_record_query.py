# coding: utf-8

"""
    crush-main 平台接口（主平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetWithdrawRecordQuery(object):
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
        'status': 'str',
        'coin_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'coin_id': 'coinId'
    }

    def __init__(self, status=None, coin_id=None):  # noqa: E501
        """GetWithdrawRecordQuery - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._coin_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if coin_id is not None:
            self.coin_id = coin_id

    @property
    def status(self):
        """Gets the status of this GetWithdrawRecordQuery.  # noqa: E501

        提币状态  # noqa: E501

        :return: The status of this GetWithdrawRecordQuery.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetWithdrawRecordQuery.

        提币状态  # noqa: E501

        :param status: The status of this GetWithdrawRecordQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["WAIT_REVIEW", "REVIEWING", "SUCCEED", "FAILED", "CONFIRMING", "CANCEL", "REFUSAL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def coin_id(self):
        """Gets the coin_id of this GetWithdrawRecordQuery.  # noqa: E501

        币id  # noqa: E501

        :return: The coin_id of this GetWithdrawRecordQuery.  # noqa: E501
        :rtype: str
        """
        return self._coin_id

    @coin_id.setter
    def coin_id(self, coin_id):
        """Sets the coin_id of this GetWithdrawRecordQuery.

        币id  # noqa: E501

        :param coin_id: The coin_id of this GetWithdrawRecordQuery.  # noqa: E501
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
        if issubclass(GetWithdrawRecordQuery, dict):
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
        if not isinstance(other, GetWithdrawRecordQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
