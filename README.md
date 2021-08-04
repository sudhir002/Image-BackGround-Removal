# Image-BackGround-Removal

________________________________
Base Repo - https://github.com/danielgatis/rembg
________________________________


Project is ready for Local server run, for production need to configure the url/endpoint of the server in html and misc file.


Added Kafka Datapile Line for Multipule Upload


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

