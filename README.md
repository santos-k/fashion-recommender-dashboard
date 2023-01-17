# Fashion Recommendation System
## Overview
The project is a neural network-based fashion recommendation system built using Python. The model used for this system is Resnet50, which is a deep learning model used for image recognition. The data used for training the model is scraped from Flipkart, with a total of 65,000 images.

The front-end of the system is designed using Python Dash, which is a web application framework for building interactive dashboards. The system is able to take a single image as input and display 10 results with live prices and ratings from Flipkart. It also includes a "buy" link that directs users to the product page on Flipkart.

In addition, the system has an analysis dashboard page that is fully customised. This page allows users to view various statistics and insights on the data used for training the model, such as the number of images per category and the distribution of ratings.

Overall, this project aims to provide users with a convenient and efficient way to find fashion products that are similar to an image they provide, with live prices and ratings from Flipkart. The customised analysis dashboard page also provides valuable insights for understanding the data used for training the model.

## Getting Started
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.6 or later
- TensorFlow 2.0 or later
- Keras 2.4 or later
- Python Dash
- Other dependencies are listed in requirements.txt

### Installation
1. Clone the repository to your local machine
   ```
   git clone https://github.com/santos-k/fashion-recommender-dashboard.git
   ```
2. Install the required packages
   ```
   pip install -r requirements.txt
   ```
### Running the System
1. Run the following command to start the web application
   ```
   python app.py
   ```
2. Open your web browser and navigate to http://localhost:port_no to access the system


## To deploy this project on Google Cloud Platform (GCP), you will need to follow these steps:

1. Create a new project on GCP by going to the GCP Console (https://console.cloud.google.com/) and selecting "Select a Project" or "Create Project".
2. Create a virtual machine instance by going to the GCP Console, selecting "Compute Engine", and clicking on "Create Instance".
3. Choose the appropriate machine type and configure it as per your requirements. Make sure to open the required ports for the application.
4. Once the virtual machine is created, connect to it using SSH by going to the GCP Console, selecting "Compute Engine", and clicking on "SSH" next to the instance.
5. Install the required packages on the virtual machine by running the command pip install -r requirements.txt.
6. Clone the repository to the virtual machine by running the command git clone https://github.com/username/fashion-recommendation-system.git.
7. Run the application by running the command python app.py
8. Assign a static IP to your instance and map it to the domain name of your choice for easy access.

The system should now be accessible by navigating to the domain name or the IP address of the virtual machine.
You can also use containerization tools such as Docker to deploy this project on GCP, but it is beyond the scope of this overview.


## To deploy this project on GCP, you will need the following files:
1. `app.py`: This is the main file that runs the web application. It contains the code for the neural network model, the front-end design using Python Dash, and the integration with Flipkart data.
2. `requirements.txt`: This file contains a list of all the dependencies required for the project. It includes packages such as TensorFlow, Keras, and Python Dash.
3. `model.h5`: This is the trained model file. It contains the weights and architecture of the Resnet50 model.
4. `data`: This folder contains the data used for training the model. It should include the scraped images and their corresponding labels.
5. `config.py`: This file contains the configuration settings for the project, such as the number of results to display and the Flipkart API key.
6. `Dockerfile` (Optional): This file is used to create a Docker image of the application. It contains instructions on how to build the image and what dependencies to install.
7. `deployment.yaml` (Optional): This file is used to deploy the application on GCP using Kubernetes. It contains instructions on how to create the necessary resources and configure the application.

Please make sure that these files are properly configured and in the correct location for successful deployment on GCP.


## To deploy this project on Heroku, you will need to follow these steps:
1. Create a new account on Heroku if you don't have one already.
2. Install the Heroku CLI by following the instructions on the [Heroku](https://devcenter.heroku.com/articles/heroku-cli) website.
3. Clone the repository to your local machine.
4. Create a new app on Heroku by running the command `heroku create` in the project directory.
5. Add the required buildpacks by running the command `heroku buildpacks:set heroku/python`
6. Push the code to Heroku by running the command `git push heroku master`
7. Create a new instance of PostgreSQL by running the command `heroku addons:create heroku-postgresql:hobby-dev`
8. Set the environment variables for the application by running the command `heroku config:set VARIABLE_NAME=value`
9. Open the app by running the command `heroku open`

- Note:
  - You will also need to add the `Procfile` file to your root directory. It is a file that tells Heroku how to run your application.
  - You will also need to add the `requirements.txt` file to your root directory.

You should now be able to access the application by going to the URL provided by Heroku.
Please make sure that these files are properly configured and in the correct location for successful deployment on Heroku.

## Authors
Santosh Kumar - [Github](https://github.com/santos-k/)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

### Don't forget to give a star if you find it helpful.
This system is made as a part of the project and is open for contributions and modifications.
