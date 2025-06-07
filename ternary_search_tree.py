class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False


class TernarySearchTree:
    def __init__(self):
        self.root = None       

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]
        if node is None:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                node.is_end = True
        return node

    def search(self, word, exact=False):
        if word == "":
            return True if not exact else self.has_empty
        return self._search(self.root, word, 0, exact)

    def _search(self, node, word, index, exact):
        if node is None:
            return False
        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index, exact)
        elif char > node.char:
            return self._search(node.right, word, index, exact)
        else:
            if index == len(word) - 1:
                return node.is_end if exact else True
            return self._search(node.eq, word, index + 1, exact)

    def __len__(self):
        count = self._count_words(self.root)
        if self.has_empty:
            count += 1
        return count

    def _count_words(self, node): 
        if node is None:
            return 0
        count = self._count_words(node.left)
        count += self._count_words(node.eq)
        count += self._count_words(node.right)
        if node.is_end:
            count += 1
        return count

    def all_strings(self):
        result = []
        if self.has_empty:
            result.append("")  
        self._collect_words(self.root, "", result)
        return result
    
    def _collect_words(self, node, prefix, result):
        if node is None:
            return
        self._collect_words(node.left, prefix, result)
        if node.is_end:
            result.append(prefix + node.char)
        self._collect_words(node.eq, prefix + node.char, result)
        self._collect_words(node.right, prefix, result)

        def __str__(self):
             lines = []
        if self.has_empty:
            lines.append("char: '', terminates: True (empty string)")
        self._collect_str(self.root, prefix="", is_eq=True, lines=lines)
        return "\n".join(lines)
