# Introduction 
This source code is designed to connect to kafka - or mosquitto MQTT to read the data inserted to any DB.

# Installation
1. Configure the external DB settings in [this](./Src/Main_Algorithm/Pilot/Pilot/settings.py) file. you can find an example blow:
```python
    'external_table': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xeye',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'OPTIONS': {
        #     'unix_socket': '/tmp/mysql.sock',  # Ensure this matches the correct socket path
        # },
    }
```

2. Install MQTT or Kafka based on their installation path and set their configs.

3. Once you installed MQTT or Kafka follow these instructions:
    - To handle `Kafka`, proceed to [this](./Pilot/Data_Connection/kafka_setup.py) python file. there feel free to custumize your connections and other configurations in [this](./Pilot/Data_Connection/management/commands/kafka.py) file.

    - To handle `MQTT`, proceed to [this](.Pilot/Data_Connection/management/commands/mqtt.py) python file. there feel free to custumize your connections and other configurations.

4. Install the requirements:
```shell script
pip install -r requirements.txt
```

34. Once configuration is completed, follow these steps:

```shell script
python ./Pilot/manage.py makemigrations
python ./Pilot/manage.py migrate
```

now by following the command blow, you should be able to see the names of `mqtt` and `kafka` in the help section:

```shell script
python ./Pilot/manage.py help
```

# Run
To Run the program follow this command:

```shell script
python ./Pilot/manage.py kafka
```

or 

```shell script
python ./Pilot/manage.py mqtt
```