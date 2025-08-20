# 🔌 Điều khiển LED_BUILTIN Arduino từ Python bằng PyFirmata2

## 📌 Giới thiệu
Dự án này hướng dẫn bạn kết nối **Arduino** với **Python** và điều khiển `LED_BUILTIN` (mặc định là chân **13**) thông qua giao thức **Firmata**.  
Thư viện **PyFirmata2** được sử dụng thay cho **PyFirmata** để đảm bảo tương thích với **Python 3.11+**.

---

## 🛠 Yêu cầu phần cứng & phần mềm

### Phần cứng
- Arduino Uno / Nano / Mega / Leonardo hoặc tương tự  
- Cáp USB kết nối Arduino với máy tính  

### Phần mềm

| Thành phần       | Phiên bản khuyến nghị | Ghi chú |
|------------------|----------------------|---------|
| Python           | ≥ 3.11               | Dùng PyFirmata2 để tránh lỗi `inspect.getargspec` |
| Arduino IDE      | Mới nhất             | Dùng để nạp firmware **StandardFirmata** |
| Thư viện Python  | pyfirmata2           | Hỗ trợ tốt Python 3.11+ |

---

## 📥 Cài đặt thư viện cần thiết
Cài PyFirmata2:  
```bash
pip install pyfirmata2
⚠️ Lưu ý:
Không dùng pyfirmata với Python ≥ 3.11 vì sẽ gặp lỗi:

pgsql
Copy
Edit
AttributeError: module 'inspect' has no attribute 'getargspec'
🔄 Nạp firmware StandardFirmata vào Arduino
Mở Arduino IDE

Vào File → Examples → Firmata → StandardFirmata

Chọn đúng Board và Port

Nhấn Upload để nạp firmware

👉 Sau bước này, Arduino đã sẵn sàng nhận lệnh từ Python.

🔍 Xác định cổng COM
Windows
Mở Device Manager → Ports (COM & LPT)

Ghi lại cổng COM, ví dụ: COM3

Linux / Mac
bash
Copy
Edit
ls /dev/tty*
Ví dụ: /dev/ttyUSB0

💡 Code Python điều khiển LED_BUILTIN
📂 File: led_control.py

python
Copy
Edit
from pyfirmata2 import Arduino
import time

# --------------------------
# 1. Kết nối Arduino qua cổng COM
# --------------------------
board = Arduino('COM3')  # Đổi COM3 thành cổng thực tế
LED_BUILTIN = 13

print("Kết nối thành công! Điều khiển LED_BUILTIN (chân 13)")

while True:
    cmd = input("Nhập 1 để BẬT LED, 0 để TẮT LED, q để THOÁT: ")

    if cmd == '1':
        board.digital[LED_BUILTIN].write(1)
        print("💡 LED SÁNG")
    elif cmd == '0':
        board.digital[LED_BUILTIN].write(0)
        print("🌑 LED TẮT")
    elif cmd.lower() == 'q':
        board.digital[LED_BUILTIN].write(0)
        board.exit()
        print("🔌 Ngắt kết nối. Kết thúc chương trình.")
        break
    else:
        print("⚠️ Lệnh không hợp lệ! Vui lòng nhập 1, 0 hoặc q.")
⏳ Ví dụ: Nhấp nháy LED tự động
📂 File: led_blink.py

python
Copy
Edit
from pyfirmata2 import Arduino
import time

# Kết nối Arduino
board = Arduino('COM3')
LED_BUILTIN = 13

print("Bắt đầu nhấp nháy LED_BUILTIN... Nhấn Ctrl+C để dừng.")

try:
    while True:
        board.digital[LED_BUILTIN].write(1)
        print("💡 LED SÁNG")
        time.sleep(1)
        
        board.digital[LED_BUILTIN].write(0)
        print("🌑 LED TẮT")
        time.sleep(1)
except KeyboardInterrupt:
    board.digital[LED_BUILTIN].write(0)
    board.exit()
    print("\n🔌 Đã ngắt kết nối.")
🚨 Lỗi thường gặp & cách khắc phục
Lỗi	Nguyên nhân	Cách khắc phục
SerialException: could not open port	Sai cổng COM hoặc COM bị chiếm	Kiểm tra COM trong Device Manager và đóng Arduino IDE
AttributeError: module 'inspect' has no attribute 'getargspec'	Dùng PyFirmata với Python ≥ 3.11	Cài PyFirmata2
LED không sáng	Sai chân LED	Dùng LED_BUILTIN = 13 hoặc chân số tương ứng

📌 Kết luận
Đối với Python ≤ 3.10: Có thể dùng PyFirmata hoặc PyFirmata2

Đối với Python ≥ 3.11: Bắt buộc dùng PyFirmata2

Khuyến khích nạp StandardFirmata vào Arduino để đảm bảo tương thích

📚 Tài liệu tham khảo
PyFirmata2 Documentation

Arduino Firmata Protocol

Python Downloads

👨‍💻 Tác giả
Beniot Phan - Tin Phan

📧 Email: beniot.robaiot1137@gmail.com

🌐 GitHub: Ben-RobAIoT
