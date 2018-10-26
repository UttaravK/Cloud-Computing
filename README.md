# Environmental Sensor Station Simulation and Analysis 
## (Domain: Cloud Computing)

#### Install and Set up Virtual Machine
```
cd ./
vagrant up  
vagrant ssh  
 ```
 
#### Install Dependencies

```
cd ./src/water_watch_project/
pip install -r requirements.txt
```

 #### Migrate Database
 ```
 python manage.py migrate 
 ```

#### In VM, run server
```
 python manage.py runserver 0.0.0.0:8080  
 ```

#### Home Page: 
```
http://localhost:8082/
```

  

