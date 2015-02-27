%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Учебные материалы, список</h2>
	  %include add_btn action="./materials/add"
	  %include refresh_btn action="./materials"
	  <div id="material_list" class="UI_list">
          %include table headers = headers, width= width, data = data, editable = True, action = "./materials/"
	  </div>
	</div>
	</div>
	</div>
%include footer
