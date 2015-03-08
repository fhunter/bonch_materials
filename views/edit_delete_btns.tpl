<div class="edit_delete_button"><table><tr>
	%if editable[0]:
	<td><a href="{{action}}/edit/{{uuid}}"><button>Редактировать</button></a></td>
	%end
	%if editable[1]:
	<td><a href="{{action}}/delete/{{uuid}}"><button>Удалить</button></a></td>
	%end
	</tr></table>
</div>
