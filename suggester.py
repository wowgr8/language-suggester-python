answer_one = ""
answer_two = ""
answer_three = ""
suggested_language = ""

print("\n""Howdy! Answer the following questions and I'll suggest a programming language for you to learn.")
print("=============================="" \n")

print("What type of applications are you most interested in developing?")
answer_one = input("- web" "\n" "- mobile" "\n" "- desktop" "\n").lower()

print("What is your preferred platform for development?")
answer_two = input("- windows" "\n" "- macOS" "\n" "- linux" "\n").lower()

print("How comfortable are you with programming?")
answer_three = input("- Beginner" "\n" "- Intermediate" "\n" "- Advanced" "\n").lower()

if (answer_one == "mobile" or answer_one == "web"):
  if (answer_two == "macos" or answer_two == "windows") and (answer_three == "beginner" or answer_three == "intermediate"):
    suggested_language = "Based on your preferences, we suggest considering Swift for iOS development or Kotlin for Android development!"
  else:
    suggested_language = "Based on your preferences, we suggest considering picking up Python!"
elif (answer_one == "desktop"):
  if (answer_two == "windows" or "linux") and (answer_three == "beginner" or answer_three == "intermediate"):
    suggested_language = "Based on your preferences, we suggest considering C# or Python for development!"
elif (answer_one == "web") and (answer_two == "windows" or answer_two == "macos" or answer_two == "linux") and (answer_three == "beginner" or answer_three == "intermediate" or answer_three == "advanced"):
    suggested_language = "Based on your preferences, we suggest considering JavaScript for development!"


print(suggested_language)