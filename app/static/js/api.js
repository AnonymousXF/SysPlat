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

$('.custom-file-input').on('change', function () {
   let filename = $(this).val().split('\\').pop();
   $(this).next('.custom-file-label').addClass("selected").html(filename);
});


function Analysis(url){
    // 获取选择的文件
    let file_obj = $('#scanResultFile').get(0).files[0];

    // 将文件对象打包成form表单类型数据
    let data = new FormData;
    data.append('file', file_obj);
    data.append('level', $('#vul_level').val());

    // 上传文件数据，并进行分析
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        processData:false,
        contentType:false,
        dataType: 'html',
        success: function (data) {
            $('#nessus_result').html(data);
        },
        error: function () {
            $('#nessus_result').html('分析失败！');
        }
    });
}
