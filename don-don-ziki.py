with open("don-don-ziki.txt","r") as f:
    lines=f.read()
s=lines.split("\n")
player_1=0
for a in s:                          # C va Z=3 qaychi
    b=a.split(" ")                   # B va Y=2 qog`oz
    if b[0] == "A" and b[1] == "Y":  # A va X=1 tosh
        player_1 = player_1 + 2 + 6  # +2 Y ni tanlagani u/n +6 yutgani u/n
    elif b[0] == "A" and b[1] == "Z":
        player_1 = player_1 + 3  # +3 Z ni tanlaganligi uchun
    elif b[0] == "A" and b[1] == "X":
        player_1 = player_1 + 1 + 3  # +1 X ni tanlaganligi uchun    +3 durang bo`lganligi uchun

    elif b[0] == "B" and b[1] == "Z":
        player_1 = player_1 + 3 + 6  # +3  Z ni tanlagani u/n +6 yutgani u/n
    elif b[0] == "B" and b[1] == "Y":
        player_1 = player_1 + 3+2  # +3  durang bo`lgani u/n
    elif b[0] == "B" and b[1] == "X":
        player_1 = player_1 + 1  # +1 x ni tanlagani u/n

    elif b[0] == "C" and b[1] == "Z":
        player_1 = player_1 + 3 + 3  # +3 z ni tanlagani uchun +3 durang u/n
    elif b[0] == "C" and b[1] == "Y":
        player_1 = player_1 + 2  # +2 y ni tanlagani uchun
    elif b[0] == "C" and b[1] == "X":
        player_1 = player_1 + 6 + 1  # +1 x  tanlagani uchun +6 yutgani u/n



print("Natijasi->",player_1)