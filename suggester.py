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

# answer_two = input("What is your preferred platform for development? " "\n" "- windows" "\n" "- macOS" "\n" "- linux" "\n")
# print("\n")
# answer_three = input( "\n" "- Beginner" "\n" "- Intermediate" "\n" "- Advanced" "\n")
# print("\n")

if (answer_one.lower() == "mobile" or answer_one.lower() == "web") and (answer_two.lower() == "macos" or answer_two.lower() == "windows") and (answer_three.lower() == "beginner" or answer_three.lower() == "intermediate"):
  suggested_language = "Based on your preferences, we suggest considering Swift for iOS development or Kotlin for Android development!"
elif: 


print(answer_one, answer_two, answer_three)