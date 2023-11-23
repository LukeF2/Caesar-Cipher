def Letters(text):
  text = text.lower()
  letters = ""
  for char in text:
      if char.isalpha():
          letters += char
  return letters


def Letters(text):
  letters=''
  for char in text:
    if char.isalpha(): #checks if characters are letters
      letters+=char.lower() #converts characters to lower case
  return(letters)

print(Letters("Hello world 12312"))

def FreqDict(text):
  freq_dict = {}
  alpha = "abcdefghijklmnopqrstuvwxyz"
  letters = Letters(text)
  total_letters = len(letters)
  for char in alpha:
    freq_dict[char] = 0

  for char in letters:
    freq_dict[char] += 1

  for char in freq_dict:
    freq_dict[char] /= total_letters
  return freq_dict

print(FreqDict("Hello world 124908u124ASDSD"))

class Caesar:
    def __init__(self, text):
        self.text = text
        self.freqdict = FreqDict(self.text)
        self.shift = None

    def Score(self, other):
        # score = 0
        # for letter in string.ascii_lowercase:
        #     score += (self.freqdict.get(letter, 0) - other.freqdict.get(letter, 0)) ** 2
        # return score
      score = 0
      for char in self.freqdict:
        score = score + ((self.freqdict[char] - other.freqdict[char])**2)
      return score

    def Encode(self, n):
        ciphertext = ""
        for char in self.text:
            if char.isalpha():
                shifted = (ord(char.lower()) - ord('a') + n) % 26
                ciphertext += chr(shifted + ord('a')).upper() if char.isupper() else chr(shifted + ord('a'))
            else:
                ciphertext += char
        return ciphertext

    def Decode(self, other):
        text = self.text
        lowest_score = float('inf')
        decoded_text = ''
        for i in range(26):
            encoded_text = self.Encode(i)
            encoded_caesar = Caesar(encoded_text)
            score = encoded_caesar.Score(other)
            if score < lowest_score:
                lowest_score = score
                decoded_text = encoded_text
                self.shift = i
        return decoded_text

    def crack(self, other):

        decoded_text = self.Decode(other)
        return decoded_text

C1 = Caesar("hello world 123124@@*($@$ USDHNOSDCMSA")
C2 = Caesar("hey there")
print(C1.Decode(C2))

print(C1.Encode(18))
C3 = Caesar("Z yfgv pfl veafpvu fli tcrjj kyzj jvdvjkvi, reu yrmv tfdv rnrp nzky jfdv ljvwlc befncvuxv fw tfuzex reu kyv nrp tfdglkvij nfib. Z rcjf yfgv pfl nzcc tfejzuvi wlikyvizex pfli vultrkzfe sp krbzex dfiv tfdglkzex-ivcrkvu tcrjjvj. Yrmv r nfeuviwlc jlddvi!")
C4 = Caesar("I hope you enjoyed our class this semester, and have come away with some useful knowledge of coding and the way computers work. I also hope you will consider furthering your education by taking more computing-related classes. Have a wonderful summer!")
C5 = Caesar("J ipqf zpv fokpzfe pvs dmbtt uijt tfnftufs, boe ibwf dpnf bxbz xjui tpnf vtfgvm lopxmfehf pg dpejoh boe uif xbz dpnqvufst xpsl. J bmtp ipqf zpv xjmm dpotjefs gvsuifsjoh zpvs fevdbujpo cz ubljoh npsf dpnqvujoh-sfmbufe dmbttft. Ibwf b xpoefsgvm tvnnfs!")
print(C3.Decode(C5))

print(C3.Decode(C4))