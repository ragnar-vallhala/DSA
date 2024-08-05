#include <iostream>
#include <string>
using namespace std;

void solve() {
    string k, s;
    cin >> k >> s;

    int i = 0;
    int last = -1;
    int one = 0;
    int zero = 0;

    while (i < s.length()-1) {
        if (s[i] == '1') {
            one++;
        }
        else
        {
            if(s[i+1]=='1')
            {
                zero++;
            }
        }
        i++;
    }
    if(s.length()>=2)
        if(s[s.length() - 1] =='0') zero++;
    if(s[s.length() - 1] =='1') one++;
    if (one > zero) {
        cout << "Yes" << endl;
    } else {
        if (s[0] == '1' && s[s.length() - 1] == '1') {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
    return 0;
}
