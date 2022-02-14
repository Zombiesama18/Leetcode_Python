"""
5947. 从给定原材料中找到所有可以做出的菜
你有 n 道不同菜的信息。给你一个字符串数组 recipes 和一个二维字符串数组 ingredients 。第 i 道菜的名字为 recipes[i] ，
如果你有它 所有 的原材料 ingredients[i] ，那么你可以 做出 这道菜。一道菜的原材料可能是 另一道 菜，也就是说 ingredients[i]
可能包含 recipes 中另一个字符串。
同时给你一个字符串数组 supplies ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。
请你返回你可以做出的所有菜。你可以以 任意顺序 返回它们。
注意两道菜在它们的原材料中可能互相包含。
"""
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(recipe):
            if able_to_cook[recipe]:
                return True
            if recipe in visited:
                return False
            visited.add(recipe)
            for ingredient in recipe_to_ingredient[recipe]:
                if ingredient in recipe_to_ingredient:
                    if not dfs(ingredient):
                        return False
                elif ingredient not in supplies:
                    return False
            able_to_cook[recipe] = True
            return True

        able_to_cook = {recipe: False for recipe in recipes}
        recipe_to_ingredient = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        supplies = set(supplies)
        visited = set()
        result = []
        for recipe in recipes:
            if dfs(recipe):
                result.append(recipe)
        return result


Solution.findAllRecipes(0,["ju","fzjnm","x","e","zpmcz","h","q"],
[["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],
["f","hveml","cpivl","d"])
Solution.findAllRecipes(0, ["bread","sandwich"],
[["yeast","flour"],["bread","meat"]],
["yeast","flour","meat"])

