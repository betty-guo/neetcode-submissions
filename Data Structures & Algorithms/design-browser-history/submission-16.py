# one tab only
# can visit url (add to end of browserHistory linked list, clear others)
# can go back in history, return the url
class BrowserHistoryNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentTab = BrowserHistoryNode(homepage)

    # time complexity is O(1)
    def visit(self, url: str) -> None:
        self.currentTab.next = BrowserHistoryNode(url) # overwrites next, disconnects rest of the browser history
        self.currentTab.next.prev = self.currentTab # set backwards pointer on the new page to existing current tab
        self.currentTab = self.currentTab.next # move to new url

    # time complexity is O(n) where n is max the length of the browser history
    def back(self, steps: int) -> str:
        while self.currentTab.prev and steps > 0:
            self.currentTab = self.currentTab.prev
            steps -= 1
        
        return self.currentTab.url

    # time complexity is O(n) where n is max the length of the browser history
    def forward(self, steps: int) -> str:
        while self.currentTab.next and steps > 0:
            self.currentTab = self.currentTab.next
            steps -= 1

        return self.currentTab.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)