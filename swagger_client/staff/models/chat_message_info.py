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


class ChatMessageInfo(object):
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
        'order_id': 'str',
        'time': 'str',
        'sender': 'str',
        'recver': 'str',
        'msg': 'str',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'order_id': 'orderId',
        'time': 'time',
        'sender': 'sender',
        'recver': 'recver',
        'msg': 'msg',
        'type': 'type'
    }

    def __init__(self, id=None, order_id=None, time=None, sender=None, recver=None, msg=None, type=None):  # noqa: E501
        """ChatMessageInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._order_id = None
        self._time = None
        self._sender = None
        self._recver = None
        self._msg = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if order_id is not None:
            self.order_id = order_id
        if time is not None:
            self.time = time
        if sender is not None:
            self.sender = sender
        if recver is not None:
            self.recver = recver
        if msg is not None:
            self.msg = msg
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ChatMessageInfo.  # noqa: E501

        msg id  # noqa: E501

        :return: The id of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChatMessageInfo.

        msg id  # noqa: E501

        :param id: The id of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this ChatMessageInfo.  # noqa: E501

        order id  # noqa: E501

        :return: The order_id of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ChatMessageInfo.

        order id  # noqa: E501

        :param order_id: The order_id of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def time(self):
        """Gets the time of this ChatMessageInfo.  # noqa: E501

        国际时间  # noqa: E501

        :return: The time of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ChatMessageInfo.

        国际时间  # noqa: E501

        :param time: The time of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def sender(self):
        """Gets the sender of this ChatMessageInfo.  # noqa: E501

        发送者id  # noqa: E501

        :return: The sender of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this ChatMessageInfo.

        发送者id  # noqa: E501

        :param sender: The sender of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def recver(self):
        """Gets the recver of this ChatMessageInfo.  # noqa: E501

        接受者id  # noqa: E501

        :return: The recver of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._recver

    @recver.setter
    def recver(self, recver):
        """Sets the recver of this ChatMessageInfo.

        接受者id  # noqa: E501

        :param recver: The recver of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._recver = recver

    @property
    def msg(self):
        """Gets the msg of this ChatMessageInfo.  # noqa: E501

        内容  # noqa: E501

        :return: The msg of this ChatMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ChatMessageInfo.

        内容  # noqa: E501

        :param msg: The msg of this ChatMessageInfo.  # noqa: E501
        :type: str
        """

        self._msg = msg

    @property
    def type(self):
        """Gets the type of this ChatMessageInfo.  # noqa: E501

        消息类型 1 文本消息 2 系统消息 3 图片  # noqa: E501

        :return: The type of this ChatMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChatMessageInfo.

        消息类型 1 文本消息 2 系统消息 3 图片  # noqa: E501

        :param type: The type of this ChatMessageInfo.  # noqa: E501
        :type: int
        """

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
        if issubclass(ChatMessageInfo, dict):
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
        if not isinstance(other, ChatMessageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
