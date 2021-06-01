## Launch
To make use of this application it is recommended to run the provided Python script in a container from the Docker image as provided in the Dockerfile. To do this follow these steps:
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
