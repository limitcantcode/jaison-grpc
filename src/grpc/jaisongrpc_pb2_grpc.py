# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import jaisongrpc_pb2 as jaisongrpc__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in jaisongrpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class STTComponentStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.invoke = channel.unary_stream(
                '/jaisongrpc.STTComponentStreamer/invoke',
                request_serializer=jaisongrpc__pb2.STTComponentRequest.SerializeToString,
                response_deserializer=jaisongrpc__pb2.STTComponentResponse.FromString,
                _registered_method=True)


class STTComponentStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_STTComponentStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'invoke': grpc.unary_stream_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=jaisongrpc__pb2.STTComponentRequest.FromString,
                    response_serializer=jaisongrpc__pb2.STTComponentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jaisongrpc.STTComponentStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('jaisongrpc.STTComponentStreamer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class STTComponentStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/jaisongrpc.STTComponentStreamer/invoke',
            jaisongrpc__pb2.STTComponentRequest.SerializeToString,
            jaisongrpc__pb2.STTComponentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class T2TComponentStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.invoke = channel.unary_stream(
                '/jaisongrpc.T2TComponentStreamer/invoke',
                request_serializer=jaisongrpc__pb2.T2TComponentRequest.SerializeToString,
                response_deserializer=jaisongrpc__pb2.T2TComponentResponse.FromString,
                _registered_method=True)


class T2TComponentStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_T2TComponentStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'invoke': grpc.unary_stream_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=jaisongrpc__pb2.T2TComponentRequest.FromString,
                    response_serializer=jaisongrpc__pb2.T2TComponentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jaisongrpc.T2TComponentStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('jaisongrpc.T2TComponentStreamer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class T2TComponentStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/jaisongrpc.T2TComponentStreamer/invoke',
            jaisongrpc__pb2.T2TComponentRequest.SerializeToString,
            jaisongrpc__pb2.T2TComponentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TTSGComponentStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.invoke = channel.unary_stream(
                '/jaisongrpc.TTSGComponentStreamer/invoke',
                request_serializer=jaisongrpc__pb2.TTSGComponentRequest.SerializeToString,
                response_deserializer=jaisongrpc__pb2.TTSGComponentResponse.FromString,
                _registered_method=True)


class TTSGComponentStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TTSGComponentStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'invoke': grpc.unary_stream_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=jaisongrpc__pb2.TTSGComponentRequest.FromString,
                    response_serializer=jaisongrpc__pb2.TTSGComponentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jaisongrpc.TTSGComponentStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('jaisongrpc.TTSGComponentStreamer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TTSGComponentStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/jaisongrpc.TTSGComponentStreamer/invoke',
            jaisongrpc__pb2.TTSGComponentRequest.SerializeToString,
            jaisongrpc__pb2.TTSGComponentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TTSCComponentStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.invoke = channel.unary_stream(
                '/jaisongrpc.TTSCComponentStreamer/invoke',
                request_serializer=jaisongrpc__pb2.TTSCComponentRequest.SerializeToString,
                response_deserializer=jaisongrpc__pb2.TTSCComponentResponse.FromString,
                _registered_method=True)


class TTSCComponentStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TTSCComponentStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'invoke': grpc.unary_stream_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=jaisongrpc__pb2.TTSCComponentRequest.FromString,
                    response_serializer=jaisongrpc__pb2.TTSCComponentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jaisongrpc.TTSCComponentStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('jaisongrpc.TTSCComponentStreamer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TTSCComponentStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/jaisongrpc.TTSCComponentStreamer/invoke',
            jaisongrpc__pb2.TTSCComponentRequest.SerializeToString,
            jaisongrpc__pb2.TTSCComponentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
