#indexing 
name = "pawan poudel"
ch = name[3]
print(ch)
#slicing in python
has_sentence = "python is amazing."
char = has_sentence[0:17]#[0:17]
print(char)
print(has_sentence[:4])#[1:4]
print(has_sentence[1:])#[2:len(str)]
print(has_sentence[9:len(has_sentence)])#[9:[len(str)]]
#negative slicing
has_id = "pawan poudel"
new_char = has_id[-5]
print(new_char)
print(has_id[-9:-1])#always take from the lowest to highest while slicing in python 
