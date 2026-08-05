dic1 = {
    "word": "apple",
    "word_t": "Apple"
}
dic2 = {
    "word": "banana",
    "word_t": "Banana"
}
dic3 = {
    "word": "orange",
    "word_t": "Orange"
}
dic = [dic1, dic2, dic3]
#print(dic)

aliens = []
for alien_number in range(30):
    new_alien = {
        "color": "green",
        "points": 10,
    }
    aliens.append(new_alien)
for alien in aliens[:5]:
    alien["color"] = "red"
    alien["points"] = 15
print(aliens[:6])
for alien in aliens[5:10]:
    alien["color"] = "yellow"
    alien["points"] = 50
print(aliens[5:10])