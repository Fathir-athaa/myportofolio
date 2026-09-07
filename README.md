# Portofolio — Fathir Atha Rizki Tasril

Website portofolio pribadi, dibangun murni pakai HTML & CSS (tanpa framework, tanpa JavaScript). Isinya tentang perkenalan aku, skill teknis yang aku kuasai, pengalaman organisasi, sampai testimoni dari orang-orang yang pernah kerja bareng aku.

---

## Fitur

- **Sticky header** dengan efek blur (`backdrop-filter`) yang nempel di atas saat di-scroll, dengan link navigasi ke tiap section (`#profile`, `#skills`, `#experience`, `#contact`) plus efek underline glow merah saat di-hover.
- **Hero / About section** — nama & identitas dengan animasi 3D flip sekali muncul (`flip3D`), foto profil dengan efek "lampu" blur merah di belakangnya yang menyala lebih terang saat di-hover (`lampGlow`), serta info NPM dan program studi dalam bentuk `<dl>`.
- **Skills section** — daftar tech stack ditampilkan sebagai _logo marquee_ yang bergeser otomatis tanpa henti (infinite scroll pakai `@keyframes`), dengan efek fade transparan di kedua ujung (`mask-image`) dan otomatis berhenti saat kursor diarahkan ke situ.
- **Experience section** — 4 kartu pengalaman organisasi/kepanitiaan, masing-masing punya _mini image slider_ 3 foto yang bergantian otomatis tiap beberapa detik (`expSlide`), lengkap dengan badge status (Active Member/Volunteer) dan deskripsi peran.
- **Contact section** — dua kolom: kiri berisi daftar testimoni/peer review (scrollable, dengan custom scrollbar merah gelap), kanan berisi ajakan kolaborasi dan tombol ikon bulat menuju GitHub, LinkedIn, dan email.
- **Fully responsive** — grid hero berubah jadi satu kolom di bawah 600px, sedangkan grid experience dan contact berubah jadi satu kolom di bawah 768px.

## Tech Stack

- HTML5 semantic markup
- CSS3 (custom properties/CSS variables, Grid, Flexbox, keyframe animation, `mask-image`)
- Google Fonts — _Space Grotesk_
- Tanpa JavaScript, tanpa build tool, tanpa framework

## Struktur Proyek

```
├── templates
|   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── poto.jpg
│       ├── javascript-original.svg, python-original.svg, html5-original.svg, ...
│       ├── google12.png, kantorGoogle.jpg, Google.jpg
│       ├── Compest 18 1.jpeg, Compest 18 2.jpeg, Compest 18 3.jpeg
│       ├── Speaker (1).jpeg, acasia.jpg
│       └── Forkoma.jpg, Forkoma 2.jpg, Forkoma 3.jpg
└── README.md
```

## Cara Menjalankan

Karena ini murni HTML/CSS statis, nggak perlu install dependency apa pun.

1. Clone repo ini
   ```bash
   git clone <url-repo-kamu>
   cd <nama-folder>
   ```
2. Pastikan folder `static/img/` sudah berisi semua asset gambar yang dipakai di `index.html` (foto profil, logo skill, dan foto-foto experience).
3. Buka `index.html` langsung di browser, **atau** jalankan local server biar path relatif jalan dengan benar:
   ```bash
   npx serve .
   # atau
   python3 -m http.server
   ```
4. Akses di `http://localhost:<port>`.

## Progress Pengerjaan

Hari 1

Sesi pagi — Setup struktur HTML dasar (header/nav, section profile, skills, experience, contact) dan nentuin color palette dark-red theme (--paper, --accent, --accent-dark). Commit awal: kerangka halaman masih polos, belum ada styling detail. Sesi siang — Bangun hero section: grid 2 kolom (identity, photo, details), styling avatar foto beserta efek glow merah di belakangnya (photo-block + animasi lampGlow saat di-hover), lanjut styling navbar sticky dengan efek blur (backdrop-filter) dan underline glow di tiap link saat di-hover. Sesi sore — Bangun Skills section: slider logo tech stack yang bergeser otomatis tanpa henti, termasuk benerin loop-nya biar mulus (dua set logo digandakan) dan efek fade transparan di kedua ujung pakai mask-image. Sesi malam — Bangun Experience section: grid 2 kolom untuk kartu pengalaman, bikin mini image slider otomatis di tiap kartu (exp-slider-track), isi konten 4 pengalaman (GDG UI, COMPFEST 18, Acasia Campus Expo, Forkoma UI Banten), sekaligus iterasi timing animasi slider gambarnya biar nggak kepotong-potong.

Hari 2

Sesi pagi — Bangun Contact section: kolom kiri untuk daftar peer review/testimoni (scrollable dengan custom scrollbar merah gelap), kolom kanan untuk ajakan kolaborasi dan tombol ikon sosial (GitHub, LinkedIn, Email). Sesi siang — Kejar isu responsive: pasang breakpoint 600px untuk hero-grid dan 768px untuk experience-grid & contact-grid, testing di beberapa ukuran layar. Sesi sore–malam — Polishing keseluruhan: rapihin CSS variable biar konsisten antar section, cek alt text & aria-label buat aksesibilitas dasar, final review sebelum commit terakhir sebelum deploy.

## Pertanyaan Reflektif

### Tugas 1

1. Iya, aku pakai elemen semantik HTML5, tapi nggak semua jenis semantik aku pakai. Struktur utama halaman ini terdiri dari `<header>` untuk navbar, `<main>` sebagai pembungkus konten inti, empat buah `<section>` (profile, skills, experience, contact), `<nav>` untuk menu, dan `<footer>`. Aku pilih `<section>` karena tiap bagian ini memang punya topik dan tujuan yang jelas berbeda satu sama lain, dan masing-masing dirujuk lewat anchor id (`#profile`, `#skills`, dst) yang dipakai navbar — jadi bukan cuma soal "kelihatan semantik", tapi memang fungsional buat navigasi.

   Yang nggak aku pakai adalah `<article>` dan `<aside>`. Sebenarnya kartu experience di section Experience itu kandidat kuat buat jadi `<article>` — tiap kartu punya judul, gambar, badge, dan deskripsi yang secara konten bisa berdiri sendiri kalau dipisah dari halaman (mirip entri blog/portofolio proyek). Aku akui ini titik lemah struktur HTML aku: idealnya kartu experience dan mungkin kartu testimoni di Contact section pakai `<article>`, bukan cuma `<div class="skill-card exp-card">`. Untuk `<aside>`, aku memang nggak pakai karena nggak ada konten tangensial/pelengkap semacam sidebar di halaman ini — semua yang tampil adalah konten inti portofolio, jadi maksa masukin `<aside>` justru nggak akan merepresentasikan isi dengan tepat.

2. Tantangan responsive terbesarku justru bukan di grid utama, tapi di **navbar**. Menu navigasi aku posisikan `position: absolute` dan di-center pakai `left: 50%; transform: translateX(-50%)` supaya persis di tengah header. Ini enak dilihat di layar lebar, tapi begitu aku evaluasi dengan resize browser pelan-pelan dari lebar penuh ke ukuran HP, ternyata navbar ini yang paling duluan "pecah" — di layar sempit, brand name, menu yang di-center absolute, dan potensi elemen lain gampang bertabrakan atau overflow, dan sejauh ini aku belum menaruh media query khusus untuk navbar itu sendiri (beda dengan `.hero-grid`, `.experience-grid`, dan `.contact-grid` yang masing-masing sudah aku kasih breakpoint).

   Cara aku evaluasi elemen mana yang harus diprioritaskan: aku cek satu per satu section dari lebar penuh sampai ~360px sambil mencatat di lebar berapa layout mulai terlihat rusak. Hasilnya, breakpoint yang sudah aku pasang juga nggak konsisten — `.hero-grid` berubah jadi satu kolom di `600px`, sementara `.experience-grid` dan `.contact-grid` baru berubah di `768px`. Untuk iterasi berikutnya, dua hal yang paling perlu aku benerin: (1) tambahin breakpoint khusus untuk header/nav (kemungkinan diubah jadi hamburger menu atau menu yang di-stack), dan (2) menyamakan angka breakpoint di semua section supaya transisi antar section di ukuran layar menengah (misalnya tablet, 600–768px) nggak terasa lompat-lompat.

3. Karena ini static web murni tanpa server-side apa pun, keterbatasan yang paling terasa ada di dua hal: pertama, form kontak beneran nggak ada — satu-satunya jalur kontak langsung cuma lewat `mailto:` di tombol email, jadi pengunjung harus keluar dari halaman dan buka aplikasi email mereka sendiri, nggak ada validasi ataupun konfirmasi pengiriman pesan di halaman itu sendiri. Kedua, semua konten — bio, daftar skill, daftar pengalaman organisasi, bahkan testimoni dari orang lain — itu hardcoded langsung di `index.html`. Setiap kali ada pengalaman baru atau testimoni baru yang mau ditambahkan, aku harus buka dan edit HTML-nya lagi, lalu re-deploy, nggak ada cara mengubah konten tanpa menyentuh kode. Ini juga berarti data testimoni yang ditampilkan nggak bisa diverifikasi atau diperbarui secara independen dari pemilik website.

   Untuk iterasi selanjutnya, dua fungsionalitas dinamis yang paling ingin aku siapkan: (1) form kontak fungsional (misalnya lewat layanan seperti Formspree, atau backend kecil sendiri) supaya pengunjung bisa langsung mengirim pesan tanpa pindah aplikasi, dan (2) daftar experience serta testimoni yang datanya diambil dari file data terpisah (JSON) atau headless CMS ringan, supaya menambah pengalaman atau testimoni baru nggak perlu mengubah struktur HTML setiap kali, dan idealnya ke depan testimoni bisa dikonfirmasi/di-submit langsung oleh yang bersangkutan, bukan sekadar teks yang aku tempel manual.

## AI Disclosure

Aku pakai AI (ChatGPT/Claude) sebagai _pair programmer_, terutama di tahap drafting awal untuk bagian-bagian yang butuh eksperimen animasi CSS — bukan buat generate satu website jadi sekali klik.

**Bagian yang dibantu AI:**

- Ide struktur awal grid 2 kolom untuk hero section (`hero-identity`, `hero-photo`, `hero-details`)
- Draft pertama logika _infinite scroll marquee_ untuk slider logo tech stack di Skills section
- Saran pendekatan slider gambar otomatis di tiap kartu Experience (`exp-slider-track`) dan efek glow di belakang foto profil (`photo-block` + `lampGlow`)
- Penyusunan kalimat di README ini sendiri — poin-poin dan progres di atas aku yang menentukan, tapi AI bantu merapikan cara penyampaiannya biar sesuai struktur bacaan

**Bagian yang aku kerjain/perbaiki manual:**

- **Loop marquee tanpa "patah"** — draft awal AI untuk slider logo cuma satu set logo dengan `translateX` sampai habis, jadi keliatan jeda/lompatan pas animasi mengulang dari awal. Aku ubah sendiri jadi dua set logo yang sama ditaruh berurutan dengan `width: max-content`, terus animasi cuma geser sampai `-50%`, jadi looping-nya mulus tanpa keliatan sambungannya.
- **Timing slider foto Experience** — versi awal `@keyframes expSlide` dari AI transisinya kepotong-potong (langsung ganti gambar tanpa jeda "diam" buat dilihat). Aku hitung ulang persentasenya sendiri (misalnya `0%–28%` diam di gambar 1, baru geser di `33%–61%`) supaya tiap foto ada waktu cukup buat dilihat sebelum gonta-ganti.
- **Efek glow foto profil** — nilai `blur()`, `opacity`, dan `box-shadow` di `lampGlow` hasil AI awalnya kelihatan terlalu flat/statis pas di-hover. Aku iterasi manual kombinasi blur–opacity–scale-nya biar efeknya lebih hidup.
- **Konsistensi visual** — nilai warna, radius, dan shadow yang disaranin AI awalnya nggak konsisten antar section (beda-beda opacity shadow di skill-card, exp-card, dan contact-card). Aku rapiin sebagian jadi CSS variables (`--accent`, `--accent-dark`, `--line`, `--radius`) biar ada satu sumber kebenaran, meskipun aku sadar belum semua nilai warna di file ini konsisten pakai variable (masih ada beberapa hex value ditulis langsung di rule tertentu).
- **Aksesibilitas dasar** — nambahin `alt` text deskriptif di tiap `<img>` (termasuk gambar-gambar di slider Experience) dan `aria-label` di social icon button, yang di draft awal AI kosong atau generic.

---
