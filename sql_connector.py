import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.1.1",
  user="root",
  password="34353435",
  database="xcelence"
)

class MySQL:
  cursor = None
  model = ''

  def __init__(s, model, lang = 'CA'):
    s.model = model
    s.lang = lang

  def init(s):
    s.cursor = mydb.cursor()

  def update(s, values):
    fields = ''
    excepted = s.getFields()
      
    for item in excepted:
      fields += f'{item}_{s.lang} = %s,'

    fields = fields[0:-1]

    s.cursor.execute(f'UPDATE {s.model} SET {fields} WHERE id = %s', values)

  def create(s, values):
    builded = ''

    for _ in values:
      builded += '%s,'

    builded = builded[0:-1]

    s.cursor.execute(f'INSERT INTO {s.model}_dic VALUES({builded});', values)

  def fetch(s):
    subquery = f'(SELECT {s.model}_id FROM {s.model}_dic WHERE language_id = 2)'

    s.cursor.execute(f'''
      SELECT * FROM {s.model}_dic
      WHERE
        language_id = 1 AND
        {s.model}_id NOT IN {subquery};
    ''')

    return s.cursor.fetchall()

  def commit(seft):
    mydb.commit()
