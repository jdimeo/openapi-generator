# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class NullableClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class integer_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, decimal.Decimal, ]),
        schemas.IntBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[int, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'integer_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class number_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, decimal.Decimal, ]),
        schemas.NumberBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[float, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'number_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class boolean_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, schemas.BoolClass, ]),
        schemas.BoolBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[bool, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'boolean_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class string_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
        schemas.StrBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[str, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'string_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class date_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
        schemas.DateBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'date_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class datetime_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
        schemas.DateTimeBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'datetime_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_nullable_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[tuple, schemas.NoneClass, ]),
        schemas.ListBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[list, tuple, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'array_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_and_items_nullable_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[tuple, schemas.NoneClass, ]),
        schemas.ListBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[list, tuple, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'array_and_items_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_items_nullable(
        schemas.ListSchema
    ):
        
        
        class _items(
            schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
            schemas.DictBase,
            schemas.NoneBase,
            schemas.Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Type[schemas.Schema],
            ) -> '_items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    
    class object_nullable_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
        schemas.DictBase,
        schemas.NoneBase,
        schemas.Schema
    ):
        _additional_properties = schemas.DictSchema
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'object_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class object_and_items_nullable_prop(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
        schemas.DictBase,
        schemas.NoneBase,
        schemas.Schema
    ):
        
        
        class _additional_properties(
            schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
            schemas.DictBase,
            schemas.NoneBase,
            schemas.Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Type[schemas.Schema],
            ) -> '_additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'object_and_items_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class object_items_nullable(
        schemas.DictSchema
    ):
        
        
        class _additional_properties(
            schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
            schemas.DictBase,
            schemas.NoneBase,
            schemas.Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Type[schemas.Schema],
            ) -> '_additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'object_items_nullable':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class _additional_properties(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
        schemas.DictBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> '_additional_properties':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        integer_prop: typing.Union[integer_prop, schemas.Unset] = schemas.unset,
        number_prop: typing.Union[number_prop, schemas.Unset] = schemas.unset,
        boolean_prop: typing.Union[boolean_prop, schemas.Unset] = schemas.unset,
        string_prop: typing.Union[string_prop, schemas.Unset] = schemas.unset,
        date_prop: typing.Union[date_prop, schemas.Unset] = schemas.unset,
        datetime_prop: typing.Union[datetime_prop, schemas.Unset] = schemas.unset,
        array_nullable_prop: typing.Union[array_nullable_prop, schemas.Unset] = schemas.unset,
        array_and_items_nullable_prop: typing.Union[array_and_items_nullable_prop, schemas.Unset] = schemas.unset,
        array_items_nullable: typing.Union[array_items_nullable, schemas.Unset] = schemas.unset,
        object_nullable_prop: typing.Union[object_nullable_prop, schemas.Unset] = schemas.unset,
        object_and_items_nullable_prop: typing.Union[object_and_items_nullable_prop, schemas.Unset] = schemas.unset,
        object_items_nullable: typing.Union[object_items_nullable, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Type[schemas.Schema],
    ) -> 'NullableClass':
        return super().__new__(
            cls,
            *args,
            integer_prop=integer_prop,
            number_prop=number_prop,
            boolean_prop=boolean_prop,
            string_prop=string_prop,
            date_prop=date_prop,
            datetime_prop=datetime_prop,
            array_nullable_prop=array_nullable_prop,
            array_and_items_nullable_prop=array_and_items_nullable_prop,
            array_items_nullable=array_items_nullable,
            object_nullable_prop=object_nullable_prop,
            object_and_items_nullable_prop=object_and_items_nullable_prop,
            object_items_nullable=object_items_nullable,
            _configuration=_configuration,
            **kwargs,
        )
