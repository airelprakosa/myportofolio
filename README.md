Name : Raden Stanislaus Airell Prakosa Sinaga
NPM : 2506657251
Kelas : [E]

### Tugas 1

1.Pada pembuatan halaman ini, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`.Setiap bagian (Profile, About Me, Skills, Experience, dan Projects) dipisahkan menggunakan `<section>` yang dilengkapi atribut `id`. Hal ini sangat memudahkan navigasi menu agar bisa diklik dan langsung *scroll* ke bagian yang dituju.Penggunaan elemen semantik ini membuat struktur kode jauh lebih rapi dan mudah dipahami fungsinya saat dibaca ulang, dibandingkan jika hanya menumpuk tag `<div>`.Saya tidak menggunakan elemen `<article>` atau `<aside>` karena alur portofolio ini bersifat linear dan menyatu, bukan konten berita yang berdiri sendiri atau *sidebar* iklan tambahan.

2.Tantangan terbesar dalam mengatur responsivitas adalah menyesuaikan tata letak *CSS Grid* pada bagian hero agar tidak saling bertabrakan saat layar mengecil.Pada tampilan desktop, saya membagi hero secttion menjadi dua kolom utama (untuk teks identitas dan foto). Jika dibiarkan statis, tampilannya akan terpotong atau tumpang tindih di layar HP.Solusinya, saya menggunakan media query pada batas layar 600px untuk mengubah tata letak menjadi satu kolom yang menumpuk ke bawah.Prioritas utamanya adalah memastikan teks nama dan bio tetap terbaca jelas di bagian atas, membatasi ukuran maksimal foto agar tidak mendominasi layar, dan menyusun kartu-kartu di bawahnya secara vertikal.

3.Hambatan utama dari static web murni ini adalah proses pengelolaan kontennya.Seluruh informasi masih bersifat static hardcoded Jika ada pembaruan proyek atau keahlian baru, saya harus memodifikasi susunan file HTML secara manual satu per satu.Hal ini tentu akan sangat merepotkan jika data portofolio sudah semakin banyak untuk dikelola.Oleh karena itu, pada iterasi proyek selanjutnya, saya berencana menyimpan data seperti riwayat pendidikan, keahlian, dan proyek ke dalam basis data(database) menggunakan arsitektur MVT Django. Dengan begitu, konten dapat dirender secara dinamis melalui sistem template tanpa perlu menyentuh kode HTML lagi.

---

### AI Disclosure

Dalam penyelesaian Tugas 1 ini, saya memanfaatkan alat bantu AI (Gemini) bertanya mengenai penerapan tata letak CSS GRID dan  Flexbox agar tersusun rapi pada bagian Hero dan Projects.
Terdapat kendala di mana AI menyarankan penamaan class CSS yang tidak sinkron dengan HTML saya (misalnya `photo-block` disarankan, padahal di HTML tertulis `photo-frame`), sehingga foto profil sempat membesar (overflow) dan membuat foto jadi super besar dan menutup web. Saya kemudian mengevaluasi dan memperbaiki masalah ini secara mandiri dengan menyamakan nama class, membatasi `max-width`, serta mengatur `transform-origin: bottom center` agar efek seperti pop out gtu berfungsi sempurna tanpa menggeser elemen di sekitarnya.


### tugas 2


1.Ketika pengguna mengakses URL halaman proyek (misalnya `/projects/`), request pertama kali diterima oleh `portofolio/urls.py` yang akan mengarahkannya ke `main/urls.py`. Di dalam `main/urls.py`, URL tersebut dicocokkan dengan view yang sesuai (misal `show_projects`). View kemudian meminta data dari `models.py` (model `Project`) yang terhubung ke database. Setelah data diambil, view memasukkannya ke dalam sebuah context dan mengirimkannya ke `projects.html` (template). Terakhir, template merender data tersebut menggunakan Django Template Language menjadi halaman HTML utuh yang dikirimkan kembali ke browser pengguna.


2.Menyimpan data di model membuat aplikasi jauh lebih dinamis dan mudah dikelola. Jika data ditulis langsung (hard-coded) di dalam HTML,harus membongkar kode sumber setiap kali ingin menambah atau mengubah data portofolio. Dengan model,bisa memisahkan antara struktur tampilan dan isi data, sehingga penambahan proyek baru bisa dilakukan dengan cepat melalui halaman admin Django tanpa harus mengubah kode HTML sama sekali.

**3. Apa perbedaan makemigrations dan migrate? Berikan contohnya:**
`makemigrations`, perintah ini berfungsi sebagai pencatat perubahan. Django akan melihat apakah ada perubahan pada file `models.py` dan membuat sebuah file skrip migrasi baru yang berisi instruksi perubahan tersebut.
`migrate`, perintah ini bertugas mengeksekusi file skrip migrasi tadi ke dalam database sungguhan agar struktur tabel di database berubah sesuai dengan model.
contohnya, Ketika saya menambahkan atribut `is_completed = models.BooleanField(default=True)` pada model `Project`, saya harus menjalankan `makemigrations` agar Django mencatat rencana penambahan kolom ini. Setelah itu, saya menjalankan `migrate` agar kolom `is_completed` benar-benar dibuat di dalam tabel database.

### AI Disclosure

Dalam penyelesaian Tugas 2 ini, saya memanfaatkan alat bantu AI (Gemini) untuk membantu memahami alur pendaftaran model ke Django Admin, konfigurasi `CSRF_TRUSTED_ORIGINS` agar terhindar dari *error* 403 saat *deployment* ke PWS, serta menyusun skenario *Unit Test* tambahan di file `tests.py`.

Terdapat kendala saat menyusun pengujian untuk skenario *empty state* pada halaman proyek. AI awalnya menyarankan untuk menguji string `self.assertContains(response, "Belum ada project")`. Namun, parameter tersebut tidak sinkron dengan *template* `projects.html` saya yang sebenarnya menggunakan kalimat "Belum ada proyek yang ditambahkan.", sehingga tes tidak bisa berjalan valid. Saya kemudian mengevaluasi dan memperbaiki masalah ini secara mandiri dengan menyamakan string pada kode pengujian di `tests.py` dengan teks asli yang ada di dalam kondisi `{% empty %}` pada *template* HTML, sehingga seluruh *unit test* berhasil berstatus `OK`.

### tugas 3

### AI Disclosure
Dalam penyelesaian Tugas 3 ini, saya memanfaatkan referensi video tutorial Django dari Corey Schafer (Part 10 - Create, Update, and Delete Posts) dan alat bantu AI chatGPT untuk memahami konsep *routing*, pengelolaan form (CRUD), serta pembuatan *endpoint* Data Delivery (JSON/XML).

sumber belajar dan pemahaman: https://www.youtube.com/watch?v=-s7e_Fy6NRU, gpt: https://chatgpt.com/share/6ab0f55a-89a8-83ec-8507-076757f0109e

1.Kita menggunakan `ModelForm` karena ia secara otomatis membuat input *field* HTML berdasarkan model yang sudah ada di `models.py`, lengkap dengan validasi datanya. Ini jauh lebih efisien dibandingkan membuat form HTML manual yang mengharuskan kita mengecek tipe data dan memetakan input ke *database* satu per satu. Sementara itu, `{% csrf_token %}` wajib ditambahkan sebagai mekanisme keamanan bawaan Django untuk mencegah serangan *Cross-Site Request Forgery*. Token ini memastikan bahwa data yang dikirimkan melalui form benar-benar berasal dari pengguna sah di situs web kita, bukan dari *script* atau situs pihak ketiga yang berniat jahat.

2.JSON lebih disukai karena sintaksnya jauh lebih ringan dan ringkas. Berbeda dengan XML yang membutuhkan tag pembuka dan penutup yang panjang (seperti `<nama>Airell</nama>`), JSON menggunakan format *key-value* yang sederhana (`"nama": "Airell"`), sehingga ukuran *file*-nya lebih kecil dan transfer datanya lebih cepat. Selain itu, JSON terintegrasi secara *native* dengan JavaScript, sehingga *frontend* dapat langsung memproses (*parsing*) data JSON tanpa memerlukan *library* tambahan yang rumit.

3.Alurnya dimulai saat ada *request* ke URL tertentu, lalu *routing* akan mengarahkannya ke fungsi *view* yang bersesuaian. Di dalam *view*, Django menggunakan ORM untuk mengambil data portofolio dari *database* (berupa *QuerySet*). *QuerySet* tersebut kemudian dilempar ke fungsi *serializer* untuk diubah menjadi format JSON. Setelah selesai, *view* akan membungkus data JSON tersebut ke dalam `HttpResponse` dan mengirimkannya kembali ke pengguna.
Proses *serialization* sangat perlu dilakukan karena data yang diambil dari *database* Django berbentuk objek Python (*QuerySet*). Jaringan internet (protokol HTTP) tidak mengerti cara membaca objek Python secara langsung; ia hanya bisa mentransmisikan data dalam bentuk teks (seperti JSON atau XML). Oleh karena itu, *serialization* berfungsi sebagai penerjemah objek kompleks Django menjadi teks terstruktur yang bisa dibaca dan dikirim melalui internet.

### tugas 4
### AI Disclosure

Dalam pengerjaan Tugas 4 ini, saya menggunakan bantuan AI ChatGPT sebagai alat bantu untuk memahami konsep Authentication, Session, dan Cookies, mendapatkan masukan terkait implementasi serta struktur kode seperti pembuatan dan pengecekan grup Editor, penanganan error, proteksi CSRF, serta implementasi reusable component pada fitur star di modul Project dan Experience. Selain itu, AI juga membantu memahami perbedaan method GET dan POST, penjelasan mengenai fungsi parameter ?next saat proses login. Seluruh keputusan arsitektur, penulisan kode akhir, dan verifikasi fungsionalitas tetap diperiksa dan disesuaikan secara mandiri oleh saya.
link chatgpt:https://chatgpt.com/share/6aba7d3d-6650-83ec-9aa8-488baab5f97e

### Tugas 5

1. Debouncing adalah teknik menunda eksekusi sebuah fungsi sampai pengguna berhenti memicu event selama jeda tertentu. Di halaman Experience, setiap ketikan di kolom pencarian membatalkan timer sebelumnya dengan `clearTimeout` lalu memasang timer baru 300 ms dengan `setTimeout`, sehingga `fetch()` baru dikirim setelah pengguna berhenti mengetik. Tanpa debouncing, mengetik "compfest" mengirim 8 permintaan ke server padahal hanya hasil terakhir yang dipakai. Itu membebani server dan database, dan respons yang datang tidak berurutan bisa membuat hasil lama menimpa hasil baru. Untuk kasus terakhir itu halaman ini juga memakai `AbortController` supaya permintaan lama dibatalkan.

2. `fetch()` tidak langsung mengembalikan data, tetapi sebuah Promise karena permintaan jaringan butuh waktu. `await` menghentikan sementara fungsi `async` sampai Promise itu selesai lalu memberikan hasilnya (objek `Response`), tanpa membekukan halaman. Hal yang sama berlaku untuk `response.json()`. Jika `await` tidak dipakai, variabel `response` berisi Promise yang masih pending, sehingga `response.ok` bernilai `undefined` dan `response.json` bukan fungsi, dan kode berikutnya berjalan sebelum data tiba. Selain itu, error jaringan tidak tertangkap oleh `try...catch` karena penolakan Promise terjadi setelah blok tersebut selesai dijalankan.

3. XSS (Cross-Site Scripting) adalah serangan ketika penyerang menyisipkan kode JavaScript ke dalam data, misalnya judul berisi `<img src="x" onerror="alert('XSS!')">`, lalu kode itu dijalankan di browser pengguna lain yang membuka halaman. Akibatnya penyerang bisa bertindak atas nama korban dengan memakai sesi login korban. Data yang ditampilkan lewat template Django lebih aman karena `{{ variabel }}` otomatis di-escape (karakter `<` menjadi `&lt;`). Perlindungan itu tidak ikut ketika data dikirim sebagai JSON lalu disusun menjadi HTML di JavaScript dengan `innerHTML`, karena browser menafsirkan string itu sebagai HTML apa adanya. Karena itu di halaman Experience setiap nilai teks dibungkus `escapeHtml()` sebelum disisipkan, dan di sisi server input dibersihkan dengan `strip_tags` pada method `clean_title` dan `clean_description` di `ExperienceForm` sebagai lapisan tambahan.

**Fitur tambahan di luar instruksi Tugas 5 (halaman Experience):**

- Star tanpa reload: tombol star mengirim `fetch()` ke `experience/<id>/star-ajax/`, lalu hanya tombol itu yang diperbarui dan toast muncul. Pengunjung yang belum login tetap diarahkan ke halaman login.
- Filter jenis pengalaman: dropdown yang bisa digabung dengan pencarian judul, lewat parameter `?category=` di `/api/experiences/`.
- Jumlah hasil ("Menampilkan N pengalaman") dan tombol "Coba lagi" saat data gagal dimuat.

### AI Disclosure

### AI Disclosure
Dalam proses pembelajaran dan pengerjaan Tugas 5 ini, saya memanfaatkan bantuan kecerdasan buatan (AI) yaitu GPT sebagai diskusi interaktif untuk:
- Berdiskusi dan memahami konsep teoretis serta alur kerja materi Tutorial 5, seperti mekanisme asinkron `fetch()` dan *Promise*, teknik *search debouncing* (`setTimeout`/`clearTimeout`), serta penggunaan `AbortController`.
- Mempelajari prinsip keamanan web secara konseptual, khususnya mitigasi kerentanan XSS (*Cross-Site Scripting*) baik di sisi *frontend* (`escapeHtml`) maupun *backend* (`strip_tags`).
- Membahas alur integrasi AJAX dengan Django views, penanganan *state* aplikasi (*loading*, *error*, *empty*), serta penyusunan logika pengujian unit (*unit testing*).

Seluruh pemahaman konsep yang didapat dari sesi diskusi interaktif tersebut kemudian saya terapkan, kembangkan, dan sesuaikan secara mandiri ke dalam struktur kode program pada proyek portofolio pribadi saya.

log percakapan: https://chatgpt.com/share/6ac3b03a-dd2c-83ec-8042-83bbb45c3174
