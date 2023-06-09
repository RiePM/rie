from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class SmartTag(Serialisable):
    tagname: str
    namespaceUri: Incomplete
    name: Incomplete
    url: Incomplete
    def __init__(
        self, namespaceUri: Incomplete | None = None, name: Incomplete | None = None, url: Incomplete | None = None
    ) -> None: ...

class SmartTagList(Serialisable):
    tagname: str
    smartTagType: Incomplete
    __elements__: Incomplete
    def __init__(self, smartTagType=()) -> None: ...

class SmartTagProperties(Serialisable):
    tagname: str
    embed: Incomplete
    show: Incomplete
    def __init__(self, embed: Incomplete | None = None, show: Incomplete | None = None) -> None: ...
