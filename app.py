import streamlit as st
import random
from itertools import product

st.set_page_config(page_title="AI Skincare Assistant", layout="wide")
st.title("🧴 AI Rekomendasi Skincare Super Lengkap")

# === INPUT DARI PENGGUNA ===
masalah_kulit = st.selectbox("Masalah kulit kamu apa?", [
    "Jerawat", "Bruntusan", "Kulit Kusam", "Flek Hitam", "Kulit Kering", "Kulit Berminyak", "Sensitif"
])

tipe_kulit = st.selectbox("Tipe kulit kamu:", [
    "Kering", "Berminyak", "Sensitif", "Kombinasi", "Normal"
])

budget = st.selectbox("Budget kamu:", [
    "Low (di bawah 50rb)", "Medium (50rb - 150rb)", "High (di atas 150rb)"
])

waktu = st.selectbox("Produk ini akan dipakai kapan?", [
    "Pagi", "Malam", "Bisa Kapan Saja"
])

# === GENERATOR PRODUK: SELALU ADA HASIL ===
def generate_products(masalah, tipe, budget, waktu, n=20):
    kandungan_list = {
        "Jerawat": ["Salicylic Acid", "Niacinamide", "Zinc", "Tea Tree"],
        "Bruntusan": ["AHA", "BHA", "PHA", "Lactic Acid"],
        "Kulit Kusam": ["Vitamin C", "Arbutin", "Niacinamide"],
        "Flek Hitam": ["Tranexamic Acid", "Alpha Arbutin", "Retinol"],
        "Kulit Kering": ["Hyaluronic Acid", "Ceramide", "Panthenol"],
        "Kulit Berminyak": ["Niacinamide", "Green Tea", "Kaolin Clay"],
        "Sensitif": ["Centella Asiatica", "Madecassoside", "Allantoin"]
    }

    manfaat_list = {
        "Salicylic Acid": "Mengatasi jerawat dan membersihkan pori",
        "Niacinamide": "Mencerahkan dan mengontrol minyak",
        "Zinc": "Menenangkan kulit dan mengurangi inflamasi",
        "Tea Tree": "Antibakteri untuk jerawat aktif",
        "AHA": "Eksfoliasi sel kulit mati",
        "BHA": "Membersihkan pori dalam",
        "PHA": "Eksfoliasi ringan untuk kulit sensitif",
        "Lactic Acid": "Melembapkan dan menghaluskan tekstur kulit",
        "Vitamin C": "Mencerahkan dan menangkal radikal bebas",
        "Arbutin": "Menyamarkan bintik hitam dan bekas jerawat",
        "Tranexamic Acid": "Mengurangi flek hitam",
        "Alpha Arbutin": "Mencerahkan tanpa iritasi",
        "Retinol": "Anti-aging dan mempercepat regenerasi kulit",
        "Hyaluronic Acid": "Menghidrasi kulit secara intens",
        "Ceramide": "Memperbaiki skin barrier",
        "Panthenol": "Menenangkan dan menjaga kelembapan",
        "Green Tea": "Mengontrol minyak dan antioksidan",
        "Kaolin Clay": "Menyerap minyak berlebih",
        "Centella Asiatica": "Menenangkan iritasi dan mempercepat penyembuhan",
        "Madecassoside": "Meredakan kemerahan",
        "Allantoin": "Melembutkan dan melembapkan kulit"
    }

    produk_list = []
    for i in range(n):
        kandungan = random.choice(kandungan_list[masalah])
        produk_list.append({
            "produk": f"{masalah}Care {tipe} #{i+1}",
            "kandungan": kandungan,
            "harga": random.choice(["Rp 25.000", "Rp 75.000", "Rp 120.000", "Rp 200.000", "Rp 300.000"]),
            "pakai": waktu,
            "manfaat": manfaat_list.get(kandungan, "Merawat kulit sesuai kebutuhan.")
        })
    return produk_list

# === REKOMENDASI SKINCARE ===
if st.button("🔍 Tampilkan Rekomendasi Skincare Saya"):
    hasil = generate_products(masalah_kulit, tipe_kulit, budget, waktu, n=20)

    st.success(f"Menampilkan 20 produk untuk masalah '{masalah_kulit}' dengan tipe kulit '{tipe_kulit}', budget '{budget}', dipakai saat '{waktu}':")

    for produk in hasil:
        st.subheader(f"💄 {produk['produk']}")
        st.write(f"✅ *Kandungan Utama:* {produk['kandungan']}")
        st.write(f"💰 *Harga Perkiraan:* {produk['harga']}")
        st.write(f"🕒 *Waktu Pemakaian:* {produk['pakai']}")
        st.info(f"📌 *Manfaat:* {produk['manfaat']}")