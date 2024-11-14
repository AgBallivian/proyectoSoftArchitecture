
# Project: TTAIO Simulation Interface


## Prerequisites

- Docker should be installed on your system and running.


### 1. Build and Run the Containers

To build and start the application, use Docker Compose:

```bash
docker-compose up --build
```

This command will:
- Build the `api` service (Flask backend).
- Build the `user_interface` service (React frontend).

### 2. Access the Application

Once the containers are running, you can access the application in your web browser:

- **User Interface**: [http://localhost:3000](http://localhost:3000)

### 3. Stopping the Containers

To stop the containers, use:

```bash
docker-compose down
```

## API Endpoints

The API provides the following endpoints:

- **GET** `/get-options`: Fetches available options for models, hardware, and optimizations.
- **POST** `/choose-model`: Selects a model.
- **POST** `/choose-hardware-simulation`: Selects hardware for simulation.
- **POST** `/choose-optimization`: Selects an optimization.
- **POST** `/run-simulation`: Initiates the simulation with selected options.


## Options

- **Modifying Options**: You can change available models, hardware, and optimizations by editing the `api/options.json` file.
