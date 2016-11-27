import datetime
import logging
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine, exc
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from functools import wraps

from sqlalchemy.sql.elements import Null

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()

# connect to db
engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe', client_encoding='utf8')

session = sessionmaker(expire_on_commit=False)
session.configure(bind=engine)


def dbsession(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        result = {'data': None, 'errors': None, 'warnings': None}
        sess = session()
        logger.info('Session started..')
        try:
            result['data'] = f(*args, session=sess, **kwargs)
            sess.commit()
        except Exception as e:
            sess.rollback()
            sess.expunge_all()
            if 'WARNING' in e.message:
                result['warnings'] = e
                logger.info('Warning:{0}'.format(e))
            else:
                result['errors'] = e
                logger.info('Error:{0}'.format(e))
        finally:
            sess.close()
            logger.info('Session closed!')
        return result

    return wrapped


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    rfid_card = Column(String(50), unique=True, nullable=True)
    admin = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)

    def __init__(self, firstname, lastname, rfid_card, admin):
        self.firstname = firstname
        self.lastname = lastname
        self.rfid_card = rfid_card
        self.admin = admin

    @classmethod
    @dbsession
    def create(self, firstname, lastname, rfid, admin, session):

        logger.info('Start creating new user..')

        try:
            if rfid in [i.rfid_card for i in session.query(User).filter().all()]:
                raise IOError('WARNING!User with card: {0} already exist!'.format(rfid))
            new_user = User(firstname=firstname, lastname=lastname, rfid_card=rfid, admin=admin)
            session.add(new_user)
            logger.info("Created user:%s %s, with RFID:%s", firstname, lastname, rfid)
            return session.query(User).filter(User.rfid_card == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("User not created with error: %s", e)
            raise Exception('User not created with error:{0}'.format(e))

    @classmethod
    @dbsession
    def delete(self, user, session):
        logger.info('Start deleting user..')
        try:
            user.deleted = True
            user.rfid_card = None
            user.admin = False
            session.add(user)
            logger.info("User deleted.")
            return True
        except exc.SQLAlchemyError as e:
            logger.info("User with id: '%s' DO NOT deleted user with RFID:'%s'", user.id, user.rfid_card)
            raise Exception('User not deleted with error:{0}'.format(e))

    @classmethod
    @dbsession
    def get_by_rfid(self, rfid, session):

        logger.info('Start getting user by rfid..')

        try:
            user = session.query(User).filter(User.rfid_card == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get user by RFID:'%s'", rfid)
            raise Exception('Cant get user by RFID:{0}'.format(e))
        if user:
            return user
        else:
            raise IOError('WARNING!User with card: {0} not found!'.format(rfid))

    @classmethod
    @dbsession
    def get_all(self, session):

        logger.info('Start getting all users..')
        try:
            users = session.query(User).filter(User.deleted == False).all()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get users. {0}".format(e))
            raise Exception("Can't get users {0}".format(e))
        if users:
            return users
        else:
            raise IOError('WARNING!Users not found')

    def __repr__(self):
        return '<{0} {1.firstname!r}:{1.lastname!r}:{1.rfid_card!r}:{1.admin!r}>'.format('UserObject', self)


class Key(Base):
    __tablename__ = 'key'

    id = Column(Integer, primary_key=True)
    room = Column(String(50))
    rfid_chip = Column(String(50), unique=True, nullable=True)
    status = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)

    def __init__(self, room, rfid_chip, status):
        self.room = room
        self.rfid_chip = rfid_chip
        self.status = status

    @classmethod
    @dbsession
    def get_by_rfid(self, rfid, session):

        logger.info('Start getting key by RFID..')

        try:
            key = session.query(Key).filter(Key.rfid_chip == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get key by rfid: %s , %s", rfid, e)
            raise Exception('Cant get key by RFID. Error:{0}'.format(e))
        if key:
            return key
        else:
            raise IOError('WARNING!Key by RFID:{0} not found'.format(rfid))

    @classmethod
    @dbsession
    def get_available_keys(self, session):
        logger.info("Start getting available keys..")

        try:
            keys = session.query(Key).filter(Key.status == True).all()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get available keys")
            raise Exception("Can't get available keys.Error:{0}".format(e))
        if keys:
            return keys
        else:
            raise IOError("WARNING!Can't find available keys")

    @classmethod
    @dbsession
    def get_taken_keys(self, session):
        logger.info("Start getting taken keys..")

        try:
            keys = session.query(Key).filter(Key.status == False).all()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get taken keys")
            raise Exception("Can't get taken keys.Error:{0}".format(e))
        if keys:
            return keys
        else:
            raise IOError("WARNING!Can't find taken keys")

    @classmethod
    @dbsession
    def get_all(self, session):

        logger.info('Getting all keys..')

        try:
            keys = session.query(Key).filter(Key.deleted == False).order_by('id').all()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get all keys. %s", e)
            raise Exception('Cant get all keys. {0}'.format(e))
        if keys:
            return keys
        else:
            raise IOError('WARNING!Keys not found')

    @classmethod
    @dbsession
    def create(self, room, rfid, session):

        logger.info('Start creating new Key..')

        try:
            if rfid in [key.rfid_chip for key in session.query(Key).filter().all()]:
                raise IOError('WARNING!Key with this RFID: {0} already exist!'.format(rfid))

            places = session.query(KeyPlaces).filter(KeyPlaces.status == True)
            if places.count() >= 1:
                place = places.first()
            else:
                raise IOError('WARNING!All key places are busy')
            place.status = False
            place.key_rfid = rfid
            new_key = Key(room=room, rfid_chip=rfid, status=True)
            session.add(new_key)
            session.add(place)
            logger.info(u"Created key for room:{0}, with RFID:{1}".format(room, rfid))
            return session.query(Key).filter(Key.rfid_chip == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Key not created with error:{0}".format(e))
            raise Exception('Key not created with error {0}'.format(e))

    @classmethod
    @dbsession
    def delete(self, key, session):

        logger.info('Start deleting key..')

        try:
            place = session.query(KeyPlaces).filter(KeyPlaces.key_rfid == key.rfid_chip).first()
            place.key_rfid = None
            place.status = True
            key.deleted = True
            key.rfid_chip = None
            session.add(key)
            session.add(place)
            logger.info("Key deleted.")
            return True
        except exc.SQLAlchemyError as e:
            logger.info("Key DO NOT deleted from room:%s with RFID:%s", key.room, key.rfid_chip)
            raise Exception('Key not deleted with error:{0}'.format(e))

    def __repr__(self):
        return '<{0}: {1.room!r}:{1.rfid_chip!r}:{1.status!r} >'.format('KeyObject', self)


class KeyPlaces(Base):
    __tablename__ = 'key_places'

    id = Column(Integer, primary_key=True)
    key_rfid = Column(String(50), unique=True, nullable=True)
    status = Column(Boolean, default=True)  # means True = free
    coordinate_place = Column(String(50))

    def __init__(self, coordinate_place):
        self.coordinate_place = coordinate_place

    @classmethod
    @dbsession
    def create(self, coordinate_place, session):
        try:
            logger.info('Start register new place..')
            register_new_place = KeyPlaces(coordinate_place=coordinate_place)
            session.add(register_new_place)
            logger.info(u"Registered place with coordinates"
                        u" by coordinates:{0}".format(coordinate_place))
        except exc.SQLAlchemyError as e:
            logger.info("Place not created with error:{0}".format(e))
            raise Exception('Place not created with error {0}'.format(e))

    @classmethod
    @dbsession
    def get_coordinates(self, rfid, session):

        logger.info('Start getting coordinates by RFID..')

        try:
            coordinates = session.query(KeyPlaces).filter(KeyPlaces.key_rfid == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get coordinates by rfid: %s , %s", rfid, e)
            raise Exception('Cant get coordinates by RFID. Error:{0}'.format(e))
        if coordinates:
            return coordinates
        else:
            raise IOError('WARNING!Coordinates by RFID:{0} not found'.format(rfid))


class UserKeyLink(Base):
    __tablename__ = 'user_key_link'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=False)
    key_id = Column(Integer, ForeignKey('key.id'), primary_key=False)
    date_taken = Column(DateTime, default=datetime.datetime.utcnow)
    date_returned = Column(DateTime, nullable=True)
    user = relationship(User, lazy='subquery')
    key = relationship(Key, lazy='subquery')

    def __init__(self, user, key):
        self.user = user
        self.key = key

    @classmethod
    @dbsession
    def getting_key(self, user, key_rfid, session):

        logger.info('Start getting Key..')
        try:
            key = session.query(Key).filter(Key.rfid_chip == key_rfid).first()

            if key.status is False:
                raise IOError('WARNING!Key already taken !')

            new_get = UserKeyLink(user=user, key=key)
            key.status = False

            session.add(new_get)
            session.add(key)
            logger.info('User: %s with RFID:%s get key from room:%s with RFID:%s',
                        user.lastname, user.rfid_card, key.room, key.rfid_chip)
            return new_get
        except exc.SQLAlchemyError as e:
            logger.info("Some error happend when user %s take a key %s. \n --- %s", user.id, key.id, e)
            raise Exception('Some error happend when user take a key:{0}'.format(e))

    @classmethod
    @dbsession
    def returning_key(self, key_rfid, session):

        logger.info('Starting returned Key..')

        try:
            key = session.query(Key).filter(Key.rfid_chip == key_rfid).first()
            if not key:
                logger.info('Key not found!', key.room)
                raise IOError('WARNING!Key not found!')

            if key.status is True:
                logger.info('Key from room:%s already returned!', key.room)
                raise IOError('WARNING!Key already returned!')

            # get last taken element
            relation = session.query(UserKeyLink).filter(UserKeyLink.key == key,
                                                         UserKeyLink.date_returned == None).first()
            # set date taken and key new status
            relation.date_returned = datetime.datetime.utcnow()
            key.status = True

            session.add(relation)
            session.add(key)
            logger.info('Key from room:%s returned!', key.room)
            return relation
        except (exc.SQLAlchemyError, InvalidRequestError) as e:
            logger.info("Some error happend when key id:%s returned %s", key.id, e)
            raise Exception('Some error happend when key returned:{0}'.format(e))

    @classmethod
    @dbsession
    def get_all_operations(self, session):

        logger.info('Starting returned data..')

        try:
            data = session.query(UserKeyLink).filter().all()
            logger.info("Data was returned!")
            return data
        except (exc.SQLAlchemyError, InvalidRequestError) as e:
            logger.info("Error happend returning data")
            raise Exception('Error happend returning data:{0}'.format(e))

    @classmethod
    @dbsession
    def get_only_taken_keys(self, key_id, session):

        logger.info('Starting returned data..')

        try:
            data = session.query(UserKeyLink).filter(UserKeyLink.date_returned == None,
                                                     UserKeyLink.key_id == key_id).first()
            logger.info("Data was returned!")
            return data
        except (exc.SQLAlchemyError, InvalidRequestError) as e:
            logger.info("Error happend returning data")
            raise Exception('Error happend returning data:{0}'.format(e))

    def __repr__(self):
        return '<{0}: {1.user!r}:{1.key!r}:{1.date_taken!r}:{1.date_returned!r} >'.format('UserKeyLinkObject', self)
