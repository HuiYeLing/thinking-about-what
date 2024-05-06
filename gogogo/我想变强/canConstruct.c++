#include <vector>
#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> chars(26, 0);  // 创建一个大小为26的向量，用于存储每个字符出现的次数
        for (char c : magazine) {  // 遍历 magazine 中的每个字符
            chars[c - 'a']++;  // 增加对应字符的计数
        }
        for (char c : ransomNote) {  // 遍历 ransomNote 中的每个字符
            if (--chars[c - 'a'] < 0) {  // 如果 magazine 中没有足够的字符，返回 false
                return false;
            }
        }
        return true; 
    }
};