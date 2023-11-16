# Temperature converter program

# -------------------------
# Subprograms
# -------------------------
def c_to_f(centigrade):
  return (centigrade * 1.8) + 32

# -------------------------
# Main program
# -------------------------
centigrade = -5
fahrenheit = c_to_f(centigrade)
print(centigrade, "degrees Centigrade is", fahrenheit, "degrees Fahrenheit.")
