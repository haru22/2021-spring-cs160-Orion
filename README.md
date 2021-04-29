# 2021-spring-cs160-Orion

## _Mentor and Mentee Match_

### Run the project 

#### 1: start the web server
```sh
#first terminal
cd 2021-spring-cs160-Orion
cd web_server/server
npm install
nodemon server.js
```

#### 2: start the application server
```sh
#open second terminal
cd 2021-spring-cs160-Orion
cd application_server/server
python server.py  # or python3 server.py
```
#### then open the web browser
localhost:3000/register 

#### UI Test
# using selenium and pytest
cd 2021-spring-cs160-Orion/web_server/UITest/
source myenv/bin/activate
pytest test.py
