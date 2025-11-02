# Machine Learning Lifecycle


# Here is the link to the document you requested:




https://docs.google.com/document/d/1wY0260k_a-Qj1qquSAMIkp7uvi4J1OVZCt9caI6No1Q/edit?usp=sharing




# Machine Learning Lifecycle: House Price Prediction Model
# Name: Sisi Anitah
#  Course: Machine Learning / Data Science
#  Date: 31/10/2025
#  Instructor: Aniebiet

https://docs.google.com/document/d/1wY0260k_a-Qj1qquSAMIkp7uvi4J1OVZCt9caI6No1Q/edit?usp=sharing


# Overview
# As a Machine Learning Engineer, the objective is to build a predictive model that estimates house prices using features such as location, number of rooms, total area, and other property attributes. The model will follow the entire Machine Learning Lifecycle — from data collection and preparation to deployment and monitoring.

# 1. Machine Learning Lifecycle Steps
# Step 1: Problem Definition
# Define the problem: Predict house prices based on given features.


# Identify the goal: Provide an accurate price estimate for real estate listings.


# Determine the type of learning: Supervised Learning (Regression).



# Step 2: Data Collection
# Collect datasets containing house features and prices.
#  Possible sources:


# Kaggle (House Prices dataset)


# Real estate company databases


# Web-scraped property data


# Example features include:


# Numerical: Number of bedrooms, bathrooms, square footage, year built


# Categorical: Location, type of house, neighborhood quality



# Step 3: Data Preprocessing
# Handle missing values using mean, median, or mode.


# Remove duplicates and outliers that may distort the model.


# Encode categorical variables (using Label Encoding or One-Hot Encoding).


# Normalize or scale features to ensure fair comparison.


# Split data into training and testing sets (e.g., 80% train / 20% test).



# Step 4: Exploratory Data Analysis (EDA)
# Visualize data using graphs such as:


# Histograms and scatter plots to understand distributions


# Correlation heatmaps to identify relationships between variables


# Detect patterns and trends (e.g., prices increase with area or number of rooms).



# Step 5: Feature Engineering
# Create new features that enhance model performance, such as:


# Price per square foot


# Age of the house


# Neighborhood average price


# Perform feature selection to keep only the most relevant features.



# Step 6: Model Selection and Training
# Choose appropriate regression models (Linear Regression, Random Forest, or Gradient Boosting).


# Train the model using training data.


# Tune hyperparameters using Cross-Validation or Grid Search for better accuracy.



# Step 7: Model Evaluation
# Evaluate the model using test data and compare results using multiple metrics (explained below).


# Check for overfitting or underfitting and adjust the model accordingly.



# Step 8: Model Deployment
# Deploy the trained model to make real-time predictions.


# Example:


# Build a REST API using Flask or FastAPI.


# Host on Heroku, AWS EC2, or Google Cloud Run.


# Create a simple frontend interface for users to input data and get price predictions.



# Step 9: Model Monitoring and Maintenance
# Continuously monitor model performance on new data.


# Detect data drift (changes in data patterns over time).


# Retrain the model periodically with updated data to maintain accuracy.



# 2. Assignment Questions
# Question 1: What type of prediction problem is this and what is the most likely ML algorithm you would use?
# Type: Regression problem (predicting continuous values — house prices).


# Possible Algorithms:


# Linear Regression (simple and interpretable)


# Random Forest Regressor or Gradient Boosting Regressor (for higher accuracy)



# Question 2: What is the loss function you would use if you were to train this model?
# The loss function measures how well the model’s predictions match actual prices.


# Common choices for regression are:


# Mean Squared Error (MSE):
#  MSE=1n∑(ytrue−ypred)2MSE = \frac{1}{n} \sum (y_{true} - y_{pred})^2MSE=n1​∑(ytrue​−ypred​)2
# Mean Absolute Error (MAE) (less sensitive to outliers)



# Question 3: What optimization algorithm would you use?
# Gradient Descent (or Stochastic Gradient Descent - SGD)


# Used to minimize the loss function by adjusting model parameters in the direction of steepest descent.



# Question 4: What are the metrics you would use to evaluate the model after training?
# Mean Squared Error (MSE) – Measures average squared error.


# Root Mean Squared Error (RMSE) – Easier to interpret as it’s in the same unit as price.


# Mean Absolute Error (MAE) – Measures average absolute difference.


# R² Score (Coefficient of Determination) – Measures how well the features explain the variance in price.



# Question 5: Name one approach you would use to deploy this model for use.
# Flask API Deployment:


# Save the trained model using pickle 


# Create a Flask API endpoint /predict that accepts input data (JSON) and returns a predicted price.


# Host the application on Heroku or Google Cloud for public access.



# Conclusion
# This project demonstrates a complete Machine Learning Lifecycle for a House Price Prediction Model, starting from defining the problem to deploying and maintaining the model in production. The process ensures the model is reliable, interpretable, and continuously improving with new data.

