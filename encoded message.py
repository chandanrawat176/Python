alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

message = input('Please enter a message: ')

for character in message:
 if character in alphabet:
  position = alphabet.find(character)
  newposition = (position + key) % 26
  newchar = alphabet[newposition]
  #print('The new character is:', newchar)
  newMessage += newchar
 else:
  character += newchar

print('your new message is', newMessage)