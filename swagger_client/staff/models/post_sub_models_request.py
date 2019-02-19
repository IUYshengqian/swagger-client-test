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


class PostSubModelsRequest(object):
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
        'identification': 'str',
        'name': 'str',
        'status': 'bool',
        'order': 'int',
        'model_id': 'str'
    }

    attribute_map = {
        'identification': 'identification',
        'name': 'name',
        'status': 'status',
        'order': 'order',
        'model_id': 'modelId'
    }

    def __init__(self, identification=None, name=None, status=None, order=None, model_id=None):  # noqa: E501
        """PostSubModelsRequest - a model defined in Swagger"""  # noqa: E501

        self._identification = None
        self._name = None
        self._status = None
        self._order = None
        self._model_id = None
        self.discriminator = None

        if identification is not None:
            self.identification = identification
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if order is not None:
            self.order = order
        if model_id is not None:
            self.model_id = model_id

    @property
    def identification(self):
        """Gets the identification of this PostSubModelsRequest.  # noqa: E501

        标识  # noqa: E501

        :return: The identification of this PostSubModelsRequest.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PostSubModelsRequest.

        标识  # noqa: E501

        :param identification: The identification of this PostSubModelsRequest.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def name(self):
        """Gets the name of this PostSubModelsRequest.  # noqa: E501

        名称  # noqa: E501

        :return: The name of this PostSubModelsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostSubModelsRequest.

        名称  # noqa: E501

        :param name: The name of this PostSubModelsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this PostSubModelsRequest.  # noqa: E501

        状态  # noqa: E501

        :return: The status of this PostSubModelsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostSubModelsRequest.

        状态  # noqa: E501

        :param status: The status of this PostSubModelsRequest.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def order(self):
        """Gets the order of this PostSubModelsRequest.  # noqa: E501

        排序  # noqa: E501

        :return: The order of this PostSubModelsRequest.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PostSubModelsRequest.

        排序  # noqa: E501

        :param order: The order of this PostSubModelsRequest.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def model_id(self):
        """Gets the model_id of this PostSubModelsRequest.  # noqa: E501

        父模型Id  # noqa: E501

        :return: The model_id of this PostSubModelsRequest.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this PostSubModelsRequest.

        父模型Id  # noqa: E501

        :param model_id: The model_id of this PostSubModelsRequest.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

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
        if issubclass(PostSubModelsRequest, dict):
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
        if not isinstance(other, PostSubModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
