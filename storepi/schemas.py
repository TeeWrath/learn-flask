from marshmallow import Schema,fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) # we did dump only true because id is a property which api cannot receive from user but it is created
    # itself and always only returned to the client. Id will not be used to validate data when incoming request is there
    
    # properties below are marked required hence these will be used to validate the data
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)
    
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)