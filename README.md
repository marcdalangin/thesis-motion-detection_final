
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


trained_model_0821

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
Epoch 1/50
318/318 [==============================] - 103s 313ms/step - loss: 2.0592 - accuracy: 0.2752 - val_loss: 4.1919 - val_accuracy: 0.1416
Epoch 2/50
318/318 [==============================] - 111s 349ms/step - loss: 1.4181 - accuracy: 0.4780 - val_loss: 9.5981 - val_accuracy: 0.2584
Epoch 3/50
318/318 [==============================] - 93s 291ms/step - loss: 1.1040 - accuracy: 0.5978 - val_loss: 11.3900 - val_accuracy: 0.1345
Epoch 4/50
318/318 [==============================] - 97s 306ms/step - loss: 0.9436 - accuracy: 0.6660 - val_loss: 6.2616 - val_accuracy: 0.2496
Epoch 5/50
318/318 [==============================] - 95s 299ms/step - loss: 0.7722 - accuracy: 0.7288 - val_loss: 8.3966 - val_accuracy: 0.2212
Epoch 6/50
318/318 [==============================] - 97s 304ms/step - loss: 0.5868 - accuracy: 0.8000 - val_loss: 0.9857 - val_accuracy: 0.6425
Epoch 7/50
318/318 [==============================] - 95s 300ms/step - loss: 0.4174 - accuracy: 0.8635 - val_loss: 0.9312 - val_accuracy: 0.7522
Epoch 8/50
318/318 [==============================] - 99s 311ms/step - loss: 0.3104 - accuracy: 0.9003 - val_loss: 0.2193 - val_accuracy: 0.9168
Epoch 9/50
318/318 [==============================] - 98s 308ms/step - loss: 0.2728 - accuracy: 0.9170 - val_loss: 0.2183 - val_accuracy: 0.9239
Epoch 10/50
318/318 [==============================] - 96s 303ms/step - loss: 0.2450 - accuracy: 0.9225 - val_loss: 0.3285 - val_accuracy: 0.8673
Epoch 11/50
318/318 [==============================] - 97s 305ms/step - loss: 0.1998 - accuracy: 0.9363 - val_loss: 0.7328 - val_accuracy: 0.7770
Epoch 12/50
318/318 [==============================] - 95s 299ms/step - loss: 0.1779 - accuracy: 0.9459 - val_loss: 0.1407 - val_accuracy: 0.9646
Epoch 13/50
318/318 [==============================] - 93s 293ms/step - loss: 0.1529 - accuracy: 0.9542 - val_loss: 0.1474 - val_accuracy: 0.9487
Epoch 14/50
318/318 [==============================] - 93s 294ms/step - loss: 0.1388 - accuracy: 0.9567 - val_loss: 0.0380 - val_accuracy: 0.9929
Epoch 15/50
318/318 [==============================] - 94s 294ms/step - loss: 0.1428 - accuracy: 0.9561 - val_loss: 0.2909 - val_accuracy: 0.9080
Epoch 16/50
318/318 [==============================] - 93s 292ms/step - loss: 0.1503 - accuracy: 0.9493 - val_loss: 0.0431 - val_accuracy: 0.9894
Epoch 17/50
318/318 [==============================] - 94s 296ms/step - loss: 0.1383 - accuracy: 0.9591 - val_loss: 0.0483 - val_accuracy: 0.9805
Epoch 18/50
318/318 [==============================] - 93s 291ms/step - loss: 0.0958 - accuracy: 0.9736 - val_loss: 0.0667 - val_accuracy: 0.9770
Epoch 19/50
318/318 [==============================] - 92s 290ms/step - loss: 0.1025 - accuracy: 0.9707 - val_loss: 0.4853 - val_accuracy: 0.8566
Epoch 20/50
318/318 [==============================] - 96s 302ms/step - loss: 0.1007 - accuracy: 0.9701 - val_loss: 0.1648 - val_accuracy: 0.9504
Epoch 21/50
318/318 [==============================] - 103s 323ms/step - loss: 0.0992 - accuracy: 0.9691 - val_loss: 0.0435 - val_accuracy: 0.9841
Epoch 22/50
318/318 [==============================] - 121s 382ms/step - loss: 0.0862 - accuracy: 0.9758 - val_loss: 0.0387 - val_accuracy: 0.9894
Epoch 23/50
318/318 [==============================] - 112s 351ms/step - loss: 0.1031 - accuracy: 0.9701 - val_loss: 0.0707 - val_accuracy: 0.9770
Epoch 24/50
318/318 [==============================] - 99s 311ms/step - loss: 0.0624 - accuracy: 0.9829 - val_loss: 0.0128 - val_accuracy: 0.9965
Epoch 25/50
318/318 [==============================] - 102s 322ms/step - loss: 0.0763 - accuracy: 0.9774 - val_loss: 0.1193 - val_accuracy: 0.9611
Epoch 26/50
318/318 [==============================] - 101s 317ms/step - loss: 0.0904 - accuracy: 0.9760 - val_loss: 0.0464 - val_accuracy: 0.9858
Epoch 27/50
318/318 [==============================] - 102s 321ms/step - loss: 0.0707 - accuracy: 0.9784 - val_loss: 0.1915 - val_accuracy: 0.9363
Epoch 28/50
318/318 [==============================] - 103s 325ms/step - loss: 0.0706 - accuracy: 0.9799 - val_loss: 0.0238 - val_accuracy: 0.9894
Epoch 29/50
318/318 [==============================] - 109s 343ms/step - loss: 0.0727 - accuracy: 0.9782 - val_loss: 0.5992 - val_accuracy: 0.8814
Epoch 30/50
318/318 [==============================] - 111s 348ms/step - loss: 0.0667 - accuracy: 0.9790 - val_loss: 0.2689 - val_accuracy: 0.9115
Epoch 31/50
318/318 [==============================] - 110s 347ms/step - loss: 0.0498 - accuracy: 0.9858 - val_loss: 0.3900 - val_accuracy: 0.8814
Epoch 32/50
318/318 [==============================] - 110s 346ms/step - loss: 0.0567 - accuracy: 0.9839 - val_loss: 0.0391 - val_accuracy: 0.9876
Epoch 33/50
318/318 [==============================] - 110s 347ms/step - loss: 0.0830 - accuracy: 0.9762 - val_loss: 0.1334 - val_accuracy: 0.9540
Epoch 34/50
318/318 [==============================] - 107s 337ms/step - loss: 0.0405 - accuracy: 0.9876 - val_loss: 0.0109 - val_accuracy: 0.9982
Epoch 35/50
318/318 [==============================] - 109s 343ms/step - loss: 0.0303 - accuracy: 0.9919 - val_loss: 0.0024 - val_accuracy: 1.0000
Epoch 36/50
318/318 [==============================] - 111s 348ms/step - loss: 0.0449 - accuracy: 0.9852 - val_loss: 0.0522 - val_accuracy: 0.9805
Epoch 37/50
318/318 [==============================] - 111s 348ms/step - loss: 0.0600 - accuracy: 0.9821 - val_loss: 0.0145 - val_accuracy: 0.9912
Epoch 38/50
318/318 [==============================] - 109s 341ms/step - loss: 0.0570 - accuracy: 0.9864 - val_loss: 0.7770 - val_accuracy: 0.8124
Epoch 39/50
318/318 [==============================] - 125s 394ms/step - loss: 0.0666 - accuracy: 0.9811 - val_loss: 0.0050 - val_accuracy: 0.9965
Epoch 40/50
318/318 [==============================] - 134s 420ms/step - loss: 0.0325 - accuracy: 0.9904 - val_loss: 0.0065 - val_accuracy: 0.9982
Epoch 41/50
318/318 [==============================] - 135s 426ms/step - loss: 0.0374 - accuracy: 0.9894 - val_loss: 0.0451 - val_accuracy: 0.9858
Epoch 42/50
318/318 [==============================] - 134s 421ms/step - loss: 0.0344 - accuracy: 0.9904 - val_loss: 0.0151 - val_accuracy: 0.9982
Epoch 43/50
318/318 [==============================] - 130s 407ms/step - loss: 0.0473 - accuracy: 0.9849 - val_loss: 0.1296 - val_accuracy: 0.9469
Epoch 44/50
318/318 [==============================] - 127s 400ms/step - loss: 0.0467 - accuracy: 0.9847 - val_loss: 0.0446 - val_accuracy: 0.9876
Epoch 45/50
318/318 [==============================] - 131s 411ms/step - loss: 0.0598 - accuracy: 0.9801 - val_loss: 0.1427 - val_accuracy: 0.9681
Epoch 46/50
318/318 [==============================] - 131s 411ms/step - loss: 0.0432 - accuracy: 0.9872 - val_loss: 0.0208 - val_accuracy: 0.9929
Epoch 47/50
318/318 [==============================] - 130s 410ms/step - loss: 0.0207 - accuracy: 0.9941 - val_loss: 0.0162 - val_accuracy: 0.9947
Epoch 48/50
318/318 [==============================] - 130s 410ms/step - loss: 0.0525 - accuracy: 0.9843 - val_loss: 0.0516 - val_accuracy: 0.9841
Epoch 49/50
318/318 [==============================] - 130s 410ms/step - loss: 0.0285 - accuracy: 0.9904 - val_loss: 0.0342 - val_accuracy: 0.9894
Epoch 50/50
318/318 [==============================] - 125s 393ms/step - loss: 0.0248 - accuracy: 0.9929 - val_loss: 0.0375 - val_accuracy: 0.9894
Test loss: 0.06903823465108871
Test accuracy: 0.9808917045593262
