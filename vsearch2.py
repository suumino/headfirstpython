# vsearch 2

def search4letters(phrase : str, letters : str = 'aeiou') -> set:
  """Return an set of the 'letters' found in 'phrase'"""
  return set(letters).intersection(set(phrase))
