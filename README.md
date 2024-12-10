# Gopher Marketplace
![Alt text](https://github.com/Daanish-Hindustani/Gopher_Marketplace/blob/main/readme_imgs/login.png?/raw=true)
![Alt text](https://github.com/Daanish-Hindustani/Gopher_Marketplace/blob/main/readme_imgs/main.png?/raw=true)
![Alt text](https://github.com/Daanish-Hindustani/Gopher_Marketplace/blob/main/readme_imgs/detail_view.png?/raw=true)

## Description
-This Project is an centralized ecommerce website for UMN students to sell different products such as books, clothing, lab equipment, tech, and anything else while retaining 100% of the profit. 

## Get Started
 1. Create a venv and install the requirments
    - python -m venv myenv
    - source myenv/bin/activate
 2. Create a .env file with local postgress db
    Note: if your using postgress but not docker change host name to local not db(use if using docker)
 3. run docker-compose up --build (optional- if you are running docker)
 4. If you are not running docker make sure to run the migration commands(make sure postgress is running)
      -python manage.py makemigrations
      -python manage.py migrate
    Note: if you are running locally use python manage.py runserver 0.0.0.0:8000 (make sure you are running postgress)
 5. Set up Google Auth
   - Go to the API Console: https://console.cloud.google.com/apis/dashboard?inv=1&invt=AbjwVw
   - From the projects list, select a project or create a new one.
   - If the APIs & services page isn't already open, open the left side menu and select APIs & services.
   - On the left, choose Credentials.
   - Click Create credentials and then select API key.
      - Name should be set to Gopher-marketplace
      - Authorized JavaScript origins should be set to http://127.0.0.1:8000
      - Authorized redirect URIs should be set to http://127.0.0.1:8000/auth-receiver

## Development
 1. Always make a branch before pushing to main 
 2. Don't leak any key, keep them in the .env file 
 3. Raise issues if there are any problem

## Project overview
- https://docs.google.com/document/d/1gOhVWaR7HDh7IOWJsWR9jCSXtPSMf91iCrLCiMsao-w/edit?usp=sharing

## Collaboration
- Collaborations are welcomed ❤️
   
## Contact
 - LinkedIn: [(https://www.linkedin.com/in/daanishhindustani)]
 - Gmail: hindu006@umn.edu
