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
		<div class="refresh_button">
			<a href="./speciality">  <button>Обновить</button></a>
		</div>
		<div id="speciality_list" class="UI_list">
      			<table>
		      %for i in data:
		      	<tr>
				<td>{{i[0]}}</td>
				<td>{{i[1]}}</td>
				<td>{{i[2]}}</td>
				<td>
					%include edit_delete_btns action = "", uuid = i[0]
				</td>
			</tr>
		      %end
		      </table>
		</div>
	</div>
</div>
</div>
%include footer
