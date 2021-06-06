# Tomorrow Rain Prediction in Australia - Deployment
<p align=left>
<img src="https://img.shields.io/badge/Type-Classification-blue"/> 
<img src="https://img.shields.io/badge/Python-3.9-brightgreen"/>
<img src="https://img.shields.io/badge/DataSet-Kaggle-brightgreen"/> 
<p/>
<br>
<p align=center>
<img src="https://media.giphy.com/media/TSuOITq0guzN815qVA/giphy.gif" width="550px" height="300px">
</p>
<br>
<br>
<H4>This Application has created for predicts whether it will rain or not in next day of Australia
  it can predicts for differrernt locations in Australia by considering sevarel factors. basically application has a
  gradient boosting ML model for predictions. and also it has trained by without using hyperparameter tuning. because of I have 
  not much enough computation power for do the hyperparameter tuning. ( but I reccomand for do hyperparameter tuning if it is possible)</H4>
 <br>
<H4>This repository consists of files required to deploy a ___WEB APPLICATION___ created by using ___Flask___ on ___Heroku___ server.</H4>
<br>
<H4>Data set got from kaggle, if you like to inspect it just click this link _https://www.kaggle.com/jsphyg/weather-dataset-rattle-package_. 
it has over 100 000 data records with 23 columns.</H4>
<br>
<H4>You can see deployed model in heroku , use below link for reach to deployed model:<br />
Heroku: _https://kangaroo-rain.herokuapp.com/_</H4>


<hr>

### Technology Adopted
• Front-End: HTML, CSS, Bootstrap (got help form Nicepage builder for make some templates) <br>
• Back-End: Flask <br>
• IDE: Jupyter notebook, Google colab, Spyder <br>

## WorkFlow

### Data PreProcessing
• Missing Values Handled by Random Sample imputation, mean, median, mode imputation and predict some missing columns values by using simple ML models. <br>
• Categorical Values like location, wind direction are handled by using Target guided encoding. <br>
• Outliers were handled using  Tukey method (IQR). <br>
• Feature transformation was done by using severl methods such as log, boxcox, reciporal, square root transformation. <br>
• Data visualization were done by using matplotlib and seborn. <br>
• Imbalanced Dataset was handled using RandomOverSampler (I reccomand for use SMOTE also). <br>


### If you are willing to check project in flask 
You must basically have Scikit Learn, Pandas (for Machine Leraning Model) and Flask installed.

### Project Structure
This project has four major parts <br>
1. model.pkl - This is our built model for predict values. <br>
2. app.py - This contains Flask APIs that receives  details through GUI , computes the precited value based on our model and returns it. <br>
3. static - This uses for store css files and some images for while presenting. <br>
4. templates - This folder contains the HTML template to allow user to enter required detail and displays the predicted result. <br>


### Running the project in flask API
• First create a virtual environment by using `conda create -n rain python=3.9` command and activate it by using `conda activate rain` command <br>
• Install requirements.txt file by using `pip install -r requirements.txt` command,it will install all of essential dependancies. <br>
• Type `python app.py` for start your server. <br> 
• Then copy the given url and paste it in your browser. <br>
• Then input valid inputs and do prediction.
