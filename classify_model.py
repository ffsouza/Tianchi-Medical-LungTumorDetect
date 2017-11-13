from keras.models import Model
from keras.layers import Input, Conv3D, MaxPooling3D, Dense, GlobalMaxPooling3D, Dropout
from config import *

def get_VGG_classifier():
    inputs = Input((INPUT_WIDTH, INPUT_HEIGHT, INPUT_DEPTH, INPUT_CHANNEL))

    x = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(inputs)
    x = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(x)
    x = MaxPooling3D(pool_size=(2, 2, 2))(x)

    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)
    x = MaxPooling3D(pool_size=(2, 2, 2))(x)

    x = Conv3D(128, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(128, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(128, (3, 3, 3), padding='same', activation='relu')(x)
    x = MaxPooling3D(pool_size=(2, 2, 2))(x)

    x = Conv3D(256, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(256, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(256, (3, 3, 3), padding='same', activation='relu')(x)
    # x = MaxPooling3D(pool_size=(2, 2, 2))(x)
    #
    # x = Conv3D(512, (3, 3, 3), padding='same', activation='relu')(x)
    # x = Conv3D(512, (3, 3, 3), padding='same', activation='relu')(x)
    # x = Conv3D(512, (3, 3, 3), padding='same', activation='relu')(x)
    x = GlobalMaxPooling3D()(x)

    x = Dense(32, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(2, activation='softmax')(x)

    model = Model(inputs=inputs, outputs=x)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

if __name__ == '__main__':
    n = get_VGG_classifier()
    n.summary()