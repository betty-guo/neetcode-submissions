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
        self.head = BrowserHistoryNode(homepage)
        self.tail = self.head
        self.currentTab = self.head # start on the homepage

    def visit(self, url: str) -> None:
        newPage = BrowserHistoryNode(url)
        self.currentTab.next = newPage # overwrites next, disconnects rest of the browser history
        self.tail = newPage # update the tail
        newPage.prev = self.currentTab # set backwards pointer on the new page to existing current tab
        self.currentTab = newPage # move to new url

    def back(self, steps: int) -> str:
        while self.currentTab and self.currentTab != self.head and steps > 0:
            self.currentTab = self.currentTab.prev
            steps -= 1
        
        return self.currentTab.url

    def forward(self, steps: int) -> str:
        while self.currentTab and self.currentTab != self.tail and steps > 0:
            self.currentTab = self.currentTab.next
            steps -= 1

        return self.currentTab.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)