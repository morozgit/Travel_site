import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const HeaderContainer = styled.header`
  width: 100%; // Устанавливаем ширину заголовка на 100%
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #fff;
`;

const Nav = styled.nav`
  display: flex;
  gap: 20px;
`;

const NavLink = styled(Link)`
  text-decoration: none;
  color: #333;
  font-weight: 500;

  &:hover {
    color: #0073e6;
  }
`;

const Logo = styled.img`
  max-width: 100%;
  height: auto;
`;

const Header = () => (
  <HeaderContainer>
    <Logo src="../static/logo.png" alt="logo" />
    <Nav>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/about">About</NavLink>
      <NavLink to="/services">Services</NavLink>
      <NavLink to="/contact">Contact</NavLink>
    </Nav>
  </HeaderContainer>
);

export default Header;
