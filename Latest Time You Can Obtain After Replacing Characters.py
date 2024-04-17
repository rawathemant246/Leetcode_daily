class Solution(object):
    def findLatestTime(self, s: str) -> str:
        
        hour, minute = s.split(":")
        
        if hour[0] == "?":
            if hour[1] == "?":
                hour = "11"
            elif '0' <= hour[1] <= '1':
                hour = '1' + hour[1]
            else:
                hour = '0' + hour[1]
        elif hour[1] == '?':
            if hour[0] == '1':
                hour = hour[0] + '1'
            else:
                hour = hour[0] + '9'
        
        if minute[0] == "?":
            minute = '5' + minute[1]
        if minute[1] == "?":
            minute = minute[0] + '9'
        
        return hour + ":" + minute

# Example to test the function
s = "0?:?5"
test1 = Solution()
time = test1.findLatestTime(s)
print(time)  # Should return "09:25"
