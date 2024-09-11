''''''

import re

def remove_duplicates(text):
  """Удаляет дубликаты слов в строке.

  Args:
    text: Строка для обработки.

  Returns:
    Строка с удаленными дубликатами слов.
  """

  words = re.findall(r'\w+', text)
  result = []
  previous_word = None

  for word in words:
    if word != previous_word:
      result.append(word)
      previous_word = word

  return ' '.join(result)

text = input()
result = remove_duplicates(text)
print(result)