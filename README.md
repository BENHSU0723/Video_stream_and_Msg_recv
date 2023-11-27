# python-webcam-socket-streaming--at the client side, CHT competition
Python OpenCV webcam sending frames through TCP socket.

Ref to: https://github.com/1010code/python-webcam-socket-streaming

## how to run video streaming and receive message
這邊的概念是要用`client.py`和`client2.py`分別建立一條TCP連線，`client.py`是要建立TCP連線去傳影像的，然後`client2.py`是要建立另一條TCP連線去接收AI server辨識完後傳的字串，並且把訊息轉傳給arduino的serial port

**注意:兩個程式啟動順序有差，要先執行client.py再開另一個Terminal執行client2.py**

* 執行client.py

`python3 client.py`

* 執行client2.py

`python3 client2.py`

其他的檔案基本上都是測試的時候使用，不用管他
