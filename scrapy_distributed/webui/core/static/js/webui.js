$(function () {
    $('form').on('click', '.add', function () {
        var $form_group = $(this).closest('.form-group');
        var $btn = $(this).closest('div').clone();
        var $input = $(this).closest('div').prev().clone();
        $input.addClass('col-md-offset-2').find('input').val('');
        $input.find('textarea').text('');
        $btn.find('.add').attr({'class': 'btn btn-danger btn-xs del', 'value': 'delete'});
        $input.appendTo($form_group);
        $btn.appendTo($form_group);
    }).on('click', '.del', function () {
        $(this).closest('div').prev().remove();
        $(this).closest('div').remove();
    });
    $('.del-form').on('click', '.remove', function () {
        $('#modal').modal({
            keyboard: true
        });
        $form = $(this).closest('.del-form');
        console.log($form);
        $('#modal').on('click', '.remove', function () {
            console.log('xxxxxx');
            $form.submit();
        });
    });

});