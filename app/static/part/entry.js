var Router = require('react-router').Router
var Route = require('react-router').Route
var Switch = require('react-router').Switch

var Sub = React.createClass({
    getInitialState:function () {
        return {
            click:false
        };
    },

    handleClick:function () {
        this.setState({click:!this.state.click})
    },

    render:function () {
        if(this.state.click){

        }
        return <button onClick={this.handleClick}>Let me in.{this.state.click}</button>
    }
});

ReactDOM.render(
    (<Router history={hashHistory}>
    <Router path = '/' component="{App}"/>
    </Router>),
     document.getElementsByClassName('login')[0]
);



var Entry = React.createClass({
    render:function () {
        return <div>
	    <h1>{this.props.title}</h1>
        <form method="post">
    	<input type="text" name="u" placeholder="Username" required="required" />
        <input type="password" name="p" placeholder="Password" required="required" />
        <Sub/>
        </form>
        </div>
    }
});

ReactDOM.render(
    <Entry title="登陆"/>,
    document.getElementsByClassName('login')[0]
);