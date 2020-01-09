from models import \
    Artist as ArtistModel, Album as AlbumModel, MediaType as MediaTypeModel,\
    Genre as GenreModel, Employee as EmployeeModel, Customer as CustomerModel,\
    Invoice as InvoiceModel, Track as TrackModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

# ARTIST CLASS
class Artist(SQLAlchemyObjectType):
    class Meta:
        model = ArtistModel
        interfaces = (relay.Node, )

class Album(SQLAlchemyObjectType):
    class Meta:
        model = AlbumModel
        interfaces = (relay.Node, )

class MediaType(SQLAlchemyObjectType):
    class Meta:
        model = MediaTypeModel
        interfaces = (relay.Node, )

class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel
        interfaces = (relay.Node, )

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class Customer(SQLAlchemyObjectType):
    class Meta:
        model = CustomerModel
        interfaces = (relay.Node, )

class Invoice(SQLAlchemyObjectType):
    class Meta:
        model = InvoiceModel
        interfaces = (relay.Node, )

class Track(SQLAlchemyObjectType):
    class Meta:
        model = TrackModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):

    allArtist = SQLAlchemyConnectionField(
        Artist, sort=Artist.sort_argument())
    allAlbum = SQLAlchemyConnectionField(
        Album, sort=None)
    allGenre = SQLAlchemyConnectionField(
        Genre, sort=None)
    allEmployee = SQLAlchemyConnectionField(
        Employee, sort=None)
    allCustomer = SQLAlchemyConnectionField(
        Customer, sort=None)
    allInvoice = SQLAlchemyConnectionField(
        Invoice, sort=None)
    allTrack = SQLAlchemyConnectionField(
        Track, sort=None)
    
    find_artist = graphene.Field(lambda: Artist, id=graphene.Int())
    def resolve_find_artist(self, info, **kwargs):
        query = Artist.get_query(info)
        id = kwargs.get("id")
        return query.filter(ArtistModel.ArtistId == id).first()

schema = graphene.Schema(query=Query, types=[Artist, Album])
