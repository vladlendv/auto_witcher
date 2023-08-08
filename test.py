from ahk import AHK
import time
ahk = AHK()

time.sleep(3)
print(ahk.pixel_get_color(252, 445))