import React, { useState, useEffect } from 'react';
import { Menu, Spin } from 'antd';
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import axios from "axios";

import TrackCarousel from './components/TrackCarousel';
import LocationCard from './components/LocationCard';
import TrackCard from './components/TrackCard';

const item_home = [
  {
    key: 'home',
    icon: (
      <Link to="/">
        <img src="../static/logo.png" alt="logo.png" border="0" />
      </Link>
    )
  },
];

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

  const handleClick = (e) => {

  };

  return (
    <Router>
      <div>
        <Menu onClick={handleClick} selectedKeys={['home']} mode="horizontal" items={item_home} />
        <TrackCarousel />
        <div className="mx-auto my-auto">
          <Switch>
            <Route path="/location/:locationId">
              <TrackCard />
            </Route>
            <Route path="/">
              {isLoading ? <Spin size="large" /> : <LocationCard locations={locations} />}
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
