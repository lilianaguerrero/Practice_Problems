def largeGroupPositions(self, S: str) -> List[List[int]]:
        result = []
        count = 1
        for indx in range(len(S)-1):
            char = S[indx]
            next_char = S[indx+1]
            if char == next_char:
                count += 1
                if count >= 3 and indx == (len(S)-2):
                    result.append([indx+2-count,indx+1])
                    count = 1
            elif count >= 3 and char != next_char:
                result.append([indx+1-count,indx])
                count = 1
            else:
                count = 1
        return result