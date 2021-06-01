#include <bits/stdc++.h>
#include <sstream>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

void solve(vector<int> arr, vector<int> queries) {
    int start_comp = 0;
    int end_comp = 0;
    
    for (int i = 0; i < queries.size(); i++) {
        vector<int>::iterator it = find(arr.begin(), arr.end(), queries[i]);
        int index = distance(arr.begin(), it);
        start_comp += index + 1;
        end_comp += arr.size() - index;
    }

    cout << start_comp << " " << end_comp << "\n";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ar_count_temp;
    getline(cin, ar_count_temp);

    int n = stoi(ltrim(rtrim(ar_count_temp)));

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split(rtrim(ar_temp_temp));

    vector<int> ar(n);

    for (int i = 0; i < n; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    string m_temp;
    getline(cin, m_temp);

    int m = stoi(ltrim(rtrim(m_temp)));

    string queries_str_temp;
    getline(cin, queries_str_temp);
    vector<string> queries_str = split(rtrim(queries_str_temp));
    vector<int> queries(m);

    for (int i = 0; i < m; i++) {
        int query = stoi(queries_str[i]);

        queries[i] = query;
    }

    solve(ar, queries);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
