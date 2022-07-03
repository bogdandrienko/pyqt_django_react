import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import "./css/my.css";
import "./css/bootstrap/bootstrap.css";
import HomePage from './pages/HomePage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />}>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
