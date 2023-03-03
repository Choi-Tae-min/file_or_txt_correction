import tensorflow as tf

# Open the event file
file_path = 'C:/Users/user/tmp/Endo_mono/train/events.out.tfevents.1677053767.DESKTOP-SFV2FI1'
file_reader = tf.data.TFRecordDataset(file_path)

# Iterate over all events in the file
for record in file_reader:
    event = tf.compat.v1.Event()
    event.ParseFromString(record.numpy())
    # Check if the event contains a summary
    if event.summary:
        # Iterate over all values in the summary
        for value in event.summary.value:
            # Extract the tag and value of the summary
            tag = value.tag
            tensor_proto = value.tensor
            # Convert the tensor proto to a numpy array
            tensor = tf.make_ndarray(tensor_proto)
            print(f'Tag: {tag}, Value: {tensor}')