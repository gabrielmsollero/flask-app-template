from marshmallow import Schema, fields, validate

class ExampleSchema(Schema):
    class NestedSchema(Schema):
        field1 = fields.Float()
        field2 = fields.Int()
    
    field1: fields.Nested(NestedSchema)
    field2: fields.List(fields.Float(), validate=validate.Length(equal=2))