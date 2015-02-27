%include header
<div id="UI_elements">
	<div id="speciality_admin" class="UI_tab" >
		<h2>Управление списком специальностей</h2>
		%include add_btn action="./speciality/add"
		%include refresh_btn action="./speciality"
		<div id="speciality_list" class="UI_list">
      		%include table headers = headers, width= width, data = data, editable = True, action = "./speciality"
		</div>
	</div>
</div>
</div>
%include footer
