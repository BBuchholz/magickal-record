from sqlite3 import Cursor
from chronio import ChronIO
from myrki_row_list import MyrkiRowList
from card_row_list import CardRowList

class DbOne:
  # database definitions for version one
  def __init__(self):
    self.version = 1
    self.chron = ChronIO()

  def ensure_table_db_meta(self, cursor):
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS DbMeta (
        DbMetaKey TEXT NOT NULL UNIQUE,
        DbMetaValue TEXT,
        PRIMARY KEY(DbMetaKey)
      )
    ''')

  def ensure_table_myrki(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS Myrki (
        myrkiValue TEXT NOT NULL UNIQUE,
        PRIMARY KEY(myrkiValue)
      )
    ''')
  
  def ensure_table_card(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS Card (
        cardId	INTEGER NOT NULL UNIQUE,
        myrkiValue	TEXT NOT NULL,
        cardCode	TEXT UNIQUE,
        cardText	TEXT,
        cetCode	TEXT,
        imageFile	TEXT,
        canvaLinkHref	TEXT,
        myrkiCreditCollabId	INTEGER,
        textCreditCollabId	INTEGER,
        imageCreditCollabId	INTEGER,
        PRIMARY KEY(cardId AUTOINCREMENT)
      )
    ''')

  def ensure_table_cet(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS Cet (
        cetCode	TEXT NOT NULL UNIQUE,
        releaseDate	TEXT,
        sabbatName	TEXT NOT NULL,
        PRIMARY KEY(cetCode)
      )
    ''')

  def ensure_table_collab_member(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS CollabMember (
        collabId	INTEGER NOT NULL,
        sourceId	INTEGER NOT NULL,
        PRIMARY KEY(collabId,sourceId)
      )
    ''')

  def ensure_table_collaboration(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS Collaboration (
        collabId	INTEGER NOT NULL UNIQUE,
        collabNotes	TEXT,
        PRIMARY KEY(collabId AUTOINCREMENT)
      )
    ''')

  def ensure_table_source(self, cursor):
    cursor.execute('''    
      CREATE TABLE IF NOT EXISTS Source (
        sourceId	INTEGER NOT NULL UNIQUE,
        sourceName	TEXT NOT NULL,
        PRIMARY KEY(sourceId AUTOINCREMENT)
      )
    ''')

  def table_exists(self, table_name):
    return False #TODO: implement

  def ensure_db_meta_values(self, cursor):
    print(f"checking current db metadata")
    current_meta = self.get_db_meta(cursor)
    print(f"current metadata is {current_meta}")
    key = 'db_version'
    if key not in current_meta:
      val = self.version
      print(f"key {key} not found, inserting")
      self.insert_db_meta(cursor, key, val)
      print(f"inserted value: {val} for key: {key}")
    else:
      val = current_meta[key]
      print(f"found existing value: {val} for key: {key}")
    key = 'db_ensured_at'
    if key not in current_meta:
      val = self.chron.get_timestamp()
      print(f"key {key} not found, inserting")
      self.insert_db_meta(cursor, key, val)
      print(f"inserted value: {val} for key: {key}")
    else:
      val = current_meta[key]
      print(f"found existing value: {val} for key: {key}")
      val = self.chron.get_timestamp()
      print(f"Updating db_ensured_at timestamp to {val}")
      self.update_db_meta(cursor, key, val)

  def select_myrkis(self, cursor: Cursor) -> MyrkiRowList:
    myrkis = MyrkiRowList()
    cursor.execute("SELECT * FROM Myrki")
    rows = cursor.fetchall()
    if len(rows) > 0:
      myrkis = self.load_myrkis_from(rows)
      # print(f"myrkis found: {myrkis}")
    else:
      print("no myrkis found")
    return myrkis


  def select_cards(self, cursor: Cursor):
    cards = []
    cursor.execute("SELECT * FROM Card")
    rows = cursor.fetchall()
    if len(rows) > 0:
      cards = self.load_cards_from(rows)
      print(f"cards found: {len(cards)}")
    else:
      print("no cards found")
    return cards

  def get_db_meta(self, cursor: Cursor):
    version = None
    cursor.execute("SELECT * FROM DbMeta")
    rows = cursor.fetchall()
    metaData = {}
    if len(rows) > 0:
      metaData = self.load_db_meta_from_rows(rows)
      print(f"metadata found: {metaData}")
    else:
      print("no db meta rows found")
    return metaData

  def insert_db_meta(self, cursor: Cursor, key, value):
    try:
      cursor.execute('''
        INSERT INTO DbMeta (DbMetaKey, DbMetaValue)
        VALUES (?, ?)
      ''', (key, value))
    except Exception as e:
      print("Exception inserting into db:")
      print(repr(e))

  def insert_myrki(self, cursor: Cursor, myrki: str):
    try:
      cursor.execute('''
        INSERT INTO Myrki (myrkiValue)
        VALUES (?)
      ''', (myrki,))
    except Exception as e:
      print("Exception inserting into db:")
      print(repr(e))

  def update_db_meta(self, cursor: Cursor, key, val):
    query = '''
      UPDATE DbMeta
      SET DbMetaValue = ?
      WHERE DbMetaKey = ?
    '''
    cursor.execute(query, (val, key))

  def load_db_meta_from_rows(self, rows):
    metaData = {}
    for row in rows:
      if row['DbMetaKey'] == 'db_version':
        version = row['DbMetaValue']
        metaData['db_version'] = version
        print(f"found db_version: {version}")
      if row['DbMetaKey'] == 'db_ensured_at':
        ensured = row['DbMetaValue']
        metaData['db_ensured_at'] = ensured
        print(f"found db_ensured_at: {ensured}")
    return metaData
  
  def load_myrkis_from(self, rows) -> MyrkiRowList:
    myrkis = MyrkiRowList()
    for row in rows:
      myrki = row['myrkiValue']
      print(f"found myrki: {myrki}")
      myrkis.append(myrki)
    return myrkis
  

  def load_cards_from(self, rows) -> list:
    cards = []
    for row in rows:
      # TODO: MAKE THIS WORK (COPIED FROM MYRKI, NOT CORRECT CURRENTLY)
      # TODO: copy values from the ERD to fully populate the dict 
      # (let cards be a list of dicts, each card a dict of 
      # key value pairs for field values)
      card = {}
      card['cardId'] = row['cardId']
      card['myrkiValue'] = row['myrkiValue']
      card['cardCode'] = row['cardCode']
      card['cardText'] = row['cardText']
      card['cetCode'] = row['cetCode']
      card['imageFile'] = row['imageFile']
      card['canvaLinkHref'] = row['canvaLinkHref']
      card['myrkiCreditCollabId'] = row['myrkiCreditCollabId']
      card['textCreditCollabId'] = row['textCreditCollabId']
      card['imageCreditCollabId'] = row['imageCreditCollabId']
      # print(f"found card: {card}")
      cards.append(card)
    return cards