# Probability-Solver-Discord-ChatBot
A simple Discord chatbot that can solve simple probability problems

This project ultilizes my knowlegde of Discord Chatbot and my statistics knowledge.
The main points of this project is to create something that can cut down the calculation required to solve a probability problem.

There are a lot of different websites that do these type of stuff already, but most of them only cover 1 distribution. This chatbot will cover mostly the basics, but it will be more generallized, i.e. you can do many distributions on here without jumping through many sites.

Aside from few random commands, most stats-related commands follow a common format.

In your Discord's chat, type: !distribution_function parameters (Ex: !binom_prob 10 0.5 4).
Alternatively, you can type !help to view all possible commands.

*available distribution is binom, multinomial, norm.

function usually includes: 

                           prob(calculate multiple simple probs like F(X = 4)),

                           ci(confident interval for true means),
                           
                           extra(give E[X], Var, SD, etc.)
# Introduction

## Probability-Solver-Discord-ChatBot
A simple Discord chatbot that can solve simple probability problems. This project is a fun small project that utilizes my knowledge of Discord Chatbot and my statistics knowledge. 
The main points of this project is to create something that can cut down the calculation required to solve a probability problem.

There are a lot of different websites that do these type of stuff already, but most of them only cover 1 distribution. This chatbot will cover mostly the basics, but it will be more generallized, i.e. you can do many distributions on here without jumping through many sites.
1. Runs the saved predicting algorithm or train a new one if no saved algorithm is found

2. Directs the user to a different page where the answer will be given

3. Allows the user to see general informations about the website and to return to the home page to try another text

# Technical Overwiew
The web application is built using Python and Flask framework. Here's an overview of the key components:

1. app.py: This is the main Python file that contains the Flask application. It handles both GET and POST requests and implements the text classification algorithm. The user's input text is processed, preprocessed using a pre-trained TF-IDF vectorizer, and classified using a pre-trained SVM model. The predicted category is then rendered on the result page.

2. helper.py: This file contains a helper function translate_category_name that can be used to translate the category names into more user-friendly labels. You can customize this function to match your specific use case.

3. base.html: This HTML template file defines the overall design of the websites (layout, background, etc.). It includes a droplist for all 20 topics and an "About" button that give an overview about the page.

4. index.html: This HTML template file defines the index page of the web application. It includes a form where users can input their text for classification.

5. result.html: This HTML template file defines the result page of the web application. It displays the predicted category label for the user's input text.

6. evaluation.txt: This text file gives an overview about the model's evaluation metrics, like accuracy, precision, recall, etc.

6. model.joblib and vectorizer.joblib: These are pre-trained files that store the trained SVM model and TF-IDF vectorizer, respectively. If these files exist in the project directory, the application will load them. Otherwise, it will train a new model and vectorizer on the 20 Newsgroups dataset and save them for future use.

# Setup & Usage

## How to Install

To run this web application locally, follow these steps:

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Make sure you have Python 3.x installed on your system.

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required Python packages by running the following command:
```
pip install -r requirements.txt
```
5. Alternatively, you can install each item in requirements.txt seperately if the file fails to work:
```
pip install -U scikit-learn
```
```
pip install -U Flask
```
```
pip install joblib
```
## Usage
Once you have installed the necessary packages, you can start using the text classification web application. Follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the Flask application by executing the following command (or run with your IDE):
```
python app.py
```
3. By default, the Flask application will be running on http://localhost:5000.

4. Open a web browser and enter http://localhost:5000 in the address bar.

5. The index page of the web application will be displayed. Enter the text you want to classify into the input field and click the "Submit" button.

6. The application will process the input text, predict its category, and display the result on the result page.

7. You can continue to enter new text inputs and get predictions as desired.

## Customization
You can customize this web application to suit your specific requirements. Here are a few possible modifications you might consider:

1. Modify the HTML templates (index.html and result.html) to change the appearance and layout of the web pages.

2. Customize the translate_category_name function in helper.py to map the predicted category labels to your desired names.

3. Use your own dataset and modify the data preprocessing and model training steps in app.py to train a model on your specific data.

4. Update the routes and endpoints in app.py to add additional functionality or implement different features.
