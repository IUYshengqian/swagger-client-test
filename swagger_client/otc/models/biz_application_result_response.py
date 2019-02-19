# coding: utf-8

"""
    crush-otc 平台接口（法币交易）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BizApplicationResultResponse(object):
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
        'code': 'int',
        'reason': 'str'
    }

    attribute_map = {
        'code': 'code',
        'reason': 'reason'
    }

    def __init__(self, code=None, reason=None):  # noqa: E501
        """BizApplicationResultResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._reason = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if reason is not None:
            self.reason = reason

    @property
    def code(self):
        """Gets the code of this BizApplicationResultResponse.  # noqa: E501

        结果码 1审核中 2 审批通过 3 审批被驳回  # noqa: E501

        :return: The code of this BizApplicationResultResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BizApplicationResultResponse.

        结果码 1审核中 2 审批通过 3 审批被驳回  # noqa: E501

        :param code: The code of this BizApplicationResultResponse.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def reason(self):
        """Gets the reason of this BizApplicationResultResponse.  # noqa: E501

        驳回理由  # noqa: E501

        :return: The reason of this BizApplicationResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this BizApplicationResultResponse.

        驳回理由  # noqa: E501

        :param reason: The reason of this BizApplicationResultResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(BizApplicationResultResponse, dict):
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
        if not isinstance(other, BizApplicationResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other