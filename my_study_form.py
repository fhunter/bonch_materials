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

def get_study_form():
	result = db_exec_sql("select uuid, study_form from study_form")
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
	pass

def study_form_mainpage():
	result=get_study_form()
	table = gen_table(result, (u"Форма обучение",),(False,))
	page = study_form_page % (table, )
	print_ui(page)

study_form_case = { "edit": edit_study_form, "delete": del_study_form, "add": add_study_form }

def study_form_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in study_form_case:
			study_form_case[action](form)
	study_form_mainpage()
