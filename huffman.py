import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code='', codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + '0', codes)
    generate_codes(node.right, current_code + '1', codes)

    return codes

def compress(text, codes):
    return ''.join(codes[char] for char in text)

def decompress(encoded_text, root):
    result = ''
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            result += current.char
            current = root
    return result

