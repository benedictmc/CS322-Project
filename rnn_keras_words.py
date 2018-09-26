import random
import numpy as np
from glob import glob
import pickle
from keras.models import Sequential, load_model
from keras.layers import CuDNNLSTM as LSTM
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import RMSprop
import heapq

class Predict_Lyrics():
    FILENAME = 'kanye_songs.txt'
    EPOCHS = 60  
    BATCH_SIZE = 128 
    MAX_LEN = 20 #Vector size
    SQUENCE_LENGTH = 5
    SQUENCE_STEP = 1 

    QUOTES = ["Well, it is a weepin' and a moanin' and ",
                "a gnashin' of teeth It is a weepin' and ",
                "a mournin' and a gnashin' of teeth It is",
                " a— when it comes to my sound which is t"]

    def __init__(self):
        ## Opens lyrics text file and loads it into a string
        self.data = open(Predict_Lyrics.FILENAME, encoding='utf-8').read()
        self.data = self.data.split()
        self.word_string = self.data  
        ## Creates a list of unquie characters in the lyrics string
        self.unquie_tokens = sorted(list(set(self.data)))
        self.preprocess_data()
        self.squences, self.saved_chars = self.create_squences()
        for i in range(10):
            print("The squence is {}, with saved_word is {}".format(self.squences[i], self.saved_chars[i]))
        self.X, self.y = self.create_feature_labels()
        # self.preform_ml()
        # self.use_model()
        # print(self.predict_completions("Hello my name is Ben and I like cheese a", 5))
        # for q in Predict_Lyrics.QUOTES:
        #     seq = q[:40].lower()
        #     print(seq)
        #     print(self.predict_completions(seq, 5))

    def preprocess_data(self):
        ## Creates a dictionary obejct with unquie characters as keys and interative counters as a values
        self.char_index = {ch:i for i, ch in enumerate(self.unquie_tokens)}
        ## Creates a dictionary obejct with interative counters as keys and unquie characters as a values
        self.index_char = {i:ch for i, ch in enumerate(self.unquie_tokens)}
        print("There are {} unquie characters".format(len(self.unquie_tokens)))

    def create_feature_labels(self):

        ## Makes a 3D array of false booleans of length amount_of_squences x squence_length (40) x amount_of_unquie_chars 
        X = np.zeros((len(self.squences), Predict_Lyrics.SQUENCE_LENGTH, len(self.unquie_tokens)), dtype=np.bool)
        ## Makes a 2D array of false booleans of length amount_of_squences x amount_of_unquie_chars 
        y = np.zeros((len(self.squences), len(self.unquie_tokens)), dtype=np.bool)

        print("The shape of the X array is {}, and the shape of the y array is {}".format(str(X.shape), str(y.shape)))

        ## Interates through squences list 
        for idx_squence, squence in enumerate(self.squences):
            ## Interates through string invariant 
            for idx_char, char in enumerate(squence):
                ## Places a true variable in the [idx_squence, idx_char, unquie_val_of_char] 
                X[idx_squence, idx_char, self.char_index[char]] = 1
             ## Places a true variable in the [idx_squence, unquie_val_of_char[saved_char_of_squence]] 
            y[idx_squence, self.char_index[self.saved_chars[idx_squence]]] = 1

        return X, y

    def create_squences(self):
        step = Predict_Lyrics.SQUENCE_STEP
        length = Predict_Lyrics.SQUENCE_LENGTH
        squences, saved_char = [], []
        ## Creates list of squences of length 40 of the lyrics string starting at 0 and steping up of length 3
        ## Creates list of chars of the next character after squence corresponding to the same index of the 'squences' list
        for pointer in range(0, len(self.word_string) - length , step):
            squences.append(self.word_string[pointer:length+pointer])
            if length+(pointer+1) <= len(self.word_string):
                saved_char.append(self.word_string[length+pointer])
        return squences, saved_char

    def preform_ml(self):
        ## Builds Keras LSTM model
        model = Sequential()
        ## Makes LSTM layer to correspond with length of squences x amount_unquie_chars
        model.add(LSTM(128, input_shape=(Predict_Lyrics.SQUENCE_LENGTH, len(self.unquie_tokens))))
        ## A Dence layer to pad out by amount_unquie_chars
        model.add(Dense(len(self.unquie_tokens)))
        ## An activation softmax layer 
        model.add(Activation('softmax'))

        optimizer = RMSprop(lr=0.01)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        history = model.fit(self.X, self.y, validation_split=0.05, batch_size=128, epochs=20, shuffle=True).history

        model.save('first_model.h5')
        pickle.dump(history, open("history.p", "wb"))



    def use_model(self):
        self.model = load_model("first_model.h5") 

    def prepare_input(self, text):
        x = np.zeros((1, Predict_Lyrics.SQUENCE_LENGTH, len(self.unquie_tokens)))
        for t, char in enumerate(text):
            x[0, t, self.char_index[char]] = 1.
        return x

    def sample(self, preds, top_n=3):
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds)
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        return heapq.nlargest(top_n, range(len(preds)), preds.take)

    def predict_completion(self, text):
        original_text = text
        generated = text
        completion = ''
        while True:
            x = self.prepare_input(text)
            preds = self.model.predict(x, verbose=0)[0]
            next_index = self.sample(preds, top_n=1)[0]
            next_char = self.index_char[next_index]
            text = text[1:] + next_char
            completion += next_char
            
            if len(original_text + completion) + 2 > len(original_text) and next_char == ' ':
                return completion


    def predict_completions(self, text, n=3):
        x = self.prepare_input(text)
        preds = self.model.predict(x, verbose=0)[0]
        next_indices = self.sample(preds, n)
        return [self.index_char[idx] + self.predict_completion(text[1:] + self.index_char[idx]) for idx in next_indices]

x = Predict_Lyrics()
