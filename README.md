
Welcome to the Mobile Price Prediction project! This project focuses on predicting the prices of mobile phones by scraping data from Flipcae and utilizing feature engineering techniques. After applying various algorithms, the model achieved a remarkable R2 score of 93%, indicating its accuracy in predicting mobile phone prices.

## Dataset

The dataset used for training and testing the mobile price prediction model was obtained by scraping mobile phone listings from Flipcae. The dataset includes the following features:

- Brand Name: The brand of the mobile phone.
- Has 5G: Whether the mobile phone supports 5G connectivity.
- Has NFC: Whether the mobile phone has NFC (Near Field Communication) capabilities.
- Has IR Blaster: Whether the mobile phone features an infrared (IR) blaster.
- Processor Brand: The brand of the mobile phone's processor.
- Number of Cores: The number of cores in the mobile phone's processor.
- Processor Speed: The speed of the mobile phone's processor.
- Battery Capacity: The capacity of the mobile phone's battery.
- Fast Charging Available: Whether the mobile phone supports fast charging.
- RAM Capacity: The capacity of the mobile phone's RAM.
- Internal Memory: The internal storage capacity of the mobile phone.
- Refresh Rate: The refresh rate of the mobile phone's display.
- Operating System (OS): The operating system installed on the mobile phone.
- Primary Camera (Rear): The specifications of the mobile phone's primary rear camera.
- Primary Camera (Front): The specifications of the mobile phone's primary front camera.
- Extended Memory Available: Whether the mobile phone supports extended memory.

## Feature Engineering

Prior to training the prediction model, extensive feature engineering techniques were applied to enhance the predictive power of the dataset. This included handling missing values, encoding categorical variables, scaling numerical features, and exploring interactions among different features.

## Model Training and Evaluation

The mobile price prediction model was trained using machine learning algorithms, resulting in an impressive R2 score of 93%. This score indicates that the model can explain 93% of the variance in the mobile phone prices. The model's high accuracy makes it a valuable tool for predicting mobile phone prices.

## Usage

To use the mobile price prediction model, follow these steps:

1. Install the required dependencies specified in the `requirements.txt` file.
2. Run the data scraping script to collect the latest mobile phone data from Flipcae.
3. Perform feature engineering on the dataset, including handling missing values, encoding categorical variables, and scaling numerical features.
4. Split the dataset into training and testing sets.
5. Train the prediction model using suitable algorithms, such as regression models or ensemble methods.
6. Evaluate the model's performance on the testing set using appropriate metrics, such as R2 score, mean absolute error (MAE), or root mean squared error (RMSE).
7. Once the model is trained, you can use it to predict the prices of new mobile phones by providing their features as input.

## File Structure

The project follows the following file structure:

## Future Improvements

Here are a few potential areas for future improvement and enhancement:

- Incorporating additional features: Explore the possibility of including more features, such as customer ratings or reviews, to further improve the prediction accuracy.
- Hyperparameter tuning: Experiment with different hyperparameter settings for the prediction model to optimize its performance.
- Web application: Develop a user-friendly web application where users can input mobile phone specifications and obtain predicted prices instantly.
