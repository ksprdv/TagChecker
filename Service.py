from math import floor
from sys import exit

class Service:
    
    TagChar = ('0', '2', '8', '9', 'P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V')

    def TagFromID(Id):
        Tag = []
        while Id > 0:
            CharIndex = floor(Id % len(Service.TagChar))
            Tag.insert(0, Service.TagChar[CharIndex])
            Id -= CharIndex
            Id /= len(Service.TagChar)
        return ''.join(Tag)

    def TagToID(Tag):
        if Tag.startswith('#'):
            TagArray = list(Tag[1:].upper())
        else:
            TagArray = list(Tag.upper())
        Id = 0
        for i in range(len(TagArray)):
            Character = TagArray[i]
            try:
                CharIndex = Service.TagChar.index(Character)
            except ValueError:
                print('Invalid tag! Supported characters: {}'.format(Service.TagChar))
                exit()
            Id *= len(Service.TagChar)
            Id += CharIndex

        HighLow = []
        HighLow.append(Id % 256)
        HighLow.append((Id - HighLow[0]) >> 8)
        return HighLow
    