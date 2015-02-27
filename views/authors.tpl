%include header
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    <input name="authors_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?authors=show">  <button>Обновить</button></a>
	  </div>
	  <div id="author_list" class="UI_list">
	  <table border=1>
	  %for i in data:
	  	<tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
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
