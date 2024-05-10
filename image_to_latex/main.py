import cv2

# 读取图像文件
image = cv2.imread('1.jpg')

# 如果图像读取成功，进行二值化操作
if image is not None:
    # 将图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用大津法（Otsu's method）自动选择阈值进行二值化
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 调整输出图像的大小为500x500像素
    binary_image_resized = cv2.resize(binary_image, (500, 500))

    # 显示二值化后的图像（可选）
    cv2.imshow('Binary Image', binary_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to read image file.")
