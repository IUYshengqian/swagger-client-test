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


class GetIndividualAuditReceiveTasksResponse(object):
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
        'submitted_at': 'datetime',
        'id': 'str',
        'account_id': 'str',
        'nation': 'str',
        'name': 'str',
        'id_type': 'str',
        'id_number': 'str',
        'front_photo': 'str',
        'back_photo': 'str',
        'handheld_photo': 'str'
    }

    attribute_map = {
        'submitted_at': 'submittedAt',
        'id': 'id',
        'account_id': 'accountId',
        'nation': 'nation',
        'name': 'name',
        'id_type': 'idType',
        'id_number': 'idNumber',
        'front_photo': 'frontPhoto',
        'back_photo': 'backPhoto',
        'handheld_photo': 'handheldPhoto'
    }

    def __init__(self, submitted_at=None, id=None, account_id=None, nation=None, name=None, id_type=None, id_number=None, front_photo=None, back_photo=None, handheld_photo=None):  # noqa: E501
        """GetIndividualAuditReceiveTasksResponse - a model defined in Swagger"""  # noqa: E501

        self._submitted_at = None
        self._id = None
        self._account_id = None
        self._nation = None
        self._name = None
        self._id_type = None
        self._id_number = None
        self._front_photo = None
        self._back_photo = None
        self._handheld_photo = None
        self.discriminator = None

        if submitted_at is not None:
            self.submitted_at = submitted_at
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if nation is not None:
            self.nation = nation
        if name is not None:
            self.name = name
        if id_type is not None:
            self.id_type = id_type
        if id_number is not None:
            self.id_number = id_number
        if front_photo is not None:
            self.front_photo = front_photo
        if back_photo is not None:
            self.back_photo = back_photo
        if handheld_photo is not None:
            self.handheld_photo = handheld_photo

    @property
    def submitted_at(self):
        """Gets the submitted_at of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        提交申请时间  # noqa: E501

        :return: The submitted_at of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this GetIndividualAuditReceiveTasksResponse.

        提交申请时间  # noqa: E501

        :param submitted_at: The submitted_at of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def id(self):
        """Gets the id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        工单编号  # noqa: E501

        :return: The id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetIndividualAuditReceiveTasksResponse.

        工单编号  # noqa: E501

        :param id: The id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        uid  # noqa: E501

        :return: The account_id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetIndividualAuditReceiveTasksResponse.

        uid  # noqa: E501

        :param account_id: The account_id of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def nation(self):
        """Gets the nation of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        国籍  # noqa: E501

        :return: The nation of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._nation

    @nation.setter
    def nation(self, nation):
        """Sets the nation of this GetIndividualAuditReceiveTasksResponse.

        国籍  # noqa: E501

        :param nation: The nation of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._nation = nation

    @property
    def name(self):
        """Gets the name of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        用户姓名  # noqa: E501

        :return: The name of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetIndividualAuditReceiveTasksResponse.

        用户姓名  # noqa: E501

        :param name: The name of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id_type(self):
        """Gets the id_type of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        证件类型[\"id_card（身份证）、identification（护照）\"]  # noqa: E501

        :return: The id_type of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this GetIndividualAuditReceiveTasksResponse.

        证件类型[\"id_card（身份证）、identification（护照）\"]  # noqa: E501

        :param id_type: The id_type of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["id_card", "identification"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(id_type, allowed_values)
            )

        self._id_type = id_type

    @property
    def id_number(self):
        """Gets the id_number of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        证件号码  # noqa: E501

        :return: The id_number of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this GetIndividualAuditReceiveTasksResponse.

        证件号码  # noqa: E501

        :param id_number: The id_number of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._id_number = id_number

    @property
    def front_photo(self):
        """Gets the front_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        证件正面照  # noqa: E501

        :return: The front_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._front_photo

    @front_photo.setter
    def front_photo(self, front_photo):
        """Sets the front_photo of this GetIndividualAuditReceiveTasksResponse.

        证件正面照  # noqa: E501

        :param front_photo: The front_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._front_photo = front_photo

    @property
    def back_photo(self):
        """Gets the back_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        证件反面照  # noqa: E501

        :return: The back_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._back_photo

    @back_photo.setter
    def back_photo(self, back_photo):
        """Sets the back_photo of this GetIndividualAuditReceiveTasksResponse.

        证件反面照  # noqa: E501

        :param back_photo: The back_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._back_photo = back_photo

    @property
    def handheld_photo(self):
        """Gets the handheld_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501

        手持证件照  # noqa: E501

        :return: The handheld_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :rtype: str
        """
        return self._handheld_photo

    @handheld_photo.setter
    def handheld_photo(self, handheld_photo):
        """Sets the handheld_photo of this GetIndividualAuditReceiveTasksResponse.

        手持证件照  # noqa: E501

        :param handheld_photo: The handheld_photo of this GetIndividualAuditReceiveTasksResponse.  # noqa: E501
        :type: str
        """

        self._handheld_photo = handheld_photo

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
        if issubclass(GetIndividualAuditReceiveTasksResponse, dict):
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
        if not isinstance(other, GetIndividualAuditReceiveTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
