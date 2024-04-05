import cv2


    def read():
        """
        capture live answer script image from live feed
        Use the below code for development and then use open cv to
        """

        file_name = "original_img_1.jpg"
        image = cv2.imread(f"test_images/original/{file_name}")
        return image
