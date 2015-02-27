# vim: set fileencoding=utf-8 :
import cgi
from my_db import *

def get_discipline():
	result = db_exec_sql("select uuid, name,semester,description from discipline")
	return result

def get_discipline_by_uuid(uuid):
	result = db_exec_sql("select name,semester from discipline where uuid = ?", (uuid,))
	return result
