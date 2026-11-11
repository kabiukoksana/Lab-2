import numpy as np
K = 2500
r_bank = 0.04
p_bank = np.array([0.99, 0.01])
x_bank = np.array([K * r_bank, 0])
m_bank = np.sum(x_bank * p_bank)
d_bank = np.sum(p_bank * (x_bank - m_bank) ** 2)
sigma_bank = np.sqrt(d_bank)
cv_bank = sigma_bank / m_bank * 100
sv_bank = np.sum(p_bank * np.maximum(m_bank - x_bank, 0) ** 2)
ssv_bank = np.sqrt(sv_bank)
r_at = 0.208
p_at = np.array([0.5, 0.5])
x_at = np.array([K * r_at, -K])
m_at = np.sum(x_at * p_at)
d_at = np.sum(p_at * (x_at - m_at) ** 2)
sigma_at = np.sqrt(d_at)
if m_at > 0:
    cv_at = sigma_at / m_at * 100
else:
    cv_at = None
sv_at = np.sum(p_at * np.maximum(m_at - x_at, 0) ** 2)
ssv_at = np.sqrt(sv_at)
p_min = (m_bank + K) / (K * r_at + K)
print("========== РЕЗУЛЬТАТИ РОЗРАХУНКІВ ==========")
print("\nВАРІАНТ 1. БАНК")
print(f"Математичне сподівання: {m_bank:.2f} дол.")
print(f"Дисперсія: {d_bank:.2f}")
print(f"Середньоквадратичне відхилення: {sigma_bank:.2f} дол.")
print(f"Коефіцієнт варіації: {cv_bank:.2f}%")
print(f"Семіваріація: {sv_bank:.2f}")
print(f"Семіквадратичне відхилення: {ssv_bank:.2f} дол.")
print("\nВАРІАНТ 2. АТ")
print(f"Математичне сподівання: {m_at:.2f} дол.")
print(f"Дисперсія: {d_at:.2f}")
print(f"Середньоквадратичне відхилення: {sigma_at:.2f} дол.")
if cv_at is not None:
    print(f"Коефіцієнт варіації: {cv_at:.2f}%")
else:
    print("Коефіцієнт варіації не визначається для від'ємного сподівання.")
print(f"Семіваріація: {sv_at:.2f}")
print(f"Семіквадратичне відхилення: {ssv_at:.2f} дол.")
print("\n========== ПОРІВНЯННЯ ==========")
if m_bank > m_at:
    print("Банк має більше математичне сподівання прибутку.")
if sigma_bank < sigma_at:
    print("Банк має менше середньоквадратичне відхилення.")
if cv_at is None:
    print("Для людини, яка не схильна до ризику,")
    print("кращим варіантом є БАНК.")
print("\n========== МІНІМАЛЬНА ЙМОВІРНІСТЬ ==========")
print(f"Мінімальна ймовірність успіху АТ: {p_min:.4f}")
print(f"У відсотках: {p_min * 100:.2f}%")
print("\nЩоб АТ було вигіднішим за банк за сподіваним")
print("прибутком, імовірність успіху має бути не меншою")
print(f"за {p_min * 100:.2f}%.")