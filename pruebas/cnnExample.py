import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import numpy as np

batch_size = 128
num_classes = 10
epochs = 12

# Dimensiones de las imagenes de entrada
img_rows, img_cols = 28, 28

# Separamos la información del dataset en conjuntos de entrenamiento y de prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# El valor de 60000 corresponde al numero de elementos del datasent para entrenamiento, el 28 al tamaño de las imagenes
# El cuarto paramentro de reshape corresponde al número de canales, en este caso es 1 porque las imagenes son escala de grises, para RGB será 3
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Convertimos nuestros valores de target en matrices binarias
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# Construimos un modelo secuencial y se le agregan capas convolucionales, del pooling, flatten, etc.
# Las capas de Droput cambain algunas neuronas en la red para obligar a los datos en encontrar diferentes caminos
# Las capas de Dense son usadas para reducir la predicción de clases (0-9)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(28,28,1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compilamos el modelo con los siguientes parametros de loss, optimizer y metrics
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# Para este caso entrenamos la red para 12 epochs y mostramos la precisión del modelo
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""# Predicción de las primeras 4 imagenes del conjunto de prueba
model.predict(x_test[:4])
# Valor real de las primeras 4 imagenes del conjunto de prueba
y_test[:4]"""