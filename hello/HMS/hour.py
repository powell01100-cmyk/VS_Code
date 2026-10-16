def convert_seconds_to_hms():
    user_input = input("Enter the number of seconds: ")
    
    try:
        total_seconds = int(user_input)
        
        if total_seconds < 0:
            print("Error: Please enter a positive number.")
            return
            
        hours = total_seconds // 3600
        remaining_seconds_after_hours = total_seconds % 3600
        
        minutes = remaining_seconds_after_hours // 60
        seconds = remaining_seconds_after_hours % 60
        
        print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
        
    except ValueError:
        print("Error: Invalid input! Please enter a valid whole number.")

convert_seconds_to_hms()

