import random
import sys
puntaje = 0
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
("// Esto es un comentario","/* Esto es un comentario */","-- Esto es un comentario","# Esto es un comentario",),("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for questions,options,answer in questions_to_ask:
    print (questions)
    for i, option in enumerate(options):
         print(f"{i + 1}. {option}") 

# El usuario tiene 2 intentos para responder correctamente
#Si la respuesta ingresada no corresponde a un integer o esta fuera del rango [1,4], se informa al usuario y se registra el error !!!!!!!!!!!!!!!!
    for intento in range(2):
         try:
             user_answer = int(input("Respuesta: ")) - 1  # Convertimos la entrada a int y ajustamos el índice

             # Se verifica el rango
             if (user_answer < 0 or user_answer > 3):
                print(f"Respuesta no válida. Debe estar entre 1 y 4")
                break
         except ValueError:
             print("Respuesta no válida. Debes ingresar un número entero.")
             sys.exit(1)

# Se verifica si la respuesta es correcta
         if user_answer == answer:
            print("¡Correcto!")
            puntaje+=1
            break
         else:
             puntaje-=0.5
         # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
    else:
         print(f"Incorrecto. La respuesta correcta es: {answer + 1}")
        
# Se imprime un blanco al final de la pregunta
    print()

#Imprimir puntaje
print(f"El puntaje final es {puntaje}")

