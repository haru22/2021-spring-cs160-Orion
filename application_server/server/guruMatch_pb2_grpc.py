# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import guruMatch_pb2 as guruMatch__pb2


class GuruMatchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/guruMatchPackage.GuruMatch/CreateUser',
                request_serializer=guruMatch__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=guruMatch__pb2.SuccessResponse.FromString,
                )
        self.CreateInterests = channel.unary_unary(
                '/guruMatchPackage.GuruMatch/CreateInterests',
                request_serializer=guruMatch__pb2.CreateInterestsRequest.SerializeToString,
                response_deserializer=guruMatch__pb2.SuccessResponse.FromString,
                )


class GuruMatchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInterests(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GuruMatchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=guruMatch__pb2.CreateUserRequest.FromString,
                    response_serializer=guruMatch__pb2.SuccessResponse.SerializeToString,
            ),
            'CreateInterests': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInterests,
                    request_deserializer=guruMatch__pb2.CreateInterestsRequest.FromString,
                    response_serializer=guruMatch__pb2.SuccessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'guruMatchPackage.GuruMatch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GuruMatch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/guruMatchPackage.GuruMatch/CreateUser',
            guruMatch__pb2.CreateUserRequest.SerializeToString,
            guruMatch__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateInterests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/guruMatchPackage.GuruMatch/CreateInterests',
            guruMatch__pb2.CreateInterestsRequest.SerializeToString,
            guruMatch__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
