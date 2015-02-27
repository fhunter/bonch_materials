# vim: set fileencoding=utf-8 :
import os

def is_post():
	if os.environ['REQUEST_METHOD'] == 'POST':
		return True
	return False

def gen_table_row(name, value ):
	text = u"<tr><td class=field_name>%s</td><td class=field_value>%s</td></tr>" % (name, value, )
	return text

def gen_table_row_wide( name, value ):
	text = u"<tr><td class=field_name>%s</td></tr><tr><td class=field_value colspan=2>%s</td></tr>" %( name, value, )
	return text

def gen_table(values, names, wide,edit=True,vertical=True):
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
		if edit:
			table += insert_edit_delete_btn( uuid, "" )
		table += "</div>"
	return table

