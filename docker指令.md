# Docker結構
<br>
Image<br>
Container<br>
Repository<br>
<br>

# 目前使用過的docker指令

docker ps <br>
功能: 查看正在執行的docker container <br>
<br>
docker ps -a <br>
功能: 查看所有(running & exit)的container <br>
<br>
docker images <br>
查看repository保存的所有image <br>
docker save -o [匯出檔案的檔名].tar [ImageID]<br>
匯出Image成壓縮檔 <br>
eg. docker save -o mysite.tar f8e3f0d10bf <br>
docker load -i [壓縮檔名] <br>
讀入壓縮檔成Image <br>
eg. docker load -i mysite.tar

# 建立postgres的docker指令

docker run --name postgresname -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=username0 -d -p 5432:5432 postgres
