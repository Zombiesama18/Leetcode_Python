package Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class 基本计算器II_227 {
    public int calculate(String s) {
        int sign = 1;
        List<Integer> stack_num = new ArrayList<>();
        List<Character> stack_ops = new ArrayList<>();
        int index = 0;
        while (index < s.length()){
            if (s.charAt(index) == '+' || s.charAt(index) == ' '){
                index += 1;
            } else if (s.charAt(index) == '-') {
                sign = -sign;
                index += 1;
            }
            else if (s.charAt(index) == '*' || s.charAt(index) == '/'){
                stack_ops.add(s.charAt(index));
                index += 1;
            }
            else{
                int num = 0;
                while (index < s.length() && Character.isDigit(s.charAt(index))){
                    num = 10 * num + Integer.parseInt(String.valueOf(s.charAt(index)));
                    index += 1;
                }
                if (!stack_ops.isEmpty()){
                    if (stack_ops.get(stack_ops.size() - 1) == '*'){
                        stack_num.add(stack_num.remove(stack_num.size() - 1) * num);
                    }
                    if (stack_ops.get(stack_ops.size() - 1) == '/'){
                        stack_num.add(stack_num.remove(stack_num.size() - 1) / num);
                    }
                    stack_ops.remove(stack_ops.size() - 1);
                }
                else{
                    stack_num.add(sign * num);
                    sign = 1;
                }
            }
        }
        return stack_num.stream().mapToInt(Integer::intValue).sum();
    }
 }
