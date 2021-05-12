import cv2

src = cv2.imread('rose.bmp')
dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920,1280))
dst3 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()
cv2.destroyAllWindows()