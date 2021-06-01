# rescue_drivers_prediction
Case study data science project for my data science studies

## Introduction
Welcome to the repository supporting my case study report paper "Rescue Drivers Prediction" by Koen Bothmer. This paper and code repository were produced as an examination excercice for the class "Case Study: Model Engineering" at International University. This work was submitted to Turnitin but for the reference of those not involved in the class the paper was also included to this Github repository.
### Main idea
The main idea of this project is to use a given dataset to produce a predictive model that aids in the planning of rescue drivers for the Red Cross in Berlin. 
## Techniques used
Folowwing the rough guidelines provided by the CRISP-DM methodology, the paper contains the folowwing chapters, supported by the repository as described:
- Business Understanding - Paper Only
- Data Understanding - Paper gives a summary of the performed exploratory data analysis, analysis steps can be found in Python Jupyter notebook in folder "Data_Understanding"
- Data Preparation - Paper gives a summary of the permormed data preparation steps that enable the modelling step. All data preparation can be found in Python Jupyter notebook in folder "Data_Preparation
For some reason, Github fails to render the notebook as provided. It can be viewed without having to download it to your own Jupyter instance through https://nbviewer.jupyter.org/github/KoenBothmer/rescue_drivers_prediction/blob/main/Data_Preparation/Data_Preparation.ipynb
- Modelling - Paper describes and justifies the modelling steps employed, the employment itself can be found in the Python Jupyter notebook in folder "Modelling"
- Deployment - Paper describes the choices made for deployment, folder "app" contains the final product as made available through Docker containerization, to be run as described in the next paragraph
## Launch
To get a general idea of the project it is sufficient to just load the notebooks as described above directly from this repository. To make more extensive use of the application itself it is recommended to run the provided Python script in a container from the Docker image as provided in the Dockerfile. To do this follow these steps:
### Set-up
* Save the folder "app" with it's contents to a local folder (referred to as "yourdir/app")
* Make sure to have Docker installed on your local machine
* Open a command prompt
* Navigate to "yourdir/app"
* Run the command "docker build -t driver_prediction --rm ." to build the docker image
### Use of application
* Make sure that on the 15th day of each month there is a file present in folder "yourdir/app/updates" containing the output from the 16th of the previous month up until the given day. As an example to demonstrate the functionality, a file named "2019_July.csv" containing the data from 16th of may up until the 15th of june is currently present in the folder. As the filename suggests, the data should be used to make predictions about the planning for July.
* Navigate to "yourdir/app" and double click the file "predict_drivers.bat" which starts the container from the driver_prediction image and runs the script "predict_drivers.py" in the container environment. 
* The script will output a file named "prediction.csv" which contains the predicted drivers needed supplemented by the predicted number of calls and the predicted number of sick drivers.
* The script will add the content of the file in "yourdir/app/Updates" to file "df_up_to_date.csv" which will be the input for the next modelling step
* The file in "yourdir/app/Updates" will be moved to folder "yourdir/app/Archive"
### Host environment
Allthough Docker makes it simple to ship applications over multiple operating systems, the script "predict_drivers.bat" is not guaranteed to run on host environments other than Windows. The volume mount to current directory using '%CD%' is host dependent and might need a small adjustment.
