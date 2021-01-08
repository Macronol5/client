# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TelemetryRecord(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    python_version: typing___Text = ...
    cli_version: typing___Text = ...
    huggingface_version: typing___Text = ...
    framework: typing___Text = ...

    @property
    def imports_init(self) -> type___Imports: ...

    @property
    def imports_finish(self) -> type___Imports: ...

    @property
    def feature(self) -> type___Feature: ...

    @property
    def env(self) -> type___Env: ...

    def __init__(self,
        *,
        imports_init : typing___Optional[type___Imports] = None,
        imports_finish : typing___Optional[type___Imports] = None,
        feature : typing___Optional[type___Feature] = None,
        python_version : typing___Optional[typing___Text] = None,
        cli_version : typing___Optional[typing___Text] = None,
        huggingface_version : typing___Optional[typing___Text] = None,
        framework : typing___Optional[typing___Text] = None,
        env : typing___Optional[type___Env] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"env",b"env",u"feature",b"feature",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cli_version",b"cli_version",u"env",b"env",u"feature",b"feature",u"framework",b"framework",u"huggingface_version",b"huggingface_version",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init",u"python_version",b"python_version"]) -> None: ...
type___TelemetryRecord = TelemetryRecord

class Imports(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    torch: builtin___bool = ...
    keras: builtin___bool = ...
    tensorflow: builtin___bool = ...
    fastai: builtin___bool = ...
    sklearn: builtin___bool = ...
    xgboost: builtin___bool = ...
    catboost: builtin___bool = ...
    lightgbm: builtin___bool = ...
    pytorch_lightning: builtin___bool = ...
    pytorch_ignite: builtin___bool = ...
    transformers: builtin___bool = ...

    def __init__(self,
        *,
        torch : typing___Optional[builtin___bool] = None,
        keras : typing___Optional[builtin___bool] = None,
        tensorflow : typing___Optional[builtin___bool] = None,
        fastai : typing___Optional[builtin___bool] = None,
        sklearn : typing___Optional[builtin___bool] = None,
        xgboost : typing___Optional[builtin___bool] = None,
        catboost : typing___Optional[builtin___bool] = None,
        lightgbm : typing___Optional[builtin___bool] = None,
        pytorch_lightning : typing___Optional[builtin___bool] = None,
        pytorch_ignite : typing___Optional[builtin___bool] = None,
        transformers : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"catboost",b"catboost",u"fastai",b"fastai",u"keras",b"keras",u"lightgbm",b"lightgbm",u"pytorch_ignite",b"pytorch_ignite",u"pytorch_lightning",b"pytorch_lightning",u"sklearn",b"sklearn",u"tensorflow",b"tensorflow",u"torch",b"torch",u"transformers",b"transformers",u"xgboost",b"xgboost"]) -> None: ...
type___Imports = Imports

class Feature(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    watch: builtin___bool = ...
    finish: builtin___bool = ...
    save: builtin___bool = ...

    def __init__(self,
        *,
        watch : typing___Optional[builtin___bool] = None,
        finish : typing___Optional[builtin___bool] = None,
        save : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"finish",b"finish",u"save",b"save",u"watch",b"watch"]) -> None: ...
type___Feature = Feature

class Env(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    jupyter: builtin___bool = ...
    kaggle: builtin___bool = ...

    def __init__(self,
        *,
        jupyter : typing___Optional[builtin___bool] = None,
        kaggle : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"jupyter",b"jupyter",u"kaggle",b"kaggle"]) -> None: ...
type___Env = Env
