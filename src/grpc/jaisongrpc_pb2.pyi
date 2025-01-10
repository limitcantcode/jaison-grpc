from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class STTComponentRequest(_message.Message):
    __slots__ = ("run_id", "audio")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    audio: bytes
    def __init__(self, run_id: _Optional[str] = ..., audio: _Optional[bytes] = ...) -> None: ...

class STTComponentResponse(_message.Message):
    __slots__ = ("run_id", "content_chunk")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    content_chunk: str
    def __init__(self, run_id: _Optional[str] = ..., content_chunk: _Optional[str] = ...) -> None: ...

class T2TComponentRequest(_message.Message):
    __slots__ = ("run_id", "system_input", "user_input")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INPUT_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    system_input: str
    user_input: str
    def __init__(self, run_id: _Optional[str] = ..., system_input: _Optional[str] = ..., user_input: _Optional[str] = ...) -> None: ...

class T2TComponentResponse(_message.Message):
    __slots__ = ("run_id", "content_chunk")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    content_chunk: str
    def __init__(self, run_id: _Optional[str] = ..., content_chunk: _Optional[str] = ...) -> None: ...

class TTSGComponentRequest(_message.Message):
    __slots__ = ("run_id", "content")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    content: str
    def __init__(self, run_id: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class TTSGComponentResponse(_message.Message):
    __slots__ = ("run_id", "audio_chunk")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHUNK_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    audio_chunk: bytes
    def __init__(self, run_id: _Optional[str] = ..., audio_chunk: _Optional[bytes] = ...) -> None: ...

class TTSCComponentRequest(_message.Message):
    __slots__ = ("run_id", "audio")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    audio: bytes
    def __init__(self, run_id: _Optional[str] = ..., audio: _Optional[bytes] = ...) -> None: ...

class TTSCComponentResponse(_message.Message):
    __slots__ = ("run_id", "audio_chunk")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHUNK_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    audio_chunk: bytes
    def __init__(self, run_id: _Optional[str] = ..., audio_chunk: _Optional[bytes] = ...) -> None: ...
