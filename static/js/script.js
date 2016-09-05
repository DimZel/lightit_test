/**
 * Created by dimze on 04.09.2016.
 */


$('.comment').click(function () {
    var form = $('form');
    $(this).parent().append(form);
    var comment_id = $(this).data('comment');
    form.find('[name="parent"]').attr('value', comment_id);
    $('#cancel_btn').show();
});

$('#cancel_btn').click(function () {
    var form = $('form');
    $('#form_origin').append(form);
    form.find('[name="parent"]').attr('value', '');
    $(this).hide();
});