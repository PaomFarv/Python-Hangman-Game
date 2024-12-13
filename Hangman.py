import random

words = [
    "apple", "banana", "orange", "mango", "coconut", "tangerine", "pineapple", "grape", "kiwi", "strawberry",
    "blueberry", "watermelon", "peach", "pear", "cherry", "plum", "apricot", "fig", "date", "papaya",
    "pineapple", "pomegranate", "avocado", "blackberry", "lemon", "lime", "melon", "nectarine", "applause",
    "adventure", "airplane", "library", "magnet", "bicycle", "dolphin", "elephant", "guitar", "handshake", "jackal",
    "kangaroo", "lighthouse", "mountain", "nightmare", "ocean", "planet", "quilt", "river", "snake", "treehouse",
    "umbrella", "volcano", "whale", "xylophone", "yacht", "zebra", "balloon", "camera", "dinosaur", "envelope",
    "fridge", "guitar", "hat", "island", "jungle", "kite", "laptop", "moon", "notebook", "octopus",
    "puzzle", "queen", "rose", "sailboat", "television", "unicorn", "vulture", "window", "xenon", "yoga",
    "zeppelin", "abstract", "banana", "cake", "diamond", "elephant", "fan", "giraffe", "hat", "island", "jacket",
    "keyboard", "lighthouse", "mountain", "noodle", "octopus", "pencil", "quilt", "robot", "sunflower", "tree",
    "umbrella", "volcano", "whale", "xylophone", "yellow", "zebra", "abacus", "bird", "cat", "dog", "elephant",
    "frog", "grape", "house", "ice", "jungle", "koala", "lemon", "meadow", "nashville", "orange", "parrot",
    "question", "rocket", "sun", "tiger", "umbrella", "vulture", "wolf", "xenon", "yacht", "zephyr",
    "acorn", "bison", "coyote", "dove", "eagle", "flame", "geese", "hawk", "ibex", "jellyfish",
    "koala", "lion", "moose", "numbat", "owl", "panda", "quail", "rabbit", "sparrow", "tortoise",
    "unicorn", "vulture", "whale", "xenon", "yak", "zebra", "apple", "berry", "cherry", "date",
    "fig", "grape", "honeydew", "kiwi", "lemon", "melon", "orange", "peach", "pear", "plum",
    "pineapple", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apricot", "avocado", "blackberry",
    "blueberry", "coconut", "cucumber", "eggplant", "mango", "papaya", "pear", "plum", "spinach", "tomato",
    "zucchini", "artichoke", "broccoli", "carrot", "celery", "chard", "chili", "cucumber", "dandelion", "endive",
    "fennel", "jalapeno", "kale", "lettuce", "mustard", "onion", "parsnip", "peas", "radish", "sweetcorn",
    "turnip", "butternut", "pumpkin", "potato", "spinach", "broccoli", "cauliflower", "asparagus", "leek",
    "radish", "zucchini", "albatross", "butterfly", "cockroach", "dragonfly", "firefly", "grasshopper", "moth",
    "prayingmantis", "scorpion", "spider", "beetle", "centipede", "ant", "termite", "wasp", "fly", "mosquito",
    "tick", "bedbug", "rolypoly", "cockroach", "earthworm", "bunny", "kangaroo", "lion", "tiger", "giraffe",
    "zebra", "elephant", "rhino", "hippopotamus", "panda", "koala", "pigeon", "owl", "parrot", "cuckoo",
    "woodpecker", "eagle", "falcon", "hawk", "sparrow", "crane", "penguin", "swallow", "bat", "crow",
    "dove", "finch", "heron", "kestrel", "kingfisher", "moose", "buffalo", "caribou", "elk", "beaver", "otter",
    "badger", "weasel", "squirrel", "hedgehog", "chipmunk", "prairie", "snake", "rattlesnake", "python",
    "anaconda", "cobra", "kingcobra", "chameleon", "gecko", "iguana", "lizard", "monitor", "viper", "cobra",
    "ferret", "polarbear", "grizzly", "puma", "turtle", "raccoon", "skunk", "mole", "wolverine", "coyote",
    "salamander", "armadillo", "wallaby", "koala", "wombat", "koala", "platypus", "wallaby", "kangaroo",
    "tapir", "gibbon", "orangutan", "gorilla", "chimpanzee", "mandrill", "baboon", "bonobo", "lemur", "meerkat"
]


hangman_art = {
    1: '''  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    2: '''  +---+
  |   |
  O   |
 /    |
      |
      |
=========''',
    3: '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    4: '''  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    5: '''  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    6: '''  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
}

def hangman(hangman_art):
    print("*"*30)
    print("        Python Hangman")
    word = random.choice(words)   
    hint = list(word)
    for char in range(len(hint)):
        hint[char] = "_"
    print("Hint: "+" ".join(hint))
    
    is_running = True
    wrong_count = 0
    user_inputs = set()
    
    while is_running:
        user_guess = input("Make a guess ('#' to quit): ").strip()
        print("*"*30)
        if len(user_guess) > 1:
            print("You can input only one character at a time.")
            continue
        if user_guess.isdigit():
            print("Invalid input.Only alphabets are acceptable.")
            continue
        if user_guess.upper() == '#':
            print("                      GoodBye!")
            break

        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    hint[i] = user_guess
            the_word = " ".join(hint)
            print(the_word)

            if user_guess in user_inputs:
                print("You already guessed it.")
            else:    
                user_inputs.add(user_guess)

        else:
            wrong_count += 1
            print(hangman_art[wrong_count])

        if "_" not in hint:
            print("\n                    YOU WON!!!")
            print("*"*30)
            is_running = False

        if wrong_count == 6:
            print("\n                     YOU LOSE!")
            print("*"*30)
            input("Press ENTER to quit. ")
            is_running = False

hangman(hangman_art)
