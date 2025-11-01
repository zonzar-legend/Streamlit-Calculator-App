import streamlit as st
import math

# App configuration
st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Advanced Streamlit Calculator")
st.write("Perform basic and advanced math operations easily!")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number (if applicable)", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    (
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Power (xⁿ)",
        "Square Root (√x)",
        "Percentage (%)"
    )
)

# Perform calculation
result = None

if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed!")
            else:
                result = num1 / num2
        elif operation == "Power (xⁿ)":
            result = math.pow(num1, num2)
        elif operation == "Square Root (√x)":
            if num1 < 0:
                st.error("❌ Cannot calculate square root of a negative number!")
            else:
                result = math.sqrt(num1)
        elif operation == "Percentage (%)":
            result = (num1 * num2) / 100
        
        # Save to history if valid
        if result is not None:
            st.session_state.history.append(f"{operation}: {result:.4f}")
            st.success(f"✅ Result: {result}")
    
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Divider
st.markdown("---")

# Show history
st.subheader("🧾 Calculation History")
if st.session_state.history:
    for i, entry in enumerate(reversed(st.session_state.history[-10:]), 1):
        st.text(f"{i}. {entry}")
else:
    st.info("No calculations yet!")

# Clear history button
if st.button("Clear History"):
    st.session_state.history.clear()
    st.info("🗑️ History cleared!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Ayaz Zafar using Streamlit")
