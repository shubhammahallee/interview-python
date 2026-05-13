import os



f = open("chand_taare.txt", "r")

data = f.readline()
print(data)

data = f.readline()
print(data)

f = open("chand_taare.txt", "w")

f.write("Jo bhi chahoon, woh main paoon\n")
f.write("Zindagi mein jeet jaoon\n")
f.write("Chand taare tod laoon\n")
f.write("Saari duniya par main chhaoon\n")
f.write("Bas itna sa khwaab hai...\n")
f.write("Bas itna sa khwaab hai...\n\n")

f = open("chand_taare.txt", "r")
data = f.read()
print(data)

with open("chand_taare.txt","r") as f:
    data = f.read()
    print(f' Words contains {len(data)}')

#os.remove("sample.txt")

f1 = open("chand_taare.txt", "a")

f1.write("[Verse 2] Yaar tu bhi sun zara, aarzoo meri hai kya\n")
f1.write("Khoobsurat ho bahar, itna mera ho nikhaar\n")
f1.write("Main kahin bhi jaoon, log dekhen mud-mudke ek baar\n")
f1.write("Mujhko dekhen, mujhko chahen, ho gaya main bekaraar\n\n")

data1 = f.read()
print(data1)


f.close()

