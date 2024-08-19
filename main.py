import random
import time

# states and their capitals
states_and_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata',
}

def ask_question(state, options, correct_option):
    print(f"\nWhat is the capital of {state}?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        start_time = time.time()
        choice = int(input("Choose the correct option (1-4): ").strip())
        elapsed_time = time.time() - start_time
        
        # If user selects the correct option within 10 seconds
        if choice == correct_option and elapsed_time <= 10:
            print("Correct!")
            return 1  # Correct answer
        elif elapsed_time > 10:
            print("Time's up!")
        else:
            print(f"Wrong! The correct answer is {options[correct_option - 1]}.")
    except (ValueError, IndexError):
        print(f"Invalid input! The correct answer is {options[correct_option - 1]}.")
    
    return 0  # Incorrect answer or timeout

def quiz():
    score = 0
    total_questions = 5  # Limit the number of questions
    
    # Shuffle the states list
    states = list(states_and_capitals.keys())
    random.shuffle(states)
    
    for state in states[:total_questions]:  # Ask only a subset of questions
        correct_capital = states_and_capitals[state]
        
        # Generate wrong options
        wrong_capitals = random.sample(list(states_and_capitals.values()), 3)
        if correct_capital in wrong_capitals:
            wrong_capitals.remove(correct_capital)
        
        # Prepare options list and shuffle
        options = wrong_capitals + [correct_capital]
        random.shuffle(options)
        correct_option = options.index(correct_capital) + 1
        
        # Ask the question and update the score
        score += ask_question(state, options, correct_option)
    
    return score  

def main():
    print("Let's Begin!")
    
    participants = {}
    num_participants = int(input("Enter the number of participants: ").strip())
    
    for _ in range(num_participants):
        name = input("Enter participant's name: ").strip()
        print(f"\n{name}, it's your turn!")
        score = quiz()
        participants[name] = score
        print(f"\n{name}, your score is {score}/{5}.\n")
    
    # Display leaderboard at the end
    print("\nFinal Leaderboard:")
    leaderboard = sorted(participants.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(leaderboard, 1):
        print(f"{i}. {name} - {score}/5 points")
    
    print("\nThanks for participating!")

if __name__ == "__main__":
    main()
