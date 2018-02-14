require.config({
    paths:{
        'react':"/static/js/react",
        'react-dom':"/static/js/react-dom",
        'browser.min':'/static/js/browser.min',
        "login" : "login"
    }
});

require(['login'] ,function (login) {
    alert(login.login(1,1))
});