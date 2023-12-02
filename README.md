# CSE6242OAN-LoL-Project

## Introduction

This project offers a comprehensive League of Legends (LoL) match outcome prediction tool, featuring a machine learning backend and a user-friendly frontend. The backend utilizes a logistic regression model trained on LoL champion statistics and matchup data to predict match outcomes. The frontend provides an interactive interface for users to input match configurations and receive predictions.

---

## Prerequisites

Before running the application, ensure you have Docker and Docker Compose installed on your system. These tools are required to build and run the application containers.

---

## Installation and Setup

1. **Build the Application:**
   
   Run the following commands to build the backend and frontend services:

   ```bash
   docker-compose build
   docker-compose up
   ```
   This process creates two containers - one for the backend (running on port 8080) and one for the frontend (running on port 8081).

2. **Accessing the Application:**

    Navigate to http://localhost:8081/ in your web browser to interact with the frontend application.

---

## Backend Overview

The backend is developed in Python using Flask and is containerized using Docker for easy deployment and scalability. It loads a pre-trained logistic regression model to make predictions based on the input received from the frontend.

---

## Key Components

### Model Initialization:
Upon startup (/ endpoint), the backend initializes global variables and loads the logistic regression model along with necessary data structures for prediction.

### Prediction Endpoint:

The /predict POST endpoint accepts match configuration data and a specified role, returning the top 5 champion predictions and the current champion's probability.

### Error Handling:

The application includes basic error handling to manage any issues during prediction.

---

## Frontend Overview
The frontend provides an intuitive interface allowing users to select champions and roles, sending this data to the backend for prediction.

---

### Docker Configuration
The application uses Docker Compose to manage multi-container Docker applications, orchestrating the build and deployment of both frontend and backend services.

### Docker Compose
The docker-compose.yml file defines the services, networks, and volumes for the application. It ensures the backend and frontend are correctly networked and can communicate seamlessly.

### Dockerfiles
Separate Dockerfiles for backend and frontend specify the environment setup, including installing dependencies and setting up the working directory.

### Requirements
The requirements.txt file lists all Python dependencies required by the backend.

---

## Usage

Before proceeding, ensure that you have completed the [Installation and Setup](#installation-and-setup) steps.

- To predict match outcomes, select champions and roles on the frontend and submit your configuration.
- The backend processes the request and sends back predictions, which are displayed on the frontend.

For detailed steps on how to build and run the application, refer back to the [Installation and Setup](#installation-and-setup) section.

---

## Additional Information
The project's backend is based on extensive exploratory data analysis (EDA) and model training detailed in `EDA/Final_Final_Python1.ipynb.`
For an in-depth understanding of the model creation and training process, refer to this notebook.The logistic regression model used in the backend is pre-trained and saved, loaded at runtime for efficient predictions.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, create a new branch for your work, and open a pull request.

## License

[MIT License](LICENSE)

## Contact



