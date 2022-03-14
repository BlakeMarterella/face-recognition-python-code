import face_recognition as fr
import pickle
import cv2
from matplotlib import image
import numpy as np
import os

path = "./faces"

# Initialize the pickle
# Reerence Dictonary
try:
    f=open("ref_name.pkl","rb")

    ref_dictt=pickle.load(f)
    f.close()
except:
    ref_dictt={}

# Embed dictionary
try:
    f=open("ref_embed.pkl","rb")

    embed_dictt=pickle.load(f)
    f.close()
except:
    embed_dictt={}
    

faces = os.listdir(path)
# Run through all of the directories and look for a face
id = 5000
for _ in os.listdir(path):
    print(_)
    person_path = path + "/" + _ + "/"
    name = str(_)
    ref_id = id
    
    ref_dictt[ref_id]=name
    f=open("ref_name.pkl","wb")
    pickle.dump(ref_dictt,f)
    f.close()
    
    # Incremet the ID
    id += 1
    
    # Run through the files in the subdirectory
    for _ in os.listdir(person_path):
        print("  |-" + _)
        face_path = person_path + _
        face = fr.load_image_file(face_path)
        # Convert the image into a small frame that can be read
        small_frame = cv2.resize(face, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        # Parse the face out of the image
        face_locations = fr.face_locations(rgb_small_frame)
        # Check that the array isnt empty so no duplicate training faces are added
        if face_locations != []:
            face_encoding = fr.face_encodings(face)[0]
            # Check if the id of the person already exists in the pickle database
            if ref_id in embed_dictt:
                embed_dictt[ref_id]+=[face_encoding]
            else:
                embed_dictt[ref_id]=[face_encoding]   
    
f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f)
f.close()