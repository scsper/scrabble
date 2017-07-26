import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/app';
import {createStore} from 'redux';
import {Provider} from 'react-redux';
import rootReducer from './reducers/index';
import {ActionTypes} from './constants';

const store = createStore(rootReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());
store.dispatch({type: ActionTypes.INITIAL_STATE});
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);

