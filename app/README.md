# Recommendation Systems with Watson Studio and IBM Cloud 
_Build an application to provide [Community Content](https://dataplatform.ibm.com/community?context=analytics) recommendations to [Watson Studio](https://dataplatform.ibm.com/)_



To get started, we'll take you through a sample Python Flask app, help you set up a development environment and deploy to IBM Cloud. 


## Prerequisites

You'll need the following:
* [Watson Studio with Watson Machine Learning](https://dataplatform.ibm.com/)
* [IBM Cloud account](https://console.ng.bluemix.net/registration/)
* [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)


## TOC

-----------

#### [0. Implementing the Recommendation System](#implement)

#### [1. Clone the sample app](#clone)

#### [2. Run the app locally](#run)

#### [3. Prepare the app for deployment](#prep)

#### [4. Deploy the app](#dep)

-----------

## 1. Clone the sample app

Now you're ready to start working with the app. Clone the repo and change to the directory where the sample app is located.
  ```
git clone https://github.com/HigginTown/UdacityIBMCollabDSND.git
  ```

Peruse the files in the directory to familiarize yourself with the contents.

## 2. Run the app locally

Install the dependencies listed in the [requirements.txt]() file to be able to run the app locally.

You can optionally use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments) to avoid having these dependencies clash with those of other Python projects or your operating system.
  ```
pip install -r requirements.txt
  ```

Run the app.
  ```
python hello.py
  ```

 View your app at: http://localhost:8000

## 3. Prepare the app for deployment

To deploy to IBM Cloud, it can be helpful to set up a manifest.yml file. One is provided for you with the sample. Take a moment to look at it.

The manifest.yml includes basic information about your app, such as the name, how much memory to allocate for each instance and the route. In this manifest.yml **random-route: true** generates a random route for your app to prevent your route from colliding with others.  You can replace **random-route: true** with **host: myChosenHostName**, supplying a host name of your choice. [Learn more...](https://console.bluemix.net/docs/manageapps/depapps.html#appmanifest)
 ```
 applications:
 - name: UdacityRecSysApp
   random-route: true
   memory: 512M
 ```

## 4. Deploy the app

You can use the Cloud Foundry CLI to deploy apps.

Choose your API endpoint
   ```
cf api <API-endpoint>
   ```

Replace the *API-endpoint* in the command with an API endpoint from the following list.

|URL                             |Region          |
|:-------------------------------|:---------------|
| https://api.ng.bluemix.net     | US South       |
| https://api.eu-de.bluemix.net  | Germany        |
| https://api.eu-gb.bluemix.net  | United Kingdom |
| https://api.au-syd.bluemix.net | Sydney         |

Login to your IBM Cloud account

```
cf login
  ```

From within the *get-started-python* directory push your app to IBM Cloud
```
cf push
```

This can take a minute. If there is an error in the deployment process you can use the command `cf logs <Your-App-Name> --recent` to troubleshoot.

When deployment completes you should see a message indicating that your app is running.  View your app at the URL listed in the output of the push command.  You can also issue the
```
cf apps
```








  command to view your apps status and see the URL.

