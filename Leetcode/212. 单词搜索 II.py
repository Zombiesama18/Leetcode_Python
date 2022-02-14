#!/usr/bin/env Python
# coding=utf-8
# 212. 单词搜索 II
# 给定一个m x n 二维字符网格board和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 思路：Trie树 + DFS 通过进入下面的DFS时将当前位置改为'.'来实现不允许被重复使用，进入下面的DFS后再改回来
import collections


def findWords(board: [[str]], words: [str]) -> [str]:
    class Trie:
        class Node:
            def __init__(self, value='', isKey=False):
                self.value = value
                self.isKey = isKey
                self.map = {}

        def __init__(self):
            self.root = self.Node()

        def insert(self, word: str):
            currentNode = self.root
            for char in word:
                if not currentNode.map.get(char):
                    currentNode.map[char] = self.Node(value=char, isKey=False)
                currentNode = currentNode.map[char]
            currentNode.isKey = True

    def DFS(currentNode, currentRow, currentCol, currentWord):
        currentChar = board[currentRow][currentCol]
        if currentChar not in currentNode.map:
            return
        nextNode = currentNode.map.get(currentChar)
        if nextNode.isKey:
            result.add(currentWord + currentChar)
        board[currentRow][currentCol] = '.'
        for direction in directions:
            nextRow, nextCol = currentRow + direction[0], currentCol + direction[1]
            if 0 <= nextRow < row and 0 <= nextCol < col:
                DFS(nextNode, nextRow, nextCol, currentWord + currentChar)
        board[currentRow][currentCol] = currentChar

    trieTree = Trie()
    for word in words:
        trieTree.insert(word)
    result = set()
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            DFS(trieTree.root, i, j, '')
    return list(result)


findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
findWords([["a"]], ["a"])


