#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main() {
    // 创建一个输入文件流对象，用于读取CSV文件
    std::ifstream file("obesity_level.csv");

    // 检查文件是否成功打开
    if (!file.is_open()) {
        std::cout << "File could not be opened!" << std::endl;
        return 1;  // 如果文件打开失败，返回1并结束程序
    }

    std::string line;
    // 使用getline函数逐行读取文件内容
    while (std::getline(file, line)) {
        // 创建一个字符串流对象，用于处理每一行的内容
        std::istringstream s(line);
        std::string field;

        // 使用getline函数，以逗号为分隔符，将每一行的内容分割成多个字段
        while (getline(s, field, ',')) {
            // 打印每个字段
            std::cout << field << " ";
        }

        // 打印一个换行符，表示一行的结束
        std::cout << std::endl;
    }

    // 关闭文件
    file.close();

    return 0;  // 程序正常结束，返回0
}