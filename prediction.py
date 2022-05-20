import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPool2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from numpy.linalg import norm
import numpy as np
from sklearn.neighbors import NearestNeighbors
import pickle

# model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False  # model is already trained

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPool2D()
])

# feature_list = np.array(pickle.load(open('assets/embeddings.pkl', 'rb')))
# filenames = pickle.load(open('filenames.pkl', 'rb'))

feature_list = np.array(pickle.load(open('flipkart_embeddings.pkl', 'rb')))

# creating feature for given image
def extract_features(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result


def get_result(img_path):
    norm_result = extract_features(img_path, model)
    neighbors = NearestNeighbors(n_neighbors=10, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([norm_result])

    # return [filenames[file] for file in indices[0]]
    return indices.tolist()[0]
