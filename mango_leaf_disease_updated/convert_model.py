import tensorflow as tf
from keras.utils import custom_object_scope
from tensorflow.keras.layers import Lambda

# Use custom_object_scope to handle TFOpLambda
with custom_object_scope({'TFOpLambda': Lambda}):
    model = tf.keras.models.load_model(
        "mango_leaf_disease_model.h5",
        compile=False  # ignore compile since we only need inference
    )
print("✅ Loaded .h5 model with TFOpLambda")

# Save as .keras file
model.save("mango_leaf_disease_model.keras")
print("✅ Saved as mango_leaf_disease_model.keras")

# Save as SavedModel folder
model.save("mango_leaf_disease_model")  # folder will be created
print("✅ Saved as SavedModel format (folder)")
