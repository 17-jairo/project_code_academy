# Task 1 - Decoding message

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q " \
          "cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_message += alphabet[(character_value + 10) % 26]
    else:
        translated_message += character

print(translated_message)

# Task 2 - Encode message

answer = "Hey man, it's good to enconde like this, its a great way to communicating"

translated_massage_1 = ""

for character in answer:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_massage_1 += alphabet[(character_value - 10) % 26]
    else:
        translated_massage_1 += character
print(translated_massage_1)


# Task 3 - Creating a function and applying in the case 3.

def ceaser_decode(message, offset):
    decoded_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decoded_message += alphabet[(character_value + offset) % 26]
        else:
            decoded_message += character

    return decoded_message


def ceaser_encode(message, offset):
    encode_message = ""

    for character in message:
        if character in alphabet.find(character):
            character_value = alphabet.find(character)
            encode_message += alphabet[(character_value - offset) % 26]
        else:
            encode_message += character

    return encode_message

    # Case 1


message_1 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'

print(ceaser_decode(message_1, 10))

message_2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(ceaser_decode(message_2, 14))

# Task 4 - Using the function with no offset

message_3 = " vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by " \
            "px ptgm mh dxxi hnk fxlltzxl ltyx."

#for i in range(10):
    #print(ceaser_decode(message_3, i))

print(ceaser_decode(message_3, 7))

    # Solution provided by code academy
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer " \
                      "lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(ceaser_decode(brute_force_message, i)))


# Task 5 - The Vigenère Cipher

def vigenere_decode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    decoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += message[i]

    return decoded_message


vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

print(vigenere_decode(vigenere_message, vigenere_keyword))

# Task 5

def vigenere_encode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    encoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index - offset_index) % 26]
            encoded_message += new_character
        else:
            encoded_message += message[i]

    return encoded_message


vigenere_message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword_for_v = "besties"

print(vigenere_encode(vigenere_message_for_v, keyword_for_v))
print(vigenere_decode(vigenere_encode(vigenere_message_for_v, keyword_for_v), keyword_for_v))