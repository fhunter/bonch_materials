# vim: set fileencoding=utf-8 :
import os

header_include= u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
"""

menu_include = u"""
      <div id="menu">
	<a href="./?page=material">  <button>Материалы</button></a>
	<a href="./?page=authors">   <button>Авторы</button></a>
	<a href="./?page=discipline"><button>Дисциплины</button></a>
	<a href="./?page=speciality"><button>Специальности</button></a>
	<a href="./?page=study_form"><button>Формы обучения</button></a>
      </div>
"""

def is_post():
	if os.environ['REQUEST_METHOD'] == 'POST':
		return True
	return False

def header_html():
        print "Content-type: text/html"
        print ""

def header_txt():
        print "Content-type: text/plain"
        print ""

def print_ui(page):
        print """<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf8"></head><body>
	<link rel="stylesheet" type="text/css" href="style.css" /><title>Система управления учебными материалами</title>"""
        print page.encode('utf-8')
	print """</body></html>"""

def insert_edit_delete_btn(uuid, func_name):
	text =  u""
	text += u"""
	<div class="edit_button">
		<form action="" method="post">
			<input type="hidden" name="uuid" value="%s"/>
			<input type="hidden" name="action" value="edit"/>
			<input type=submit value="Редактировать"/>
		</form>
	</div>
	<div class="delete_button">
		<form action="" method="post">
			<input type="hidden" name="uuid" value="%s"/>
			<input type="hidden" name="action" value="delete"/>
			<input type=submit value="Удалить"/>
		</form>
	</div>
	""" % (uuid, uuid)
  	return text

def gen_table_row(name, value ):
	text = u"<tr><td class=field_name>%s</td><td class=field_value>%s</td></tr>" % (name, value, )
	return text

def gen_table_row_wide( name, value ):
	text = u"<tr><td class=field_name>%s</td></tr><tr><td class=field_value colspan=2>%s</td></tr>" %( name, value, )
	return text

def gen_table(values, names, wide):
	table = u""
	for i in values:
		table += "<div class=\"list_element\">"
		table += "<table>"
		uuid = i[0]
		for j in range(0,len(names)):
			if(wide[j]):
				table += gen_table_row_wide( names[j], i[j+1])
			else:
				table += gen_table_row( names[j], i[j+1])
		table += "</table>"
		table += insert_edit_delete_btn( uuid, "" )
		table += "</div>"
	return table

