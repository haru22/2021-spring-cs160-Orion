# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guruMatch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='guruMatch.proto',
  package='guruMatchPackage',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fguruMatch.proto\x12\x10guruMatchPackage\"-\n\x11\x43reateUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\"\n\x0fSuccessResponse\x12\x0f\n\x07success\x18\x01 \x01(\x05\"\x1b\n\rIDonlymessage\x12\n\n\x02id\x18\x01 \x01(\t\"\xa4\x01\n\x0cUserFormData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07userBio\x18\x03 \x01(\t\x12\x17\n\x0fuserDescription\x18\x04 \x01(\t\x12\x11\n\tuserSkill\x18\x05 \x01(\t\x12\x14\n\x0cuserIndustry\x18\x06 \x01(\t\x12\x0f\n\x07userTag\x18\x07 \x01(\t\x12\x12\n\nprofilePic\x18\x08 \x01(\t\"\xa5\x01\n\x0bUserProfile\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07userBio\x18\x02 \x01(\t\x12\x17\n\x0fuserDescription\x18\x03 \x01(\t\x12\x11\n\tuserSkill\x18\x04 \x01(\t\x12\x14\n\x0cuserIndustry\x18\x05 \x01(\t\x12\x0f\n\x07userTag\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x12\n\nprofilePic\x18\x08 \x01(\t\"N\n\x13\x43reateMenteeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08interest\x18\x02 \x01(\t\x12\x19\n\x11menteeDescription\x18\x03 \x01(\t\"N\n\x13\x43reateMentorRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08interest\x18\x02 \x01(\t\x12\x19\n\x11mentorDescription\x18\x03 \x01(\t\"=\n\x0eMentorResponse\x12\x10\n\x08interest\x18\x02 \x03(\t\x12\x19\n\x11mentorDescription\x18\x03 \x01(\t\"\x80\x01\n\x06Mentor\x12\x10\n\x08mentorID\x18\x01 \x01(\t\x12\x32\n\x0buserProfile\x18\x02 \x01(\x0b\x32\x1d.guruMatchPackage.UserProfile\x12\x30\n\x06mentor\x18\x03 \x01(\x0b\x32 .guruMatchPackage.MentorResponse\"H\n\x13MatchMentorResponse\x12\x31\n\x0f\x61llMatchMentors\x18\x01 \x03(\x0b\x32\x18.guruMatchPackage.Mentor\"=\n\x0eMenteeResponse\x12\x10\n\x08interest\x18\x02 \x03(\t\x12\x19\n\x11menteeDescription\x18\x03 \x01(\t\"\x80\x01\n\x06Mentee\x12\x10\n\x08menteeID\x18\x01 \x01(\t\x12\x32\n\x0buserProfile\x18\x02 \x01(\x0b\x32\x1d.guruMatchPackage.UserProfile\x12\x30\n\x06mentee\x18\x03 \x01(\x0b\x32 .guruMatchPackage.MenteeResponse\"H\n\x13MatchMenteeResponse\x12\x31\n\x0f\x61llMatchMentees\x18\x01 \x03(\x0b\x32\x18.guruMatchPackage.Mentee\"7\n\x11MenteeAndMentorID\x12\x10\n\x08menteeID\x18\x01 \x01(\t\x12\x10\n\x08mentorID\x18\x02 \x01(\t\"@\n\nAllMatches\x12\x18\n\x10\x61llMenteeRequest\x18\x01 \x03(\t\x12\x18\n\x10\x61llMentorRequest\x18\x02 \x03(\t2\x81\x08\n\tGuruMatch\x12V\n\nCreateUser\x12#.guruMatchPackage.CreateUserRequest\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12W\n\x0fIsUsernameExist\x12\x1f.guruMatchPackage.IDonlymessage\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12T\n\rStoreUserForm\x12\x1e.guruMatchPackage.UserFormData\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12R\n\x0eGetUserProfile\x12\x1f.guruMatchPackage.IDonlymessage\x1a\x1d.guruMatchPackage.UserProfile\"\x00\x12Z\n\x0c\x43reateMentee\x12%.guruMatchPackage.CreateMenteeRequest\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12Z\n\x0c\x43reateMentor\x12%.guruMatchPackage.CreateMentorRequest\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12[\n\x0fGetMatchMentors\x12\x1f.guruMatchPackage.IDonlymessage\x1a%.guruMatchPackage.MatchMentorResponse\"\x00\x12[\n\x0fGetMatchMentees\x12\x1f.guruMatchPackage.IDonlymessage\x1a%.guruMatchPackage.MatchMenteeResponse\"\x00\x12\x66\n\x1aInsertMentorSelectedMentee\x12#.guruMatchPackage.MenteeAndMentorID\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12\x66\n\x1aInsertMenteeSelectedMentor\x12#.guruMatchPackage.MenteeAndMentorID\x1a!.guruMatchPackage.SuccessResponse\"\x00\x12W\n\x14GetAllMatchesRequest\x12\x1f.guruMatchPackage.IDonlymessage\x1a\x1c.guruMatchPackage.AllMatches\"\x00\x62\x06proto3'
)




_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='guruMatchPackage.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='guruMatchPackage.CreateUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='guruMatchPackage.CreateUserRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=82,
)


_SUCCESSRESPONSE = _descriptor.Descriptor(
  name='SuccessResponse',
  full_name='guruMatchPackage.SuccessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='guruMatchPackage.SuccessResponse.success', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=118,
)


_IDONLYMESSAGE = _descriptor.Descriptor(
  name='IDonlymessage',
  full_name='guruMatchPackage.IDonlymessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='guruMatchPackage.IDonlymessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=147,
)


_USERFORMDATA = _descriptor.Descriptor(
  name='UserFormData',
  full_name='guruMatchPackage.UserFormData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='guruMatchPackage.UserFormData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='guruMatchPackage.UserFormData.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userBio', full_name='guruMatchPackage.UserFormData.userBio', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userDescription', full_name='guruMatchPackage.UserFormData.userDescription', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userSkill', full_name='guruMatchPackage.UserFormData.userSkill', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userIndustry', full_name='guruMatchPackage.UserFormData.userIndustry', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userTag', full_name='guruMatchPackage.UserFormData.userTag', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profilePic', full_name='guruMatchPackage.UserFormData.profilePic', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=314,
)


_USERPROFILE = _descriptor.Descriptor(
  name='UserProfile',
  full_name='guruMatchPackage.UserProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='guruMatchPackage.UserProfile.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userBio', full_name='guruMatchPackage.UserProfile.userBio', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userDescription', full_name='guruMatchPackage.UserProfile.userDescription', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userSkill', full_name='guruMatchPackage.UserProfile.userSkill', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userIndustry', full_name='guruMatchPackage.UserProfile.userIndustry', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userTag', full_name='guruMatchPackage.UserProfile.userTag', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='guruMatchPackage.UserProfile.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profilePic', full_name='guruMatchPackage.UserProfile.profilePic', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=482,
)


_CREATEMENTEEREQUEST = _descriptor.Descriptor(
  name='CreateMenteeRequest',
  full_name='guruMatchPackage.CreateMenteeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='guruMatchPackage.CreateMenteeRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interest', full_name='guruMatchPackage.CreateMenteeRequest.interest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='menteeDescription', full_name='guruMatchPackage.CreateMenteeRequest.menteeDescription', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=562,
)


_CREATEMENTORREQUEST = _descriptor.Descriptor(
  name='CreateMentorRequest',
  full_name='guruMatchPackage.CreateMentorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='guruMatchPackage.CreateMentorRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interest', full_name='guruMatchPackage.CreateMentorRequest.interest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mentorDescription', full_name='guruMatchPackage.CreateMentorRequest.mentorDescription', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=642,
)


_MENTORRESPONSE = _descriptor.Descriptor(
  name='MentorResponse',
  full_name='guruMatchPackage.MentorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interest', full_name='guruMatchPackage.MentorResponse.interest', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mentorDescription', full_name='guruMatchPackage.MentorResponse.mentorDescription', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=705,
)


_MENTOR = _descriptor.Descriptor(
  name='Mentor',
  full_name='guruMatchPackage.Mentor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mentorID', full_name='guruMatchPackage.Mentor.mentorID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userProfile', full_name='guruMatchPackage.Mentor.userProfile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mentor', full_name='guruMatchPackage.Mentor.mentor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=836,
)


_MATCHMENTORRESPONSE = _descriptor.Descriptor(
  name='MatchMentorResponse',
  full_name='guruMatchPackage.MatchMentorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allMatchMentors', full_name='guruMatchPackage.MatchMentorResponse.allMatchMentors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=910,
)


_MENTEERESPONSE = _descriptor.Descriptor(
  name='MenteeResponse',
  full_name='guruMatchPackage.MenteeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interest', full_name='guruMatchPackage.MenteeResponse.interest', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='menteeDescription', full_name='guruMatchPackage.MenteeResponse.menteeDescription', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=973,
)


_MENTEE = _descriptor.Descriptor(
  name='Mentee',
  full_name='guruMatchPackage.Mentee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='menteeID', full_name='guruMatchPackage.Mentee.menteeID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userProfile', full_name='guruMatchPackage.Mentee.userProfile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mentee', full_name='guruMatchPackage.Mentee.mentee', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=1104,
)


_MATCHMENTEERESPONSE = _descriptor.Descriptor(
  name='MatchMenteeResponse',
  full_name='guruMatchPackage.MatchMenteeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allMatchMentees', full_name='guruMatchPackage.MatchMenteeResponse.allMatchMentees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1106,
  serialized_end=1178,
)


_MENTEEANDMENTORID = _descriptor.Descriptor(
  name='MenteeAndMentorID',
  full_name='guruMatchPackage.MenteeAndMentorID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='menteeID', full_name='guruMatchPackage.MenteeAndMentorID.menteeID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mentorID', full_name='guruMatchPackage.MenteeAndMentorID.mentorID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1180,
  serialized_end=1235,
)


_ALLMATCHES = _descriptor.Descriptor(
  name='AllMatches',
  full_name='guruMatchPackage.AllMatches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allMenteeRequest', full_name='guruMatchPackage.AllMatches.allMenteeRequest', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allMentorRequest', full_name='guruMatchPackage.AllMatches.allMentorRequest', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1237,
  serialized_end=1301,
)

_MENTOR.fields_by_name['userProfile'].message_type = _USERPROFILE
_MENTOR.fields_by_name['mentor'].message_type = _MENTORRESPONSE
_MATCHMENTORRESPONSE.fields_by_name['allMatchMentors'].message_type = _MENTOR
_MENTEE.fields_by_name['userProfile'].message_type = _USERPROFILE
_MENTEE.fields_by_name['mentee'].message_type = _MENTEERESPONSE
_MATCHMENTEERESPONSE.fields_by_name['allMatchMentees'].message_type = _MENTEE
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['SuccessResponse'] = _SUCCESSRESPONSE
DESCRIPTOR.message_types_by_name['IDonlymessage'] = _IDONLYMESSAGE
DESCRIPTOR.message_types_by_name['UserFormData'] = _USERFORMDATA
DESCRIPTOR.message_types_by_name['UserProfile'] = _USERPROFILE
DESCRIPTOR.message_types_by_name['CreateMenteeRequest'] = _CREATEMENTEEREQUEST
DESCRIPTOR.message_types_by_name['CreateMentorRequest'] = _CREATEMENTORREQUEST
DESCRIPTOR.message_types_by_name['MentorResponse'] = _MENTORRESPONSE
DESCRIPTOR.message_types_by_name['Mentor'] = _MENTOR
DESCRIPTOR.message_types_by_name['MatchMentorResponse'] = _MATCHMENTORRESPONSE
DESCRIPTOR.message_types_by_name['MenteeResponse'] = _MENTEERESPONSE
DESCRIPTOR.message_types_by_name['Mentee'] = _MENTEE
DESCRIPTOR.message_types_by_name['MatchMenteeResponse'] = _MATCHMENTEERESPONSE
DESCRIPTOR.message_types_by_name['MenteeAndMentorID'] = _MENTEEANDMENTORID
DESCRIPTOR.message_types_by_name['AllMatches'] = _ALLMATCHES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

SuccessResponse = _reflection.GeneratedProtocolMessageType('SuccessResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSRESPONSE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.SuccessResponse)
  })
_sym_db.RegisterMessage(SuccessResponse)

IDonlymessage = _reflection.GeneratedProtocolMessageType('IDonlymessage', (_message.Message,), {
  'DESCRIPTOR' : _IDONLYMESSAGE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.IDonlymessage)
  })
_sym_db.RegisterMessage(IDonlymessage)

UserFormData = _reflection.GeneratedProtocolMessageType('UserFormData', (_message.Message,), {
  'DESCRIPTOR' : _USERFORMDATA,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.UserFormData)
  })
_sym_db.RegisterMessage(UserFormData)

UserProfile = _reflection.GeneratedProtocolMessageType('UserProfile', (_message.Message,), {
  'DESCRIPTOR' : _USERPROFILE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.UserProfile)
  })
_sym_db.RegisterMessage(UserProfile)

CreateMenteeRequest = _reflection.GeneratedProtocolMessageType('CreateMenteeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMENTEEREQUEST,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.CreateMenteeRequest)
  })
_sym_db.RegisterMessage(CreateMenteeRequest)

CreateMentorRequest = _reflection.GeneratedProtocolMessageType('CreateMentorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMENTORREQUEST,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.CreateMentorRequest)
  })
_sym_db.RegisterMessage(CreateMentorRequest)

MentorResponse = _reflection.GeneratedProtocolMessageType('MentorResponse', (_message.Message,), {
  'DESCRIPTOR' : _MENTORRESPONSE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.MentorResponse)
  })
_sym_db.RegisterMessage(MentorResponse)

Mentor = _reflection.GeneratedProtocolMessageType('Mentor', (_message.Message,), {
  'DESCRIPTOR' : _MENTOR,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.Mentor)
  })
_sym_db.RegisterMessage(Mentor)

MatchMentorResponse = _reflection.GeneratedProtocolMessageType('MatchMentorResponse', (_message.Message,), {
  'DESCRIPTOR' : _MATCHMENTORRESPONSE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.MatchMentorResponse)
  })
_sym_db.RegisterMessage(MatchMentorResponse)

MenteeResponse = _reflection.GeneratedProtocolMessageType('MenteeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MENTEERESPONSE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.MenteeResponse)
  })
_sym_db.RegisterMessage(MenteeResponse)

Mentee = _reflection.GeneratedProtocolMessageType('Mentee', (_message.Message,), {
  'DESCRIPTOR' : _MENTEE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.Mentee)
  })
_sym_db.RegisterMessage(Mentee)

MatchMenteeResponse = _reflection.GeneratedProtocolMessageType('MatchMenteeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MATCHMENTEERESPONSE,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.MatchMenteeResponse)
  })
_sym_db.RegisterMessage(MatchMenteeResponse)

MenteeAndMentorID = _reflection.GeneratedProtocolMessageType('MenteeAndMentorID', (_message.Message,), {
  'DESCRIPTOR' : _MENTEEANDMENTORID,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.MenteeAndMentorID)
  })
_sym_db.RegisterMessage(MenteeAndMentorID)

AllMatches = _reflection.GeneratedProtocolMessageType('AllMatches', (_message.Message,), {
  'DESCRIPTOR' : _ALLMATCHES,
  '__module__' : 'guruMatch_pb2'
  # @@protoc_insertion_point(class_scope:guruMatchPackage.AllMatches)
  })
_sym_db.RegisterMessage(AllMatches)



_GURUMATCH = _descriptor.ServiceDescriptor(
  name='GuruMatch',
  full_name='guruMatchPackage.GuruMatch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1304,
  serialized_end=2329,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='guruMatchPackage.GuruMatch.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='IsUsernameExist',
    full_name='guruMatchPackage.GuruMatch.IsUsernameExist',
    index=1,
    containing_service=None,
    input_type=_IDONLYMESSAGE,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StoreUserForm',
    full_name='guruMatchPackage.GuruMatch.StoreUserForm',
    index=2,
    containing_service=None,
    input_type=_USERFORMDATA,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserProfile',
    full_name='guruMatchPackage.GuruMatch.GetUserProfile',
    index=3,
    containing_service=None,
    input_type=_IDONLYMESSAGE,
    output_type=_USERPROFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateMentee',
    full_name='guruMatchPackage.GuruMatch.CreateMentee',
    index=4,
    containing_service=None,
    input_type=_CREATEMENTEEREQUEST,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateMentor',
    full_name='guruMatchPackage.GuruMatch.CreateMentor',
    index=5,
    containing_service=None,
    input_type=_CREATEMENTORREQUEST,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMatchMentors',
    full_name='guruMatchPackage.GuruMatch.GetMatchMentors',
    index=6,
    containing_service=None,
    input_type=_IDONLYMESSAGE,
    output_type=_MATCHMENTORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMatchMentees',
    full_name='guruMatchPackage.GuruMatch.GetMatchMentees',
    index=7,
    containing_service=None,
    input_type=_IDONLYMESSAGE,
    output_type=_MATCHMENTEERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertMentorSelectedMentee',
    full_name='guruMatchPackage.GuruMatch.InsertMentorSelectedMentee',
    index=8,
    containing_service=None,
    input_type=_MENTEEANDMENTORID,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertMenteeSelectedMentor',
    full_name='guruMatchPackage.GuruMatch.InsertMenteeSelectedMentor',
    index=9,
    containing_service=None,
    input_type=_MENTEEANDMENTORID,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllMatchesRequest',
    full_name='guruMatchPackage.GuruMatch.GetAllMatchesRequest',
    index=10,
    containing_service=None,
    input_type=_IDONLYMESSAGE,
    output_type=_ALLMATCHES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GURUMATCH)

DESCRIPTOR.services_by_name['GuruMatch'] = _GURUMATCH

# @@protoc_insertion_point(module_scope)
