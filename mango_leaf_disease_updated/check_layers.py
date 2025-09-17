import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model("mango_leaf_disease_model.h5")

# Print all layers
for i, layer in enumerate(model.layers):
    print(i, layer.name, layer.__class__.__name__)
