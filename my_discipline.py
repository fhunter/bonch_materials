# vim: set fileencoding=utf-8 :
from my_db import *
from my_html import *

discipline_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  <div class="add_form">
	  <form id="discipline_add_form" method="post" action="">
	    Название:<input name="discipline_name"><br>
	    Семестр:<input name="discipline_semester"><br>
	    Описание:<br>
	    <textarea name="discipline_description"></textarea>
	    <br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?discipline=show">  <button>Обновить</button></a>
	  </div>
	  <div id="discipline_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

def get_discipline():
	result = db_exec_sql("select uuid, name,semester,description from discipline")
	return result

def add_discipline(name,semester,description):
	db_exec_sql("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(name).decode('utf-8'),str(semester).decode('utf-8'),str(description).decode('utf-8'),))

def del_discipline(uuid):
	db_exec_sql("delete from discipline where uuid = ?", (uuid,))

def discipline_showui(form):
	header_html()
	if is_post():
		if ("discipline_name" in form) and ("discipline_semester" in form):
			discipline_name = cgi.escape(form.getfirst("discipline_name",""))
			discipline_semester = cgi.escape(form.getfirst("discipline_semester",""))
			discipline_description = cgi.escape(form.getfirst("discipline_description",""))
			add_discipline(discipline_name,discipline_semester,discipline_description)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_discipline(uuid)
	result=get_discipline()
	table = gen_table(result, (u"Название",u"Семестр",u"Описание"),(False,False,True))
	page = discipline_page % (table, )
	print_ui(page)

