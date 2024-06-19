from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter

# Contoh teks berita online Bahasa Indonesia (Anda bisa ganti dengan berita yang sebenarnya)
text = "Presiden Joko Widodo mengumumkan program vaksinasi untuk meningkatkan imunitas masyarakat. Program ini akan melibatkan berbagai pihak, termasuk pemerintah, lembaga kesehatan, dan masyarakat umum."

# Proses tokenizing menggunakan word_tokenize
tokenized_word = word_tokenize(text)

# Menghapus stopwords Bahasa Indonesia dari tokenized_word
stopword_factory = StopWordRemoverFactory()
stopwords = stopword_factory.get_stop_words()
filtered_list = [word for word in tokenized_word if word.lower() not in stopwords]

# Proses Stemming menggunakan Sastrawi
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_list]

# Hitung distribusi frekuensi kata
word_freq = Counter(stemmed_words)

print("Teks Asli:")
print(text)
print("\nTokenized Word:")
print(tokenized_word)
print("\nKata setelah filtering stopwords:")
print(filtered_list)
print("\nKata setelah proses stemming:")
print(stemmed_words)
print("\nDistribusi Frekuensi Kata:")
print(word_freq)
