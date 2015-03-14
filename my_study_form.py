# vim: set fileencoding=utf-8 :
import cgi
from my_db import *
from my_html import *

study_form_page=header_include + menu_include + u"""
      <div id="UI_elements">
	  <div id="study_form_admin" class="UI_tab" >
	  <h2>Управление списком форм обучения</h2>
	  <div class="add_form">
	  <form id="study_form_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    <input name="study_form_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?page=study_form">  <button>Обновить</button></a>
	  </div>
	  <div id="study_form_list" class="UI_list">
	  %s
	  </div>
	</div>

      </div>
    </div>
"""

study_form_edit = header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование формы обучения</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Название:<input name="study_form_name" value="%s"><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>
	"""

def get_study_form():
	result = db_exec_sql("select uuid, study_form from study_form")
	return result

def get_study_form_by_uuid(uuid):
	result = db_exec_sql("select study_form from study_form where uuid=?", (uuid,))
	return result

def add_study_form(form):
	if "study_form_name" in form:
		name = cgi.escape(form.getfirst("study_form_name",""))
		db_exec_sql("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(name).decode('utf-8'),))

def del_study_form(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from study_form where uuid = ?", (uuid,))

def edit_study_form(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		material = db_exec_sql("select uuid, study_form from study_form where uuid = ?", (uuid,))
		material= material[0]
		page = study_form_edit % (material[0],material[1],)
		print_ui(page )
		exit(0)

def update_study_form(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		study_form = db_exec_sql("select uuid, study_form from study_form where uuid = ?", (uuid,))[0]
		name = study_form[1]
		if "study_form_name" in form:
			name= cgi.escape(form.getfirst("study_form_name",""))
			db_exec_sql("update study_form set study_form= ? where uuid = ?", (name.decode('utf-8'), uuid,))

def study_form_mainpage():
	result=get_study_form()
	table = gen_table(result, (u"Форма обучение",),(False,))
	page = study_form_page % (table, )
	print_ui(page)

study_form_case = { "edit": edit_study_form, "delete": del_study_form, "add": add_study_form, "update": update_study_form, }

def study_form_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in study_form_case:
			study_form_case[action](form)
	study_form_mainpage()

