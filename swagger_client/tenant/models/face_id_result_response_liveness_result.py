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

from swagger_client.tenant.models.face_id_result_response_liveness_result_details import FaceIdResultResponseLivenessResultDetails  # noqa: F401,E501
from swagger_client.tenant.models.face_id_result_response_liveness_result_face_genuineness import FaceIdResultResponseLivenessResultFaceGenuineness  # noqa: F401,E501


class FaceIdResultResponseLivenessResult(object):
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
        'procedure_type': 'str',
        'result': 'str',
        'details': 'FaceIdResultResponseLivenessResultDetails',
        'face_genuineness': 'FaceIdResultResponseLivenessResultFaceGenuineness'
    }

    attribute_map = {
        'procedure_type': 'procedure_type',
        'result': 'result',
        'details': 'details',
        'face_genuineness': 'face_genuineness'
    }

    def __init__(self, procedure_type=None, result=None, details=None, face_genuineness=None):  # noqa: E501
        """FaceIdResultResponseLivenessResult - a model defined in Swagger"""  # noqa: E501

        self._procedure_type = None
        self._result = None
        self._details = None
        self._face_genuineness = None
        self.discriminator = None

        if procedure_type is not None:
            self.procedure_type = procedure_type
        if result is not None:
            self.result = result
        if details is not None:
            self.details = details
        if face_genuineness is not None:
            self.face_genuineness = face_genuineness

    @property
    def procedure_type(self):
        """Gets the procedure_type of this FaceIdResultResponseLivenessResult.  # noqa: E501


        :return: The procedure_type of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :rtype: str
        """
        return self._procedure_type

    @procedure_type.setter
    def procedure_type(self, procedure_type):
        """Sets the procedure_type of this FaceIdResultResponseLivenessResult.


        :param procedure_type: The procedure_type of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :type: str
        """

        self._procedure_type = procedure_type

    @property
    def result(self):
        """Gets the result of this FaceIdResultResponseLivenessResult.  # noqa: E501


        :return: The result of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FaceIdResultResponseLivenessResult.


        :param result: The result of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "TIMEOUT"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def details(self):
        """Gets the details of this FaceIdResultResponseLivenessResult.  # noqa: E501


        :return: The details of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :rtype: FaceIdResultResponseLivenessResultDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this FaceIdResultResponseLivenessResult.


        :param details: The details of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :type: FaceIdResultResponseLivenessResultDetails
        """

        self._details = details

    @property
    def face_genuineness(self):
        """Gets the face_genuineness of this FaceIdResultResponseLivenessResult.  # noqa: E501


        :return: The face_genuineness of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :rtype: FaceIdResultResponseLivenessResultFaceGenuineness
        """
        return self._face_genuineness

    @face_genuineness.setter
    def face_genuineness(self, face_genuineness):
        """Sets the face_genuineness of this FaceIdResultResponseLivenessResult.


        :param face_genuineness: The face_genuineness of this FaceIdResultResponseLivenessResult.  # noqa: E501
        :type: FaceIdResultResponseLivenessResultFaceGenuineness
        """

        self._face_genuineness = face_genuineness

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
        if issubclass(FaceIdResultResponseLivenessResult, dict):
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
        if not isinstance(other, FaceIdResultResponseLivenessResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
