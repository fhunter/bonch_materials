<div class="edit_delete_button"><table><tr><td>
	<form action="{{action}}" method="post">
		<input type="hidden" name="uuid" value="{{uuid}}"/>
		<input type="hidden" name="action" value="edit"/>
		<input type=submit value="Редактировать"/>
	</form>
	</td><td>
	<form action="{{action}}" method="post">
		<input type="hidden" name="uuid" value="{{uuid}}"/>
		<input type="hidden" name="action" value="delete"/>
		<input type=submit value="Удалить"/>
	</form>
	</tr></table>
</div>
