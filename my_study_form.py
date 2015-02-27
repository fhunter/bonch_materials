# vim: set fileencoding=utf-8 :
import cgi
from my_db import *

def get_study_form():
	result = db_exec_sql("select uuid, study_form from study_form")
	return result

def get_study_form_by_uuid(uuid):
	result = db_exec_sql("select study_form from study_form where uuid=?", (uuid,))
	return result

