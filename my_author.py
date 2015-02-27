# vim: set fileencoding=utf-8 :
import cgi
from my_db import *

def get_authors():
	result = db_exec_sql("select uuid, fio from authors")
	return result

def add_authors(form):
	if "authors_name" in form:
		authors_name = cgi.escape(form.getfirst("authors_name",""))
		db_exec_sql("insert into authors (uuid, fio) select *, ? from next_uuid", (str(authors_name).decode('utf-8'),))

def del_authors(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from authors where uuid = ?", (uuid,))

def edit_authors(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		author = db_exec_sql("select uuid, fio from authors where uuid = ?", (uuid,))
		author= author[0]
		page = authors_edit % (author[0],author[1],)
		print_ui(page )
		exit(0)

def update_authors(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		study_form = db_exec_sql("select uuid, fio from authors where uuid = ?", (uuid,))[0]
		name = study_form[1]
		if "authors_name" in form:
			name= cgi.escape(form.getfirst("authors_name",""))
			db_exec_sql("update authors set fio= ? where uuid = ?", (name.decode('utf-8'), uuid,))

authors_case = { "edit": edit_authors, "delete": del_authors, "add": add_authors, "update": update_authors }
