# vim: set fileencoding=utf-8 :
import cgi
from my_db import *
from my_html import *

speciality_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="speciality_admin" class="UI_tab" >
	  <h2>Управление списком специальностей</h2>
	  <div class="add_form">
	  <form id="speciality_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    Шифр:<input name="speciality_code"><br>
	    Название:<input name="speciality_name"><br>
	    Описание<br>
	    <textarea name="speciality_description"></textarea><br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?speciality=show">  <button>Обновить</button></a>
	  </div>
	  <div id="speciality_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

speciality_edit = header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование специальности</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Шифр:<input name="speciality_code" value="%s"><br>
	    Название:<input name="speciality_name" value="%s"><br>
	    Описание<br>
	    <textarea name="speciality_description">%s</textarea><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>
	"""


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

def speciality_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in speciality_case:
			speciality_case[action](form)
	result=get_speciality()
	table = gen_table(result, (u"Шифр",u"Название",u"Описание"),(False,False,True))
	page = speciality_page % (table, )
	print_ui(page)
