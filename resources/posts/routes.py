from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.users.models import UserModel

from .Travelmodel import Travelmodel, destination, package_deal, travelers, booking
from schemas import TravelSchema, destinationSchema, package_dealSchema, travelersSchema, bookingSchema
from . import bp


@bp.route('/')
class TravelList(MethodView):
  
  @jwt_required()
  @bp.response(200, TravelSchema(many=True))
  def get(self):
    return Travelmodel.query.all()

  @jwt_required()
  @bp.arguments(TravelSchema)
  @bp.response(200, TravelSchema)
  def post(self, Travel_data):
    user_id = get_jwt_identity()
    p = Travelmodel(**Travel_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<Travel_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, TravelSchema)
  def get(self, Travel_id):
    p = Travelmodel.query.get(Travel_id)
    if p:
      return p
    abort(400, message='Invalid Travel Id')

  @jwt_required()
  @bp.arguments(TravelSchema)
  @bp.response(200, TravelSchema)
  def put(self, Travel_data, Travel_id):
    p = Travelmodel.query.get(Travel_id)
    if p and Travel_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = Travel_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Travel Data')

  @jwt_required()
  def delete(self, Travel_id):
     user_id = get_jwt_identity()
     p = Travelmodel.query.get(Travel_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'Travel Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid Travel Id')


@bp.route('/')
class destinationList(MethodView):
  
  @jwt_required()
  @bp.response(200, destinationSchema(many=True))
  def get(self):
    return destination.query.all()

  @jwt_required()
  @bp.arguments(destinationSchema)
  @bp.response(200, destinationSchema)
  def post(self, destination_data):
    user_id = get_jwt_identity()
    p = destination(**destination_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<destination_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, destinationSchema)
  def get(self, destination_id):
    p = destination.query.get(destination_id)
    if p:
      return p
    abort(400, message='Invalid Travel Id')

  @jwt_required()
  @bp.arguments(destinationSchema)
  @bp.response(200, destinationSchema)
  def put(self, destination_data, destination_id):
    p = destination.query.get(destination_id)
    if p and destination_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = destination_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Travel Data')

  @jwt_required()
  def delete(self, destination_id):
     user_id = get_jwt_identity()
     p = destination.query.get(destination_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'destination Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid destination Id')




@bp.route('/')
class package_dealList(MethodView):
  
  @jwt_required()
  @bp.response(200, package_dealSchema(many=True))
  def get(self):
    return package_deal.query.all()

  @jwt_required()
  @bp.arguments(package_dealSchema)
  @bp.response(200, package_dealSchema)
  def post(self, package_deal_data):
    user_id = get_jwt_identity()
    p = package_deal(**package_deal_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<package_deal_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, package_dealSchema)
  def get(self, package_deal_id):
    p = package_deal.query.get(package_deal_id)
    if p:
      return p
    abort(400, message='Invalid Travel Id')

  @jwt_required()
  @bp.arguments(package_dealSchema)
  @bp.response(200, package_dealSchema)
  def put(self, package_deal_data, package_deal_id):
    p = package_deal.query.get(package_deal_id)
    if p and package_deal_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = package_deal_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Travel Data')

  @jwt_required()
  def delete(self, package_deal_id):
     user_id = get_jwt_identity()
     p = package_deal.query.get(package_deal_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'package_deal Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid package_deal Id')





@bp.route('/')
class travelersList(MethodView):
  
  @jwt_required()
  @bp.response(200, travelersSchema(many=True))
  def get(self):
    return travelers.query.all()

  @jwt_required()
  @bp.arguments(travelersSchema)
  @bp.response(200, travelersSchema)
  def post(self, travelers_data):
    user_id = get_jwt_identity()
    p = travelers(**travelers_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<travelers_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, travelersSchema)
  def get(self, travelers_id):
    p = travelers.query.get(travelers_id)
    if p:
      return p
    abort(400, message='Invalid travelers Id')

  @jwt_required()
  @bp.arguments(travelersSchema)
  @bp.response(200, travelersSchema)
  def put(self, travelers_data, travelers_id):
    p = travelers.query.get(travelers_id)
    if p and travelers_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = travelers_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Travelers Data')

  @jwt_required()
  def delete(self, travelers_id):
     user_id = get_jwt_identity()
     p = travelers.query.get(travelers_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'travelers Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid travelers Id')





@bp.route('/')
class bookingList(MethodView):
  
  @jwt_required()
  @bp.response(200, bookingSchema(many=True))
  def get(self):
    return booking.query.all()

  @jwt_required()
  @bp.arguments(bookingSchema)
  @bp.response(200, bookingSchema)
  def post(self, booking_data):
    user_id = get_jwt_identity()
    p = travelers(**booking_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<booking_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, bookingSchema)
  def get(self, booking_id):
    p = booking.query.get(booking_id)
    if p:
      return p
    abort(400, message='Invalid booking Id')

  @jwt_required()
  @bp.arguments(bookingSchema)
  @bp.response(200, bookingSchema)
  def put(self, booking_data, booking_id):
    p = booking.query.get(booking_id)
    if p and booking_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = booking_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Travelers Data')

  @jwt_required()
  def delete(self, booking_id):
     user_id = get_jwt_identity()
     p = booking.query.get(booking_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'booking Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid booking Id')