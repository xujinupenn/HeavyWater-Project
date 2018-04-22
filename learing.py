import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.models import load_model  
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.optimizers import Adam

import os 

import win_unicode_console
win_unicode_console.enable()

class learn:
    def __init__(self,x_train,y_train):
        self.x_train =x_train
        self.y_train = y_train


    def run(self):
        # Generate dummy data


        model = Sequential()
        # input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
        # this applies 32 convolution filters of size 3x3 each.
        
        model.add(Dense(256, activation='relu', input_shape=(self.x_train.shape[1],)))
        model.add(Dense(124, activation='relu'))
        #model.add(Flatten())
        model.add(Dense(50, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dropout(0.5))
        model.add(Dense(512, activation='softmax'))
        model.add(Dropout(0.5))
        model.add(Dense(256, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(32, activation='softmax'))
        model.add(Dropout(0.5))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(self.y_train.shape[1], activation='softmax'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        adam_lr = 0.0002

        adam_beta_1 = 0.5
        adam_test =Adam(lr=adam_lr, beta_1=adam_beta_1)
        model.compile(loss='categorical_crossentropy',  optimizer=adam_test,metrics=['accuracy'])

        model.fit(self.x_train, self.y_train, batch_size=32, epochs=100)
        #save the model 

        model.save('my_model.h5')

    def load_model(self):
        if os.path.exists('my_model.h5'):
            self.model  = load_model('my_model.h5')

        else:
            self.run()

    def predict_model(self,test):
        self.load_model()
        if self.model==None:
            self.load_model()
        else:
            return self.model.predict(test)
            
if __name__ =="__main__":
    x_train = np.zeros((100,10000))
    y_train = keras.utils.to_categorical(np.random.randint(100, size=(100, 1)), num_classes=100)
    print(y_train.shape)
    peihongliang =learn(x_train,y_train)
    peihongliang.load_model()