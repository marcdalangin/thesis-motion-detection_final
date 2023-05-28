x_train shape: (7062, 28, 28, 3)
7062 train samples
1413 test samples
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 28, 28, 64)        1792

 batch_normalization (BatchN  (None, 28, 28, 64)       256
 ormalization)

 activation (Activation)     (None, 28, 28, 64)        0

 conv2d_1 (Conv2D)           (None, 28, 28, 64)        36928

 batch_normalization_1 (Batc  (None, 28, 28, 64)       256
 hNormalization)

 activation_1 (Activation)   (None, 28, 28, 64)        0

 conv2d_2 (Conv2D)           (None, 28, 28, 64)        36928

 dropout (Dropout)           (None, 28, 28, 64)        0

 conv2d_3 (Conv2D)           (None, 28, 28, 64)        4160

 conv2d_4 (Conv2D)           (None, 28, 28, 64)        36928

 max_pooling2d (MaxPooling2D  (None, 14, 14, 64)       0
 )

 conv2d_5 (Conv2D)           (None, 14, 14, 128)       73856

 batch_normalization_2 (Batc  (None, 14, 14, 128)      512
 hNormalization)

 activation_2 (Activation)   (None, 14, 14, 128)       0

 conv2d_6 (Conv2D)           (None, 14, 14, 128)       147584

 batch_normalization_3 (Batc  (None, 14, 14, 128)      512
 hNormalization)

 activation_3 (Activation)   (None, 14, 14, 128)       0

 conv2d_7 (Conv2D)           (None, 14, 14, 128)       147584

 dropout_1 (Dropout)         (None, 14, 14, 128)       0

 conv2d_8 (Conv2D)           (None, 14, 14, 128)       16512

 conv2d_9 (Conv2D)           (None, 14, 14, 128)       147584

 max_pooling2d_1 (MaxPooling  (None, 7, 7, 128)        0
 2D)

 conv2d_10 (Conv2D)          (None, 7, 7, 256)         295168

 batch_normalization_4 (Batc  (None, 7, 7, 256)        1024
 hNormalization)

 activation_4 (Activation)   (None, 7, 7, 256)         0

 conv2d_11 (Conv2D)          (None, 7, 7, 256)         590080

 batch_normalization_5 (Batc  (None, 7, 7, 256)        1024
 hNormalization)

 activation_5 (Activation)   (None, 7, 7, 256)         0

 conv2d_12 (Conv2D)          (None, 7, 7, 256)         590080

 dropout_2 (Dropout)         (None, 7, 7, 256)         0

 conv2d_13 (Conv2D)          (None, 7, 7, 256)         65792

 conv2d_14 (Conv2D)          (None, 7, 7, 256)         590080

 global_average_pooling2d (G  (None, 256)              0
 lobalAveragePooling2D)

 dense (Dense)               (None, 128)               32896

 batch_normalization_6 (Batc  (None, 128)              512
 hNormalization)

 activation_6 (Activation)   (None, 128)               0

 dropout_3 (Dropout)         (None, 128)               0

 dense_1 (Dense)             (None, 10)                1290

=================================================================
Total params: 2,819,338
Trainable params: 2,817,290
Non-trainable params: 2,048
_________________________________________________________________
None
Epoch 1/50
318/318 [==============================] - 120s 366ms/step - loss: 2.0881 - accuracy: 0.2838 - val_loss: 7.9173 - val_accuracy: 0.1593
Epoch 2/50
318/318 [==============================] - 108s 340ms/step - loss: 1.3568 - accuracy: 0.5079 - val_loss: 17.7419 - val_accuracy: 0.1292
Epoch 3/50
318/318 [==============================] - 103s 323ms/step - loss: 1.0929 - accuracy: 0.6178 - val_loss: 5.2629 - val_accuracy: 0.4230
Epoch 4/50
318/318 [==============================] - 96s 303ms/step - loss: 0.7716 - accuracy: 0.7459 - val_loss: 0.6720 - val_accuracy: 0.7770
Epoch 5/50
318/318 [==============================] - 96s 301ms/step - loss: 0.4483 - accuracy: 0.8609 - val_loss: 1.3425 - val_accuracy: 0.6088
Epoch 6/50
318/318 [==============================] - 95s 300ms/step - loss: 0.3637 - accuracy: 0.8830 - val_loss: 0.7178 - val_accuracy: 0.7487
Epoch 7/50
318/318 [==============================] - 94s 297ms/step - loss: 0.2606 - accuracy: 0.9235 - val_loss: 0.7973 - val_accuracy: 0.7628
Epoch 8/50
318/318 [==============================] - 94s 296ms/step - loss: 0.2309 - accuracy: 0.9298 - val_loss: 0.2786 - val_accuracy: 0.9062
Epoch 9/50
318/318 [==============================] - 95s 298ms/step - loss: 0.1900 - accuracy: 0.9404 - val_loss: 0.0547 - val_accuracy: 0.9823
Epoch 10/50
318/318 [==============================] - 112s 352ms/step - loss: 0.1640 - accuracy: 0.9504 - val_loss: 0.4906 - val_accuracy: 0.8637
Epoch 11/50
318/318 [==============================] - 107s 336ms/step - loss: 0.1452 - accuracy: 0.9548 - val_loss: 0.0960 - val_accuracy: 0.9646
Epoch 12/50
318/318 [==============================] - 109s 341ms/step - loss: 0.1211 - accuracy: 0.9648 - val_loss: 0.3892 - val_accuracy: 0.8850
Epoch 13/50
318/318 [==============================] - 108s 340ms/step - loss: 0.1001 - accuracy: 0.9703 - val_loss: 0.6951 - val_accuracy: 0.8000
Epoch 14/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0966 - accuracy: 0.9731 - val_loss: 0.1771 - val_accuracy: 0.9487
Epoch 15/50
318/318 [==============================] - 106s 333ms/step - loss: 0.1012 - accuracy: 0.9717 - val_loss: 0.0546 - val_accuracy: 0.9841
Epoch 16/50
318/318 [==============================] - 106s 334ms/step - loss: 0.0781 - accuracy: 0.9776 - val_loss: 0.0825 - val_accuracy: 0.9717
Epoch 17/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0764 - accuracy: 0.9754 - val_loss: 0.0980 - val_accuracy: 0.9681
Epoch 18/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0835 - accuracy: 0.9766 - val_loss: 0.0461 - val_accuracy: 0.9841
Epoch 19/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0945 - accuracy: 0.9738 - val_loss: 0.4742 - val_accuracy: 0.8389
Epoch 20/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0870 - accuracy: 0.9774 - val_loss: 0.0501 - val_accuracy: 0.9858
Epoch 21/50
318/318 [==============================] - 105s 331ms/step - loss: 0.0746 - accuracy: 0.9774 - val_loss: 1.3460 - val_accuracy: 0.8372
Epoch 22/50
318/318 [==============================] - 105s 330ms/step - loss: 0.0781 - accuracy: 0.9772 - val_loss: 0.0227 - val_accuracy: 0.9894
Epoch 23/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0591 - accuracy: 0.9839 - val_loss: 0.0062 - val_accuracy: 1.0000
Epoch 24/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0471 - accuracy: 0.9878 - val_loss: 0.0407 - val_accuracy: 0.9876
Epoch 25/50
318/318 [==============================] - 104s 328ms/step - loss: 0.0696 - accuracy: 0.9811 - val_loss: 0.2218 - val_accuracy: 0.9416
Epoch 26/50
318/318 [==============================] - 105s 330ms/step - loss: 0.0501 - accuracy: 0.9864 - val_loss: 0.1614 - val_accuracy: 0.9593
Epoch 27/50
318/318 [==============================] - 104s 327ms/step - loss: 0.0708 - accuracy: 0.9790 - val_loss: 0.0946 - val_accuracy: 0.9770
Epoch 28/50
318/318 [==============================] - 105s 331ms/step - loss: 0.0418 - accuracy: 0.9884 - val_loss: 0.0842 - val_accuracy: 0.9752
Epoch 29/50
318/318 [==============================] - 105s 329ms/step - loss: 0.0418 - accuracy: 0.9882 - val_loss: 0.1026 - val_accuracy: 0.9735
Epoch 30/50
318/318 [==============================] - 106s 332ms/step - loss: 0.0455 - accuracy: 0.9847 - val_loss: 0.0276 - val_accuracy: 0.9894
Epoch 31/50
318/318 [==============================] - 105s 330ms/step - loss: 0.0501 - accuracy: 0.9843 - val_loss: 0.0046 - val_accuracy: 0.9982
Epoch 32/50
318/318 [==============================] - 104s 328ms/step - loss: 0.0324 - accuracy: 0.9904 - val_loss: 3.8109e-04 - val_accuracy: 1.0000
Epoch 33/50
318/318 [==============================] - 104s 328ms/step - loss: 0.0208 - accuracy: 0.9947 - val_loss: 0.0509 - val_accuracy: 0.9876
Epoch 34/50
318/318 [==============================] - 105s 331ms/step - loss: 0.0445 - accuracy: 0.9862 - val_loss: 0.0059 - val_accuracy: 0.9982
Epoch 35/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0160 - accuracy: 0.9974 - val_loss: 0.0013 - val_accuracy: 1.0000
Epoch 36/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0323 - accuracy: 0.9904 - val_loss: 0.0230 - val_accuracy: 0.9929
Epoch 37/50
318/318 [==============================] - 107s 338ms/step - loss: 0.0629 - accuracy: 0.9807 - val_loss: 0.0505 - val_accuracy: 0.9876
Epoch 38/50
318/318 [==============================] - 105s 331ms/step - loss: 0.0392 - accuracy: 0.9880 - val_loss: 0.0039 - val_accuracy: 0.9982
Epoch 39/50
318/318 [==============================] - 107s 336ms/step - loss: 0.0313 - accuracy: 0.9927 - val_loss: 0.0271 - val_accuracy: 0.9894
Epoch 40/50
318/318 [==============================] - 107s 336ms/step - loss: 0.0332 - accuracy: 0.9910 - val_loss: 0.0914 - val_accuracy: 0.9823
Epoch 41/50
318/318 [==============================] - 107s 337ms/step - loss: 0.0376 - accuracy: 0.9878 - val_loss: 0.0213 - val_accuracy: 0.9965
Epoch 42/50
318/318 [==============================] - 108s 339ms/step - loss: 0.0268 - accuracy: 0.9915 - val_loss: 0.1015 - val_accuracy: 0.9770
Epoch 43/50
318/318 [==============================] - 108s 339ms/step - loss: 0.0188 - accuracy: 0.9945 - val_loss: 0.0060 - val_accuracy: 0.9982
Epoch 44/50
318/318 [==============================] - 107s 338ms/step - loss: 0.0227 - accuracy: 0.9943 - val_loss: 0.0045 - val_accuracy: 0.9982
Epoch 45/50
318/318 [==============================] - 107s 337ms/step - loss: 0.0135 - accuracy: 0.9967 - val_loss: 4.3447e-04 - val_accuracy: 1.0000
Epoch 46/50
318/318 [==============================] - 108s 340ms/step - loss: 0.0172 - accuracy: 0.9943 - val_loss: 0.0146 - val_accuracy: 0.9947
Epoch 47/50
318/318 [==============================] - 109s 343ms/step - loss: 0.0557 - accuracy: 0.9856 - val_loss: 0.0267 - val_accuracy: 0.9947
Epoch 48/50
318/318 [==============================] - 109s 342ms/step - loss: 0.0334 - accuracy: 0.9904 - val_loss: 0.0333 - val_accuracy: 0.9929
Epoch 49/50
318/318 [==============================] - 108s 339ms/step - loss: 0.0160 - accuracy: 0.9953 - val_loss: 0.0034 - val_accuracy: 0.9982
Epoch 50/50
318/318 [==============================] - 106s 333ms/step - loss: 0.0179 - accuracy: 0.9959 - val_loss: 0.0012 - val_accuracy: 1.0000
Test loss: 0.017648886889219284
Test accuracy: 0.9957537055015564
