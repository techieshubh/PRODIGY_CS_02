from PIL import Image
import numpy as np
def encrypt_image(image_path, key):
    image = Image.open(image_path)
    img_array = np.array(image)
    encrypted_array = img_array ^ key
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save("encrypted_image.png")
def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)
    decrypted_array = encrypted_array ^ key
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save("decrypted_image.png")
key = 200  
encrypt_image("input_image.png", key)
decrypt_image("encrypted_image.png", key)
