#blyat

#йцукенгшщзфывапролдячсмитьхъжэбю!"№;%:?*()_+-=
#ЯВЕРТЫУИОПАСДФГХЙКЛЗЬЦЖБНМ

#blyat: ди islдиd fцll Фf ъдидидs
#phonetic: ан исланд фулл оф бананас

#blyat: дll ндil тне нФlу мФтнеяlдиd, тне бяедт sФviет яцssiд
#phonetic: алл хаил тхе холы мохтерланд, тхе греад сожиет руссиа

russianate_list = {'w':'щ', 'e':'е', 'r':'я', 't':'т', 'y':'у', 'u':'ц', 'o':'Ф', 'p':'р', 'a':'д', 'g':'б', 'h':'н', 'k':'к', 'x':'ж', 'c':'с', 'b':'ъ', 'n':'и', 'm':'м'}

def russianate(input):
    for letter in russianate_list:
        input = input.replace(letter, russianate_list[letter])
    return(input)

print(russianate(input("Рlедsе еитея уФця тежт: ")))