import time
import cv2
import pandas
from gtts import gTTS
import os
from gpiozero import Button
from mutagen.mp3 import MP3

def scanQR(LinkExcel, a):
    # LinkExcel là path của file Excel

    df = pandas.read_excel(LinkExcel)
    # doc file excel dinh kem
    va = ''
    lin = ''
    # tao file link trong
    capture = cv2.VideoCapture(0)
    # tao mot doi tuong de doc anh
    det = cv2.QRCodeDetector()
    # ma do QR trong opcv
    speak("Đưa mã QR vào vị trí quét")
    print("Đưa mã QR vào vị trí quét")
    time_scan = time.time()
    while time.time() < time_scan + a:
        _, img = capture.read()
        va, pts, _ = det.detectAndDecode(img)
        if va:
            # val la cot name picture
            print(va)
            time_scan = time.time()
            for i in range(0, 16, 1):
                # luu 15 gia tri anh1
                if (df.loc[i]['name'] == va):
                    lin = df.loc[i]['link']
                    # print(lin)
                    # b = webbrowser.open(str(link))
                    # speak("Bạn đã chọn "+str(val))
                    # time.sleep(3)
                    # speak("Tiến hành vẽ")
                    break
            if (lin == ''):
                print('Không có mã quét  ' + va)
                speak("Mã không hợp lệ, hãy quét lại ")
            else:
                capture.release()
                break
    if va == '' and lin == '':
        print(' no found')
    return va, lin


def speak(text):
    tts = gTTS(text=text, lang='vi', slow=False)  # ngoonngu "vi",tốc độ mặc định
    tts.save("speech.mp3")  # lưu file
    # playsound.playsound("speech.mp3", False)  # nói True ns xong dừng ctr
    os.system('mpg321 speech.mp3 &')
    time.sleep(MP3("speech.mp3").info.length)
    print(MP3("speech.mp3").info.length)
    os.remove("speech.mp3")  # xóa đi tránh vòng lặp


if __name__ == '__main__':
    val = ""
    link = ""

    button = Button(23)
    button1 = Button(24)
    button2 = Button(18)
    speak("Nhập 1 để để quét")
    print("Nhập 1 để để quét")
    time_start_0 = time.time()
    time_out_0 = time_start_0 + 15
    while time_start_0 < time_out_0:
        if button.is_pressed:
            val, link = scanQR("Picture_Link.xlsx", 30)
            if val == "" and link == '':
                break
            speak("đã chọn hình {} với {}".format(val, link))
            print("đã chọn hình {} với {}".format(val, link))
            speak("bạn đã chọn được hình mong muốn, nhập 3 để bắt đầu vẽ")
            print("bạn đã chọn được hình mong muốn, nhập 3 để bắt đầu vẽ")

            time_start_1 = time.time()
            time_out_1 = time_start_1 + 15
            while time.time() < time_out_1:
                if button1.is_pressed:
                    print('dang ve')
                    speak("lệnh báo đang vẽ, và vẽ từng bước")
                    time.sleep(5)
                    speak("lệnh báo vẽ xong")
                    print('ve xong')
                    speak("nhập 2 để vẽ hình khác, e để tắt ")
                    print("nhập 2 để vẽ hình khác, e để tắt ")
                    time_start_0 = time.time()
                    time_out_0 = time_start_0 + 15
                    break


        if button2.is_pressed:
            speak("bạn đã thoát")
            print("bạn đã thoát")
            break
