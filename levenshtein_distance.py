def levenshtein_distance(A, B):
    def compute_dist_between_prefixes(indA, indB):
        if indA < 0:
            #A is empty, so add all of B's characters
            return indB + 1
        elif indB < 0:
            #B is empty so delete all A's characters
            return indA + 1
        
        if distance_between_prefixes[indA][indB] == -1:
            if A[indA] == B[indB]:
                distance_between_prefixes[indA][indB] =  compute_dist_between_prefixes(indA-1, indB-1)
            else:
                sub_last = compute_dist_between_prefixes(indA - 1, indB - 1)
                add_last = compute_dist_between_prefixes(indA - 1, indB)
                delete_last = compute_dist_between_prefixes(indA, indB - 1)                   
                min_last = min(sub_last,add_last,delete_last)
                
                distance_between_prefixes[indA][indB] = 1 + min_last
        return distance_between_prefixes[indA][indB]
    
 
    distance_between_prefixes = [[-1] * len(B) for _ in A]
    return compute_dist_between_prefixes(len(A) - 1, len(B) - 1)
        