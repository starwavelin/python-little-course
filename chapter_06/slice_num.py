text = "X-DSPAM-Confidence:    0.8475";
colon_pos = text.find(':')
num = float(text[colon_pos + 1:].lstrip())
print(num)
