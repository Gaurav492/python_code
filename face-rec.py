import os
import cv2
import face_recognition

# Function to detect faces in an image
def detect_faces(image_path):
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)
    return [(top, right, bottom, left) for (top, right, bottom, left) in face_locations]

# Function to encode faces in an image
def encode_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

# Main function to process images
def sort_images_by_faces(image_folder):
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        faces = detect_faces(image_path)
        if len(faces) == 0:
            print(f"No faces found in {image_file}")
            continue
        
        # For simplicity, just take the first face
        face_encoding = encode_faces(image_path)[0]
        # Now you can compare this face encoding with others and sort accordingly
        # For demonstration purposes, you might want to save or move the images to different folders based on face similarities.

# Example usage
image_folder = "path_to_your_image_folder"
sort_images_by_faces(image_folder)