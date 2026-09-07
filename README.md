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