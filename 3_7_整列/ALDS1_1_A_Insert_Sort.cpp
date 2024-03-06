//https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A&lang=jp

//g++ -std=c++11 -stdlib=libc++ ALDS1_1_A_Insert_Sort.cpp -o ALDS1_1_A_Insert_Sort
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

void insertionSort(int N, std::vector<int>& array){
	for (int i=1; i < N; i++){
		int v = array[i];
		int j = i - 1;
		while (j >= 0 && array[j] > v){
			array[j+1] = array[j];
			array[j] = v;
			j--;
			for (int k=0; k < array.size(); k++){
				std::cout << array[k] << " ";
			}
			std::cout << std::endl;
		}
	}
}

int main() {
    // テスト用の配列
    std::vector<int> arr = {12, 11, 13, 5, 6};

    // 挿入ソートを実行
    insertionSort(5, arr);

    // ソートされた配列を表示
    std::cout << "Sorted array: ";
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
