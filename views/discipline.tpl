%include header
      <div id="UI_elements">
	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  <div class="add_form">
	  <form id="discipline_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    Название:<input name="discipline_name"><br>
	    Семестр:<input name="discipline_semester"><br>
	    Описание:<br>
	    <textarea name="discipline_description"></textarea>
	    <br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./discipline">  <button>Обновить</button></a>
	  </div>
	  <div id="discipline_list" class="UI_list">
	  <table border=1>
	  %for i in data:
	  	<tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
		<td>{{i[3]}}</td>
		<td>
		%include edit_delete_btns action="", uuid=""
		</tr>
	  %end
	  </table>
	  </div>
	</div>
	</div>
	</div>
%include footer
