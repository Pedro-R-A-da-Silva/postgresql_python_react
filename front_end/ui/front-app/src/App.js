import React from 'react';

import {BrowserRouter as Router ,Route, Routes, NavLink} from 'react-router-dom';

import './App.css';
import {Home} from './Home';
import {Cadastro} from './Cadastro';
import {AtualizarFuncionario} from './AtualizarFuncionario';
import { Listagem } from './Listagem';


const App = () => {
  return (
    <Router>
    <div className="App container">
      <h3 className = "d-flex justify-content-center m-3">
        React JS front_end
      </h3>
    
    <nav className='navbar navbar-expand-sm bg-light navbar-dark'>
      <ul className='navbar-nav'>
        <li className='nav-item- m-1'>
          <NavLink className='btn btn-light btn-outline-primary' to='/Home'> 
            Home
          </NavLink>
          
        </li>
        <li className='nav-item- m-1'>
          <NavLink className='btn btn-light btn-outline-primary' to='/Cadastro'> 
            Cadastro
          </NavLink>
          
        </li>
        <li className='nav-item- m-1'>
          <NavLink className='btn btn-light btn-outline-primary' to='/AtualizarFuncionario'> 
            Atualizar Funcionario
          </NavLink>
          
        </li>
        <li className='nav-item- m-1'>
          <NavLink className='btn btn-light btn-outline-primary' to='/Listagem'> 
            Listagem Funcionarios
          </NavLink>
          
        </li>

      </ul>

    </nav>
    <Routes>
      <Route exact path='/Home' element = {<Home/>} />
      <Route exact path='/Cadastro' element = {<Cadastro/>} />
      <Route exact path='/AtualizarFuncionario' element = {<AtualizarFuncionario/>} />
      <Route exact path='/Listagem' element = {<Listagem/>} />
      </Routes>
    </div>

    </Router>
  );
}

export default App;
