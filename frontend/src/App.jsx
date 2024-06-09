import React, { useState, useEffect } from 'react';
import { Spin } from 'antd';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import axios from "axios";

import LocationCard from './components/LocationCard';
import TrackCard from './components/TrackCard';
import Header from './components/Header';
import styled from 'styled-components';

const AppContainer = styled.div`
  width: 100%;
  overflow-x: hidden; // Предотвращаем горизонтальную прокрутку
`;

const ContentContainer = styled.div`
  position: relative;
  z-index: 3; // Задаем z-index выше, чтобы контент был поверх карусели
`;

// Стили для параллакс-контейнера
const ParallaxContainer = styled.div`
  background: url('../static/noch-luna-planeta.png') no-repeat center center fixed;
  background-size: cover;
  height: 100%;
  position: absolute;
  width: 100%;
`;

const ParallaxOverlay = styled.div`
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  z-index: 1; // Устанавливаем z-index для наложения
`;

function App() {
  const [locations, setLocations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchLocations();
  }, []);

  const fetchLocations = () => {
    setIsLoading(true);
    axios.get('http://127.0.0.1:8000/location/all_location')
      .then(response => {
        setLocations(response.data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
        setIsLoading(false);
      });
  };


  return (
    <Router>
      <AppContainer>
        <Header />
        <ParallaxContainer>
            <ParallaxOverlay />
          </ParallaxContainer>
        <ContentContainer className="mx-auto my-auto">
          <Switch>
            <Route path="/location/:locationId">
              <TrackCard />
            </Route>
            <Route path="/">
              {isLoading ? <Spin size="large" /> : <LocationCard locations={locations} />}
            </Route>
          </Switch>
        </ContentContainer>
      </AppContainer>
    </Router>
  );
}

export default App;
