#encrypt = lambda clear, key: "/".join([hex(ord(clear[i]) * ord(key[i]))[2:] for i in range(4)])

text = "1110/dbf/c90/1008"
key = "4309"
ans = ""

text = text.split("/")
for i in range(4):
    ans+=chr(int(int(text[i], 16) / ord(key[i])))

with open('0_ans.txt', 'w') as file:
    file.write(ans)