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


class PutProjectRequestProjectInfo(object):
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
        'white_paper_key': 'str',
        'official_website': 'str',
        'email': 'str',
        'area_code': 'str',
        'cellphone': 'str',
        'telephone': 'str',
        'project_poster_key': 'str',
        'description': 'str'
    }

    attribute_map = {
        'white_paper_key': 'whitePaperKey',
        'official_website': 'officialWebsite',
        'email': 'email',
        'area_code': 'areaCode',
        'cellphone': 'cellphone',
        'telephone': 'telephone',
        'project_poster_key': 'projectPosterKey',
        'description': 'description'
    }

    def __init__(self, white_paper_key=None, official_website=None, email=None, area_code=None, cellphone=None, telephone=None, project_poster_key=None, description=None):  # noqa: E501
        """PutProjectRequestProjectInfo - a model defined in Swagger"""  # noqa: E501

        self._white_paper_key = None
        self._official_website = None
        self._email = None
        self._area_code = None
        self._cellphone = None
        self._telephone = None
        self._project_poster_key = None
        self._description = None
        self.discriminator = None

        if white_paper_key is not None:
            self.white_paper_key = white_paper_key
        if official_website is not None:
            self.official_website = official_website
        if email is not None:
            self.email = email
        if area_code is not None:
            self.area_code = area_code
        if cellphone is not None:
            self.cellphone = cellphone
        if telephone is not None:
            self.telephone = telephone
        if project_poster_key is not None:
            self.project_poster_key = project_poster_key
        if description is not None:
            self.description = description

    @property
    def white_paper_key(self):
        """Gets the white_paper_key of this PutProjectRequestProjectInfo.  # noqa: E501

        白皮书PDF  # noqa: E501

        :return: The white_paper_key of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._white_paper_key

    @white_paper_key.setter
    def white_paper_key(self, white_paper_key):
        """Sets the white_paper_key of this PutProjectRequestProjectInfo.

        白皮书PDF  # noqa: E501

        :param white_paper_key: The white_paper_key of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._white_paper_key = white_paper_key

    @property
    def official_website(self):
        """Gets the official_website of this PutProjectRequestProjectInfo.  # noqa: E501

        官方网站  # noqa: E501

        :return: The official_website of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._official_website

    @official_website.setter
    def official_website(self, official_website):
        """Sets the official_website of this PutProjectRequestProjectInfo.

        官方网站  # noqa: E501

        :param official_website: The official_website of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._official_website = official_website

    @property
    def email(self):
        """Gets the email of this PutProjectRequestProjectInfo.  # noqa: E501

        电子邮箱  # noqa: E501

        :return: The email of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PutProjectRequestProjectInfo.

        电子邮箱  # noqa: E501

        :param email: The email of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def area_code(self):
        """Gets the area_code of this PutProjectRequestProjectInfo.  # noqa: E501

        电话区号  # noqa: E501

        :return: The area_code of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this PutProjectRequestProjectInfo.

        电话区号  # noqa: E501

        :param area_code: The area_code of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def cellphone(self):
        """Gets the cellphone of this PutProjectRequestProjectInfo.  # noqa: E501

        手机号  # noqa: E501

        :return: The cellphone of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._cellphone

    @cellphone.setter
    def cellphone(self, cellphone):
        """Sets the cellphone of this PutProjectRequestProjectInfo.

        手机号  # noqa: E501

        :param cellphone: The cellphone of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._cellphone = cellphone

    @property
    def telephone(self):
        """Gets the telephone of this PutProjectRequestProjectInfo.  # noqa: E501

        固定电话号  # noqa: E501

        :return: The telephone of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PutProjectRequestProjectInfo.

        固定电话号  # noqa: E501

        :param telephone: The telephone of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def project_poster_key(self):
        """Gets the project_poster_key of this PutProjectRequestProjectInfo.  # noqa: E501

        项目广告图Key  # noqa: E501

        :return: The project_poster_key of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_poster_key

    @project_poster_key.setter
    def project_poster_key(self, project_poster_key):
        """Sets the project_poster_key of this PutProjectRequestProjectInfo.

        项目广告图Key  # noqa: E501

        :param project_poster_key: The project_poster_key of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._project_poster_key = project_poster_key

    @property
    def description(self):
        """Gets the description of this PutProjectRequestProjectInfo.  # noqa: E501

        项目简介  # noqa: E501

        :return: The description of this PutProjectRequestProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutProjectRequestProjectInfo.

        项目简介  # noqa: E501

        :param description: The description of this PutProjectRequestProjectInfo.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(PutProjectRequestProjectInfo, dict):
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
        if not isinstance(other, PutProjectRequestProjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
