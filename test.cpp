#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

vector<string> solution(vector<vector<long long>> a) {
    vector<string> ans;
    map<long long, int> rowFlip;
    map<long long, int> columnFlip;
    
    for (const auto& query : a) {
        long long x = query[0];
        long long y = query[1];
        int valX = query[2];
        int valY = query[3];
        
        // Determine the current flip state for row and column
        int currentRowFlip = rowFlip[x];
        int currentColumnFlip = columnFlip[y];
        
        // Calculate the expected value in X after flips
        int expectedValue = valX;
        if (currentRowFlip % 2 != 0) {
            expectedValue *= -1;
        }
        if (currentColumnFlip % 2 != 0) {
            expectedValue *= -1;
        }
        
        // Check if the expected value matches the target value
        if (expectedValue == valY) {
            ans.push_back("Yes");
        } else {
            ans.push_back("No");
        }
        
        // Update row and column flip maps
        if (valX != valY) {
            rowFlip[x]++;
        } else {
            columnFlip[y]++;
        }
    }
    
    return ans;
}

int main() {
    // Example input
    vector<vector<long long>> input1 = {{1, 1, 1, 1}, {1, 2, 1, -1}};
    vector<vector<long long>> input2 = {{1, 1, 1, 1}, {1, 2, 1, 1}, {2, 2, 1, 1}, {2, 1, 1, -1}};
    
    vector<string> result1 = solution(input1);
    vector<string> result2 = solution(input2);
    
    cout << "Output 1: ";
    for (const string& s : result1) {
        cout << s << " ";
    }
    cout << endl;
    
    cout << "Output 2: ";
    for (const string& s : result2) {
        cout << s << " ";
    }
    cout << endl;
    
    return 0;
}
