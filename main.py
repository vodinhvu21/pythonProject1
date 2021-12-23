import time
import cv2
import pandas
from gtts import gTTS
import os
from gpiozero import Button

button = Button(23)
button1 = Button(24)
button2 = Button(18)
button3 = Button(16)
def scanQR(LinkExcel):
    # LinkExcel là path của file Excel
    df = pandas.read_excel(LinkExcel)
    # doc file excel dinh kem
    link = ''
    # tao file link trong
    capture = cv2.VideoCapture(0)
    # tao mot doi tuong de doc anh
    det = cv2.QRCodeDetector()
    # ma do QR trong opcv
    print("Đưa mã QR vào vị trí quét")
    speak("Đưa mã QR vào vị trí quét")
    while True:
        _, img = capture.read()
        val, pts, _ = det.detectAndDecode(img)
        if val:
            # val la cot name picture
            print(val)
            for i in range(0, 16, 1):
                # luu 15 gia tri anh1
                if (df.loc[i]['name'] == val):
                    link = df.loc[i]['link']
                    print(link)
                    # b = webbrowser.open(str(link))
                    # speak("Bạn đã chọn "+str(val))
                    # time.sleep(3)
                    # speak("Tiến hành vẽ")
                    break
            if (link == ''):
                print('Không có mã quét  ' + val)
                speak("Mã không hợp lệ, hãy quét lại ")
            else:
                capture.release()
                break
    return val, link
def speak(text):
    tts = gTTS(text=text, lang='vi', slow=False)  # ngoonngu "vi",tốc độ mặc định
    tts.save("speech.mp3")  # lưu file
    # playsound.playsound("speech.mp3", False)  # nói True ns xong dừng ctr
    os.system('mpg321 speech.mp3 &')
    time.sleep(1)
    os.remove("speech.mp3")  # xóa đi tránh vòng lặp



if __name__ == '__main__':
    val = ""
    link = ""

    p1 = p2 = 1
    #speak("Nhập 1 để khởi động")
    print("Nhập 1 để khởi động")
    time_0 = time.time()
    timeout_0 = 15

    while int(time.time()) != int(time_0 + timeout_0):
        if button.is_pressed:
            timeout_0 = -1
            #("Nhập 2 để quét, e để thoát ")
            print("Nhập 2 để quét, e để thoát ")
            time_1 = time.time()
            timeout_1 = 5
            while time.time() < time_1 + timeout_1:
                if button1.is_pressed:
                    timeout_1 = 60 * 60
                    val, link = scanQR("Picture_Link.xlsx")
                    #speak("đã chọn hình {} với {}".format(val, link))
                    print("đã chọn hình {} với {}".format(val, link))
                    #speak("bạn đã chọn được hình mong muốn, nhập 3 để bắt đầu vẽ")
                    print("bạn đã chọn được hình mong muốn, nhập 3 để bắt đầu vẽ")
                    time_2 = time.time()
                    timeout_2 = 30
                    while time.time() < time_2 + timeout_2:

                        if button2.is_pressed:
                            timeout_2 = 3600
                            print('dang ve')
                            # speak("lệnh báo đang vẽ, và vẽ từng bước")
                            time.sleep(5)
                            # speak("lệnh báo vẽ xong")
                            print('ve xong')
                            # speak("nhập 2 để vẽ hình khác, e để tắt ")
                            print("nhập 2 để vẽ hình khác, e để tắt ")
                            time_1 = time.time()
                            timeout_1 = 30
                            break
                    break

                if button3.is_pressed:
                    #speak("bạn đã thoát")
                    print("bạn đã thoát")
                    timeout_0 = 0
                    break

            break


