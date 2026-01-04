import mcu
import time

mp3 = mcu.MP3()

# print(f"10進位的{100}，轉成16進位是{hex(100),16}")
mp3.start(volume=int(hex(100), 16), song=int(hex(1), 16))
time.sleep(10)
mp3.stop()
