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

from swagger_client.tenant.models.face_id_result_response_idcard_info_back_side_ocr_result import FaceIdResultResponseIdcardInfoBackSideOcrResult  # noqa: F401,E501
from swagger_client.tenant.models.face_id_result_response_idcard_info_front_side_ocr_result_legality import FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality  # noqa: F401,E501


class FaceIdResultResponseIdcardInfoBackSide(object):
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
        'ocr_result': 'FaceIdResultResponseIdcardInfoBackSideOcrResult',
        'upload_times': 'float',
        'legality': 'FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality'
    }

    attribute_map = {
        'ocr_result': 'ocr_result',
        'upload_times': 'upload_times',
        'legality': 'legality'
    }

    def __init__(self, ocr_result=None, upload_times=None, legality=None):  # noqa: E501
        """FaceIdResultResponseIdcardInfoBackSide - a model defined in Swagger"""  # noqa: E501

        self._ocr_result = None
        self._upload_times = None
        self._legality = None
        self.discriminator = None

        if ocr_result is not None:
            self.ocr_result = ocr_result
        if upload_times is not None:
            self.upload_times = upload_times
        if legality is not None:
            self.legality = legality

    @property
    def ocr_result(self):
        """Gets the ocr_result of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501


        :return: The ocr_result of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :rtype: FaceIdResultResponseIdcardInfoBackSideOcrResult
        """
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, ocr_result):
        """Sets the ocr_result of this FaceIdResultResponseIdcardInfoBackSide.


        :param ocr_result: The ocr_result of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :type: FaceIdResultResponseIdcardInfoBackSideOcrResult
        """

        self._ocr_result = ocr_result

    @property
    def upload_times(self):
        """Gets the upload_times of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501


        :return: The upload_times of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :rtype: float
        """
        return self._upload_times

    @upload_times.setter
    def upload_times(self, upload_times):
        """Sets the upload_times of this FaceIdResultResponseIdcardInfoBackSide.


        :param upload_times: The upload_times of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :type: float
        """

        self._upload_times = upload_times

    @property
    def legality(self):
        """Gets the legality of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501


        :return: The legality of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :rtype: FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality
        """
        return self._legality

    @legality.setter
    def legality(self, legality):
        """Sets the legality of this FaceIdResultResponseIdcardInfoBackSide.


        :param legality: The legality of this FaceIdResultResponseIdcardInfoBackSide.  # noqa: E501
        :type: FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality
        """

        self._legality = legality

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
        if issubclass(FaceIdResultResponseIdcardInfoBackSide, dict):
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
        if not isinstance(other, FaceIdResultResponseIdcardInfoBackSide):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
