def selection_sort(data):
    hasil = data.copy()
    for i in range(len(hasil)):
        indeks_min = i
        for j in range(i + 1, len(hasil)):
            if hasil[j] < hasil[indeks_min]:
                indeks_min = j
        hasil[i], hasil[indeks_min] = hasil[indeks_min], hasil[i]
    return hasil

print(selection_sort([5, 2, 9, 1]))
