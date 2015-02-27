%include header
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
	  %include refresh_btn action="./materials"
	  <div id="material_list" class="UI_list">
	  <table border=1>
	  %for i in data:
	  	<tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
		<td>{{i[3]}}</td>
		<td>{{i[4]}}</td>
		<td>{{i[5]}}</td>
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
