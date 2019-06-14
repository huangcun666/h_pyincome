
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
                    message: '<a href="/project?status=0&tag=projects_transition">您好! 您当前' + data + '份资料交接待确认,尽快确认哦,谢谢!</a>',
                   
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
