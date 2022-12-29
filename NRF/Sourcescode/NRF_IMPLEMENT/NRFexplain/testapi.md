## Chạy test thử api 
# Chạy và test thử các api trên free5gc
 bước 1: clone code từ trang free5gc/openapi
''''
 cd vào thư mục cần lưu
 git clone https://github.com/free5gc/openapi.git
''''
 bước 2: lên web swagger api dùng để test api
  Đăng nhập vào web

  Sau đó import api bằng cách chọn

  Create New --> Import and Document API -->  Import file yml/json(ở đây file 5gc dùng sẽ là file yml )
  
  <img src=images/Untitled1.png>

  Chọn 1 api để test
  Ở đây tôi chọn api khối nrf discovery-service

   <img src=images/Untitled2.png>

   Sau khi đã chọn import được ta sẽ thu được giao diện như hình vẽ

   <img src=images/Untitled3.png>

   # Giải thích 
    Ở phần giao diện ta thấy file yml 
    file yml này là file cấu hình-file thực thi của toàn bộ hệ thống khi chạy go(chưa biết cách export =)) )
    Một API gồm 2 phương thức GET SET
    Với khối này ta có NRF Authencations - Phần này để chúng ta đưa Ip 2 máy vào và test =)) 
    AE nào rảnh test thử này với 2 con VM trên lab xem ntn
    với phương thức GET chúng ta có thể đưa ra các imput đầu vào và sẽ thu được các thông tin Output tương ứng



