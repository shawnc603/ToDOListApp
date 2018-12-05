function sendEmail(){ 
    alert('sending email');
    var form = document.getElementById("frmEmail");
    var emaildata = toJSONString(form);
    var userid = getCookie("userid");
    var objEmail = JSON.parse(emaildata);
    objEmail["userid"] = userid;

    var radioValue = $("input[name='transport_type']:checked").val();
    console.log(radiovalue);
    $.ajax({
        url: 'http://127.0.0.1:5000/sendEmail',
        type: 'POST',
        data:objEmail,            
        contentType: "application/json;charset=utf-8",
        headers:{
            'Access-Control-Allow-Origin':'*'
        },       		
        success: function(data, textStatus, jQxhr ){
            alert(JSON.stringify(data, undefined, 4));
            var obj = JSON.stringify(data);
            console.log(obj);
            if(data.status =="200")
            {
                window.location.href = "http://127.0.0.1:5000/main"
            }
            else
            {
   
            }
        },
        error: function( jqXhr, textStatus, errorThrown ){

        }
    });  
}
function registerUser(){ 
    var form = document.getElementById("frmRegisterUser");
    var userdata = toJSONString(form);
    console.log(userdata);
    
    $.ajax({
        url: 'http://127.0.0.1:5000/registerUser',
        type: 'POST',
        data:userdata,            
        contentType: "application/json;charset=utf-8",
        headers:{
            'Access-Control-Allow-Origin':'*'
        },       		
        success: function(data, textStatus, jQxhr ){
            alert(JSON.stringify(data, undefined, 4));
            var obj = JSON.stringify(data);
            console.log(obj);
            if(data.status =="200")
            {
                setCookie("userid", data.userid, 0.25);
                checkCookie();
                window.location.href = "http://127.0.0.1:5000/main"
            }
            else
            {
   
            }
        },
        error: function( jqXhr, textStatus, errorThrown ){

        }
    });  
}
function SubmitTasks(){ 
    var form = document.getElementById("frmAddTask");
    var taskdata = toJSONString(form);
    var userid = getCookie("userid");
    console.log('userid:' + userid);
    var objTask = JSON.parse(taskdata);
    objTask["userid"] = userid;
    console.log(objTask);
    $.ajax({
        url: 'http://127.0.0.1:5000/registerTask',
        type: 'POST',
        data: JSON.stringify(objTask),            
        contentType: "application/json;charset=utf-8",
        headers:{
            'Access-Control-Allow-Origin':'*'
        },       		
        success: function( data, textStatus, jQxhr ){
             alert(JSON.stringify(data, undefined, 4));
            //  $('#sucessAlert').val(JSON.stringify(data, undefined, 4));
            //  $('#sucessAlert').show();
            //  $('#errorAlert').hide();
             window.location.href = "http://127.0.0.1:5000/main"
        },
        error: function( jqXhr, textStatus, errorThrown ){

            console.log("error:"+ errorThrown );
        }
    });  
}
function login(){ 
    var form = document.getElementById("frmlogin");
    var userdata = toJSONString(form);
    console.log(userdata);
    
    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        type: 'POST',
        data:userdata,            
        contentType: "application/json;charset=utf-8",
        headers:{
            'Access-Control-Allow-Origin':'*'
        },       		
        success: function(data, textStatus, jQxhr ){
            alert(JSON.stringify(data, undefined, 4));
            if(data.status =="200")
            {
                console.log(data.userid);
                setCookie("userid", data.userid, 1);
                checkCookie();
                window.location.href = "http://127.0.0.1:5000/main"
            }
            else
            {
    
            }
        },
        error: function( jqXhr, textStatus, errorThrown ){

            console.log("error:"+ errorThrown );
        }
    });  
}
function toJSONString(form) {
    var obj = {};
    var elements = form.querySelectorAll("input, select, textarea");
    
    for( var i = 0; i < elements.length; ++i ) {
        var element = elements[i];
        var name = element.name;
        var value = element.value;
        console.log(name);
        console.log(value);
        if( name ) {
            obj[name] = value;
        }
    }
    return JSON.stringify(obj);
}      
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function deleteCookie() {
    var cookie=getCookie("userid");
    if (cookie != "") {
        cookie = "userid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    }         
}
