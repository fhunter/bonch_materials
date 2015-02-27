# vim: set fileencoding=utf-8 :
import cgi
from my_db import *


def get_speciality():
	result = db_exec_sql("select uuid, code, name, description from speciality")
	return result

def get_speciality_by_uuid(uuid):
	result = db_exec_sql("select name from speciality where uuid= ?", (uuid,))
	return result

