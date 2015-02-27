# vim: set fileencoding=utf-8 :
import cgi
from my_db import *

def get_authors():
	result = db_exec_sql("select uuid, fio from authors")
	return result

