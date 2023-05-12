from collections.abc import Callable, Iterable, Sequence
from logging import Logger
from socket import socket
from threading import Condition, Event, Lock, Thread
from types import ModuleType
from typing import Any, Protocol
from typing_extensions import TypeAlias

from paramiko.auth_handler import AuthHandler, _InteractiveCallback
from paramiko.channel import Channel
from paramiko.message import Message
from paramiko.packet import Packetizer
from paramiko.pkey import PKey
from paramiko.server import ServerInterface, SubsystemHandler
from paramiko.sftp_client import SFTPClient
from paramiko.ssh_gss import _SSH_GSSAuth
from paramiko.util import ClosingContextManager

_Addr: TypeAlias = tuple[str, int]
_SocketLike: TypeAlias = str | _Addr | socket | Channel

class _KexEngine(Protocol):
    def start_kex(self) -> None: ...
    def parse_next(self, ptype: int, m: Message) -> None: ...

class Transport(Thread, ClosingContextManager):
    active: bool
    hostname: str | None
    sock: socket | Channel
    packetizer: Packetizer
    local_version: str
    remote_version: str
    local_cipher: str
    local_kex_init: bytes | None
    local_mac: str | None
    local_compression: str | None
    session_id: bytes | None
    host_key_type: str | None
    host_key: PKey | None
    use_gss_kex: bool
    gss_kex_used: bool
    kexgss_ctxt: _SSH_GSSAuth | None
    gss_host: str
    kex_engine: _KexEngine | None
    H: bytes | None
    K: int | None
    initial_kex_done: bool
    in_kex: bool
    authenticated: bool
    lock: Lock
    channel_events: dict[int, Event]
    channels_seen: dict[int, bool]
    default_max_packet_size: int
    default_window_size: int
    saved_exception: Exception | None
    clear_to_send: Event
    clear_to_send_lock: Lock
    clear_to_send_timeout: float
    log_name: str
    logger: Logger
    auth_handler: AuthHandler | None
    global_response: Message | None
    completion_event: Event | None
    banner_timeout: float
    handshake_timeout: float
    auth_timeout: float
    disabled_algorithms: dict[str, Iterable[str]] | None
    server_mode: bool
    server_object: ServerInterface | None
    server_key_dict: dict[str, PKey]
    server_accepts: list[Channel]
    server_accept_cv: Condition
    subsystem_table: dict[str, tuple[type[SubsystemHandler], tuple[Any, ...], dict[str, Any]]]
    sys: ModuleType
    def __init__(
        self,
        sock: _SocketLike,
        default_window_size: int = 2097152,
        default_max_packet_size: int = 32768,
        gss_kex: bool = False,
        gss_deleg_creds: bool = True,
        disabled_algorithms: dict[str, Iterable[str]] | None = None,
        server_sig_algs: bool = True,
    ) -> None: ...
    @property
    def preferred_ciphers(self) -> Sequence[str]: ...
    @property
    def preferred_macs(self) -> Sequence[str]: ...
    @property
    def preferred_keys(self) -> Sequence[str]: ...
    @property
    def preferred_kex(self) -> Sequence[str]: ...
    @property
    def preferred_compression(self) -> Sequence[str]: ...
    def atfork(self) -> None: ...
    def get_security_options(self) -> SecurityOptions: ...
    def set_gss_host(self, gss_host: str | None, trust_dns: bool = True, gssapi_requested: bool = True) -> None: ...
    def start_client(self, event: Event | None = None, timeout: float | None = None) -> None: ...
    def start_server(self, event: Event | None = None, server: ServerInterface | None = None) -> None: ...
    def add_server_key(self, key: PKey) -> None: ...
    def get_server_key(self) -> PKey | None: ...
    @staticmethod
    def load_server_moduli(filename: str | None = None) -> bool: ...
    def close(self) -> None: ...
    def get_remote_server_key(self) -> PKey: ...
    def is_active(self) -> bool: ...
    def open_session(
        self, window_size: int | None = None, max_packet_size: int | None = None, timeout: float | None = None
    ) -> Channel: ...
    def open_x11_channel(self, src_addr: _Addr | None = None) -> Channel: ...
    def open_forward_agent_channel(self) -> Channel: ...
    def open_forwarded_tcpip_channel(self, src_addr: _Addr, dest_addr: _Addr) -> Channel: ...
    def open_channel(
        self,
        kind: str,
        dest_addr: _Addr | None = None,
        src_addr: _Addr | None = None,
        window_size: int | None = None,
        max_packet_size: int | None = None,
        timeout: float | None = None,
    ) -> Channel: ...
    def request_port_forward(
        self, address: str, port: int, handler: Callable[[Channel, _Addr, _Addr], object] | None = None
    ) -> int: ...
    def cancel_port_forward(self, address: str, port: int) -> None: ...
    def open_sftp_client(self) -> SFTPClient | None: ...
    def send_ignore(self, byte_count: int | None = None) -> None: ...
    def renegotiate_keys(self) -> None: ...
    def set_keepalive(self, interval: int) -> None: ...
    def global_request(self, kind: str, data: Iterable[Any] | None = None, wait: bool = True) -> Message | None: ...
    def accept(self, timeout: float | None = None) -> Channel | None: ...
    def connect(
        self,
        hostkey: PKey | None = None,
        username: str = "",
        password: str | None = None,
        pkey: PKey | None = None,
        gss_host: str | None = None,
        gss_auth: bool = False,
        gss_kex: bool = False,
        gss_deleg_creds: bool = True,
        gss_trust_dns: bool = True,
    ) -> None: ...
    def get_exception(self) -> Exception | None: ...
    def set_subsystem_handler(self, name: str, handler: type[SubsystemHandler], *larg: Any, **kwarg: Any) -> None: ...
    def is_authenticated(self) -> bool: ...
    def get_username(self) -> str | None: ...
    def get_banner(self) -> bytes | None: ...
    def auth_none(self, username: str) -> list[str]: ...
    def auth_password(self, username: str, password: str, event: Event | None = None, fallback: bool = True) -> list[str]: ...
    def auth_publickey(self, username: str, key: PKey, event: Event | None = None) -> list[str]: ...
    def auth_interactive(self, username: str, handler: _InteractiveCallback, submethods: str = "") -> list[str]: ...
    def auth_interactive_dumb(
        self, username: str, handler: _InteractiveCallback | None = None, submethods: str = ""
    ) -> list[str]: ...
    def auth_gssapi_with_mic(self, username: str, gss_host: str, gss_deleg_creds: bool) -> list[str]: ...
    def auth_gssapi_keyex(self, username: str) -> list[str]: ...
    def set_log_channel(self, name: str) -> None: ...
    def get_log_channel(self) -> str: ...
    def set_hexdump(self, hexdump: bool) -> None: ...
    def get_hexdump(self) -> bool: ...
    def use_compression(self, compress: bool = True) -> None: ...
    def getpeername(self) -> tuple[str, int]: ...
    def stop_thread(self) -> None: ...
    def run(self) -> None: ...

class SecurityOptions:
    def __init__(self, transport: Transport) -> None: ...
    @property
    def ciphers(self) -> Sequence[str]: ...
    @ciphers.setter
    def ciphers(self, x: Sequence[str]) -> None: ...
    @property
    def digests(self) -> Sequence[str]: ...
    @digests.setter
    def digests(self, x: Sequence[str]) -> None: ...
    @property
    def key_types(self) -> Sequence[str]: ...
    @key_types.setter
    def key_types(self, x: Sequence[str]) -> None: ...
    @property
    def kex(self) -> Sequence[str]: ...
    @kex.setter
    def kex(self, x: Sequence[str]) -> None: ...
    @property
    def compression(self) -> Sequence[str]: ...
    @compression.setter
    def compression(self, x: Sequence[str]) -> None: ...

class ChannelMap:
    def __init__(self) -> None: ...
    def put(self, chanid: int, chan: Channel) -> None: ...
    def get(self, chanid: int) -> Channel: ...
    def delete(self, chanid: int) -> None: ...
    def values(self) -> list[Channel]: ...
    def __len__(self) -> int: ...
