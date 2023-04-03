import collections 

def analiza_texto(text): 
	# Separamos el texto en palabras 
	words = text.split() 
	# Contamos el número de palabras  
	num_words = len(words) 

	# Contamos el número de caracteres  
	num_chars = len(text)

	# Creamos un diccionario para contar las veces que aparece cada palabra  
	counter = collections.Counter(words)

	# Imprimimos los resultados  
	print("Número de palabras:", num_words) 
	print("Número de caracteres:", num_chars) 

	for word, count in counter.items(): 
		print(word + ": " + str(count)) 


#----------- Prueba

text = "Esta es una prueba para ver si nuestro programa funciona bien. Esta frase tiene algunas palabras repetidas como 'esta' y 'palabras'" 
analiza_texto(text)