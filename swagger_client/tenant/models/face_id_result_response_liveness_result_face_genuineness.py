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


class FaceIdResultResponseLivenessResultFaceGenuineness(object):
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
        'synthetic_face_confidence': 'float',
        'synthetic_face_threshold': 'float',
        'mask_confidence': 'float',
        'mask_threshold': 'float',
        'screen_replay_confidence': 'float',
        'screen_replay_threshold': 'float'
    }

    attribute_map = {
        'synthetic_face_confidence': 'synthetic_face_confidence',
        'synthetic_face_threshold': 'synthetic_face_threshold',
        'mask_confidence': 'mask_confidence',
        'mask_threshold': 'mask_threshold',
        'screen_replay_confidence': 'screen_replay_confidence',
        'screen_replay_threshold': 'screen_replay_threshold'
    }

    def __init__(self, synthetic_face_confidence=None, synthetic_face_threshold=None, mask_confidence=None, mask_threshold=None, screen_replay_confidence=None, screen_replay_threshold=None):  # noqa: E501
        """FaceIdResultResponseLivenessResultFaceGenuineness - a model defined in Swagger"""  # noqa: E501

        self._synthetic_face_confidence = None
        self._synthetic_face_threshold = None
        self._mask_confidence = None
        self._mask_threshold = None
        self._screen_replay_confidence = None
        self._screen_replay_threshold = None
        self.discriminator = None

        if synthetic_face_confidence is not None:
            self.synthetic_face_confidence = synthetic_face_confidence
        if synthetic_face_threshold is not None:
            self.synthetic_face_threshold = synthetic_face_threshold
        if mask_confidence is not None:
            self.mask_confidence = mask_confidence
        if mask_threshold is not None:
            self.mask_threshold = mask_threshold
        if screen_replay_confidence is not None:
            self.screen_replay_confidence = screen_replay_confidence
        if screen_replay_threshold is not None:
            self.screen_replay_threshold = screen_replay_threshold

    @property
    def synthetic_face_confidence(self):
        """Gets the synthetic_face_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The synthetic_face_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._synthetic_face_confidence

    @synthetic_face_confidence.setter
    def synthetic_face_confidence(self, synthetic_face_confidence):
        """Sets the synthetic_face_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param synthetic_face_confidence: The synthetic_face_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._synthetic_face_confidence = synthetic_face_confidence

    @property
    def synthetic_face_threshold(self):
        """Gets the synthetic_face_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The synthetic_face_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._synthetic_face_threshold

    @synthetic_face_threshold.setter
    def synthetic_face_threshold(self, synthetic_face_threshold):
        """Sets the synthetic_face_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param synthetic_face_threshold: The synthetic_face_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._synthetic_face_threshold = synthetic_face_threshold

    @property
    def mask_confidence(self):
        """Gets the mask_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The mask_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._mask_confidence

    @mask_confidence.setter
    def mask_confidence(self, mask_confidence):
        """Sets the mask_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param mask_confidence: The mask_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._mask_confidence = mask_confidence

    @property
    def mask_threshold(self):
        """Gets the mask_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The mask_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._mask_threshold

    @mask_threshold.setter
    def mask_threshold(self, mask_threshold):
        """Sets the mask_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param mask_threshold: The mask_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._mask_threshold = mask_threshold

    @property
    def screen_replay_confidence(self):
        """Gets the screen_replay_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The screen_replay_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._screen_replay_confidence

    @screen_replay_confidence.setter
    def screen_replay_confidence(self, screen_replay_confidence):
        """Sets the screen_replay_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param screen_replay_confidence: The screen_replay_confidence of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._screen_replay_confidence = screen_replay_confidence

    @property
    def screen_replay_threshold(self):
        """Gets the screen_replay_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501


        :return: The screen_replay_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :rtype: float
        """
        return self._screen_replay_threshold

    @screen_replay_threshold.setter
    def screen_replay_threshold(self, screen_replay_threshold):
        """Sets the screen_replay_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.


        :param screen_replay_threshold: The screen_replay_threshold of this FaceIdResultResponseLivenessResultFaceGenuineness.  # noqa: E501
        :type: float
        """

        self._screen_replay_threshold = screen_replay_threshold

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
        if issubclass(FaceIdResultResponseLivenessResultFaceGenuineness, dict):
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
        if not isinstance(other, FaceIdResultResponseLivenessResultFaceGenuineness):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
