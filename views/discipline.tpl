%include header
      <div id="UI_elements">
	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  %include add_btn action="./discipline/add"
	  %include refresh_btn action="./discipline"
	  <div id="discipline_list" class="UI_list">
      	  %include table headers = headers, width= width, data = data, editable = [True, True], action = "./discipline"
	  </div>
	</div>
	</div>
	</div>
%include footer
