// 注册账户
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


// 更新上传文件输入框的显示内容
$('.custom-file-input').on('change', function () {
   let filename = $(this).val().split('\\').pop();
   $(this).next('.custom-file-label').addClass("selected").html(filename);
});


// 分析csv格式的Nessus扫描结果
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


// 新增漏洞记录
function AddRecordInfo(url) {
    let form_data = $('#addRecord').serialize();
    console.log(form_data);
    $.ajax({
        url: url,
        type: 'POST',
        data: form_data,
        dataType: 'json',
        success: function (data) {
            $('#addRecordInfoModal').modal('hide');
            if('success' in data){
                let html = "<div class=\"alert alert-success alert-dismissible\" style=\"height: 50px;text-align: center\">" + data['success'] + "<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
                $('#vulName').val("");
                $('#nessusPluginID').val("");
                $('#vulLink').val("");
                $('#detailInfo').val("");
            }
            if('failed' in data){
                let html = "<div class=\"alert alert-danger alert-dismissible\" style=\"height: 50px;text-align: center\">" + data['failed'] + "<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
                $('#vulName').val("");
                $('#nessusPluginID').val("");
                $('#vulLink').val("");
                $('#detailInfo').val("");
            }
            if('warning' in data){
                let html = "<div class=\"alert alert-warning alert-dismissible\" style=\"height: 50px;text-align: center\">" + data['warning'] + "<button type=\"button\" class=\"close\" data-dismiss=\"alert\"><span aria-hidden=\"true\">&times;</span></button></div>";
                $('#message').html(html);
            }
        }
    })
}


// 刷新当前页面
function refresh() {
    window.location.reload();
}
