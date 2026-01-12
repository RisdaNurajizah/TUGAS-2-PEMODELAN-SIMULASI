import streamlit as st

# Pengaturan tema warna pastel ungu lewat sidebar atau config (opsional)
st.set_page_config(page_title="Queuing Calculator", layout="centered")

# CSS kustom untuk warna pastel ungu
st.markdown("""
    <style>
    .stApp { background-color: #f3effb; }
    .stButton>button { 
        background-color: #9b89cf; color: white; border-radius: 10px; width: 100%; border: none;
    }
    .stButton>button:hover { background-color: #8572bd; color: white; }
    .solution-box { 
        background-color: white; padding: 20px; border-radius: 15px; 
        border: 1px solid #e1d9f3; font-family: monospace; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💜 Queuing Theory Calculator 💜")
st.write("Model Antrian M/M/2 (Kantor Pos)")

# Input User
arrival_time = st.number_input("Waktu Antar Kedatangan (menit):", min_value=0.1, step=0.1, value=4.0, format="%g")
service_time = st.number_input("Waktu Pelayanan per Pelayan (menit):", min_value=0.1, step=0.1, value=3.0, format="%g" )

# Tombol Calculate
if st.button("Calculate"):
    # Perhitungan [cite: 21, 22, 24, 26, 28]
    lam = 1 / arrival_time
    mu = 1 / service_time
    rho = lam / (2 * mu)
    W = 1 / (mu - (lam / 2))
    Wq = (lam**2) / (2 * mu * (mu - (lam / 2)))

    # Tampilan Solution
    st.markdown("### 📝 Solution Step-by-Step")
    with st.container():
        st.markdown(f"""
        <div class="solution-box">
            <strong>Diketahui:</strong><br>
            Waktu Antar Kedatangan (&lambda;) = 1 / {arrival_time:g} = {round(lam, 3):g} per menit<br>
            Waktu Pelayanan per Pelayan (&mu;) = 1 / {service_time:g} = {round(mu, 3):g} per menit<br>
            Jumlah Loket (s) = 2<br>
            <hr>
            <strong>1. Pemanfaatan Pelayan (&rho;)</strong><br>
            &rho; = &lambda; / (s * &mu;) = {round(lam, 3):g} / (2 * {round(mu, 3):g}) = <b>{round(rho, 3):g}</b><br><br>
            <strong>2. Waktu dalam Sistem (W)</strong><br>
            W = 1 / (&mu; - &lambda;/2) = <b>{round(W, 3):g} menit</b><br><br>
            <strong>3. Waktu dalam Antrian (Wq)</strong><br>
            Wq = &lambda;² / [2&mu; * (&mu; - &lambda;/2)] = <b>{Wq:.3f} menit</b>
        </div>
        """, unsafe_allow_html=True)