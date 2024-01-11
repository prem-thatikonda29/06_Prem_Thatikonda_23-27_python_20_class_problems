# Quiz Application

import os

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        print(f"Welcome {user.name}, to the {self.name} quiz!")
        score = 0

        for question in self.questions:
            print()
            question.display_question()
            user_answer = int(input("Your answer (enter the option number): "))

            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was option {question.correct_option}.\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        return score


class User:
    def __init__(self, name):
        self.name = name


def main():
    # Sample questions for quizzes
    gk_questions = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
        Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], 2),
        Question("What is the largest mammal on Earth?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 1),
        Question("In which year did the Titanic sink?", ["1905", "1912", "1920", "1931"], 1),
        Question("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], 1),
        Question("Who developed the theory of relativity?", ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"], 2)
    ]

    math_questions = [
        Question("What is the result of 5 + 7?", ['12', '14', '10', '16'], 1),
        Question("What is the square of 4?", ['14', '15', '16', '17'], 3),
        Question("If x = 3 and y = 2, what is x + y?", ['3', '5', '6', '7'],2),
        Question("What is the product of 6 and 9?", ['50', '52', '54', '56'],3)
    ]

    anime_questions = [
    Question("Who is the main character in 'Naruto'?", ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake"], 1),
    Question("In 'One Piece', what is the name of Monkey D. Luffy's straw hat?", ["Strawberry Hat", "Sun Hat", "Gum-Gum Hat", "Wanted Hat"], 3),
    Question("What is the highest-grossing anime film of all time?", ["Your Name", "Spirited Away", "Demon Slayer: Mugen Train", "Attack on Titan: Chronicle"], 3),
    Question("In 'Dragon Ball Z', who is Goku's eternal rival?", ["Vegeta", "Piccolo", "Frieza", "Cell"], 1),
    Question("Which anime features a Death Note that allows its user to kill anyone by writing their name?", ["Bleach", "Death Parade", "Fullmetal Alchemist", "Death Note"], 4),
    ]

    history_questions = [
        Question("Who was the first President of the United States?", ["John Adams", "Thomas Jefferson", "George Washington", "James Madison"], 3),
        Question("In which year did World War II end?", ["1943", "1945", "1948", "1950"], 2),
        Question("Who was the Egyptian queen known for her relationship with Julius Caesar and Mark Antony?", ["Cleopatra", "Nefertiti", "Hatshepsut", "Isis"], 1),
        Question("The Renaissance period originated in which country?", ["France", "Italy", "England", "Germany"], 2),
        Question("Who was the leader of the Soviet Union during the Cuban Missile Crisis?", ["Vladimir Putin", "Joseph Stalin", "Nikita Khrushchev", "Leon Trotsky"], 3),
    ]

    sports_questions = [
        Question("Which country won the FIFA World Cup in 2018?", ["Germany", "Brazil", "France", "Argentina"], 3),
        Question("In tennis, what is a Grand Slam?", ["Winning all four major tournaments in a calendar year", "A powerful serve", "Scoring 100 points in a match", "Winning the Davis Cup"], 1),
        Question("Who is often called 'The Greatest' in the history of boxing?", ["Muhammad Ali", "Mike Tyson", "Floyd Mayweather", "Evander Holyfield"], 1),
        Question("Which country is known for inventing the modern game of golf?", ["Scotland", "United States", "England", "Australia"], 1),
        Question("In which sport would you perform a slam dunk?", ["Basketball", "Soccer", "Tennis", "Golf"], 1),
    ]
    # Create quiz instances
    gk_quiz = Quiz("General Knowledge", gk_questions)
    math_quiz = Quiz("Mathematics", math_questions)
    anime_quiz = Quiz("Anime", anime_questions)
    history_quiz = Quiz("History", history_questions)
    sports_quiz = Quiz("Sports", sports_questions)

    user_name = input("Enter your name: ")
    user = User(user_name)

    while True:
        print("\n---------Welcome to QuizMania---------")
        print("\n\n1) Maths Quiz")
        print("2) GK Quiz")
        print("3) Anime Quiz")
        print("4) History Quiz")
        print("5) Sports Quiz")
        print("6) Exit")
        quiz_type = int(input("Enter the quiz you want to take (1, 2, 3, 4, 5, or 6 to exit): "))

        if quiz_type == 1:
            user_score = math_quiz.take_quiz(user)
        elif quiz_type == 2:
            user_score = gk_quiz.take_quiz(user)
        elif quiz_type == 3:
            user_score = anime_quiz.take_quiz(user)
        elif quiz_type == 4:
            user_score = history_quiz.take_quiz(user)
        elif quiz_type == 5:
            user_score = sports_quiz.take_quiz(user)
        elif quiz_type == 6:
            print("Thanks for playing QuizMania! Goodbye.")
            break
        else:
            print("Invalid input. Please enter a valid option.")

        while True:
            decision = input("Do you wanna take another quiz? 'y' / 'n': ")
            if decision=='y':
                os.system('clear')
                break
            elif decision=='n':
                print("Thank you for playing!")
                exit()
            else:
                print("Invalid input")

if __name__ == "__main__":
    main()
