
#Greedy Approach 
class Solution(object):
    def fullJustify(self,words, maxWidth):
        result = []
        current_line = []
        current_width = 0

        for word in words:
            if current_width + len(word) + len(current_line) > maxWidth:
                # Distribute spaces evenly
                spaces = maxWidth - current_width
                gaps = len(current_line) - 1
                if gaps == 0:
                    result.append(current_line[0] + ' ' * spaces)
                else:
                    space_each_gap, extra_spaces = divmod(spaces, gaps)
                    result.append(''.join(word + ' ' * (space_each_gap + 1) if i < extra_spaces else word + ' ' * space_each_gap for i, word in enumerate(current_line[:-1])) + current_line[-1])
                current_line = []
                current_width = 0
            current_line.append(word)
            current_width += len(word)

        # Handle the last line
        last_line = ' '.join(current_line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))
        return result



    def fulljustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]