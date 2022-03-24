lb=LabelEncoder()
data['airline_sentiment'] = lb.fit_transform(data['airline_sentiment'])

tokenizer = Tokenizer(num_words=500, split=' ') 
tokenizer.fit_on_texts(data['text_tokenized'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X)

model = Sequential()
model.add(Embedding(500, 120, input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(176, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
print(model.summary())

#Splitting the data into training and testing
y=pd.get_dummies(data['airline_sentiment'])
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.1, random_state = 42)

batch_size=32
history = model.fit(X_train, y_train, epochs = 10, validation_data = (X_test, y_test),batch_size=batch_size, verbose = 'auto')
# print(history.history.keys())
# print(type(history))
history2 = model.evaluate(X_test,y_test)
