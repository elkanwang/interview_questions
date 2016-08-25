class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        files = input.split('\n')
        current_file_path = ''
        longest_path = ''
        current_lv = 0
        for file in files:
            lv = file.count('\t')
            if lv == current_lv:
                current_file_path += '/' + file.lstrip('\t')
                current_lv += 1
            else:
                current_file_path = '/'.join(current_file_path.split('/')[:-abs(current_lv-lv)]) + '/' + file.lstrip('\t')
                current_lv += -abs(current_lv-lv) + 1
            print(current_lv, repr(current_file_path))
            if '.' in file and len(current_file_path) > len(longest_path):
                longest_path = current_file_path
        parts = longest_path.split('/')[1:]
        if not longest_path:
            if '.' in input:
                return len(input)
            else:
                return 0
        count  = 0
        for part in parts:
            count += len(part)
        return count + (len(parts)-1)


sol = Solution()
print(sol.lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'))
a = "dir\nsubdir1\n\tsubdir2\n\t\tfile.ext"
b = "a"

print (sol.lengthLongestPath(a))
print (sol.lengthLongestPath(b))
print (sol.lengthLongestPath("a\n\tb\n\t\tc"))