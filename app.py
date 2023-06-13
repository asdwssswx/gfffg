
import streamlit as st



st.title("201921054 임채민")

st.header("201921054 임채민")
st.subheader("과제")
st.text("폐루프 함수=G(s) = 100 / (s^2 + 5s + 6)")




import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


s1 = signal.lti([100],[1,5,6])

frequencies = np.logspace(-2,2,500)

w, mag, phase= s1. bode(frequencies)

plt.figure()
plt.subplot(2,1,1)
plt.semilogx(w,mag)
plt.title('Bode plot of G(s)=100/(s+2)(s+3)')
plt.ylabel('Magnitude [dB]')

plt.subplot(2,1,2)
plt.semilogx(w,phase)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')


st.pyplot(plt)