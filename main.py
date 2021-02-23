morse = {'!': '-.-.--',
          "'": '.----.',
          '"': '.-..-.',
          '$': '...-..-',
          '&': '.-...',
          '(': '-.--.',
          ')': '-.--.-',
          '+': '.-.-.',
          ',': '--..--',
          '-': '-....-',
          '.': '.-.-.-',
          '/': '-..-.',
          '0': '-----',
          '1': '.----',
          '2': '..---',
          '3': '...--',
          '4': '....-',
          '5': '.....',
          '6': '-....',
          '7': '--...',
          '8': '---..',
          '9': '----.',
          ':': '---...',
          ';': '-.-.-.',
          '=': '-...-',
          '?': '..--..',
          '@': '.--.-.',
          'A': '.-',
          'B': '-...',
          'C': '-.-.',
          'D': '-..',
          'E': '.',
          'F': '..-.',
          'G': '--.',
          'H': '....',
          'I': '..',
          'J': '.---',
          'K': '-.-',
          'L': '.-..',
          'M': '--',
          'N': '-.',
          'O': '---',
          'P': '.--.',
          'Q': '--.-',
          'R': '.-.',
          'S': '...',
          'T': '-',
          'U': '..-',
          'V': '...-',
          'W': '.--',
          'X': '-..-',
          'Y': '-.--',
          'Z': '--..',
          '_': '..--.-'
          }

sources = ['''
                                :______.-':      :  .--------------.  :             
                                | ______  |      | :                : |             
                                |:______B:|      | |  Eng to Morse: | |             
                                |:______B:|      | |                | |             
                                |:______B:|      | |  Ready!        | |             
                                |         |      | |  db if found.  | |             
                                |:_____:  |      | |                | |             
                                |    ==   |      | :                : |             
                                |       O |      :  '--------------'  :             
                                |       o |      :'---...______...---'              
                                |       o |-._.-i___/'             \._              
                                |'-.____o_|   '-.   '-...______...-'  `-._          
                                :_________:      `.____________________   `-.___.-. 
                                                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
                                               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
                                              :____________________________:\n''', '']

def string_to_morse(eng):
    return [morse[char.upper()] for char in eng]
more = "Ystart"
while more == "Ystart" or more == "Y":
    try:
        if more == "Ystart":
            text_eng = str(input(f'{sources[0]}'
                                'type: '))
        else:
            text_eng = str(input(f'{sources[1]}'
                                 'type: '))


        print(f'result: {string_to_morse(text_eng)}')

        more = str(input("Press 'Y' for another try or any-key to leave ")).upper()

    except KeyError:
        print("\nSome chars can't be transform to morse")
        more = str(input("Press 'Y' for another try or any-key to leave ")).upper()