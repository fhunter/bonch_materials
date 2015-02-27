# vim: set fileencoding=utf-8 :
import cgi
from my_db import *

def get_discipline():
	result = db_exec_sql("select uuid, name,semester,description from discipline")
	return result

def get_discipline_by_uuid(uuid):
	result = db_exec_sql("select name,semester from discipline where uuid = ?", (uuid,))
	return result

def add_discipline(form):
	if ("discipline_name" in form) and ("discipline_semester" in form):
		name = cgi.escape(form.getfirst("discipline_name",""))
		semester = cgi.escape(form.getfirst("discipline_semester",""))
		description = cgi.escape(form.getfirst("discipline_description",""))
		db_exec_sql("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(name).decode('utf-8'),str(semester).decode('utf-8'),str(description).decode('utf-8'),))

def del_discipline(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from discipline where uuid = ?", (uuid,))

def edit_discipline(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		discipline = db_exec_sql("select uuid, name, description,semester from discipline where uuid = ?", (uuid,))[0]
		page = discipline_edit % ( discipline[0], discipline[1], discipline[3], discipline[2])
		print_ui(page)

def update_discipline(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		discipline = db_exec_sql("select uuid, name, semester, description from discipline where uuid = ?", (uuid,))[0]
		name = discipline[1]
		semester = discipline[2]
		description = discipline[3]
		if "discipline_name" in form:
			name= cgi.escape(form.getfirst("discipline_name",""))
			db_exec_sql("update discipline set name= ? where uuid = ?", (name.decode('utf-8'), uuid,))
		if "discipline_semester" in form:
			semester= cgi.escape(form.getfirst("discipline_semester",""))
			db_exec_sql("update discipline set semester= ? where uuid = ?", (semester.decode('utf-8'), uuid,))
		if "discipline_description" in form:
			description = cgi.escape(form.getfirst("discipline_description",""))
			db_exec_sql("update discipline set description= ? where uuid = ?", (description.decode('utf-8'), uuid,))

discipline_case = { "edit": edit_discipline, "delete": del_discipline, "add": add_discipline, "update": update_discipline }

