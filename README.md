# python_streamlit

# streamlit install手順
- pip 更新  
$ pip install --upgrade pip

- streamlitインストール  
windows32bit では、streamlit0.63移行は未対応のため、0.62指定  
$ pip install streamlit==0.62  
※追加されたapacheのモジュールが原因らしい  

- protobufのダウングレード  
$ pip install protobuf==3.20.*  
streamlit起動するとエラーになるのでダウングレード  

- streamlit起動  
$  streamlit.exe run app.py  
app.py は作成したコード  

