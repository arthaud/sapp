from typing import Any, Callable, Optional

from .base import class_mapper as class_mapper
from .interfaces import InspectionAttr

NO_ATTRIBUTE: Any = ...

class Mapper(InspectionAttr):
    class_: Any = ...
    class_manager: Any = ...
    non_primary: Any = ...
    order_by: Any = ...
    always_refresh: Any = ...
    version_id_prop: Any = ...
    version_id_col: Any = ...
    version_id_generator: bool = ...
    concrete: Any = ...
    single: bool = ...
    inherits: Any = ...
    local_table: Any = ...
    inherit_condition: Any = ...
    inherit_foreign_keys: Any = ...
    batch: Any = ...
    eager_defaults: Any = ...
    column_prefix: Any = ...
    polymorphic_on: Any = ...
    validators: Any = ...
    passive_updates: Any = ...
    passive_deletes: Any = ...
    legacy_is_orphan: Any = ...
    allow_partial_pks: Any = ...
    confirm_deleted_rows: bool = ...
    with_polymorphic: Any = ...
    polymorphic_identity: Any = ...
    polymorphic_map: Any = ...
    include_properties: Any = ...
    exclude_properties: Any = ...
    configured: bool = ...
    def __init__(
        self,
        class_,
        local_table: Optional[Any] = ...,
        properties: Optional[Any] = ...,
        primary_key: Optional[Any] = ...,
        non_primary: bool = ...,
        inherits: Optional[Any] = ...,
        inherit_condition: Optional[Any] = ...,
        inherit_foreign_keys: Optional[Any] = ...,
        extension: Optional[Any] = ...,
        order_by: bool = ...,
        always_refresh: bool = ...,
        version_id_col: Optional[Any] = ...,
        version_id_generator: Optional[Any] = ...,
        polymorphic_on: Optional[Any] = ...,
        _polymorphic_map: Optional[Any] = ...,
        polymorphic_identity: Optional[Any] = ...,
        concrete: bool = ...,
        with_polymorphic: Optional[Any] = ...,
        allow_partial_pks: bool = ...,
        batch: bool = ...,
        column_prefix: Optional[Any] = ...,
        include_properties: Optional[Any] = ...,
        exclude_properties: Optional[Any] = ...,
        passive_updates: bool = ...,
        passive_deletes: bool = ...,
        confirm_deleted_rows: bool = ...,
        eager_defaults: bool = ...,
        legacy_is_orphan: bool = ...,
        _compiled_cache_size: int = ...,
    ) -> None: ...
    is_mapper: bool = ...
    @property
    def mapper(self): ...
    @property
    def entity(self): ...
    mapped_table: Any = ...
    tables: Any = ...
    primary_key: Any = ...
    base_mapper: Any = ...
    columns: Any = ...
    c: Any = ...
    def dispose(self): ...
    def add_properties(self, dict_of_properties): ...
    def add_property(self, key, prop): ...
    def has_property(self, key): ...
    def get_property(self, key, _configure_mappers: bool = ...): ...
    def get_property_by_column(self, column): ...
    @property
    def iterate_properties(self): ...
    with_polymorphic_mappers: Any = ...
    @property
    def selectable(self): ...
    def attrs(self): ...
    def all_orm_descriptors(self): ...
    def synonyms(self): ...
    def column_attrs(self): ...
    def relationships(self): ...
    def composites(self): ...
    def common_parent(self, other): ...
    def isa(self, other): ...
    def iterate_to_root(self): ...
    def self_and_descendants(self): ...
    def polymorphic_iterator(self): ...
    def primary_mapper(self): ...
    @property
    def primary_base_mapper(self): ...
    def identity_key_from_row(self, row, adapter: Optional[Any] = ...): ...
    def identity_key_from_primary_key(self, primary_key): ...
    def identity_key_from_instance(self, instance): ...
    def primary_key_from_instance(self, instance): ...
    def cascade_iterator(self, type_, state, halt_on: Optional[Any] = ...): ...

def configure_mappers(): ...
def reconstructor(fn): ...
def validates(*names, **kw) -> Callable[..., Any]: ...

class _ColumnMapping(dict):
    mapper: Any = ...
    def __init__(self, mapper) -> None: ...
    def __missing__(self, column): ...
