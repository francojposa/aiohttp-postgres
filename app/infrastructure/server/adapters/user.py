from marshmallow import fields

from app.infrastructure.server.adapters.base import BaseSchema, BaseHTTPAdapter
from app.usecases import User


class UserSchema(BaseSchema):
    """User Serializer"""

    class Meta:
        """Meta data for UserSchema."""

        record_type_ = "user"

    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class UserHTTPAdapter(BaseHTTPAdapter):
    def __init__(self):
        super().__init__(schema=UserSchema(), usecase_class=User)
