import cv2

# Đường dẫn RTSP của camera
rtsp_url = "rtsp://192.168.1.78:37777/Streaming/Channels/1"

# Mở kết nối đến camera
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Không thể kết nối đến camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể nhận khung hình từ camera.")
            break

        # Hiển thị khung hình
        cv2.imshow("Camera Feed", frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Giải phóng kết nối và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
