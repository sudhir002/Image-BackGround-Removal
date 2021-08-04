# Image-BackGround-Removal

________________________________
Base Repo - https://github.com/danielgatis/rembg
________________________________


Project is ready for Local server run, for production need to configure the url/endpoint of the server in html and misc file.


Added Kafka Datapile Line for Multipule Upload

setup Kafka in ubuntu:\

sudo apt update\
sudo apt install default-jdk\
wget https://downloads.apache.org/kafka/2.8.0/kafka_2.12-2.8.0.tgz\
tar xzf kafka_2.12-2.8.0.tgz\
mv kafka_2.12-2.8.0 /usr/local/kafka\
sudo nano /etc/systemd/system/zookeeper.service\
       [Unit]\
       Description=Apache Zookeeper server\
       Documentation=http://zookeeper.apache.org\
       Requires=network.target remote-fs.target\
       After=network.target remote-fs.target\
       [Service]\
       Type=simple\
       ExecStart=/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties\
       ExecStop=/usr/local/kafka/bin/zookeeper-server-stop.sh\
       Restart=on-abnormal\
       [Install]\
       WantedBy=multi-user.target\
       
sudo nano /etc/systemd/system/kafka.service\
       [Unit]\
       Description=Apache Kafka Server\
       Documentation=http://kafka.apache.org/documentation.html\
       Requires=zookeeper.service\
       [Service]\
       Type=simple\
       Environment="JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64"\
       ExecStart=/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties\
       ExecStop=/usr/local/kafka/bin/kafka-server-stop.sh\
       [Install]\
       WantedBy=multi-user.target\
       
systemctl daemon-reload\
sudo systemctl start zookeeper\
sudo systemctl start kafka\
sudo systemctl status kafka


Steps To Start Using This Project 

1  install mongoDB in your system (verify it is installed - https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) \
2. clone this repo  \
3. create a virtual envirnment  \
4. activate virtual envirnment  \
5. run : pip install requirements.txt  \
6. run : python app.py (make sure server started after runing it)  \
7. run : python consumer.py (make sure started)  

_____________________  

Now our Backend server is running...  \
We can use our UI (Html Client)  \
Go to html_client and open index.html file as any browser.  \
Note - You can upload mutipule images at a time, and datapipeline is responsible to process your images and give you back with processed images.\
       Status = Completed means your processed files is ready (open image url you will get result).  \
       Status = Pending means processing is going on.  \
       Status = error means with this perticular file got error.  

