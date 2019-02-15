from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
menu_available = Table('menu_available', post_meta,
    Column('event_code', Integer, primary_key=True, nullable=False),
    Column('submenu', Unicode, primary_key=True, nullable=False),
    Column('dish', Unicode, primary_key=True, nullable=False),
    Column('dish_desc', Unicode),
    Column('image_path', Unicode),
)

menu_vote = Table('menu_vote', post_meta,
    Column('event_code', Integer, primary_key=True, nullable=False),
    Column('voter', Unicode, primary_key=True, nullable=False),
    Column('submenu', Unicode, primary_key=True, nullable=False),
    Column('item', Unicode, primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['menu_available'].create()
    post_meta.tables['menu_vote'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['menu_available'].drop()
    post_meta.tables['menu_vote'].drop()
