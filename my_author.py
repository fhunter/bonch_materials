# vim: set fileencoding=utf-8 :
import cgi
from my_db import *
from my_html import *

authors_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    <input name="authors_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?authors=show">  <button>Обновить</button></a>
	  </div>
	  <div id="author_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

authors_edit = header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование автора</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    ФИО:<input name="authors_name" value="%s"><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>
	"""

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

def authors_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in authors_case:
			authors_case[action](form)
	result = get_authors()
	table = gen_table(result, (u"ФИО автора",),(False,))
	page = authors_page % (table, )
	print_ui(page)
