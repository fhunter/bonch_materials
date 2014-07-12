# vim: set fileencoding=utf-8 :
import cgi
from my_db import *
from my_html import *
from my_speciality import get_speciality_by_uuid
from my_study_form import get_study_form_by_uuid
from my_discipline import get_discipline_by_uuid

material_page= header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Учебные материалы, список</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    <input name="material_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?page=material">  <button>Обновить</button></a>
	  </div>
	  <div id="material_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

material_edit = header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование учебного материала</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="" enctype="multipart/form-data">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Название:<input name="material_name" value="%s"><br>
	    Дата заливки: %s<br>
	    Дата последнего редактирования: %s<br>
	    Описание:
	    <textarea name="material_description">%s</textarea><br>
	    Владелец: %s<br>
	    Авторы: %s<br>
	    Файлы:<br>
	    %s
	    <br>Приложить файл
	    <input type="file" name="attach"  /><br>
	    Принадлежность: <br>
	    %s
	    <br>
	    Добавить принадлежность:
	    <br>
	    <input type=submit value="Обновить">
	  </form>
	  </div>
	</div>
	</div>
	</div>
	"""

def get_materials():
	result = db_exec_sql("select uuid, name,description,owner, upload_date, edit_date from materials")
	return result

def get_belongs_string(uuid, editdelete = False):
	belongs = get_belongs(uuid)
	if belongs != []:
		belongs1 = []
		belongs_string = "<table><tr>"
		for j in [ u"Специальность", u"Год", u"Форма обучения", u"Дисциплина", u"Семестр" ]:
			belongs_string += "<td class=field_name>%s</td>" % j
		if editdelete:
			belongs_string += "<td></td>"
		belongs_string += "</tr>"
		for j in belongs:
			element = (get_speciality_by_uuid(j[1])[0][0],j[2],get_study_form_by_uuid(j[3])[0][0],get_discipline_by_uuid(j[4])[0][0],get_discipline_by_uuid(j[4])[0][1])
			belongs_string += "<tr>"
			for i in element:
				belongs_string += "<td class=field_value>%s</td>" % i
			if editdelete:
				belongs_string += "<td>%s</td>" % j[0]
			belongs_string += "</tr>"
		belongs_string += "</table>"
		return belongs_string
	else:
		return ""

def add_material(form):
	if ("material_name" in form):
		name = cgi.escape(form.getfirst("material_name",""))
		owner = os.environ["REMOTE_USER"]
		db_exec_sql("insert into materials (uuid, name, owner) select *, ?, ? from next_uuid", (str(name).decode('utf-8'), owner))

def del_material(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from materials where uuid = ?", (uuid,))
		path = 'materials' + uuid.replace('{','/').replace('}','')
		if os.path.isdir(path):
			for j in os.listdir(path):
				if os.path.isfile(path + "/" + j):
					os.remove(path + "/" + j)
			os.rmdir(path)

def update_material(form):
	#TODO: Add updating material and creation of file data
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		material = db_exec_sql("select uuid, name, description, owner, upload_date, edit_date from materials where uuid = ?", (uuid,))
		material= material[0]
		name = material[1]
		description = material[2]
		if "material_name" in form:
			name= cgi.escape(form.getfirst("material_name",""))
			db_exec_sql("update materials set name= ?, edit_date = (datetime())  where uuid = ?", (name.decode('utf-8'), uuid,))
			#TODO: add update statement for name
		if "material_description" in form:
			description = cgi.escape(form.getfirst("material_description",""))
			db_exec_sql("update materials set description= ?, edit_date = (datetime()) where uuid = ?", (description.decode('utf-8'), uuid,))
		if "attach" in form:
			attach = form["attach"]
			path = 'materials' + uuid.replace('{','/').replace('}','')
			try:
				os.mkdir(path)
			except:
				pass
			if attach.file and attach.filename !="":
				db_exec_sql("update materials set edit_date = (datetime()) where uuid = ?", (uuid,))
				filename=path+"/"+os.path.basename(attach.filename)
				open(filename,"w").write(attach.file.read())

def edit_material(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		material = db_exec_sql("select uuid, name, description, owner, upload_date, edit_date from materials where uuid = ?", (uuid,))
		material= material[0]

		filedata = "<table>"
		path = 'materials' + material[0].replace('{','/').replace('}','')
		if os.path.isdir(path):
			for j in os.listdir(path):
				if os.path.isfile(path + "/" + j):
					html = u"""<a href="%s/%s">%s</a>""" % ( path, j, j,)
					filedata += gen_table_row( u"Файлы", html + u" " + unicode(os.path.getsize(path + "/" + j)/(1024*1024)) + u"Мб" )
		filedata += "</table>"
		authorship_string = ""
		tmp = get_authorship(uuid)
		for j in tmp:
			authorship_string += gen_table_row( u"Автор", j[1])
		authorship_string = "<table>%s</table>" % authorship_string
		belongs_string = get_belongs_string(uuid, True)
		page = material_edit % (material[0],material[1],material[4],material[5],material[2],material[3],authorship_string,filedata, belongs_string)
		print_ui(page )
		exit(0)

material_case = { "edit": edit_material, "delete": del_material, "add": add_material, "update": update_material }

def material_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in material_case:
			material_case[action](form)
	result=get_materials()
	table = u""
	for i in result:
		table += """<div class="list_element">"""
		table += "<table>"
		table += gen_table_row( u"Название" , i[1])
		table += gen_table_row( u"Дата заливки" , i[4])
		if i[5] == None:
			table += gen_table_row( u"Дата редактирования" , u"Никогда")
		else:
			table += gen_table_row( u"Дата редактирования" , i[5])
		table += gen_table_row( u"Заливал", i[3])
		tmp = get_authorship(i[0])
		for j in tmp:
			table += gen_table_row( u"Автор", j[1])
		table += gen_table_row_wide( u"Описание", i[2])

		belongs_string = get_belongs_string(i[0],False)
		if belongs_string !="":
			table += gen_table_row(u"Принадлежность", belongs_string)

		path = 'materials' + i[0].replace('{','/').replace('}','')
		if os.path.isdir(path):
			for j in os.listdir(path):
				if os.path.isfile(path + "/" + j):
					html = u"""<a href="%s/%s">%s</a>""" % ( path, j, j,)
					table += gen_table_row( u"Файлы", html + u" " + unicode(os.path.getsize(path + "/" + j)/(1024*1024)) + u"Мб" )

		table += "</table>"
		table += insert_edit_delete_btn(i[0], "delete_material")
	page = material_page % (table, )
	print_ui(page )


def get_authorship(uuid):
	result = db_exec_sql("select authorship.author_uuid, authors.fio from authorship,authors where authorship.material_uuid = ? and authors.uuid = authorship.author_uuid", (uuid,))
	return result

def get_belongs(uuid):
	result = db_exec_sql("select id,speciality_uuid, student_year, study_form_uuid, discipline_uuid from belongs where material_uuid = ?", (uuid, ))
	return result
