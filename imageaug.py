import imgaug.augmenters as iaa
import cv2
import glob

# 1. Load Dataset
images = []
images_path = glob.glob("images/simpan/*.jpg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)

# 2. Image Augmentation
augmentation = iaa.Sequential([
    # 1. Flip
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),

    # # 2. Affine
    # iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
    #            rotate=(-30, 30),
    #            scale=(0.5, 1.5)),

    # # 3. Multiply
    # iaa.Multiply((0.8, 1.2)),

    # # 4. Linearcontrast
    # iaa.LinearContrast((0.6, 1.4)),

    # # Perform methods below only sometimes
    # iaa.Sometimes(0.5,
    #     # 5. GaussianBlur
    #     iaa.GaussianBlur((0.0, 3.0))
    #     )
])

# 3. Show Images

augmented_images = augmentation(images=images)
# print(augmented_images)
i=0
for img in augmented_images:
    # gambar = cv2.imread(img)
    cv2.imshow("Image", img)
    
    cv2.imwrite("images/simpan2/img%03i.jpg" %i, img)
    i +=1
    print(i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()