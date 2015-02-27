%include header
  <div id="UI_elements">
      <div id="study_form_admin" class="UI_tab" >
      <h2>Управление списком форм обучения</h2>
      %include add_btn action=""
      <div class="add_form">
      <form id="study_form_add_form" method="post" action="">
	<input type="hidden" name="action" value="add"/>
	<input name="study_form_name">
	<input type=submit value="Добавить">
      </form>
      </div>
      %include refresh_btn action="./study_form"
      <div id="study_form_list" class="UI_list">
      <table>
      %for i in data:
      	<tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
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
