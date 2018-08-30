from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta: 
        model = Account
 