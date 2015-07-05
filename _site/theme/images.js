$(function() {
	$('figure > img').each(function(index, value) {
		var el = $(value);
		var link = $('<a>', {
			href: el.attr('src'),
			target: '_blank'
		});
		link.insertBefore(el.parent());
		el.parent().detach();
		el.parent().appendTo(link);
	});
});
