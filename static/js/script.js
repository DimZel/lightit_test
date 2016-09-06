/**
 * Created by dimze on 04.09.2016.
 */


$('.comment').click(function () {
    var form = $('form');
    form.attr('action', 'add_comment/');
    form.find('textarea').val('');
    $(this).parent().append(form);
    var comment_id = $(this).data('comment');
    form.find('[name="parent"]').attr('value', comment_id);
    $('#cancel_btn').show();
});

$('#cancel_btn').click(function () {
    var form = $('form');
    form.attr('action', 'add_comment/');
    $('#form_origin').append(form);
    form.find('[name="parent"]').attr('value', '');
    $(this).hide();
});

$('.fa-edit').click(function () {
    var form = $('form');
    form.attr('action', 'edit_comment/');
    $(this).parent().append(form);
    var text = $(this).parent().children('.text').html();
    form.find('textarea').val(text);
    var comment_id = $(this).data('comment');
    var parent_id = $(this).data('parent');
    form.find('[name="id"]').attr('value', comment_id);
    form.find('[name="parent"]').attr('value', parent_id);
    $('#cancel_btn').show();
});