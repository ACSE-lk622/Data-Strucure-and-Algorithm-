from xml.dom.expatbuilder import FragmentBuilderNS


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i 
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    def searchString(self,word): #TC:O(n), SC:O(1)
        currentNode = self.root
        for i in word :
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString is True:
            return True
        else:
            return False
def deleteString(root,word,index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1 :
        deleteString(currentNode,word,index+1)
        return False
    if index == len(word)-1:
        if len(currentNode.children) >= 1: #has other same prefix children
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfString == True: # when arrive prefix of another String end 
        deleteString(currentNode,word,index+1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode,word,index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie = Trie()
newTrie.insertString("APPS")
newTrie.insertString("APPSL")
deleteString(newTrie.root,"APPS",0)
print(newTrie.searchString("APPSL"))