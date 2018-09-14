$(function(){
    $('.delete').click(function(){
        var id=$(this).attr('id');
        var name=$(this).attr('name');
        var del_btn=$('.delete_btn');
        del_btn.attr('id',id);
        $('#alert').text('删除订单'+name+'?');
    });
    $('.delete_btn').click(function () {
        var id=$(this).attr('id');
        $.get(
            'http://192.168.2.71:8888/delete/'+id,
            function (data) {
               $('tr[id='+id+']').remove();
             }
        )
        $("#close_btn").click();
      })
    $('.customer_delete').click(function () { 
        var id=$(this).attr('id');
        var name=$(this).attr('name');
        var del_btn=$('.customer_delete_btn');
        del_btn.attr('id',id);
        $('#alert').text('删除客户'+name+'?');
     })
     $('.customer_delete_btn').click(function () { 
        var id=$(this).attr('id');
        $.get(
            'http://192.168.2.71:8888/customer_delete/'+id,
            function (data) {
               $('tr[id='+id+']').remove();
             }
        )
        $("#customer_close_btn").click();
      })

    $('.out_delete').click(function () { 
        var id=$(this).attr('id');
        var name=$(this).attr('name');
        var del_btn=$('.out_delete_btn');
        del_btn.attr('id',id);
        $('#alert').text('删除编号为'+name+'的出库单'+'?');
       })

    $('.out_delete_btn').click(function () { 
        var id=$(this).attr('id');
        $.get(
            'http://192.168.2.71:8888/out_delete/'+id,
            function (data) {
               $('tr[id='+id+']').remove();
             }
        )
        $("#customer_close_btn").click();
      })
  
    

    if($('#error_model').length>0){
        $('#error_model').append('<a  style="display:none;" '+
        'class="btn btn-danger error_model" type="button" data-toggle="modal" data-target="#error_model">删除</a>')
        $('.error_model').click();
    }
    
    if($('#cus_id').val()==''){
        var id=$('.error_id').text();
        $('.error_id').remove();  
        if(id!=''){
        var notfound='<div id="alert_btn" class="alert alert-warning"'+
            'role="alert">温馨提示：你要创建的收据订单编号【'+id+'】不存在</div>';
        $('#cus_id').parents('form').before(notfound);
        setTimeout(function(){
            $('#alert_btn').hide(1000);
        },3000);  
        }
    }
    
    var id=$('.error_message').text();
    if(id!=''){
        var notfound='<div id="alert_btn" class="alert alert-warning"'+
        'role="alert">温馨提示：编号为【'+id+'】的客户订单已经存在</div>';
        $('#customer_id').parents('form').before(notfound);
        setTimeout(function(){
        $('#alert_btn').hide(1000);
        },3000);  
    }
    
    var id=$('.error_repetition').text();
    if(id!=''){
        var notfound='<div id="alert_btn" class="alert alert-warning"'+
        'role="alert">温馨提示：编号为【'+id+'】的收据订单已经存在</div>';
        $('#cus_id').parents('form').before(notfound);
        setTimeout(function(){
        $('#alert_btn').hide(1000);
        },3000);  
    }

    var id=$('.repeat_id').text();
    if(id!=''){
        var notfound='<div id="alert_btn" class="alert alert-warning"'+
        'role="alert">温馨提示：编号为【'+id+'】的收据订单已经存在</div>';
        $('#cus_id').parents('form').before(notfound);
        setTimeout(function(){
        $('#alert_btn').hide(1000);
        },3000);  
    }

    $('#customer_btn').click(function () { 
        $(this).css({'font-size':'24px'});
        $('#receipt_btn').css({'font-size':'20px'});
        $('#out_btn').css({'font-size':'20px'});
     })
     $('#receipt_btn').click(function () { 
        $(this).css({'font-size':'24px'});
        $('#customer_btn').css({'font-size':'20px'});
        $('#out_btn').css({'font-size':'20px'});
     })
     $('#out_btn').click(function () { 
        $(this).css({'font-size':'24px'});
        $('#customer_btn').css({'font-size':'20px'});
        $('#receipt_btn').css({'font-size':'20px'});
     })
    $('#customer_id').blur(function () { 
        var value=$(this).val();
        $('#alert_customer_id').remove();
        if(value){
            if(isNaN(value)){
                $(this).parent().append('<p class="text-danger" id="alert_customer_id">客户编号必须为数字</p>');
            }else{
                $('#alert_customer_id').remove();
            }
        }
     })
     $('#cus_id').blur(function () { 
        var value=$(this).val();
        $('#alert_customer_id').remove();
        if(value){
            if(isNaN(value)){
                $(this).parent().append('<p class="text-danger" id="alert_customer_id">客户编号必须为数字</p>');
            }else{
                $('#alert_customer_id').remove();
            }
        }
     })
    
})
