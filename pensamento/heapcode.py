
def heapify(array, tamanho_heap, indice):
    maior = indice
    filho_esquerdo = 2 * indice + 1
    filho_direito = 2 * indice + 2

    if filho_esquerdo < tamanho_heap and array[maior] < array[filho_esquerdo]:
        maior = filho_esquerdo

    if filho_direito < tamanho_heap and array[maior] < array[filho_direito]:
        maior = filho_direito

    if maior != indice:
        array[indice], array[maior] = array[maior], array[indice]
        heapify(array, tamanho_heap, maior)

def heap_sort(array):
    tamanho = len(array)

    for indice in range(tamanho // 2 - 1, -1, -1):
        heapify(array, tamanho, indice)

    for indice in range(tamanho -1, 0, -1):
        array[indice], array[0] = array[0], array[indice]
        heapify(array, indice, 0)

#teste
array = [10, 154, 8, 0, 9, 48, 7, 55, 5] 
heap_sort(array)
print(f"Heap Sort do array: {array}")