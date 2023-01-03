import streamlit as st
import pandas as pd

# aturan kalimat dengan struktur kalimat(grammar) 
t_kalimat = [["K", "SPO"],
          ["K", "SPOKet"],
          ["K", "SPOpel"],
          ["K", "SP"],
          ["K", "SPKet"],
          ["K", "SPpel"]]

# aturan penggantian struktur kalimat (SPOKetPel)
rules = [["S", "Noun", "Pronoun", "PropNoun", "NounNoun", "NounPronoun", "NounPropNoun", "NounAdj", "NounAdv", "NumNoun"],
         ["P", "Verb", "VerbAdj", "AdvVerb"],
         ["O", "Noun", "Pronoun", "PropNoun", "NounNoun", "NounPronoun", "NounPropNoun", "NounAdj", "NounAdv", "NumNoun"],
         ["pel", "AdvVerb", "AdvAdj"],
         ["Ket", "PrepNoun", "PrepPronoun", "PrepPropNoun", "PrepAdj", "PrepNum"]]

# data untuk diganti menjadi noun, verb, adj, adv, prep, pronoun, propnoun, dan num
noun = "Noun | ibu | makanan | hak | manusia | uud | kultur | jaringan | wadah | sifat | masalah | presentasi | mobil | suara | ayah | barang | sepeda | adik | taman | bermain | rumah | gaun | acara | orang | pasar | motor | pekarangan | bajunya | sayur-sayuran | kursi | bengkel | atas | meja | harga | martabak | manis | pertigaan | jalan | kucing | kampung | sepatu | anaknya | bapak | guru | diri | pak | keliling | lapangan | pohon | tubuh | mawar | rasa | air | laut | sekolahku | hatinya | hujan | celana | anak | permainan | siswa | kelas | keluarga | asap | rokok | pipi | kainnya | matahari | gadis | jendela | rumahnya | berita | senja | langit | gedung | kaki | kebun | bunga | bis | tangisan | bayi | kopinya | gadis-gadis | pekerjaan | pertanyaan | waktu | fajar | buaya | desa | badan | badanku | anjing | wajan | paman | polisi | harta | suami | kamar | kakinya | kakimu | drum | potongan | kayu | kotaknya | bolanya | permen | kain | bukunya | rambutnya | tangannya | pantai | perumahan | tubuhnya | sendok | kolam | kesayangan | warna | gorden | bibi | laptop | keranjang | pria | kemeja | bibirnya | pintu | dapur | mata | bagian | bawah | kue | tangkai | sapu | baju | pengantin | boneka | jaket | kulihat | hidupnya | dadu | koin | tanah | topi | pesta | buah | terung | wajah | cermin | lensa | kamera | kura-kura | pidato | seminar | bocah | rumahku | usianya | guci | ketua | periode | temanku | mangga | rumah-rumah | jeda | daki | tv | ular | rongga | mulut | sakura | tembok | kemenangan | kemarin | petir | hukuman | malam | kucingnya | keputusan | prestasinya | keberhasilan | hal | kisah | perjuangan | masakan | parfum | nanas | lukisan | pisau | lantai | kulit | buku | obat | teh | tulisan | layar | ingin | antara | bulan | dahulu | zaman | saat | matematika | kakek | atom | ujian | bola | dinding | peraturan | kuliah | penyakit | bantuan | kepanitiaan | sedih | vaksin | pramuka | pancasila | lemari | audisi | puncak | lawan | ikan | ketenarannya | setahun | pertandingan | sungai | hari | nanti | neneknya | minggu | akhir | cupang | usia | tahun | murid | hunian | lurah | pencuri | tante | keripik | sekolah | payung | kakak | karyawan | otak | kematian | fasilitas | umum | garam | roti | lampu | kota | sikap | juara | kabar | usul | mungkin | kenyataan | mahasiswa | korban | bencana | alam | uang | tugas | beban | gereja | kecamatan | tok | tempat | komputer | pebasket"
verb = "Verb | membawa | disebutkan | dilakukan | dijelaskan | melaju | menyukai | percaya | mengajak | pergi | tersebut | adalah | berhenti | mencuci | membeli | menggunakan | menduduki | diperbaiki | ditaruh | berkeliaran | menyuruh | murid | memperkenalkan | menghukum | lari | memiliki | turun | terkena | menjadi | membuat | merupakan | ada | menggembirakan | melangkahkan | belajar | menghampiri | berjalan | terdengar | mengerjakan | menjawab | berharga | membantu | memakai | berwarna | suka | mengecat | berubah | melempar | pulang | tinggal | berlangsung | dimulai | membuka | mengetuk | berdebat | berpamitan | menginjak | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | sayang | melawan | melakukan | berteriak | merasa | membenci | mengajar | lalu | menang | melihat | berhasil | dilewati | meduduki | memberikan | menangkap | dikenal | mendapatkan  | menjadi | mendengar | berprilaku | mewarnai | menolak | menyatakan | dibuat | menerima | dihukum | lulus | mengungsi | mencuri | berlari | tidur | meminjam | mengangkat | mengantuk | datang | menembak"
adj = "Adj | enak | asasi | jelas | steril | sombong | singkat | hijau | cepat | merdu | murah | baru | kecil | baik | tua | kotor | suka | segar | biru | rusak | bulat | mewah | mahal | liar | nakal | kokoh | merah | asin | dekat | resah | gundah | kepanjangan | menyenangkan | basah | elok | bahagia | patah | pintar | harmonis | kemerahan | menyeramkan | kering | terik | langsing | besar | kebesaran | kemerah-merahan | megah | yakin | ragu-ragu | secepatnya | sebaik-baiknya | sungguh-sungguh | takut | malam | nyaring | panas | cantik | hati-hati | rajin | benar | boros | ganas | kaya | kikir | miskin | ramah | sehat | jinak | dingin | kejam | malas | cocok | hemat | tamak | angkuh | bersih | berat | banyak | tipis | tebal | panjang | pendek | mungil | luas | sempit | ideal | gemuk | kurus | ringan | jutek | lebar | dangkal | cokelat | kekuning-kuningan | putih | abu-abu | ungu | lumut | jambu | bata | kebiru-biruan | jingga | lembayung | lesi | hitam | pekat | lentur | kaku | tinggi | tabung | balok | kubus | persegi | lingkaran | kerucut | cembung | cekung | rata | bundar | datar | lonjong | larut | lambat | lama | perlahan | mendadak | kuno | antik | primitif | lawas | lelet | jauh | akrab | lebat | rapat | bangga | bosan | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | jahat | lezat | harum | semerbak | manis | asam | tampan | serak | bising | indah | tajam | kasar | licin | halus | pahit | rapi | hebat | puas | pudar | sakit | dewasa | termuda | lihai | pedas | dalam | cerdas | terenak | umum | kecewa | ketus | senang | panik | muda | sepi | tegas | semanis | setegar | secepat | tenang | semampu | kuat | akurat"
adv = "Adv | dengan | secara | begitu | akan | tidak | jangan | sangat | terlalu | sekali | paling | cukup | sudah | sedikit | segera | sedang | jarang | sering | selalu | agak | baru | telah | belum | ingin | mau | harus | mesti | masih | rasa | diam"
prep = "Prep | ke | pada | dalam | di | dari | karena | untuk | kepada | saat | dengan | jika | atas | terhadap | sejak | dekat | ketika | sehingga | yang"
pronoun = "Pronoun | saya | dia | itu | kami | ia | ini | aku | hamba | kita | kamu | anda | engkau | kalian | beliau | mereka"
propnoun = "PropNoun | gunggus | agung | wawan | gung | frady | raindra | jati | budi | ani | toni | asri | adi | wisnu | dila | pablo | rani | harto | ayu | jakarta | dio | bima | doni | diva | nayla | andi | indra | dalang | upin | saputra | susi | banu | wahyu | intan | dara | syifa | kadek | indah | abi | putri | wati | manda | dian | arya | diah | citra | bali | steven | matthew | roni | dito | amanda | sultan | jihan | david | rina | dina | agus | nanda | kinan | ari | gusde"
num = "Num | 1945 | semua | sembilan | banyak | suatu | setiap | satu | dua | tiga | empat | lima | enam | tujuh | delapan"

# list data untuk menyimpan data kamus
data = [ ]
data.append(noun.split(" | "))
data.append(verb.split(" | "))
data.append(adj.split(" | "))
data.append(adv.split(" | "))
data.append(prep.split(" | ")) 
data.append(propnoun.split(" | "))
data.append(pronoun.split(" | "))
data.append(num.split(" | "))

# list untuk menyimpan kata yang tidak terdaftar dalam data kamus
notInData = [ ]

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
  for i in range(len(list1)):
    for j in range(len(list2)):
      # ada perubahan string ke notasi kalimat (contoh : noun)
      # jika elemen pada list2 ada pada list1, maka dapat diubah
      for k in list2[j][1:]:
        if k == list1[i]:
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

# fungsi yang akan digunakan jika mengecek paragraf (saat ini belum digunakan)
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

# fungsi untuk memproses kalimat dari awal (fungsi utama)
def cek_kalimat(strinx):
  strinx = prepare_input(strinx)
  # membuat segitiga tabel sesuai banyak kata pada string
  ar = array(len(strinx))
  # membuat var test untuk mengganti kata menjadi notasi kalimat (contoh : Noun, Verb)
  test = initiate(strinx, data, ar)
  # pemrosesan grammar tahap 1
  progressing(test, len(strinx))
  # pemrosesan grammar tahap 2
  progressing2(test, len(strinx))
  # meminta nilai return dari fungsi cek_baku (nilai 1 atau 0)
  return cek_baku(test)

# fungsi untuk menyiapkan kalimat sebelum diproses
def prepare_input(strink):
  # mengubah string menjadi huruf kecil semua
  strink = strink.lower()
  # string dipecah dan dijadikan list
  strink = strink.split(" ")
  return strink

# fungsi untuk mengecek apakah kalimat ada dalam data kamus
def cek_input(string):
  # mengelompokan data kamus menjadi 1 list
  db = []
  db += noun.split(" | ")
  db += verb.split(" | ")
  db += adj.split(" | ")
  db += adv.split(" | ")
  db += prep.split(" | ")
  db += propnoun.split(" | ")
  db += pronoun.split(" | ")
  db += num.split(" | ")
  kalimat = prepare_input(string)
  # mengecek apakah setiap kata pada kalimat ada dalam data kamus
  for i in kalimat:
    if i not in db:
      # variabel untuk menampung kata yang tidak ada dalam data kamus
      notInData.append(i)
  # jika variabel notInData kosong, maka semua kata ada dalam data kamus
  if notInData == [ ]:
    return 1
  else:
    return 0

# fungsi untuk menyamakan panjang list
def matching(noun, list):
  for i in range(len(noun) - len(list)):
    list.append("")
  return list

# di bawah merupakan sintaks-sintaks streamlit untuk membuat tampilan aplikasi
st.set_page_config(page_title="FP • Kelompok 5", page_icon="5️⃣")
menu = st.sidebar.selectbox("📂 Menu ", ["🔍 Cek Kalimat", "📖 Kamus Kami", "👥 Contact Us"])


if menu == "🔍 Cek Kalimat":

  st.write("""
  # Aplikasi Pengecekan Kalimat Baku
  Ini adalah apliaksi pengecekan kalimat baku sederhana yang dibuat oleh **KELOMPOK 5** menggunakan Python dan Streamlit. Aplikasi ini dipergunakan untuk memenuhi tugas akhir mata kuliah Teori Bahasa dan Otomata, yang diampu oleh Ibu Dr. Anak Agung Istri Ngurah Eka Karyawati, S.Si., M.Eng.
  """)

  input = st.text_input("Masukkan kalimat yang ingin dicek 👇", placeholder="Ketik disini")
  cek = st.button("Cek")

  if cek:
    if cek_input(input):
      if cek_kalimat(input) == 1:
          st.success("✔ Kalimat baku")
      elif cek_kalimat(input) == 0:
          st.error("✖ Kalimat tidak baku")
    else:
      error = f'ERROR: Kata {notInData} tidak ditemukan dalam kamus kami'
      st.error(error)


elif menu == "📖 Kamus Kami":
  
  st.title("Kamus Kami")

  noun = noun.split(" | ")
  verb = verb.split(" | ")
  adj = adj.split(" | ")
  adv = adv.split(" | ")
  prep = prep.split(" | ")
  pronoun = pronoun.split(" | ")
  propnoun = propnoun.split(" | ")
  num = num.split(" | ")
  
  verb = matching(noun, verb)
  adj = matching(noun, adj)
  adv = matching(noun, adv)
  prep = matching(noun, prep)
  pronoun = matching(noun, pronoun)
  propnoun = matching(noun, propnoun)
  num = matching(noun, num)

  kamus = pd.DataFrame(columns=["Noun", "Verb", "Adjective", "Adverb", "Preposition", "Pronoun", "Proper Noun", "Number"])
  for i in range(1, len(noun)):
    kamus.loc[i] = [noun[i], verb[i], adj[i], adv[i], prep[i], pronoun[i], propnoun[i], num[i]]
  
  kamus


elif menu == "👥 Contact Us":
  st.title("Contact Us")

  st.markdown(
      """
      <style>
          div[data-testid="column"]
          {
              text-align: center;
          } 
      </style>
      """,unsafe_allow_html=True
  )

  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
    st.image("https://avatars.githubusercontent.com/u/72916363?v=4")
    st.markdown("[Gunggus](https://github.com/BangAjus)")
  with col2:
    st.image("https://avatars.githubusercontent.com/u/100138244?v=4")
    st.caption("[Agung Mahadana](https://github.com/agungmahadana)")
  with col3:
    st.image("https://avatars.githubusercontent.com/u/107167667?v=4")
    st.caption("[Wawan](https://github.com/Wawan-092)")
  with col4:
    st.image("https://avatars.githubusercontent.com/u/107132486?v=4")
    st.caption("[Gung Frady](https://github.com/Gungfrady)")
  with col5:
    st.image("https://avatars.githubusercontent.com/u/94416844?v=4")
    st.caption("[Raindra Pramathana](https://github.com/RaindraP)")