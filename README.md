# Project Overview
This project demonstrates continuous delivery with a simple Flask application in Google Cloud Platform. By using continuous delivery and integrating Github with GCP Cloud Build, adjustments made to the code and pushed to Github will automatically be reflected once the build has finished and the Flask application is refreshed. 

This particular app allows a user to input a date in MM-DD-YYYY format and the day of the week for that specific date will be returned. By default, the app will return the day of the week of today's date unless a different date is entered. You can find the app itself at this [link](https://gcp-flask-cd.uc.r.appspot.com/).

# Setting up the Project
1. Create a new project in GCP
2. Activate the Cloud Shell
3. Configure the shell to run the project using the following command:

```
gcloud config set project $GOOGLE_CLOUD PROJECT
```

4. Clone the repo and change to its directory.

```
git clone https://github.com/vprasad60/gcp-flask-cd.git
cd gcp-flask-cd
```

5. Create and source a virtual environment

```
virtualenv --python $(which python3) venv
source venv/bin/activate
```

6. Install the packages and lint 

```
make all
```

7. Create the app in GCP App Engine and select a region

```
gcloud app create
```

8. Run the application locally to test it 

```
python main.py
```

9. Once you have tested, you can deploy the app

```
gcloud app deploy
```

# Overview of GCP and Continuous Delivery
Continuous Delivery (CD) enables developers to have their applications update based on specific commits/pushes to version control systems such as GitHub. Using GCP, we can take advantage of CD using the Cloud Build service. To set up Cloud Build with your specific repository, please see this [link](https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories). Follow the instructions on setting up Cloud Build and creating triggers for new GitHub pushes. Note that you may need to connect the GitHub Cloud Build App to your repository to properly establish CD. In addition, ensure that the App Engine API and Service Accounts services in the Cloud Build settings have been enabled. If the triggers have been set up correctly, CD will update your app whenever you make new pushes to your repository. 

# References
[Tutorial of GCP and Flask by Noah Gift](https://github.com/noahgift/gcp-hello-ml)

[Demonstration of Continuous Delivery in GCP](https://www.youtube.com/watch?v=_TfWdOvQXwU) 
