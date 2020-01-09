from database import Base
from sqlalchemy import Table, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import Float, DateTime

# association_table = Table('association', Base.metadata, 
#     Column('TrackId', Integer, ForeignKey('tracks.TrackId')),
#     Column('PlaylistId', Integer, ForeignKey('playlists.PlaylistId'))
# )

class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Album = relationship("Album")

class Album(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    Artist = relationship("Artist")

class MediaType(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)

class Genre(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)

class Employee(Base):
    __tablename__ = 'employees'
    EmployeeId = Column(Integer, primary_key=True)
    ReportsTo = Column(Integer, ForeignKey('employees.EmployeeId'))
    FirstName = Column(String)
    LastName = Column(String)
    Title = Column(String)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)

class Customer(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key=True)
    SupportRepId = Column(Integer, ForeignKey('employees.EmployeeId'))
    FirstName = Column(String)
    LastName = Column(String)   
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRep = relationship(Employee,backref=backref('employees',uselist=True,cascade='delete,all'))
    Invoice = relationship(Employee,backref=backref('invoices',uselist=True,cascade='delete,all'))

class Invoice(Base):
    __tablename__ = 'invoices'
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey('customers.CustomerId'))
    InvoiceDate = Column(DateTime)
    BillingAddress = Column(String)
    BillingCity = Column(String)  

class InvoiceItem(Base):
    __tablename__ = 'invoice_items'
    InvoiceItemId = Column(Integer, primary_key=True)
    invoiceId = Column(Integer, ForeignKey('invoices.InvoiceId'))
    TrackId = Column(Integer, ForeignKey('tracks.TrackId'))
    UnitPrice = Column(Float)
    Quantity = Column(Integer)
    Invoice = relationship(Invoice,backref=backref('invoices',uselist=True,cascade='delete,all'))


class Track(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    Name = Column(String)
    Composer = Column(String)
    Miliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Integer)

    album = relationship(Album,backref=backref('albums',uselist=True,cascade='delete,all'))
    mediatype = relationship(MediaType,backref=backref('media_type',uselist=True,cascade='delete,all'))
    genre = relationship(Genre,backref=backref('genres',uselist=True,cascade='delete,all'))
    # invoice_item = relationship(InvoiceItem,backref=backref('tracks',uselist=True,cascade='delete,all'))
    # playlist = relationship("playlists",secondary=lambda:association_table,backref="tracks")





# class Playlist(Base):
#     __tablename__ = 'playlists'
#     PlaylistId = Column(Integer, primary_key=True)
#     Name = Column(String)
    # track = relationship("tracks",secondary=association_table,back_populates="playlists")

# class PlaylistTrack(Base):
#     __tablename__ = 'playlist_track'
#     PlaylistId = Column(Integer, ForeignKey('playlits.PlaylistId'))
#     TrackId = Column(Integer, ForeignKey('tracks.TrackId'))





# class Customer(Base):
#     __tablename__ = 'customers'
#     CustomerId = Column(Integer, primary_key=True)
#     CustomerId = Column(Integer, ForeignKey('customers.CustomerId'))
#     InvoiceDate = Column(DateTime)
#     BillingAddress = Column(String)
#     BillingCity = Column(String)  



# role = relationship(
# Role,
# backref=backref('roles',
#                 uselist=True,
#                 cascade='delete,all'))