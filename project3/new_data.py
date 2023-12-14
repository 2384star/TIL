import tensorflow as tf

def prepare_training_data(category_columns, numeric_columns, train_data):
    X_train_cate_input = train_data[[col + "_enc" for col in category_columns]].values
    X_train_num_input = train_data[[col + "_std" for col in numeric_columns]].values

    training_dataset = tf.data.Dataset.from_tensor_slices(((X_train_cate_input, X_train_num_input),))
    training_dataset = training_dataset.batch(1)
    return training_dataset
