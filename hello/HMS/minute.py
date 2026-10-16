def convert_seconds_to_hms():
    print("=== အချိန်ပြောင်းလဲပေးမည့် စက်ရုံမှ ကြိုဆိုပါသည် ===")
    user_input = input("Enter the number of seconds (စက္ကန့် အရေအတွက် ရိုက်ထည့်ပါ): ")
    
    try:
        # စာသားကို ဂဏန်းအစစ် ပြောင်းလဲခြင်း
        total_seconds = int(user_input)
        
        # အနှုတ်ဂဏန်း စစ်ထုတ်ခြင်း
        if total_seconds < 0:
            print("Error: Please enter a positive number. (အနှုတ်ဂဏန်းများ တွက်ချက်၍မရပါ)")
            return
            
        # သင်္ချာ Logic အတိုင်း စားလဒ် (//) နှင့် အကြွင်း (%) ရှာခြင်း
        hours = total_seconds // 3600
        remaining_seconds_after_hours = total_seconds % 3600
        
        minutes = remaining_seconds_after_hours // 60
        seconds = remaining_seconds_after_hours % 60
        
        # ရလဒ်ကို စာသားလှလှလေး ထုတ်ပြခြင်း
        print("\n--- တွက်ချက်မှု ရလဒ် ---")
        print(f"Result: {total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
        print("=======================")
        
    except ValueError:
        # ဂဏန်းမဟုတ်တာ ရိုက်ထည့်ရင် အလုပ်လုပ်မည့်နေရာ
        print("\nError: Invalid input! Please enter a valid WHOLE NUMBER (e.g., 5000).")
        print("စာသားများ၊ ဒဿမကိန်းများ ရိုက်ထည့်၍ မရပါ။ ဂဏန်းအပြည့်အဝကိုသာ ရိုက်ပေးပါ။")

# အိပ်ပျော်နေသော ဖန်ရှင် (အလုပ်သမား) ကို နှိုး၍ စတင်အလုပ်လုပ်ခိုင်းခြင်း
convert_seconds_to_hms()
