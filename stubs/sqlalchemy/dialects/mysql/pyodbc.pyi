# Stubs for sqlalchemy.dialects.mysql.pyodbc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from ...connectors.pyodbc import PyODBCConnector as PyODBCConnector
from .base import MySQLDialect as MySQLDialect
from .base import MySQLExecutionContext as MySQLExecutionContext

class MySQLExecutionContext_pyodbc(MySQLExecutionContext):
    def get_lastrowid(self): ...

class MySQLDialect_pyodbc(PyODBCConnector, MySQLDialect):
    supports_unicode_statements: bool = ...
    execution_ctx_cls: Any = ...
    pyodbc_driver_name: str = ...
    def __init__(self, **kw) -> None: ...

dialect: Any = ...
