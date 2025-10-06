class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.eow = True

    def display(self):
        self._display(self.root, "")
    
    def _display(self, node, prefix):
        if node.eow:
            print(prefix)
        for letter, children in node.children.items():
            self._display(children, prefix+letter)

    def autocomplete(self, word):
        print("Auto complete")
        results = []
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        def dfs(current_node, path):
            if current_node.eow:
                print(path)
                results.append("".join(path))


            for char, next_node in current_node.children.items():
                path.append(char)
                dfs(next_node, path)
                path.pop()

        dfs(node, list(word))


    def delete(self, word):
        node = self.root
        stack = []
        for letter in word:
            if letter not in node.children:
                return False
            stack.append((letter, node))
            node = node.children[letter]
        if not node.eow:
            return
        node.eow = False

        for letter, parent in reversed(stack):
            print(letter, parent)
            child = parent.children[letter]
            if child.eow or child.children:
                break
            del parent.children[letter]






t = Trie()
words = [
    "a",          # single-letter word
    "an",         # prefix of "and"
    "and",        # longer word sharing prefix
    "ant",        # diverges at the end from "and"
    "anty",
    "bat",        # different root character, new branch
    "batch",      # longer word extending "bat"
    "bats",       # same prefix "bat", diverges at last char
    "cat",        # new root branch
    "cater",      # extends "cat"
    "dog",        # another new root branch
    "do",         # prefix of "dog"
    "dot",        # shares prefix "do", diverges
    "zoo"         # completely independent branch
]
for word in words:
    t.insert(word)

t.delete("an")
    
t.display()
