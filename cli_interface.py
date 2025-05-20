from redblacktree import RedBlackTree
from b_plus_tree import BPlusTree
from huffman import build_huffman_tree, generate_codes, compress, decompress
import json

def compress_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        root = build_huffman_tree(text)
        codes = generate_codes(root)
        encoded = compress(text, codes)

        # Save the code table in JSON format
        with open(filename + ".huff", "w", encoding="utf-8") as f:
            f.write(json.dumps(codes) + "\n")  # first line: code table
            f.write(encoded)  # second line: compressed data

        print(f"{filename} successfully compressed → {filename}.huff")
    except FileNotFoundError:
        print("File not found!")

def decompress_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            codes = json.loads(lines[0].strip())
            encoded = lines[1].strip()

        # Reverse the code table (binary → character)
        reverse_codes = {v: k for k, v in codes.items()}

        result = ""
        current = ""
        for bit in encoded:
            current += bit
            if current in reverse_codes:
                result += reverse_codes[current]
                current = ""

        original_name = filename.replace(".huff", "_decoded.txt")
        with open(original_name, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"{filename} successfully decompressed → {original_name}")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during decompression:", str(e))

def main():
    rb_tree = RedBlackTree()
    bptree = BPlusTree(t=4)

    while True:
        print("\n=== FILE MANAGEMENT SYSTEM ===")
        print("1. Compress file")
        print("2. Decompress file")
        print("3. Add file (by name)")
        print("4. Search file")
        print("5. Show index (B+ Tree)")
        print("6. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            name = input("Enter the name of the file to compress: ")
            compress_file(name)

        elif choice == "2":
            name = input("Enter the name of the file to decompress: ")
            decompress_file(name)

        elif choice == "3":
            name = input("Enter the file name: ")
            rb_tree.insert(name)
            bptree.insert(name)
            print(f"{name} added.")

        elif choice == "4":
            name = input("Enter the file name to search: ")
            if rb_tree.search(name):
                print("File found ✅")
            else:
                print("File not found ❌")

        elif choice == "5":
            print("B+ Tree index structure:")
            bptree.print_tree()

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
