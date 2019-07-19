
$(function(){
  // 获取多个cookie，并设置到当前插件页面下
  curr_url = $(location).attr('href');



      // content.js

      if(curr_url.indexOf("?bszmFrom=1&ticket=")> 0){
          // launchPlugin();
          // function launchPlugin() {
          //   if($("#userName").text()!=""){
          //         site_company = $("#userName").text().replace("欢迎，","")
          //         console.log(site_company+"ok")
          //         company = localStorage.getItem("company")
            
          //   } else{
          //     setTimeout(
          //       function(){
          //         launchPlugin();
          //       }, 3000);
          //   }
        
        
          // }

          var timeout = setTimeout(function()
          {
              
            if($("#userName").text()!=""){
                site_company = $("#userName").text().replace("欢迎，","")
                console.log(site_company+"ok")
                company = localStorage.getItem("company")
                customer_id = localStorage.getItem("customer_id")
                site_company = site_company.replace("（","(").replace("）",")")
                if(site_company==company){
                    chrome.runtime.sendMessage({greeting: "您好","customer_id":customer_id,"company":company}, function(response) {
                      console.log(response.farewell);
          
                      console.log(company)
                      console.log(customer_id)
                    });
                }else{
                    if( confirm("发业辅助助手提醒您: 当期操作客户("+site_company+") 与管理系统("+company+")不一致,请确认是否有误! ")){


                    }
                }
              } 


          }, 1000);
      }
      else if (curr_url.indexOf("/web-sbzs/nssb/printPdf2.do") > 0 ){
          ht =  document.documentElement.innerHTML
          start  = ht.indexOf('pdfURL ="')+9
          console.log(start)
          rm_start  = ht.slice(start)
          end  = rm_start.indexOf('"')
          rm_start  = rm_start.slice(0,end)
          go_url = "https://www.etax-gd.gov.cn"+rm_start
          location.href=go_url
      }
      else if (curr_url.indexOf("/sso/login") > 0 ){
          //  if(curr_url.indexOf("&tt=")>0){
          // var umsg = curr_url.slice(curr_url.lastIndexOf("&tt=")+4)
             
          //     var decodedString = atob(umsg);
          //     var arr = decodedString.split("|")
          //     var user = decodeURIComponent(arr[0])
          //     var pwd = arr[1]
      
          //     console.log(user); // Outputs: "Hello World!"
          //     $("#userName").val(user)
          //     $("#passWord").val(pwd)
     
          //     let a = localStorage.getItem('a');
          //     if (!a) {
          //       localStorage.setItem('a', user);
          //     }
              
              
          // }
          if(curr_url.lastIndexOf("&tt=")>0){
            
          var umsg = curr_url.slice(curr_url.indexOf("&tt=")+4)
         // var decodedString = atob(umsg);
           var arr = decodedString.split("|")
           var user = decodeURIComponent(arr[0])
           var pwd = arr[1]
           var company = decodeURIComponent(arr[2])
           var customer_id=arr[3]
         
           localStorage.setItem('user', user);
           localStorage.setItem('pwd', pwd);
           localStorage.setItem('company', company);
           localStorage.setItem('customer_id', customer_id);

           $("#userName").val(user)
           $("#passWord").val(pwd)
  
           company = localStorage.getItem("company")
   
          }else{
  
            company = localStorage.getItem("company")
  
      
                  user  = localStorage.getItem("user")
                  pwd = localStorage.getItem("pwd")
                  $("#userName").val(user)
                  $("#passWord").val(pwd)

           
          }
  
      }
      else if(curr_url.lastIndexOf("/xxmh/html/index.html") > 0 ){
          is_login = localStorage.getItem("is_login")
          if(is_login=="1"){
              localStorage.setItem('is_login', 0);
              location.href="https://www.etax-gd.gov.cn/sso/login?service=https://www.etax-gd.gov.cn/xxmh/html/index_login.html?bszmFrom=1&t=1562144801212"
  
          }
      
          company = localStorage.getItem("company")
          customer_id = localStorage.getItem("customer_id")
          console.log(company)
          console.log(customer_id)
      }
    else if(curr_url.lastIndexOf("index_login.html?tt=") > 0 ){
  
          var umsg = curr_url.slice(curr_url.indexOf("?tt=")+4)
           
              var decodedString = atob(umsg);
              var arr = decodedString.split("|")
              var user = decodeURIComponent(arr[0])
              var pwd = arr[1]
                localStorage.setItem('user', user);
                localStorage.setItem('pwd', pwd);
                localStorage.setItem('is_login', 1);
                var company = decodeURIComponent(arr[2])
                var customer_id=arr[3]
                localStorage.setItem('company', company);
                localStorage.setItem('customer_id', customer_id);
             
               location.href="https://www.etax-gd.gov.cn/sso/logout?service=https%3a%2f%2fwww.etax-gd.gov.cn%2fsso%2flogin"
     
          
  
  
    }else if(curr_url.lastIndexOf("index_login.html") > 0 ){

    }


    
    })
  
