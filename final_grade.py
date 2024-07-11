import math
with open("final_grade.txt", "r") as f:
  data = list(f)

for i in range(len(data)):
  data[i] = data[i].strip()

trials = data.pop(0)

def calculate(project, paper, midterm):
  points_without_final = int(project)*0.01 * 15 + int(paper)*0.01 * 20 + int(midterm)*0.01 * 25
  final_required_points = 90-points_without_final
  final_percentage = math.ceil(final_required_points/0.4)

  if final_percentage <= 100:
    return final_percentage
  else:
    return "impossible"

for i in range(len(data)):
  main = data[i].split(" ")
  print(calculate(main[0], main[1], main[2]))