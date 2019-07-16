function PostRegisterInfo(url) {
    let username = $('#registerUsername').val();
    let password = $('#registerPassword').val();
    let confirm = $('#registerConfirmPassword').val();
    let email = $('#registerEmail').val();
    let data = {
        'username': username,
        'password': password,
        'confirm':  confirm,
        'email': email
    };
    console.log(data);
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        dataType: 'json',
        success: function (data) {
            $('#registerModal').modal('hide');
            if('success' in data){
                let html = "<div class=\"alert alert-success alert-dismissible\" style=\"height: 50px;text-align: center\">" + data['success'] + "<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
            }
            if('failed' in data){
                let html = "<div class=\"alert alert-warning alert-dismissible\" style=\"height: 50px;text-align: center\">" + data['failed'] + "<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
            }
        }
    });
}
