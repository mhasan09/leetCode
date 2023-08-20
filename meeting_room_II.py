def meeting_room_II(slots):
    room = 1
    slots = sorted(slots, key=lambda x:x[0])
    for i in range(len(slots) -1 ):
        for j in range(i+1, len(slots) - 1):
            if slots[i][0] <= slots[j][1] <= slots[i][1]:
                room += 1
    return room

print(meeting_room_II([[0, 30],[5, 10],[15, 20]]))
print(meeting_room_II([[1,10],[30,40],[50,60],[11,14]]))