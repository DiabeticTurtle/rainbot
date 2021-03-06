# Stubs for pymongo.change_stream (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from bson.timestamp import Timestamp
from pymongo.collation import Collation
from pymongo.client_session import ClientSession
from typing import Any, Mapping, Optional, Sequence

class ChangeStream:
    def __init__(
        self,
        target: Any,
        pipeline: Optional[Sequence[Mapping[str, Any]]],
        full_document: str,
        resume_after: Optional[str],
        max_await_time_ms: Optional[int],
        batch_size: Optional[int],
        collation: Optional[Collation],
        start_at_operation_time: Optional[Timestamp],
        session: Optional[ClientSession]) -> None: ...
    def close(self) -> None: ...
    def __iter__(self) -> ChangeStream: ...
    def next(self) -> Mapping[str, Any]: ...
    def __next__(self) -> Mapping[str, Any]: ...
    def __enter__(self) -> ChangeStream: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class CollectionChangeStream(ChangeStream): ...
class DatabaseChangeStream(ChangeStream): ...
class ClusterChangeStream(DatabaseChangeStream): ...
