def show_result(score, total):
  if total == 0:
    return

  print("\n" + "=" * 30)
  print("         QUIZ RESULT")
  print("=" * 30)
  print(f"You got {score} out of {total} correct!")

  percentage = (score / total) * 100
  print(f"Score Percentage: {percentage:.2f}%")

  if percentage >= 50:
    print("Awesome job! You passed! ")
  else:
    print("Keep practicing! You'll get it next time.")
  print("=" * 30)
