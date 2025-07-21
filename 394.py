class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []

        for chr in s:

            if chr == "]":

                curr_str = ""
                while st[-1] != "[":
                    curr_str = st.pop() + curr_str

                st.pop()

                multiple = ""

                while st and st[-1] in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]:
                    multiple = st.pop() + multiple

                curr_str = int(multiple) * curr_str

                st.append(curr_str)

            else:
                st.append(chr)

        return "".join(st)
