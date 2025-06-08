import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from models import TagModel,StoreModel,ItemModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from schemas import TagSchema,TagAndItemSchema

blp = Blueprint("Tags","tags",description="Operations on tags")

@blp.route("/tag")
class AllTags(MethodView):
    @blp.response(200,TagAndItemSchema)
    def get(self):
        return TagModel.query.all()

@blp.route("/store/<string:store_id>/tag")
class TagsInStore(MethodView):
    @blp.response(200,TagSchema(many=True))
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        
        return store.tags.all()
    
    @blp.arguments(TagSchema)
    @blp.response(201,TagSchema)
    def post(self,tag_data,store_id):
        # checks if tag is unique for that store or not
        # if TagModel.query.filter(TagModel.store_id == store_id,TagModel.name == tag_data["name"]).first():
        #     abort(400,message=f"A tag with the name {tag_data["name"]} already exists in the store {store_id}.")
        # if the tag is unique only then we move to next part
        tag = TagModel(**tag_data,store_id=store_id)
        
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e)
            )
            
        return tag

@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201,TagSchema)
    def post(self,item_id,tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        
        if item.store_id != tag.store_id:
            abort(400,message="Item from a store must be linked to the tag of the same store.")
        item.tags.append(tag)
        try :
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,message=str(e))
        
        return tag
    
    @blp.response(200,TagAndItemSchema)
    def delete(self,item_id,tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        
        item.tags.remove(tag)
        try :
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,message=str(e))
        
        return {"message": "Item removed from tag", "item": item, "tag": tag}
    
@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200,TagSchema)
    def get(self,tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag
    
    @blp.response(202,description="Deletes a tag if no item is tagged with it.")
    @blp.alt_response(404,description="tag not found.")
    @blp.alt_response(400,description="Returned if the tag is assigned to one or more items. In this case the tag is not deleted.")
    def delete(self,tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "tag deleted."}
        abort(400,message="Could not delete the tag. Make sure the tag is not associated with any item.")
            