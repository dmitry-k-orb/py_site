from sqlalchemy import create_engine
from sqlalchemy import text

def get_citate():
    engine = create_engine("mysql+pymysql://py_site_user:Baikal#1324@192.168.1.27/py_site_db", echo = True)
    with engine.connect() as conn:
        result = conn.execute(text("select s_name, f_name, text from Authors left join Citate on id = AuthorId"))
       # print (result.all())
    return result.all()
