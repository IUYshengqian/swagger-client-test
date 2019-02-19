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


class PostRegisterRequest(object):
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
        'email': 'str',
        'password': 'str',
        'promotion_code': 'str',
        'verification_code': 'str',
        'nationality_code': 'str',
        'nick_name': 'str',
        'challenge': 'str',
        'seccode': 'str',
        'validate': 'str'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'promotion_code': 'promotionCode',
        'verification_code': 'verificationCode',
        'nationality_code': 'nationalityCode',
        'nick_name': 'nickName',
        'challenge': 'challenge',
        'seccode': 'seccode',
        'validate': 'validate'
    }

    def __init__(self, email=None, password=None, promotion_code=None, verification_code=None, nationality_code=None, nick_name=None, challenge=None, seccode=None, validate=None):  # noqa: E501
        """PostRegisterRequest - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._password = None
        self._promotion_code = None
        self._verification_code = None
        self._nationality_code = None
        self._nick_name = None
        self._challenge = None
        self._seccode = None
        self._validate = None
        self.discriminator = None

        self.email = email
        self.password = password
        if promotion_code is not None:
            self.promotion_code = promotion_code
        self.verification_code = verification_code
        self.nationality_code = nationality_code
        if nick_name is not None:
            self.nick_name = nick_name
        self.challenge = challenge
        self.seccode = seccode
        self.validate = validate

    @property
    def email(self):
        """Gets the email of this PostRegisterRequest.  # noqa: E501

        只能邮箱注册  # noqa: E501

        :return: The email of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostRegisterRequest.

        只能邮箱注册  # noqa: E501

        :param email: The email of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 64:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `64`")  # noqa: E501
        if email is not None and len(email) < 6:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `6`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this PostRegisterRequest.  # noqa: E501

        密码  # noqa: E501

        :return: The password of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostRegisterRequest.

        密码  # noqa: E501

        :param password: The password of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 16:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `16`")  # noqa: E501
        if password is not None and len(password) < 8:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")  # noqa: E501

        self._password = password

    @property
    def promotion_code(self):
        """Gets the promotion_code of this PostRegisterRequest.  # noqa: E501

        邀请码  # noqa: E501

        :return: The promotion_code of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._promotion_code

    @promotion_code.setter
    def promotion_code(self, promotion_code):
        """Sets the promotion_code of this PostRegisterRequest.

        邀请码  # noqa: E501

        :param promotion_code: The promotion_code of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if promotion_code is not None and len(promotion_code) > 20:
            raise ValueError("Invalid value for `promotion_code`, length must be less than or equal to `20`")  # noqa: E501
        if promotion_code is not None and len(promotion_code) < 4:
            raise ValueError("Invalid value for `promotion_code`, length must be greater than or equal to `4`")  # noqa: E501

        self._promotion_code = promotion_code

    @property
    def verification_code(self):
        """Gets the verification_code of this PostRegisterRequest.  # noqa: E501

        验证码  # noqa: E501

        :return: The verification_code of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this PostRegisterRequest.

        验证码  # noqa: E501

        :param verification_code: The verification_code of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if verification_code is None:
            raise ValueError("Invalid value for `verification_code`, must not be `None`")  # noqa: E501
        if verification_code is not None and len(verification_code) > 6:
            raise ValueError("Invalid value for `verification_code`, length must be less than or equal to `6`")  # noqa: E501
        if verification_code is not None and len(verification_code) < 6:
            raise ValueError("Invalid value for `verification_code`, length must be greater than or equal to `6`")  # noqa: E501

        self._verification_code = verification_code

    @property
    def nationality_code(self):
        """Gets the nationality_code of this PostRegisterRequest.  # noqa: E501

        国籍  # noqa: E501

        :return: The nationality_code of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._nationality_code

    @nationality_code.setter
    def nationality_code(self, nationality_code):
        """Sets the nationality_code of this PostRegisterRequest.

        国籍  # noqa: E501

        :param nationality_code: The nationality_code of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if nationality_code is None:
            raise ValueError("Invalid value for `nationality_code`, must not be `None`")  # noqa: E501
        if nationality_code is not None and len(nationality_code) > 128:
            raise ValueError("Invalid value for `nationality_code`, length must be less than or equal to `128`")  # noqa: E501
        if nationality_code is not None and len(nationality_code) < 2:
            raise ValueError("Invalid value for `nationality_code`, length must be greater than or equal to `2`")  # noqa: E501

        self._nationality_code = nationality_code

    @property
    def nick_name(self):
        """Gets the nick_name of this PostRegisterRequest.  # noqa: E501

        昵称  # noqa: E501

        :return: The nick_name of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this PostRegisterRequest.

        昵称  # noqa: E501

        :param nick_name: The nick_name of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if nick_name is not None and len(nick_name) > 8:
            raise ValueError("Invalid value for `nick_name`, length must be less than or equal to `8`")  # noqa: E501
        if nick_name is not None and len(nick_name) < 2:
            raise ValueError("Invalid value for `nick_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._nick_name = nick_name

    @property
    def challenge(self):
        """Gets the challenge of this PostRegisterRequest.  # noqa: E501

        极验参数  # noqa: E501

        :return: The challenge of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this PostRegisterRequest.

        极验参数  # noqa: E501

        :param challenge: The challenge of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def seccode(self):
        """Gets the seccode of this PostRegisterRequest.  # noqa: E501

        极验参数  # noqa: E501

        :return: The seccode of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._seccode

    @seccode.setter
    def seccode(self, seccode):
        """Sets the seccode of this PostRegisterRequest.

        极验参数  # noqa: E501

        :param seccode: The seccode of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if seccode is None:
            raise ValueError("Invalid value for `seccode`, must not be `None`")  # noqa: E501

        self._seccode = seccode

    @property
    def validate(self):
        """Gets the validate of this PostRegisterRequest.  # noqa: E501

        极验参数  # noqa: E501

        :return: The validate of this PostRegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._validate

    @validate.setter
    def validate(self, validate):
        """Sets the validate of this PostRegisterRequest.

        极验参数  # noqa: E501

        :param validate: The validate of this PostRegisterRequest.  # noqa: E501
        :type: str
        """
        if validate is None:
            raise ValueError("Invalid value for `validate`, must not be `None`")  # noqa: E501

        self._validate = validate

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
        if issubclass(PostRegisterRequest, dict):
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
        if not isinstance(other, PostRegisterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
