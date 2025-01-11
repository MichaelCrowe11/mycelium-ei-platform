# Mycelium EI System API Documentation

## Overview
The Mycelium EI System provides REST APIs for managing sensor data, AI predictions, and autonomous drone deployment. These APIs facilitate seamless integration with external systems and real-time monitoring.

---

## Base URL
`https://api.mycelium-ei.io/v1`

---

## Endpoints

### 1. **Sensor Data Ingestion**
**POST** `/sensors/data`
- **Description**: Submit real-time environmental data from sensors.
- **Headers**:
  - `Authorization`: `Bearer <API_KEY>`
- **Body Parameters**:
  ```json
  {
    "temperature": 35,
    "humidity": 40,
    "co2": 600,
    "region_code": 1,
    "vegetation_type": 3
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Data received successfully."
  }
  ```

---

### 2. **Risk Prediction**
**POST** `/ai/predict`
- **Description**: Predict the risk level for a given dataset.
- **Headers**:
  - `Authorization`: `Bearer <API_KEY>`
- **Body Parameters**:
  ```json
  {
    "temperature": 35,
    "humidity": 40,
    "co2": 600,
    "region_code": 1,
    "vegetation_type": 3
  }
  ```
- **Response**:
  ```json
  {
    "risk_level": 0.75,
    "recommendation": "Deploy drones to target location."
  }
  ```

---

### 3. **Drone Deployment**
**POST** `/drones/deploy`
- **Description**: Deploy drones to a target location for specific tasks.
- **Headers**:
  - `Authorization`: `Bearer <API_KEY>`
- **Body Parameters**:
  ```json
  {
    "task": "Disperse Mycelium Broth",
    "location": {
      "latitude": 34.0528,
      "longitude": -118.2439
    }
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Drone deployment initiated.",
    "drone_id": 1
  }
  ```

---

## Authentication
- **API Key**:
  - Every request requires a valid API key for authentication.
- To request an API key, contact: `api-support@mycelium-ei.com`

---

## Error Codes
- **401 Unauthorized**: Invalid or missing API key.
- **400 Bad Request**: Invalid input parameters.
- **500 Internal Server Error**: Server-side issue.

---

## Rate Limits
- **Requests per minute**: 60
- **Burst capacity**: 100

---

## Support
For API-related queries or issues, contact:
- **Email**: api-support@mycelium-ei.com
- **Website**: [www.mycelium-ei.io](https://www.mycelium-ei.io)
