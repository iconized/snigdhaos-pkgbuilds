from _typeshed import OptExcInfo, StrOrBytesPath
from collections.abc import Callable
from types import FrameType, TracebackType
from typing import IO, Any, Final

__UNDEF__: Final[object]  # undocumented sentinel

def reset() -> str: ...  # undocumented
def small(text: str) -> str: ...  # undocumented
def strong(text: str) -> str: ...  # undocumented
def grey(text: str) -> str: ...  # undocumented
def lookup(name: str, frame: FrameType, locals: dict[str, Any]) -> tuple[str | None, Any]: ...  # undocumented
def scanvars(
    reader: Callable[[], bytes], frame: FrameType, locals: dict[str, Any]
) -> list[tuple[str, str | None, Any]]: ...  # undocumented
def html(einfo: OptExcInfo, context: int = 5) -> str: ...
def text(einfo: OptExcInfo, context: int = 5) -> str: ...

class Hook:  # undocumented
    def __init__(
        self,
        display: int = 1,
        logdir: StrOrBytesPath | None = None,
        context: int = 5,
        file: IO[str] | None = None,
        format: str = "html",
    ) -> None: ...
    def __call__(self, etype: type[BaseException] | None, evalue: BaseException | None, etb: TracebackType | None) -> None: ...
    def handle(self, info: OptExcInfo | None = None) -> None: ...

def handler(info: OptExcInfo | None = None) -> None: ...
def enable(display: int = 1, logdir: StrOrBytesPath | None = None, context: int = 5, format: str = "html") -> None: ...
