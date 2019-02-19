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


class FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality(object):
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
        'id_photo': 'float',
        'temporary_id_photo_': 'float',
        'photocopy': 'float',
        'screen': 'float',
        'edited': 'float'
    }

    attribute_map = {
        'id_photo': 'ID Photo',
        'temporary_id_photo_': 'Temporary ID Photo ',
        'photocopy': 'Photocopy',
        'screen': 'Screen',
        'edited': 'Edited'
    }

    def __init__(self, id_photo=None, temporary_id_photo_=None, photocopy=None, screen=None, edited=None):  # noqa: E501
        """FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality - a model defined in Swagger"""  # noqa: E501

        self._id_photo = None
        self._temporary_id_photo_ = None
        self._photocopy = None
        self._screen = None
        self._edited = None
        self.discriminator = None

        if id_photo is not None:
            self.id_photo = id_photo
        if temporary_id_photo_ is not None:
            self.temporary_id_photo_ = temporary_id_photo_
        if photocopy is not None:
            self.photocopy = photocopy
        if screen is not None:
            self.screen = screen
        if edited is not None:
            self.edited = edited

    @property
    def id_photo(self):
        """Gets the id_photo of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501


        :return: The id_photo of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :rtype: float
        """
        return self._id_photo

    @id_photo.setter
    def id_photo(self, id_photo):
        """Sets the id_photo of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.


        :param id_photo: The id_photo of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :type: float
        """

        self._id_photo = id_photo

    @property
    def temporary_id_photo_(self):
        """Gets the temporary_id_photo_ of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501


        :return: The temporary_id_photo_ of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :rtype: float
        """
        return self._temporary_id_photo_

    @temporary_id_photo_.setter
    def temporary_id_photo_(self, temporary_id_photo_):
        """Sets the temporary_id_photo_ of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.


        :param temporary_id_photo_: The temporary_id_photo_ of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :type: float
        """

        self._temporary_id_photo_ = temporary_id_photo_

    @property
    def photocopy(self):
        """Gets the photocopy of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501


        :return: The photocopy of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :rtype: float
        """
        return self._photocopy

    @photocopy.setter
    def photocopy(self, photocopy):
        """Sets the photocopy of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.


        :param photocopy: The photocopy of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :type: float
        """

        self._photocopy = photocopy

    @property
    def screen(self):
        """Gets the screen of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501


        :return: The screen of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :rtype: float
        """
        return self._screen

    @screen.setter
    def screen(self, screen):
        """Sets the screen of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.


        :param screen: The screen of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :type: float
        """

        self._screen = screen

    @property
    def edited(self):
        """Gets the edited of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501


        :return: The edited of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :rtype: float
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """Sets the edited of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.


        :param edited: The edited of this FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality.  # noqa: E501
        :type: float
        """

        self._edited = edited

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
        if issubclass(FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality, dict):
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
        if not isinstance(other, FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
