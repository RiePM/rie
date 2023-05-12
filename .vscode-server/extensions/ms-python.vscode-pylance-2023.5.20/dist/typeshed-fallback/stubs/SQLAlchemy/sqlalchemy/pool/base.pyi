from _typeshed import Incomplete
from _typeshed.dbapi import DBAPIConnection
from collections.abc import Callable
from typing import Any

from .. import log
from ..util import memoized_property

reset_rollback: Any
reset_commit: Any
reset_none: Any

class _ConnDialect:
    is_async: bool
    def do_rollback(self, dbapi_connection) -> None: ...
    def do_commit(self, dbapi_connection) -> None: ...
    def do_close(self, dbapi_connection) -> None: ...
    def do_ping(self, dbapi_connection) -> None: ...
    def get_driver_connection(self, connection): ...

class _AsyncConnDialect(_ConnDialect):
    is_async: bool

class Pool(log.Identified):
    logging_name: Any
    echo: Any
    def __init__(
        self,
        creator: Callable[[], DBAPIConnection],
        recycle: int = -1,
        echo: Incomplete | None = None,
        logging_name: Incomplete | None = None,
        reset_on_return: bool = True,
        events: Incomplete | None = None,
        dialect: Incomplete | None = None,
        pre_ping: bool = False,
        _dispatch: Incomplete | None = None,
    ) -> None: ...
    def recreate(self) -> None: ...
    def dispose(self) -> None: ...
    def connect(self): ...
    def status(self) -> None: ...

class _ConnectionRecord:
    finalize_callback: Any
    def __init__(self, pool, connect: bool = True) -> None: ...
    fresh: bool
    fairy_ref: Any
    starttime: Any
    dbapi_connection: Any
    @property
    def driver_connection(self): ...
    @property
    def connection(self): ...
    @connection.setter
    def connection(self, value) -> None: ...
    @memoized_property
    def info(self): ...
    @memoized_property
    def record_info(self): ...
    @classmethod
    def checkout(cls, pool): ...
    def checkin(self, _fairy_was_created: bool = True) -> None: ...
    @property
    def in_use(self): ...
    @property
    def last_connect_time(self): ...
    def close(self) -> None: ...
    def invalidate(self, e: Incomplete | None = None, soft: bool = False) -> None: ...
    def get_connection(self): ...

class _ConnectionFairy:
    dbapi_connection: Any
    def __init__(self, dbapi_connection, connection_record, echo) -> None: ...
    @property
    def driver_connection(self): ...
    @property
    def connection(self): ...
    @connection.setter
    def connection(self, value) -> None: ...
    @property
    def is_valid(self): ...
    @memoized_property
    def info(self): ...
    @property
    def record_info(self): ...
    def invalidate(self, e: Incomplete | None = None, soft: bool = False) -> None: ...
    def cursor(self, *args, **kwargs): ...
    def __getattr__(self, key: str): ...
    def detach(self) -> None: ...
    def close(self) -> None: ...