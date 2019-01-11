def prob(l_mean, l_standard_deviation, l_n, l_x1, l_x2):
    z_score1 = (l_x1 - l_mean*l_n) / (l_standard_deviation * (l_n ** 0.5))
    z_score2 = (l_x2 - l_mean*l_n) / (l_standard_deviation * (l_n ** 0.5))
    return z_score1,z_score2


g_mean = 2
g_standard_deviation = 1**0.5
g_n = 50
g_x1 = 90
g_x2 = 110

print(prob(g_mean, g_standard_deviation, g_n, g_x1, g_x2))
z = 0.9207 - 0.793
print("Probability = ", z)