/**
 *  BootTree Treeview plugin for Bootstrap.
 *
 *  Based on BootSnipp TreeView Example by Sean Wessell
 *  URL:	http://bootsnipp.com/snippets/featured/bootstrap-30-treeview
 *
 *	Revised code by Leo "LeoV117" Myers
 *
 */
$.fn.extend({
	treeview:	function() {
		return this.each(function() {
			// Initialize the top levels;
			var tree = $(this);

			tree.addClass('treeview-tree');
			tree.find('li').each(function() {
				var stick = $(this);
			});
			tree.find('li').has("ul").each(function () {
				var branch = $(this); //li with children ul

				branch.children('div').prepend("<i class='tree-indicator fa fa-chevron-right'></i>");
				branch.addClass('tree-branch');

				branch.find('i').click(function (e) {
                    if (this == e.target) {
						var icon = $(this);
						icon.toggleClass("fa-chevron-down fa-chevron-right");
						$(this).parent().parent().children().children('li').toggle();
					}
				});
				branch.children().children('li').toggle();

				/**
				 *	The following snippet of code enables the treeview to
				 *	function when a button, indicator or anchor is clicked.
				 *
				 *	It also prevents the default function of an anchor and
				 *	a button from firing.
				 */
				branch.children('.tree-indicator, button, a').click(function(e) {
					branch.click();

					e.preventDefault();
				});
			});
		});
	}
});

/**
 *	The following snippet of code automatically converst
 *	any '.treeview' DOM elements into a treeview component.
 */
$('.treeview').each(function () {
	var tree = $(this);
	tree.treeview();
});

$('#expand-all').click(function () {
    if (!$(this).data("expanded")) {
        $('.tree-branch').each(function () {
            var icon = $(this).find('i');
            icon.attr("class", "tree-indicator fa fa-chevron-down");
            $(this).children().children('li').show();
        });
        $(this).html('Скрыть все');
        $(this).data("expanded", 1);
    }
    else {
        $('.tree-branch').each(function () {
            var icon = $(this).find('i');
            icon.attr("class", "tree-indicator fa fa-chevron-right");
            $(this).children().children('li').hide();
        });
        $(this).html('Показать все');
        $(this).data("expanded", 0);
    }
});

