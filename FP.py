import streamlit as st

# aturan kalimat dengan struktur kalimat(grammar) 
t_kalimat = [["K", "SPO"],
          ["K", "SPOKet"],
          ["K", "SPOpel"],
          ["K", "SPKet"],
          ["K", "SP"],
          ["K", "SPpel"]]
# aturan penggantian struktur kalimat (SPOKetPel)
rules = [["S", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
         ["P", "Verb", "VerbAdj"],
         ["O", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
         ["pel", "AdvVerb", "AdvAdj"],
         ["Ket", "PrepPronoun", "PrepPropNoun", "PrepNoun", "PrepAdj"]]

# data untuk diganti menjadi noun, verb, adj, prep, dan adv
noun = "Noun | gunggus | agung | wawan | gung | frady | raindra | ibu | makanan | hak | manusia | UUD | 1945 | kultur | jaringan | wadah | sifat | masalah | presentasi | mobil | suara | ayah | barang | sepeda | adik | gunuggus | adik | taman | bermain | rumah | dia | gaun | acara | orang | pasar | itu | saya | motor | pekarangan | bajunya | sayur-sayuran | kursi | bengkel | atas | meja | harga | martabak | manis | pertigaan | jalan | kucing | kampung | kami | sepatu | anaknya | bapak | guru | diri | pak | keliling | lapangan | pohon | jati | tubuh | mawar | rasa | air | laut | sekolahku | hatinya | hujan | celana | anak | permainan | siswa | kelas | keluarga | asap | rokok | pipi | kainnya | matahari | gadis | jendela | rumahnya | berita | senja | langit | gedung | kaki | kebun | bunga | bis | tangisan | bayi | kopinya | gadis-gadis | pekerjaan | pertanyaan"
verb = "Verb | membawa | disebutkan | dilakukan | dijelaskan | melaju | menyukai | percaya | mengajak | pergi | tersebut | adalah | berhenti | mencuci | membeli | menggunakan | menduduki | diperbaiki | ditaruh | berkeliaran | menyuruh | murid | memperkenalkan | menghukum | lari | memiliki | turun | terkena | menjadi | membuat | merupakan | ada | menggembirakan | melangkahkan | belajar | menghampiri | berjalan | terdengar | mengerjakan | menjawab | berharga"
adj = "Adj | enak | asasi | jelas | steril | sombong | singkat | hijau | cepat | merdu | murah | baru | kecil | baik | tua | kotor | suka | segar | biru | rusak | bulat | mewah | mahal | liar | baru | nakal | kokoh | merah | asin | dekat | resah | gundah | kepanjangan | menyenangkan | basah | elok | bahagia | patah | pintar | harmonis | kemerahan | menyeramkan | kering | terik | langsing | besar | kebesaran | kemerah-merahan | megah | yakin | ragu-ragu | secepatnya | sebaik-baiknya | sungguh-sungguh | takut | malam | cepat | nyaring | panas | cantik | hati-hati | rajin | benar"
prep = "Prep | ke | pada | dalam | di | dari | karena | untuk"
adv = "Adv | dengan | secara | begitu | akan | tidak | jangan | sangat | terlalu"

# list data untuk menyimpan data
data = [ ]
# karena berbentuk string dengan pemisah " | ", maka harus dipisah
# sintaksnya = str.split(" | ")
data.append(noun.split(" | "))
data.append(verb.split(" | "))
data.append(adj.split(" | "))
data.append(prep.split(" | ")) 
data.append(adv.split(" | "))

# fungsi array untuk membuat array untuk segitiga tabel feeling
def array(n : int) -> list:
  list1 = [ ]
  # segitiga yg dibuat adalah segitiga menurun
  for i in range(n, 0, -1):
    list2 = [ ]
    for j in range(i):
      list2.append("")
    list1.append(list2)
  return list1

# fungsi untuk concat 2 string
def concat_str(str1 : str, str2 : str) -> str:
  str3 = ""
  for i in str1:
    for j in str2:
      str3 = str3 + (i + j)
  return str3

# fungsi untuk mencari nilai unik dalam string
def unique_str(str1 : str) -> str:
  str3 = ""
  for i in str1:
    # jika tidak ada dalam str3, maka nilai unik bisa ditambahkan
    if i not in str3:
        str3 = str3 + i
  return str3

# fungsi untuk mengubah string ke dalam notasi kalimat (contoh : SPO)
def converting(str1 : str, list1 : list) -> str:
  str2 = ""
  for i in range(len(list1[:])):
    for j in list1[i][1:]:
      # jika elemen pada list1 ada pada string, dengan kata lain
      # jika notasi terdapat dalam aturan, maka bisa diganti menjadi contoh : SPO
      if j in str1:
        str2 = str2 + list1[i][0]
  return unique_str(str2)

# fungsi ini digunakan untuk menginisiasi tabel segitiga feeling
def initiate(list1 : list, list2 : list, array : list):
  for i in range(0, len(list1)):
    for j in range(len(list2)):
      # ada perubahan string ke notasi kalimat (contoh : noun)
      # jika elemen pada list2 ada pada list1, maka dapat diubah
      for k in list2[j][1:]:
        if k in list1[i]:
          array[i][0] = list2[j][0]
  return array

# fungsi untuk menambah string dalam segitiga tabel feeling
def calculate(y : int, x : int, list1 : list):
  # pada fungsi ini, koordinat x dan y dikurangi 1 agar sesuai indeks
  x -= 1
  y -= 1
  i = 0
  j = y + 1
  k = x - 1
  while(i < x):
    # operasi yang dilakukan dalam loop adalah
    # array[i][j] = array[i][i] + array[i + 1][j - 1]
    list1[y][x] = list1[y][i] + list1[j][k]
    i += 1
    j += 1
    k -= 1

# fungsi untuk memproses array yang sudah diinisiasi dengan fungsi initiate
def progressing(list1 : list, x : int):
  leng = x
  for i in range(1, x+1):
    for j in range(1, leng+1):
      # pertama, dilakukan fungsi calculate untuk menambah string pada
      # indeks array yang ditentukan berdasarkan 2 loop bersarang di atas
      calculate(j, i, list1)
    leng -= 1
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      # setelah penambahan string, dilakukan converting untuk mengubah
      # string ke aturan-aturan grammar
      alba = list1[i][j]
      alba = converting(alba, rules)
      list1[i][j] = alba
    leng -= 1

# fungsi untuk proses kedua untuk proses tabel
def progressing2(list1 : list, x : int):
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      # converting lagi sekali dilakukan untuk menentukan nilai "K"
      # yang dimana K tersebut merupakan string yang menandakan kalimat baku
      alba = converting(alba, t_kalimat)
      list1[i][j] = alba
    leng -= 1
  # untuk melihat hasil, digunakan print
  for i in range(0, x):
    print(list1[i][:])

# fungsi untuk mengecek nilai K pada array[0][akhir]
def cek_baku(list1 : list) -> int:
  if "K" in list1[0][-1]:
    return 1
  elif "K" not in list1[0][-1]:
    return 0

def progressing_x(list2 : list):
  count = 0
  for list1 in list2:
    tabel = array(len(list1))
    initiate(data, list1, tabel)
    progressing(tabel, len(tabel[:]))
    list1.append(cek_baku(tabel))
    for i in range(len(list1)):
      for x, j in enumerate(list1):
        if j == 1:
          count += 1
  print(count)

# fungsi untuk memproses kalimat dari awal
def cek_kalimat(strinx):
  # string dipecah dahulu
  strinx = strinx.split(" ") 
  # lalu buat segitiga tabel sesuai banyak kata pada string
  ar = array(len(strinx))
  # membuat var test untuk mengganti kata menjadi notasi kalimat (contoh : Noun, Verb)
  test = initiate(strinx, data, ar)
  # pemrosesan grammar tahap 1
  progressing(test, len(strinx))
  # pemrosesan grammar tahap 2
  progressing2(test, len(strinx))
  # meminta nilai return dari fungsi cek_baku (nilai 1 atau 0)
  return cek_baku(test)

st.write("""
# Aplikasi Pengecekan Kalimat Baku
Ini adalah apliaksi pengecekan kalimat baku sederhana yang dibuat oleh **KELOMPOK 5** menggunakan Python dan Streamlit. Aplikasi ini dipergunakan untuk memenuhi tugas akhir mata kuliah Teori Bahasa dan Otomata, yang diampu oleh Ibu Dr. Anak Agung Istri Ngurah Eka Karyawati, S.Si., M.Eng.
""")

input = st.text_input("Masukkan kalimat yang ingin dicek: ")
cek = st.button("Cek")

if cek:
    if cek_kalimat(input) == 1:
        st.success("Kalimat baku")
    else:
        st.error("Kalimat tidak baku")