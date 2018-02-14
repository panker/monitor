define(["jquery-3.2.1.min",'app/static/js/react','app/static/js/react-dom','app/static/js/browser.min'],function (jquery , React , ReactDOM) {
    function fun(){
      ReactDOM.render(
          <div>12133</div>,
          document.getElementsByClassName('login')[0])
    }
    return   {
           fun:fun
    }

});