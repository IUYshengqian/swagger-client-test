# coding: utf-8

"""
    crush-otc 平台接口（法币交易）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendMsgRequest(object):
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
        'recver_id': 'str',
        'order_id': 'str',
        'msg': 'str',
        'type': 'int'
    }

    attribute_map = {
        'recver_id': 'recverId',
        'order_id': 'orderId',
        'msg': 'msg',
        'type': 'type'
    }

    def __init__(self, recver_id=None, order_id=None, msg=None, type=None):  # noqa: E501
        """SendMsgRequest - a model defined in Swagger"""  # noqa: E501

        self._recver_id = None
        self._order_id = None
        self._msg = None
        self._type = None
        self.discriminator = None

        self.recver_id = recver_id
        self.order_id = order_id
        self.msg = msg
        self.type = type

    @property
    def recver_id(self):
        """Gets the recver_id of this SendMsgRequest.  # noqa: E501

        接受者id  # noqa: E501

        :return: The recver_id of this SendMsgRequest.  # noqa: E501
        :rtype: str
        """
        return self._recver_id

    @recver_id.setter
    def recver_id(self, recver_id):
        """Sets the recver_id of this SendMsgRequest.

        接受者id  # noqa: E501

        :param recver_id: The recver_id of this SendMsgRequest.  # noqa: E501
        :type: str
        """
        if recver_id is None:
            raise ValueError("Invalid value for `recver_id`, must not be `None`")  # noqa: E501

        self._recver_id = recver_id

    @property
    def order_id(self):
        """Gets the order_id of this SendMsgRequest.  # noqa: E501

        订单id  # noqa: E501

        :return: The order_id of this SendMsgRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SendMsgRequest.

        订单id  # noqa: E501

        :param order_id: The order_id of this SendMsgRequest.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def msg(self):
        """Gets the msg of this SendMsgRequest.  # noqa: E501

        内容  # noqa: E501

        :return: The msg of this SendMsgRequest.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SendMsgRequest.

        内容  # noqa: E501

        :param msg: The msg of this SendMsgRequest.  # noqa: E501
        :type: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501
        if msg is not None and len(msg) > 250:
            raise ValueError("Invalid value for `msg`, length must be less than or equal to `250`")  # noqa: E501
        if msg is not None and len(msg) < 1:
            raise ValueError("Invalid value for `msg`, length must be greater than or equal to `1`")  # noqa: E501

        self._msg = msg

    @property
    def type(self):
        """Gets the type of this SendMsgRequest.  # noqa: E501

        消息类型  1 文本消息 3 图片  # noqa: E501

        :return: The type of this SendMsgRequest.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SendMsgRequest.

        消息类型  1 文本消息 3 图片  # noqa: E501

        :param type: The type of this SendMsgRequest.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(SendMsgRequest, dict):
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
        if not isinstance(other, SendMsgRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
