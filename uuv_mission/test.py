from dynamic import Mission


#test file

#testing Mission read

missionread= Mission.from_csv("data/mission.csv")

print(missionread.cave_depth)