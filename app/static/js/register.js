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
        dataType: 'html',      //改为返回json，{'status':'messgge'}
        success: function (data) {
            $('#registerModal').modal('hide');
            if(data === 'success'){
                html = "<div class=\"alert alert-success alert-dismissible\" style=\"height: 50px;text-align: center\">Register Successful!<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
            }
            else{
                html = "<div class=\"alert alert-warning alert-dismissible\" style=\"height: 50px;text-align: center\">Register Failed!Exist the same Username or Email!<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
            }
        }
    });
}
