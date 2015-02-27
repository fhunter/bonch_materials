# vim: set fileencoding=utf-8 :
import cgi
from my_db import *


def get_speciality():
	result = db_exec_sql("select uuid, code, name, description from speciality")
	return result

def get_speciality_by_uuid(uuid):
	result = db_exec_sql("select name from speciality where uuid= ?", (uuid,))
	return result

def add_speciality(form):
	if ("speciality_code" in form) and ("speciality_name" in form):
		speciality_code = cgi.escape(form.getfirst("speciality_code",""))
		speciality_name = cgi.escape(form.getfirst("speciality_name",""))
		speciality_description = cgi.escape(form.getfirst("speciality_description",""))
		db_exec_sql("insert into speciality (uuid, name, code, description) select *, ?, ?, ? from next_uuid", (str(speciality_name).decode('utf-8'),str(speciality_code).decode('utf-8'),str(speciality_description).decode('utf-8'),))

def del_speciality(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from speciality where uuid = ?", (uuid,))

def edit_speciality(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		speciality = db_exec_sql("select uuid, name, code, description from speciality where uuid = ?", (uuid,))[0]
		page = speciality_edit % ( speciality[0], speciality[1], speciality[2], speciality[3])
		print_ui(page)

def update_speciality(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		speciality = db_exec_sql("select uuid, name, code, description from speciality where uuid = ?", (uuid,))[0]
		name = speciality[1]
		code = speciality[2]
		description = speciality[3]
		if "speciality_name" in form:
			name= cgi.escape(form.getfirst("speciality_name",""))
			db_exec_sql("update speciality set name= ? where uuid = ?", (name.decode('utf-8'), uuid,))
		if "speciality_code" in form:
			code= cgi.escape(form.getfirst("speciality_code",""))
			db_exec_sql("update speciality set code= ? where uuid = ?", (code.decode('utf-8'), uuid,))
		if "speciality_description" in form:
			description = cgi.escape(form.getfirst("speciality_name",""))
			db_exec_sql("update speciality set description= ? where uuid = ?", (description.decode('utf-8'), uuid,))

speciality_case = { "edit": edit_speciality, "delete": del_speciality, "add": add_speciality, "update": update_speciality }
