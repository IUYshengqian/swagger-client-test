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

from swagger_client.venture.models.get_venture_sponsor_list_response_projects import GetVentureSponsorListResponseProjects  # noqa: F401,E501


class GetVentureSponsorListResponseItems(object):
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
        'name': 'str',
        'logo': 'str',
        'summary': 'str',
        'website': 'str',
        'success_num': 'int',
        'projects': 'list[GetVentureSponsorListResponseProjects]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'logo': 'logo',
        'summary': 'summary',
        'website': 'website',
        'success_num': 'successNum',
        'projects': 'projects'
    }

    def __init__(self, id=None, name=None, logo=None, summary=None, website=None, success_num=None, projects=None):  # noqa: E501
        """GetVentureSponsorListResponseItems - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._logo = None
        self._summary = None
        self._website = None
        self._success_num = None
        self._projects = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if logo is not None:
            self.logo = logo
        if summary is not None:
            self.summary = summary
        if website is not None:
            self.website = website
        if success_num is not None:
            self.success_num = success_num
        if projects is not None:
            self.projects = projects

    @property
    def id(self):
        """Gets the id of this GetVentureSponsorListResponseItems.  # noqa: E501

        保荐方id  # noqa: E501

        :return: The id of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetVentureSponsorListResponseItems.

        保荐方id  # noqa: E501

        :param id: The id of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetVentureSponsorListResponseItems.  # noqa: E501

        保荐方名称  # noqa: E501

        :return: The name of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetVentureSponsorListResponseItems.

        保荐方名称  # noqa: E501

        :param name: The name of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this GetVentureSponsorListResponseItems.  # noqa: E501

        保荐方logo  # noqa: E501

        :return: The logo of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetVentureSponsorListResponseItems.

        保荐方logo  # noqa: E501

        :param logo: The logo of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def summary(self):
        """Gets the summary of this GetVentureSponsorListResponseItems.  # noqa: E501

        保荐方简介  # noqa: E501

        :return: The summary of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GetVentureSponsorListResponseItems.

        保荐方简介  # noqa: E501

        :param summary: The summary of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def website(self):
        """Gets the website of this GetVentureSponsorListResponseItems.  # noqa: E501

        官网  # noqa: E501

        :return: The website of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GetVentureSponsorListResponseItems.

        官网  # noqa: E501

        :param website: The website of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def success_num(self):
        """Gets the success_num of this GetVentureSponsorListResponseItems.  # noqa: E501

        保荐项目成功数量  # noqa: E501

        :return: The success_num of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this GetVentureSponsorListResponseItems.

        保荐项目成功数量  # noqa: E501

        :param success_num: The success_num of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: int
        """

        self._success_num = success_num

    @property
    def projects(self):
        """Gets the projects of this GetVentureSponsorListResponseItems.  # noqa: E501

        热门项目  # noqa: E501

        :return: The projects of this GetVentureSponsorListResponseItems.  # noqa: E501
        :rtype: list[GetVentureSponsorListResponseProjects]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this GetVentureSponsorListResponseItems.

        热门项目  # noqa: E501

        :param projects: The projects of this GetVentureSponsorListResponseItems.  # noqa: E501
        :type: list[GetVentureSponsorListResponseProjects]
        """

        self._projects = projects

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
        if issubclass(GetVentureSponsorListResponseItems, dict):
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
        if not isinstance(other, GetVentureSponsorListResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
