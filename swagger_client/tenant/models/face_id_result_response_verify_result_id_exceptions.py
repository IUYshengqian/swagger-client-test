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


class FaceIdResultResponseVerifyResultIdExceptions(object):
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
        'id_attacked': 'float',
        'id_photo_monochrome': 'float'
    }

    attribute_map = {
        'id_attacked': 'id_attacked',
        'id_photo_monochrome': 'id_photo_monochrome'
    }

    def __init__(self, id_attacked=None, id_photo_monochrome=None):  # noqa: E501
        """FaceIdResultResponseVerifyResultIdExceptions - a model defined in Swagger"""  # noqa: E501

        self._id_attacked = None
        self._id_photo_monochrome = None
        self.discriminator = None

        if id_attacked is not None:
            self.id_attacked = id_attacked
        if id_photo_monochrome is not None:
            self.id_photo_monochrome = id_photo_monochrome

    @property
    def id_attacked(self):
        """Gets the id_attacked of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501


        :return: The id_attacked of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501
        :rtype: float
        """
        return self._id_attacked

    @id_attacked.setter
    def id_attacked(self, id_attacked):
        """Sets the id_attacked of this FaceIdResultResponseVerifyResultIdExceptions.


        :param id_attacked: The id_attacked of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501
        :type: float
        """

        self._id_attacked = id_attacked

    @property
    def id_photo_monochrome(self):
        """Gets the id_photo_monochrome of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501


        :return: The id_photo_monochrome of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501
        :rtype: float
        """
        return self._id_photo_monochrome

    @id_photo_monochrome.setter
    def id_photo_monochrome(self, id_photo_monochrome):
        """Sets the id_photo_monochrome of this FaceIdResultResponseVerifyResultIdExceptions.


        :param id_photo_monochrome: The id_photo_monochrome of this FaceIdResultResponseVerifyResultIdExceptions.  # noqa: E501
        :type: float
        """

        self._id_photo_monochrome = id_photo_monochrome

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
        if issubclass(FaceIdResultResponseVerifyResultIdExceptions, dict):
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
        if not isinstance(other, FaceIdResultResponseVerifyResultIdExceptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
