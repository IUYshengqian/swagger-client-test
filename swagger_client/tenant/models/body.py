# coding: utf-8

"""
    crush-tenant 平台接口(租户平台)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body(object):
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
        'contact_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'contact_id': 'contactId',
        'status': 'status'
    }

    def __init__(self, contact_id=None, status=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._contact_id = None
        self._status = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if status is not None:
            self.status = status

    @property
    def contact_id(self):
        """Gets the contact_id of this Body.  # noqa: E501

        对接ID  # noqa: E501

        :return: The contact_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Body.

        对接ID  # noqa: E501

        :param contact_id: The contact_id of this Body.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def status(self):
        """Gets the status of this Body.  # noqa: E501

        accepted接受，rejected拒绝  # noqa: E501

        :return: The status of this Body.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body.

        accepted接受，rejected拒绝  # noqa: E501

        :param status: The status of this Body.  # noqa: E501
        :type: str
        """
        allowed_values = ["accepted", "rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
