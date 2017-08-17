from peewee import *
from constants import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT, DATABASE_USER

# mysql connection
# DB = MySQLDatabase(
#     DATABASE_NAME,
#     host=DATABASE_HOST,
#     port=DATABASE_PORT,
#     user=DATABASE_USER,
#     passwd=DATABASE_PASSWORD,
#     use_unicode=True,
#     charset='utf8'
# )

# postgresql connection
DB = PostgresqlDatabase(DATABASE_NAME, user=DATABASE_USER)

class Notice(Model):
    notice = CharField(null=False)
    url = CharField(null=False)
    date = CharField(null=False)
    news_id = IntegerField(null=False)

    class Meta:
        database = DB

def add_to_table(notice_text, url, date, news_id):
    DB.connect()
    notice = Notice(notice=notice_text, url=url, date=date, news_id=news_id)
    
    if not Notice.table_exists():
        DB.create_table(Notice)

    notice.save()
    DB.close()

def check_if_exist(news_id):
    flag = False
    DB.connect()
    query = Notice.select().where(Notice.news_id==news_id)
    
    if query.exists():
        flag = True
    
    DB.close()
    return flag

def create_table():
    DB.connect()
    DB.create_table(Notice)
    DB.close()
    print('------------------------------------------ Table created ------------------------------------------')
    

if __name__ == '__main__':
    # DB.connect()
    # DB.create_tables([Notice])
    # notice1 = Notice(notice='This is notice body', url='http://someurl.com', date='14 July 2017', news_id=321)
    # notice1.save()
    # DB.close()
    #check_if_exist(111)
    # add_to_table(notice_text='This is notice body', url='http://someurl.com', date='14 July 2017', news_id=321)
    create_table()
