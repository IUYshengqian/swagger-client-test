# coding: utf-8

"""
    crush-staff 平台接口（职员管理平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutSponsorRequest(object):
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
        'id': 'str',
        'logo': 'str',
        'website': 'str',
        'summary': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'logo': 'logo',
        'website': 'website',
        'summary': 'summary',
        'phone': 'phone'
    }

    def __init__(self, id=None, logo=None, website=None, summary=None, phone=None):  # noqa: E501
        """PutSponsorRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._logo = None
        self._website = None
        self._summary = None
        self._phone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if logo is not None:
            self.logo = logo
        if website is not None:
            self.website = website
        if summary is not None:
            self.summary = summary
        if phone is not None:
            self.phone = phone

    @property
    def id(self):
        """Gets the id of this PutSponsorRequest.  # noqa: E501

        保荐方id  # noqa: E501

        :return: The id of this PutSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutSponsorRequest.

        保荐方id  # noqa: E501

        :param id: The id of this PutSponsorRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def logo(self):
        """Gets the logo of this PutSponsorRequest.  # noqa: E501

        logo 上传图片返回的id  # noqa: E501

        :return: The logo of this PutSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this PutSponsorRequest.

        logo 上传图片返回的id  # noqa: E501

        :param logo: The logo of this PutSponsorRequest.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def website(self):
        """Gets the website of this PutSponsorRequest.  # noqa: E501

        官网  # noqa: E501

        :return: The website of this PutSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PutSponsorRequest.

        官网  # noqa: E501

        :param website: The website of this PutSponsorRequest.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def summary(self):
        """Gets the summary of this PutSponsorRequest.  # noqa: E501

        简介  # noqa: E501

        :return: The summary of this PutSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PutSponsorRequest.

        简介  # noqa: E501

        :param summary: The summary of this PutSponsorRequest.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def phone(self):
        """Gets the phone of this PutSponsorRequest.  # noqa: E501

        手机  # noqa: E501

        :return: The phone of this PutSponsorRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PutSponsorRequest.

        手机  # noqa: E501

        :param phone: The phone of this PutSponsorRequest.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(PutSponsorRequest, dict):
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
        if not isinstance(other, PutSponsorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
