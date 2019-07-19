
function fullChar2halfChar(result) {

    return result.replace("（", "(").replace("）", ")") ;
}
    $(function () {


        $.get("/project?tag=get_trans_count", {}, function (data) {
            if (data > 0) {

                $.notify({
                    icon: '/static/77.png',
                    title: '来自岑美凤的提醒',
                    allow_dismiss:true,
                    message: '<a href="/project?status=0&tag=projects_transition&is_inner=1">您好! 您当前' + data + '份资料交接待确认,尽快确认哦,谢谢!</a>',
                   
                }, {
                        animate: {
                            enter: 'animated lightSpeedIn',
                            exit: 'animated lightSpeedOut'
                        },
                        type: 'minimalist',
                       
                        placement: {
                            from: 'top',
                            align: 'right'
                        },
                        offset: 55, spacing: 5,
                        delay: 500000,
                        icon_type: 'image',
                        
                        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                            '<img data-notify="icon" class="img-circle pull-left">' +
                            '<span data-notify="title">{1}</span>' +
                            '<span data-notify="message">{2}</span>' +
                            '</div>'
                    });


            }

        })
        $.get("/project?tag=get_trans_daijie_count", {}, function (data) {
            if (data['count'] > 0) {

                $.notify({
                    icon: '/static/77.png',
                    title: '订单流转待接提醒',
                    allow_dismiss:true,
                    message: '<a href='+data["url"]+'>您好! 您当前有' + data['count'] + '条待接单,尽快接单哦,谢谢!</a>',
                   
                }, {
                        animate: {
                            enter: 'animated lightSpeedIn',
                            exit: 'animated lightSpeedOut'
                        },
                        type: 'minimalist',
                       
                        placement: {
                            from: 'top',
                            align: 'right'
                        },
                        offset: 55, spacing: 5,
                        delay: 500000,
                        icon_type: 'image',
                        
                        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                            '<img data-notify="icon" class="img-circle pull-left">' +
                            '<span data-notify="title">{1}</span>' +
                            '<span data-notify="message">{2}</span>' +
                            '</div>'
                    });


            }

        })
        $.get("/project?tag=get_project_reject", {}, function (data) {
          
            if (data['c']!='0') {
                $.notify({
                    icon: '/static/77.png',
                    title: '确认单信息填写错误'+data['txt'],
                    allow_dismiss:true,
                    message: '<a href="/project?tag=project_reject&step='+data['step']+'&my=1">您好! 您当前有' + data['c'] + '条'+data['txt']+',尽快处理哦,谢谢!</a>',
                   
                }, {
                        animate: {
                            enter: 'animated lightSpeedIn',
                            exit: 'animated lightSpeedOut'
                        },
                        type: 'minimalist',
                       
                        placement: {
                            from: 'top',
                            align: 'right'
                        },
                        offset: 55, spacing: 5,
                        delay: 500000,
                        icon_type: 'image',
                        
                        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                            '<img data-notify="icon" class="img-circle pull-left">' +
                            '<span data-notify="title">{1}</span>' +
                            '<span data-notify="message">{2}</span>' +
                            '</div>'
                    });


            }

        })
    })
