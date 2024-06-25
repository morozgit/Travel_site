import React, { useState, useEffect } from 'react';
import {Route, useParams} from 'react-router-dom';
import { Card, Row, Col, Spin } from "antd";
import axios from 'axios';

function TrackCard() {
  const { locationId } = useParams();
  const [tracks, setTracks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchTracks();
  }, [locationId]);

  const fetchTracks = () => {
    setIsLoading(true);
    axios.get(`http://127.0.0.1:8000/track/location/${locationId}`)
      .then(response => {
        setTracks(response.data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
        setIsLoading(false);
      });
  };

  const handleImageError = (e) => {
    console.log('Клик ', e);
  };

  return (
    <div>
      {isLoading ? (
        <Spin size="large" />
      ) : (
        <Row gutter={[16, 16]}>
          {tracks.map(track => {
            return (
              <Col key={track.id} xs={24} sm={12} md={8} lg={6}>
                <Card
                  title={track.name}
                  style={{ width: '100%' }}
                >
                  <p>{track.name}</p>
                  <img src={`../${track.image}`} alt={track.name}/>
                  <p>{track.description}</p>
                </Card>
              </Col>
            );
          })}
        </Row>
      )}
    </div>
  );
}

export default TrackCard;
