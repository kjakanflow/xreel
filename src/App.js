// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MainPage from 'components\mainpage';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" component={MainPage} />
          {/* Define other routes and components */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
