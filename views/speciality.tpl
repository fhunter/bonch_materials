%include header
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
		%include refresh_btn action="./speciality"
		<div id="speciality_list" class="UI_list">
      		%include table headers = headers, width= width, data = data, editable = True
		</div>
	</div>
</div>
</div>
%include footer
