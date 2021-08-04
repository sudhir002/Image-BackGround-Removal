# Image-BackGround-Removal

________________________________
Base Repo - https://github.com/danielgatis/rembg
________________________________

Added Kafka Datapile Line for Multipule Upload


Steps To Start Using This Project \n

1  install mongoDB in your system (verify it is installed - https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) \n
2. clone this repo  \n
3. create a virtual envirnment  \n
4. activate virtual envirnment  \n
5. run : pip install requirements.txt  \n
6. run : python app.py (make sure server started after runing it)  \n
7. run : python consumer.py (make sure started)  \n
_____________________  \n
Now our Backend server is running...  \n
We can use our UI (Html Client)  \n
Go to html_client and open index.html file as any browser.  \n
Note - You can upload mutipule images at a time, and datapipeline is responsible to process your images and give you back with processed images.\n
       Status = Completed means your processed files is ready (open image url you will get result).  \n
       Status = Pending means processing is going on.  \n
       Status = error means with this perticular file got error.  \n

