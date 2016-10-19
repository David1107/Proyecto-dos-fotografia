import cv2  
  
img = cv2.imread('./data/imagenes/a_elefante.jpg')
imgb = cv2.imread('./data/imagenes/b_leon.jpg')   
#cv2.imshow('src', img)  

kernel_size = 3
scale = 1
delta = 0
ddepth = cv2.CV_16S
# Filtros paso bajo
img_g = cv2.GaussianBlur(img,(3,3),0);
img_b = cv2.blur(img,(3,3),0);
img_m = cv2.medianBlur(img,5);

cv2.imwrite('./data/a_gaussian.jpg',img_g)
cv2.imwrite('./data/a_blur.jpg',img_b)
cv2.imwrite('./data/a_media.jpg',img_m)

# Filtros paso alto
img_l = cv2.Laplacian(imgb,ddepth,ksize = kernel_size,scale = scale,delta = delta)
img_s = cv2.Sobel(imgb,cv2.CV_16S,1,1) 
img_c = cv2.Canny(imgb,100,200)

cv2.imwrite('./data/b_laplacian.jpg',img_l)
cv2.imwrite('./data/b_sobel.jpg',img_s)
cv2.imwrite('./data/b_canny.jpg',img_c)

cv2.waitKey(0)