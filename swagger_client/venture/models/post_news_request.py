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


class PostNewsRequest(object):
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
        'title': 'str',
        'link': 'str',
        'source': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'link': 'link',
        'source': 'source',
        'project_id': 'projectId'
    }

    def __init__(self, title=None, link=None, source=None, project_id=None):  # noqa: E501
        """PostNewsRequest - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._link = None
        self._source = None
        self._project_id = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if link is not None:
            self.link = link
        if source is not None:
            self.source = source
        if project_id is not None:
            self.project_id = project_id

    @property
    def title(self):
        """Gets the title of this PostNewsRequest.  # noqa: E501

        标题  # noqa: E501

        :return: The title of this PostNewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PostNewsRequest.

        标题  # noqa: E501

        :param title: The title of this PostNewsRequest.  # noqa: E501
        :type: str
        """
        if title is not None and len(title) > 30:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `30`")  # noqa: E501

        self._title = title

    @property
    def link(self):
        """Gets the link of this PostNewsRequest.  # noqa: E501

        链接  # noqa: E501

        :return: The link of this PostNewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this PostNewsRequest.

        链接  # noqa: E501

        :param link: The link of this PostNewsRequest.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def source(self):
        """Gets the source of this PostNewsRequest.  # noqa: E501

        来源  # noqa: E501

        :return: The source of this PostNewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PostNewsRequest.

        来源  # noqa: E501

        :param source: The source of this PostNewsRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def project_id(self):
        """Gets the project_id of this PostNewsRequest.  # noqa: E501

        项目ID  # noqa: E501

        :return: The project_id of this PostNewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PostNewsRequest.

        项目ID  # noqa: E501

        :param project_id: The project_id of this PostNewsRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

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
        if issubclass(PostNewsRequest, dict):
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
        if not isinstance(other, PostNewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
