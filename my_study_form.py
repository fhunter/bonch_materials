# vim: set fileencoding=utf-8 :
from my_db import *
from my_html import *

study_form_page=header_include + menu_include + u"""
      <div id="UI_elements">
	  <div id="study_form_admin" class="UI_tab" >
	  <h2>Управление списком форм обучения</h2>
	  <div class="add_form">
	  <form id="study_form_add_form" method="post" action="">
	    <input name="study_form_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?study_form=show">  <button>Обновить</button></a>
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

def add_study_form(name):
	db_exec_sql("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(name).decode('utf-8'),))

def del_study_form(uuid):
	db_exec_sql("delete from study_form where uuid = ?", (uuid,))

def study_form_showui(form):
	header_html()
	if is_post():
		if "study_form_name" in form:
			study_form_name = cgi.escape(form.getfirst("study_form_name",""))
			add_study_form(study_form_name)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_study_form(uuid)
	result=get_study_form()
	table = gen_table(result, (u"Форма обучение",),(False,))
	page = study_form_page % (table, )
	print_ui(page)
	

