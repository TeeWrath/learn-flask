import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from models import TagModel,StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from schemas import TagSchema

blp = Blueprint("Tags","tags",description="Operations on tags")

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
    
@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200,TagSchema)
    def get(self,tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag