# File Compression and Indexing System

This project implements a command-line based file management system using:

- Huffman Coding for compression and decompression
- Red-Black Tree for file name indexing
- B+ Tree for ordered file structure

## Features

- Compress `.txt` files to `.huff`
- Decompress `.huff` files back to `.txt`
- Add and search file names in a tree structure
- Display file index (via B+ Tree)

## How to Run

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the system:
   ```
   python cli_interface.py
   ```

## Folder Structure

```
project/
│
├── cli_interface.py
├── huffman.py
├── redblacktree.py
├── b_plus_tree.py
├── requirements.txt
├── README.md
├── test_system.py
└── storage/
    ├── example.txt
    ├── example.txt.huff
```
