class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        citations_count = [0 for _ in range(papers + 1)]

        for cit in citations:
            citations_count[min(cit, papers)] += 1

        h_index = 0

        for h in range(papers, -1, -1):
            h_index += citations_count[h]
            if h_index >= h:
                return h