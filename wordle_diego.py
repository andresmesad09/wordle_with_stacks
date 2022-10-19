from rich.console import Console
from random import choice
from words import word_list
from queue_implementation import Queue, Letter

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

WELCOME_MESSAGE = f'\n[white on blue] BIENVENIDO A WORDLE [/]\n'
PLAYER_INSTRUCTIONS = "ADIVINA LA PALABRA \n"
GUESS_STATEMENT = "\nINGRESA TU PALABRA:  "


def check_guess(guess: Queue, answer: str):
    # convertimos la respuesta en cola
    answer_queue = Queue()
    for letter in answer:
        answer_queue.enqueue(letter.upper())
    # palabras coloreadas cada intento
    guessed = []
    # Esto sale al final, como una matriz de SQUARES
    wordle_pattern = []
    # contar posiciones correctas
    aciertos = 0
    answe_full_queue = answer_queue.queue.copy()
    for _ in range(len(chosen_word)):
        letter = guess.dequeue()
        if answer_queue.dequeue() == letter:
            my_letter = Letter(letter, '[black on green]')
            guessed += my_letter.set_up
            wordle_pattern.append(SQUARES['correct_place'])
            aciertos += 1
        elif letter in answe_full_queue:
            my_letter = Letter(letter, '[black on yellow]')
            guessed += my_letter.set_up
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            my_letter = Letter(letter, '[black on white]')
            guessed += my_letter.set_up
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern), aciertos


def game(console, chosen_word):
    end_of_game = False
    # tries
    already_guessed = 0
    # lista con cuadros de colores
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = input(GUESS_STATEMENT).upper()  # str

        # si la palabra no es de 5 letras, pedir nuevamente
        while len(guess) != len(chosen_word):

            console.print('[red]ERROR!! NO CUMPLE EL TAMAÑO\n[/]')
            guess = input(GUESS_STATEMENT).upper()

        # encolamos cada letra
        guess_queue = Queue()
        for letter in guess:
            guess_queue.enqueue(letter)

        #
        guessed, pattern, aciertos = check_guess(guess_queue, chosen_word)
        # aumentamos intentos en 1
        already_guessed += 1
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        # los intentos cambian, al ser la palabra mas larga o corta
        if already_guessed == len(chosen_word) or aciertos == len(guess):
            end_of_game = True

    if already_guessed == len(chosen_word) and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{len(chosen_word)}[/]")
        console.print(f'\n[green]Palabra correcta: {chosen_word}[/]')
    else:
        console.print(
            f"\n[green]WORDLE {already_guessed}/{len(chosen_word)}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':

    console = Console()

    chosen_word = str(input("Ingrese la palabra que quiere adivinar: "))

    console.print(WELCOME_MESSAGE)

    console.print(f'\n{chosen_word}\n')

    console.print(PLAYER_INSTRUCTIONS)

    game(console, chosen_word)
