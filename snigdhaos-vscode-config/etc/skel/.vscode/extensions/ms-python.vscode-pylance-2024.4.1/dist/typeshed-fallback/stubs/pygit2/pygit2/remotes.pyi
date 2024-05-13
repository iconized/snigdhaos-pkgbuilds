from collections.abc import Iterator
from typing import Literal, TypedDict
from typing_extensions import TypeAlias

from _cffi_backend import _CDataBase

from ._pygit2 import Oid
from .callbacks import RemoteCallbacks
from .enums import FetchPrune
from .refspec import Refspec
from .repository import BaseRepository
from .utils import _IntoStrArray

class TransferProgress:
    total_objects: int
    indexed_objects: int
    received_objects: int
    local_objects: int
    total_deltas: int
    indexed_deltas: int
    received_bytes: int
    def __init__(self, tp: _CDataBase) -> None: ...

_ProxySpec: TypeAlias = Literal[True] | str | None

class _LsRemotesResultEntry(TypedDict):
    local: bool
    loid: Oid | None
    name: str | None
    symref_target: str | None
    oid: Oid

class Remote:
    def __init__(self, repo: BaseRepository, ptr: _CDataBase) -> None: ...
    def __del__(self) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def url(self) -> str | None: ...
    @property
    def push_url(self) -> str | None: ...
    def connect(self, callbacks: RemoteCallbacks | None = None, direction: int = 0, proxy: _ProxySpec = None) -> None: ...
    def fetch(
        self,
        refspecs: _IntoStrArray = None,
        message: bytes | str | None = None,
        callbacks: RemoteCallbacks | None = None,
        prune: FetchPrune = ...,
        proxy: _ProxySpec = None,
        depth: int = 0,
    ) -> TransferProgress: ...
    def ls_remotes(self, callbacks: RemoteCallbacks | None = None, proxy: _ProxySpec = None) -> list[_LsRemotesResultEntry]: ...
    def prune(self, callbacks: RemoteCallbacks | None = None) -> None: ...
    @property
    def refspec_count(self) -> int: ...
    def get_refspec(self, n: int) -> Refspec: ...
    @property
    def fetch_refspecs(self) -> list[str]: ...
    @property
    def push_refspecs(self) -> list[str]: ...
    def push(self, specs: _IntoStrArray, callbacks: RemoteCallbacks | None = None, proxy: _ProxySpec = None) -> None: ...

_RemoteName: TypeAlias = bytes | str

class RemoteCollection:
    def __init__(self, repo: BaseRepository) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Remote]: ...
    def __getitem__(self, name: int | _RemoteName) -> Remote: ...
    def names(self) -> Iterator[str | None]: ...
    def create(self, name: _RemoteName, url: bytes | str, fetch: bytes | str | None = None) -> Remote: ...
    def create_anonymous(self, url: bytes | str) -> Remote: ...
    def rename(self, name: _RemoteName, new_name: bytes | str) -> list[str]: ...
    def delete(self, name: _RemoteName) -> None: ...
    def set_url(self, name: _RemoteName, url: bytes | str) -> None: ...
    def set_push_url(self, name: _RemoteName, url: bytes | str) -> None: ...
    def add_fetch(self, name: _RemoteName, refspec: bytes | str) -> None: ...
    def add_push(self, name: _RemoteName, refspec: bytes | str) -> None: ...
