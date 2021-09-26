import cv2
import numpy as np


def cv_show(name,img):
   cv2.imshow(name,img)
   cv2.waitKey()
   cv2.destroyAllWindows()


img = cv2.imread("image/test2.png")
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

scharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
scharry=cv2.Scharr(img,cv2.CV_64F,0,1)
scharrx=cv2.convertScaleAbs(scharrx)
scharry=cv2.convertScaleAbs(scharry)
scharrxy=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)

res=np.hstack((img,sobelxy,scharrxy,laplacian))
cv_show('res',res)


