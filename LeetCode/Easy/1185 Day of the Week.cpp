#include <bits/stdc++.h>

class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        string days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        tm time_in = {};
        time_in.tm_year = year - 1900;
        time_in.tm_mon = month - 1;
        time_in.tm_mday = day;

        mktime(&time_in);

        return days[time_in.tm_wday];
    }
};