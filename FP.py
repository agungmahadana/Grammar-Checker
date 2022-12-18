import streamlit as st

t_kalimat = [["K", "SPO"],
          ["K", "SPOKet"],
          ["K", "SPOpel"],
          ["K", "SPKet"],
          ["K", "SP"],
          ["K", "SPpel"]]

rules = [["S", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
         ["P", "Verb", "VerbAdj"],
         ["O", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
         ["pel", "AdvVerb", "AdvAdj"],
         ["Ket", "PrepPronoun", "PrepPropNoun", "PrepNoun", "PrepAdj"]]

noun = "Noun | ibu | makanan | hak | manusia | UUD | 1945 | kultur | jaringan | wadah | sifat | masalah | presentasi | mobil | suara | ayah | barang | sepeda | adik | gunuggus | adik | taman | bermain | rumah"
verb = "Verb | membawa | disebutkan | dilakukan | membawa | dijelaskan | melaju | menyukai | percaya | mengajak | pergi"
adj = "Adj | enak | asasi | jelas | steril | sombong | singkat | hijau | cepat | merdu | murah | baru | kecil"
prep = "Prep | ke | pada | dalam | di | dari"
adv = "Adv | dengan | secara | begitu"

data = [ ]
data.append(noun.split(" | "))
data.append(verb.split(" | "))
data.append(adj.split(" | "))
data.append(prep.split(" | ")) 
data.append(adv.split(" | "))

def array(n : int) -> list:
  list1 = [ ]
  for i in range(n, 0, -1):
    list2 = [ ]
    for j in range(i):
      list2.append("")
    list1.append(list2)
  return list1

def concat_str(str1 : str, str2 : str) -> str:
  str3 = ""
  for i in str1:
    for j in str2:
      str3 = str3 + (i + j)
  return str3

def unique_str(str1 : str) -> str:
  str3 = ""
  for i in str1:
    if i not in str3:
        str3 = str3 + i
  return str3

def converting(str1 : str, list1 : list) -> str:
  str2 = ""
  for i in range(len(list1[:])):
    for j in list1[i][1:]:
      if j in str1:
        str2 = str2 + list1[i][0]
  return unique_str(str2)

def initiate(list1 : list, list2 : list, array : list):
  for i in range(0, len(list1)):
    for j in range(len(list2)):
      for k in list2[j][1:]:
        if k in list1[i]:
          array[i][0] = list2[j][0]
  return array

def calculate(y : int, x : int, list1 : list):
  x -= 1
  y -= 1
  i = 0
  j = y + 1
  k = x - 1
  while(i < x):
    list1[y][x] = list1[y][i] + list1[j][k]
    i += 1
    j += 1
    k -= 1

def progressing(list1 : list, x : int):
  leng = x
  for i in range(1, x+1):
    for j in range(1, leng+1):
      calculate(j, i, list1)
    leng -= 1
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      alba = converting(alba, rules)
      list1[i][j] = alba
    leng -= 1

def progressing2(list1 : list, x : int):
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      alba = converting(alba, t_kalimat)
      list1[i][j] = alba
    leng -= 1
  
  for i in range(0, x):
    print(list1[i][:])

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

def cek_kalimat(strinx):
  strinx = strinx.split(" ") 
  ar = array(len(strinx))
  test = initiate(strinx, data, ar)
  progressing(test, len(strinx))
  progressing2(test, len(strinx))
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
