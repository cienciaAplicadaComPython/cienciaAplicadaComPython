import streamlit as st
import matplotlib.pyplot as plt

x = st.sidebar.slider('x')
st.sidebar.write(x, 'squared is', x * x)

y = x**2

fig, ax = plt.subplots(figsize = (10,5))
ax.scatter(x, y, label = 'Valores')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()

st.pyplot(fig)
