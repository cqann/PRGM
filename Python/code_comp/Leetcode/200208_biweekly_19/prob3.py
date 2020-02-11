

hour = 1
minutes = 57

hour = hour % 12
m_an = (minutes/60)*360
h_an = 360 * (hour/12) + (m_an/360)*(360/12)

res = abs(m_an-h_an)
res = 360 - res if res > 180 else res
print(res)
