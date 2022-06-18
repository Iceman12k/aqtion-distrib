# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_gameservers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_gameservers.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\220\001\001'),
  serialized_pb=_b('\n\x1fsteammessages_gameservers.proto\x1a steammessages_unified_base.proto\"\x9f\x01\n\"CGameServers_GetServerList_Request\x12(\n\x06\x66ilter\x18\x01 \x01(\tB\x18\x82\xb5\x18\x14Query filter string.\x12O\n\x05limit\x18\x02 \x01(\r:\x03\x31\x30\x30\x42;\x82\xb5\x18\x37The maximum number of servers to return in the response\"\xe0\x03\n#CGameServers_GetServerList_Response\x12\x65\n\x07servers\x18\x01 \x03(\x0b\x32+.CGameServers_GetServerList_Response.ServerB\'\x82\xb5\x18#List of servers matching the filter\x1a\xd1\x02\n\x06Server\x12\x30\n\x04\x61\x64\x64r\x18\x01 \x01(\tB\"\x82\xb5\x18\x1eThe server\'s IP and query port\x12\x10\n\x08gameport\x18\x02 \x01(\r\x12\x10\n\x08specport\x18\x03 \x01(\r\x12\x0f\n\x07steamid\x18\x04 \x01(\x06\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x12\x0f\n\x07gamedir\x18\x07 \x01(\t\x12\x0f\n\x07version\x18\x08 \x01(\t\x12\x0f\n\x07product\x18\t \x01(\t\x12\x0e\n\x06region\x18\n \x01(\x05\x12\x0f\n\x07players\x18\x0b \x01(\x05\x12\x13\n\x0bmax_players\x18\x0c \x01(\x05\x12\x0c\n\x04\x62ots\x18\r \x01(\x05\x12\x0b\n\x03map\x18\x0e \x01(\t\x12\x0e\n\x06secure\x18\x0f \x01(\x08\x12\x11\n\tdedicated\x18\x10 \x01(\x08\x12\n\n\x02os\x18\x11 \x01(\t\x12\x10\n\x08gametype\x18\x12 \x01(\t\"@\n*CGameServers_GetServerSteamIDsByIP_Request\x12\x12\n\nserver_ips\x18\x01 \x03(\t\"\x90\x01\n%CGameServers_IPsWithSteamIDs_Response\x12>\n\x07servers\x18\x01 \x03(\x0b\x32-.CGameServers_IPsWithSteamIDs_Response.Server\x1a\'\n\x06Server\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"E\n*CGameServers_GetServerIPsBySteamID_Request\x12\x17\n\x0fserver_steamids\x18\x01 \x03(\x06\x32\xab\x04\n\x0bGameServers\x12\x8c\x01\n\rGetServerList\x12#.CGameServers_GetServerList_Request\x1a$.CGameServers_GetServerList_Response\"0\x82\xb5\x18,Gets a list of servers given a filter string\x12\xa4\x01\n\x15GetServerSteamIDsByIP\x12+.CGameServers_GetServerSteamIDsByIP_Request\x1a&.CGameServers_IPsWithSteamIDs_Response\"6\x82\xb5\x18\x32Gets a list of server SteamIDs given a list of IPs\x12\xad\x01\n\x15GetServerIPsBySteamID\x12+.CGameServers_GetServerIPsBySteamID_Request\x1a&.CGameServers_IPsWithSteamIDs_Response\"?\x82\xb5\x18;Gets a list of server IP addresses given a list of SteamIDs\x1a\x36\x82\xb5\x18\x32\x41 service for searching and managing game servers.B\x03\x90\x01\x01')
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])




_CGAMESERVERS_GETSERVERLIST_REQUEST = _descriptor.Descriptor(
  name='CGameServers_GetServerList_Request',
  full_name='CGameServers_GetServerList_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='CGameServers_GetServerList_Request.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\265\030\024Query filter string.'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='CGameServers_GetServerList_Request.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\265\0307The maximum number of servers to return in the response'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=229,
)


_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='CGameServers_GetServerList_Response.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='CGameServers_GetServerList_Response.Server.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\265\030\036The server\'s IP and query port'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameport', full_name='CGameServers_GetServerList_Response.Server.gameport', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specport', full_name='CGameServers_GetServerList_Response.Server.specport', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CGameServers_GetServerList_Response.Server.steamid', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='CGameServers_GetServerList_Response.Server.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='CGameServers_GetServerList_Response.Server.appid', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gamedir', full_name='CGameServers_GetServerList_Response.Server.gamedir', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='CGameServers_GetServerList_Response.Server.version', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='CGameServers_GetServerList_Response.Server.product', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region', full_name='CGameServers_GetServerList_Response.Server.region', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='CGameServers_GetServerList_Response.Server.players', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_players', full_name='CGameServers_GetServerList_Response.Server.max_players', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bots', full_name='CGameServers_GetServerList_Response.Server.bots', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map', full_name='CGameServers_GetServerList_Response.Server.map', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secure', full_name='CGameServers_GetServerList_Response.Server.secure', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dedicated', full_name='CGameServers_GetServerList_Response.Server.dedicated', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='CGameServers_GetServerList_Response.Server.os', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gametype', full_name='CGameServers_GetServerList_Response.Server.gametype', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=712,
)

_CGAMESERVERS_GETSERVERLIST_RESPONSE = _descriptor.Descriptor(
  name='CGameServers_GetServerList_Response',
  full_name='CGameServers_GetServerList_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='CGameServers_GetServerList_Response.servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\265\030#List of servers matching the filter'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=712,
)


_CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST = _descriptor.Descriptor(
  name='CGameServers_GetServerSteamIDsByIP_Request',
  full_name='CGameServers_GetServerSteamIDsByIP_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_ips', full_name='CGameServers_GetServerSteamIDsByIP_Request.server_ips', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=778,
)


_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='CGameServers_IPsWithSteamIDs_Response.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='CGameServers_IPsWithSteamIDs_Response.Server.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CGameServers_IPsWithSteamIDs_Response.Server.steamid', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=886,
  serialized_end=925,
)

_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE = _descriptor.Descriptor(
  name='CGameServers_IPsWithSteamIDs_Response',
  full_name='CGameServers_IPsWithSteamIDs_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='CGameServers_IPsWithSteamIDs_Response.servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=781,
  serialized_end=925,
)


_CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST = _descriptor.Descriptor(
  name='CGameServers_GetServerIPsBySteamID_Request',
  full_name='CGameServers_GetServerIPsBySteamID_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_steamids', full_name='CGameServers_GetServerIPsBySteamID_Request.server_steamids', index=0,
      number=1, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=927,
  serialized_end=996,
)

_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER.containing_type = _CGAMESERVERS_GETSERVERLIST_RESPONSE
_CGAMESERVERS_GETSERVERLIST_RESPONSE.fields_by_name['servers'].message_type = _CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER
_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER.containing_type = _CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE
_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE.fields_by_name['servers'].message_type = _CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER
DESCRIPTOR.message_types_by_name['CGameServers_GetServerList_Request'] = _CGAMESERVERS_GETSERVERLIST_REQUEST
DESCRIPTOR.message_types_by_name['CGameServers_GetServerList_Response'] = _CGAMESERVERS_GETSERVERLIST_RESPONSE
DESCRIPTOR.message_types_by_name['CGameServers_GetServerSteamIDsByIP_Request'] = _CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST
DESCRIPTOR.message_types_by_name['CGameServers_IPsWithSteamIDs_Response'] = _CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE
DESCRIPTOR.message_types_by_name['CGameServers_GetServerIPsBySteamID_Request'] = _CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CGameServers_GetServerList_Request = _reflection.GeneratedProtocolMessageType('CGameServers_GetServerList_Request', (_message.Message,), dict(
  DESCRIPTOR = _CGAMESERVERS_GETSERVERLIST_REQUEST,
  __module__ = 'steammessages_gameservers_pb2'
  # @@protoc_insertion_point(class_scope:CGameServers_GetServerList_Request)
  ))
_sym_db.RegisterMessage(CGameServers_GetServerList_Request)

CGameServers_GetServerList_Response = _reflection.GeneratedProtocolMessageType('CGameServers_GetServerList_Response', (_message.Message,), dict(

  Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), dict(
    DESCRIPTOR = _CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER,
    __module__ = 'steammessages_gameservers_pb2'
    # @@protoc_insertion_point(class_scope:CGameServers_GetServerList_Response.Server)
    ))
  ,
  DESCRIPTOR = _CGAMESERVERS_GETSERVERLIST_RESPONSE,
  __module__ = 'steammessages_gameservers_pb2'
  # @@protoc_insertion_point(class_scope:CGameServers_GetServerList_Response)
  ))
_sym_db.RegisterMessage(CGameServers_GetServerList_Response)
_sym_db.RegisterMessage(CGameServers_GetServerList_Response.Server)

CGameServers_GetServerSteamIDsByIP_Request = _reflection.GeneratedProtocolMessageType('CGameServers_GetServerSteamIDsByIP_Request', (_message.Message,), dict(
  DESCRIPTOR = _CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST,
  __module__ = 'steammessages_gameservers_pb2'
  # @@protoc_insertion_point(class_scope:CGameServers_GetServerSteamIDsByIP_Request)
  ))
_sym_db.RegisterMessage(CGameServers_GetServerSteamIDsByIP_Request)

CGameServers_IPsWithSteamIDs_Response = _reflection.GeneratedProtocolMessageType('CGameServers_IPsWithSteamIDs_Response', (_message.Message,), dict(

  Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), dict(
    DESCRIPTOR = _CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER,
    __module__ = 'steammessages_gameservers_pb2'
    # @@protoc_insertion_point(class_scope:CGameServers_IPsWithSteamIDs_Response.Server)
    ))
  ,
  DESCRIPTOR = _CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE,
  __module__ = 'steammessages_gameservers_pb2'
  # @@protoc_insertion_point(class_scope:CGameServers_IPsWithSteamIDs_Response)
  ))
_sym_db.RegisterMessage(CGameServers_IPsWithSteamIDs_Response)
_sym_db.RegisterMessage(CGameServers_IPsWithSteamIDs_Response.Server)

CGameServers_GetServerIPsBySteamID_Request = _reflection.GeneratedProtocolMessageType('CGameServers_GetServerIPsBySteamID_Request', (_message.Message,), dict(
  DESCRIPTOR = _CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST,
  __module__ = 'steammessages_gameservers_pb2'
  # @@protoc_insertion_point(class_scope:CGameServers_GetServerIPsBySteamID_Request)
  ))
_sym_db.RegisterMessage(CGameServers_GetServerIPsBySteamID_Request)


DESCRIPTOR._options = None
_CGAMESERVERS_GETSERVERLIST_REQUEST.fields_by_name['filter']._options = None
_CGAMESERVERS_GETSERVERLIST_REQUEST.fields_by_name['limit']._options = None
_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER.fields_by_name['addr']._options = None
_CGAMESERVERS_GETSERVERLIST_RESPONSE.fields_by_name['servers']._options = None

_GAMESERVERS = _descriptor.ServiceDescriptor(
  name='GameServers',
  full_name='GameServers',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\202\265\0302A service for searching and managing game servers.'),
  serialized_start=999,
  serialized_end=1554,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerList',
    full_name='GameServers.GetServerList',
    index=0,
    containing_service=None,
    input_type=_CGAMESERVERS_GETSERVERLIST_REQUEST,
    output_type=_CGAMESERVERS_GETSERVERLIST_RESPONSE,
    serialized_options=_b('\202\265\030,Gets a list of servers given a filter string'),
  ),
  _descriptor.MethodDescriptor(
    name='GetServerSteamIDsByIP',
    full_name='GameServers.GetServerSteamIDsByIP',
    index=1,
    containing_service=None,
    input_type=_CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST,
    output_type=_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE,
    serialized_options=_b('\202\265\0302Gets a list of server SteamIDs given a list of IPs'),
  ),
  _descriptor.MethodDescriptor(
    name='GetServerIPsBySteamID',
    full_name='GameServers.GetServerIPsBySteamID',
    index=2,
    containing_service=None,
    input_type=_CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST,
    output_type=_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE,
    serialized_options=_b('\202\265\030;Gets a list of server IP addresses given a list of SteamIDs'),
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMESERVERS)

DESCRIPTOR.services_by_name['GameServers'] = _GAMESERVERS

GameServers = service_reflection.GeneratedServiceType('GameServers', (_service.Service,), dict(
  DESCRIPTOR = _GAMESERVERS,
  __module__ = 'steammessages_gameservers_pb2'
  ))

GameServers_Stub = service_reflection.GeneratedServiceStubType('GameServers_Stub', (GameServers,), dict(
  DESCRIPTOR = _GAMESERVERS,
  __module__ = 'steammessages_gameservers_pb2'
  ))


# @@protoc_insertion_point(module_scope)
