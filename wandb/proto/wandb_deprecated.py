# Generated by wandb/proto/wandb_internal_codegen.py.  DO NOT EDIT!


import sys


if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


DEPRECATED_FEATURES = Literal[
    "keras_callback__data_type",
    "run__mode",
    "run__save_no_args",
    "run__join"
]


class Deprecated:
    keras_callback__data_type: DEPRECATED_FEATURES = "keras_callback__data_type"
    run__mode: DEPRECATED_FEATURES = "run__mode"
    run__save_no_args: DEPRECATED_FEATURES = "run__save_no_args"
    run__join: DEPRECATED_FEATURES = "run__join"
