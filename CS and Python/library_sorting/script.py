import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
  print(book['title'])

print(ord('a'), ord(' '), ord('A'))

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else: return False

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else: return False

bookshelf_v1 = bookshelf.copy()

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['author'])

bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2,0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
  print(book['author'])

# print(bookshelf)
def by_total_length(book_a, book_b):
  book_a_total = len(book_a['author']) + len(book_a['title'])
  book_b_total = len(book_b['author']) + len(book_b['title'])

  if book_a_total > book_b_total:
    return True
  else:
    return False

#loading in long list
long_bookshelf = utils.load_books('books_large.csv')

sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)