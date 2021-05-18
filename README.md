# 2021-spring-cs160-Orion

## _Mentor and Mentee Match_
Welcome to our GuruMatch Application

## Requirements
```sh
pip3 install 'pymongo[srv]'
pip3 install pymongo
pip3 install grpc
```
### Run the project 
Open two terminals where the file directory is located
#### 1: start the web server
```sh
#first terminal
cd 2021-spring-cs160-Orion
cd web_server/server
npm install
npm run start
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
```sh
#using selenium and pytest
cd 2021-spring-cs160-Orion/web_server/UITest/
source myenv/bin/activate
pytest test.py
```
#### New Members
New team members can review code and create a new branch to add or implement features. 
The branch will be reviewed and merged when changes are accepted by the team.

