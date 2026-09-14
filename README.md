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