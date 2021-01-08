class Solution {
public:
    int longestValidParentheses(string s) {
        if (s.size() < 2) return 0;
        int d[s.size()];
        d[s.size()-1] = 0;
        d[s.size()-2] = (s[s.size()-2] == '(' && s.back() == ')') ? 2 : 0;
        int longest_so_far = d[s.size()-2];
        for (int i = s.size()-3; i >= 0; --i) {
            d[i] = 0;
            if (s[i] != '(') continue; 
            int closing_expected_at = i + d[i+1] + 1;
            if (closing_expected_at < s.size() && s[closing_expected_at] == ')') {
                d[i] = d[i+1] + 2;
                if (closing_expected_at+1 < s.size()) {
                    d[i] += d[closing_expected_at + 1];
                }
                longest_so_far = max(longest_so_far, d[i]);
            }
        }
        return longest_so_far;
    }
};
