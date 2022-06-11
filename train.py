import numpy as np
import face_recognition
import os

#This is face recognisation model train using face_recognition from facenet
##
facedir='knownfaces'

known_face_encoding_file='known_face_encodings.npy'

def facenetFaceencoding(facedir):
    known_face_encoding_file='known_face_encodings.npy'
    known_face_names_file='known_face_names.npy'
    if os.path.isfile(known_face_encoding_file):
        os.remove(known_face_encoding_file)
    if os.path.isfile(known_face_names_file):
        os.remove(known_face_names_file)
    known_face_encodings=[]
    known_face_names=[]
    for i in os.listdir(facedir):
        if i.endswith('.jpg') or i.endswith('.JPG') or i.endswith('.JPEG') or i.endswith('.png') or i.endswith('.jpeg'):
            imagePath=os.path.join(facedir,i)
            name=i.split('.')[0]
            name_image=name+'_image'
            name_image=face_recognition.load_image_file(imagePath)
            name_face_encode=name+'_face_encoding'
            name_face_encode=face_recognition.face_encodings(name_image)[0]
            known_face_encodings.append(name_face_encode)
            known_face_names.append(name)
    np.save(known_face_encoding_file,known_face_encodings)
    np.save(known_face_names_file,known_face_names)
    return known_face_encodings,known_face_names

facenetFaceencoding(facedir)
