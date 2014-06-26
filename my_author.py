# vim: set fileencoding=utf-8 :
from my_db import *
from my_html import *

authors_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" method="post" action="">
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

def get_authors():
	result = db_exec_sql("select uuid, fio from authors")
	return result

def add_authors(name):
	db_exec_sql("insert into authors (uuid, fio) select *, ? from next_uuid", (str(name).decode('utf-8'),))

def del_authors(uuid):
	db_exec_sql("delete from authors where uuid = ?", (uuid,))

def authors_showui(form):
	header_html()
	if is_post():
		if "authors_name" in form:
			authors_name = cgi.escape(form.getfirst("authors_name",""))
			add_authors(authors_name)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_authors(uuid)
	result = get_authors()
	table = gen_table(result, (u"ФИО автора",),(False,))
	page = authors_page % (table, )
	print_ui(page)
