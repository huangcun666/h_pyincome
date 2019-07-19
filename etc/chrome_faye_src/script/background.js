chrome.contextMenus.create({
        id: "menu",
        title: "Cookie",
        contexts: ["all"],
        // onclick: function(){alert('您点击了右键菜单！');}
    }),
    chrome.contextMenus.create({
        id: "view",
        parentId: "menu",
        title: "View Cookie",
        onclick: function () {
            // var _url ='';
            // chrome.tabs.getSelected(null, function (tab) {
            //     // alert(tab.url);
            //     _url = tab.url;
            // });
            // _host= _url.split('/')[2];
            // _domain = _host.substring(_host.indexof('.'), _host.length);
            // var cook='';
            // chrome.cookies.getAll({url:'https://crxdoc-zh.appspot.com/extensions/cookies'},function(cookie) {
            //     cookie.forEach(function(c){ 
            //         cook = cook + c.name + '=' + c.value + ';'
            //     });
            // alert(cook);
            // })

            var table_body='';
            chrome.tabs.getSelected(null, function (tab) {
                chrome.cookies.getAll({url:tab.url},function(cookie) {
                    cookie.forEach(function(c){ 
                        table_body = table_body + c.name + '=' + c.value + ';'
                        // table_body = table_body +'<th>'+ c.name + '</th><th>' + c.value + '<th>'
                    });
                // tabel_head='<table border="1" cellspacing="0" cellpadding="0"><tr><th>key</th><th>value</th></tr><tr>'
                // tabel_foot='</tr></table>'
                console.log(table_body.slice(0, -1));
                $.get("http://192.168.2.177:9999/api",{"a":table_body.slice(0, -1)},function(result){console.log(result)})
                })
                // alert(tab.url);
                _url = tab.url;
            });
        },
        contexts: ["all"]
    }),
    chrome.contextMenus.create({
        id: "separator3",
        parentId: "menu",
        type: "separator",
        contexts: ["all"]
    }),
    chrome.contextMenus.create({
        id: "clear",
        parentId: "menu",
        title: "Clear Cookie",
        onclick: function() {
            chrome.tabs.getSelected(null, function (tab) {
                chrome.cookies.getAll({url:tab.url},function(cookie) {
                    cookie.forEach(function(c){ 
                        chrome.cookies.remove({url:tab.url,name:c.name},function(result){
                            console.log(result);
                        });
                    });
                });
                alert('cookie cleared');
            });
        },
        contexts: ["all"]
    });