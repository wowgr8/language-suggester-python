answer_one = ""
answer_two = ""
answer_three = ""
suggested_language = ""

print("\n""Howdy! Answer the following questions and I'll suggest a programming language for you to learn.")
print("=============================="" \n")

answer_one = input("What type of applications are you most interested in developing?\n- web\n- mobile\n- desktop\n").lower()
answer_two = input("What is your preferred platform for development?\n- windows\n- macOS\n- linux\n").lower()
answer_three = input("How comfortable are you with programming?\n- Beginner\n- Intermediate\n- Advanced\n").lower()

if (answer_one == "mobile" or answer_one == "web"):
  if (answer_two == "macos" or answer_two == "windows") and (answer_three == "beginner" or answer_three == "intermediate"):
    suggested_language = "Based on your preferences, we suggest considering Swift for iOS development or Kotlin for Android development!"
  else:
    suggested_language = "Based on your preferences, we suggest considering picking up Python!"
elif (answer_one == "desktop"):
  if (answer_two == "windows" or "linux") and (answer_three == "beginner" or answer_three == "intermediate"):
    suggested_language = "Considering desktop development on Windows or Linux? Explore C# or Python for your projects!"
elif (answer_one == "web") and (answer_two == "windows" or answer_two == "macos" or answer_two == "linux") and (answer_three == "beginner" or answer_three == "intermediate" or answer_three == "advanced"):
    suggested_language = "Interested in web development? JavaScript is a fantastic choice!"


print(suggested_language)