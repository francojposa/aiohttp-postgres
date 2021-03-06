from typing import Dict, Mapping, Type

from marshmallow import Schema, post_dump


class BaseSchema(Schema):
    """Base Serializer"""

    class Meta:
        """Meta data for BaseSchema."""

        ordered = True
        strict = True
        record_type = None

        patchable_fields = []

    @post_dump
    def tag_record_type(self, data, **kwargs):
        """Adds record type metadata post-dump."""
        data["record_type"] = self.Meta.record_type
        return data


class BaseHTTPAdapter:
    def __init__(self, schema: BaseSchema, usecase_class: Type):
        self.schema = schema
        self.usecase_class: Type = usecase_class

    def mapping_to_usecase(self, mapping: Mapping):
        usecase_data: Dict = self.schema.load(mapping)
        return self.usecase_class(**usecase_data)

    def usecase_to_mapping(self, usecase) -> Mapping:
        return self.schema.dump(usecase)
