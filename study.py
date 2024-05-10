import cv2

def laplacian_filter(image):
    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用拉普拉斯滤波器
    laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)

    # 将结果转换为图像格式
    laplacian_image = cv2.convertScaleAbs(laplacian_image)

    return laplacian_image
# 读取图像
image = cv2.imread('image_to_latex/1.jpg')

# 进行拉普拉斯滤波
sharpened_image = laplacian_filter(image)

# 将灰度图像转换为三通道图像
laplacian_image_bgr = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Image', laplacian_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

