from keras.models import load_model,model_from_json
"""

model = load_model('./models/models_ECGModel.hdf5')

model._make_predict_function()          # Necessary



#file = cv2.imread("f.jpeg")


pred = model.predict(data.reshape((1, 128, 128, 3)))    
pred_class = pred.argmax(axis=-1)

json_config = model.to_json()

with open('model.json', 'w') as json_file:
    json_file.write(json_config)


# Save weights to disk
model.save_weights('weights_cnn.h5')

"""
import cv2

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()

json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('weights_cnn.h5')

file = cv2.imread("f.jpeg")


pred = loaded_model.predict(file.reshape((1, 128, 128, 3)))    
pred_class = pred.argmax(axis=-1)
print(pred_class)

"""
signature = predict_signature_def(
    inputs={"inputs": loaded_model.input}, outputs={"score": loaded_model.output})}}

from keras import backend as K

with K.get_session() as sess:
    # Save the meta graph and variables
    builder.add_meta_graph_and_variables(
        sess=sess, tags=[tag_constants.SERVING], signature_def_map={"serving_default": signature})
    builder.save()
"""