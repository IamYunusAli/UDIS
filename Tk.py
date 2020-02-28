from tkinter import *
import requests
import cv2
import numpy as np

#url = "http://192.168.43.1:8080"

#while True:

 #   img_resp = requests.get(url)
  #  img_arr = np.array(bytearray(img_resp.content), dtype=np.unit8)
   # img = cv2.imdecode(img_arr, -1)

   # cv2.imshow("UDIS", img)

    #if cv2.waitKey(1) == 27:
     #   break

root = Tk()

photo = PhotoImage(file="astu.png")
theLable = Label(root, image=photo)
theLable.pack()

root.mainloop()

# pic = PhotoImage(file="ASTU.png")
# lbl = Label(root, image=pic)
# lbl.pack()
