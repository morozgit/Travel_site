import { Card, Row, Col } from "antd";
import { Link } from 'react-router-dom';

function LocationCard(props) {
  const { locations } = props;

  return (
    <div>
      <Row gutter={[16, 16]}>
        {locations.map(location => (
          <Col key={location.id} xs={24} sm={12} md={8} lg={6}>
            <Card
              title={location.name}
              style={{ width: '100%' }}
            >
              <p>{location.description}</p>
              <img src={location.image} alt={location.name} style={{ width: '100%' }} />
              <Link to={`/location/${location.id}`}>Маршруты</Link>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default LocationCard;
