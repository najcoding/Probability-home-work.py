# Program: Probability that the winner belongs to a club

def calculate_probability(club_members, total_students):
    """
    Calculate probability that a randomly chosen student belongs to a club.
    Returns a float between 0 and 1.
    """
    if total_students <= 0:
        raise ValueError("Total number of students must be greater than zero.")
    if club_members < 0 or club_members > total_students:
        raise ValueError("Club members must be between 0 and total students.")
    
    return club_members / total_students

def main():
    try:
        # Get inputs from user
        club_members = int(input("Enter number of club members: "))
        total_students = int(input("Enter total number of students: "))
        
        # Calculate probability
        probability = calculate_probability(club_members, total_students)
        
        # Display result as fraction and percentage
        print(f"Probability: {probability:.4f} ({probability * 100:.2f}%)")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Unexpected error. Please enter valid integers.")

if __name__ == "__main__":
    main()
