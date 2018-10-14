Pic --> 1 * 1200 * 1400
Load --> None, 1680000
Conv --> Convolution2D(
    batch_input_shape=(None, 1400, 1200, 1),
    filters=256,
    kernel_size=5,
    strides=1,
    padding='same',     # Padding method
    data_format='channels_first',
)