import requests
from typing import Optional, Any
import webbrowser
from selenium import webdriver

#ref: https://www.selenium.dev/documentation/webdriver/getting_started/quick_start/
#ref: https://docs.python.org/3/library/webbrowser.html
#ref: https://www.geeksforgeeks.org/python-web-scraping-using-beautifulsoup-and-requests/
#ref: https://www.geeksforgeeks.org/python-web-scraping-using-selenium/

class WebSearch:
    def __init__(self, search_engine: str = "Google") -> None:
        self.search_engine: str = search_engine
        # consider using a more complex data structure for queries
        # consider using a list to store multiple queries
        # consider using a dictionary to store queries with their results
        # consider initializing query as an empty string or None or default value
        # or with constructor parameter
        #self.query: Optional[str | None] = query
        #TODO: attempt to pass browser option if not available
        #TODO: consider writing a method to set the browser with option based on availability in system or default browser
        self.browser: str = "chrome|firefox|safari|edge"
        self.browser_open: bool = False
        self.registered_browser: webbrowser.BaseBrowser | None = None
        self.is_registered: bool = False
        
    def web_browser_register(self) -> None:
        #TODO: confirm if this is the correct way to register a web browser
        #TODO: confirm return type of this function
        # register a web browser with the specified search engine or browser
        # purpose is control the opening and closing of the browser and tabs
        print(f"Web browser registered with {self.search_engine} as the search engine.")
        # simpler way to register a web browser
        #webbrowser.get('firefox')
        self.registered_browser = webbrowser.get("firefox")  # or "chrome", "safari", "edge", etc.
        # or use webbrowser.register() to register a custom browser
        #self.registered_browser = webbrowser.register(name="chrome", klass=None, instance=None, preferred=False)
        return webbrowser.register(name="firefox", klass=None, instance=None, preferred=False)
    
    def web_browser_unregister(self) -> None:
        # unregister the web browser
        # purpose is to stop using the browser and free up resources
        print(f"Web browser unregistered from {self.search_engine}.")
        if self.registered_browser:
            self.registered_browser = None
            #webbrowser.register(name=self.registered_browser, klass=None, instance=None, preferred=False)
            print("Browser unregistered successfully.")
            
        else:
            print("No registered browser to unregister.")
            
    def web_browser_is_registered(self) -> bool:
        # check if the web browser is registered
        # purpose is to confirm if the browser is registered before using it
        if self.registered_browser:
            print(f"Web browser is registered with {self.search_engine}.")
            self.is_registered = True
            return True
        else:
            print("No registered browser found.")
            self.is_registered = False
            return False
        
    def web_browser_registered_manager(self) -> None:
        # manage the web browser registration
        # purpose is to open or close the browser based on its registration status
        if self.web_browser_is_registered():
            print("Browser is already registered.")
        else:
            self.web_browser_register()
            print("Browser registered successfully.")
        
        if self.registered_browser is not None:
            self.registered_browser.open("https://www.google.com")
            self.registered_browser.open_new_tab("https://www.python.org")
            self.registered_browser.open_new("https://www.google.com") 
        #TODO: how to close the browser if it is open, no method in webbrowser module??
        else:
            print("No registered browser available to open URLs.")

    def search_sim(self, query: Optional[str | None])-> None:
        # simulate a web search using the specified search engine
        print(f"Searching for '{query}' using {self.search_engine}...")

    def display_results_sim(self, results: Optional[list[str] | str | None]) -> str | None:
        # simulate displaying search results
        print("Search Results:")
        if results is None:
            return "No results found."
        for result in results:
            if isinstance(result, str):
                print(f"- {result}")            
            
    def open_browser_sim(self) -> None:
        # simulate opening a browser
        print("Opening browser...")
        self.browser_open = True
        self.query = input("Enter your search query: ")
        if not self.query:
            print("No query provided. Exiting.")
            return
        self.search_sim(self.query)
        
        # simulate search results
        results = [f"Result {i+1} for '{self.query}'" for i in range(5)]
        self.display_results(results)
        
    def closer_browser_sim(self) -> None:
        # simulate closing the browser
        print("Closing the browser...")
        print("Browser closed.")
        self.browser_open = False
        
        
    def search(self, query: Optional[str | None]) -> str | None:
        # perform a web search using the specified search engine
        # format the query for the search URL
        local_query = query.lower().replace(" ", "+").lstrip().rstrip() if query else ""
        url = f"https://wwww.google.com/search?q={local_query}"
        
        # open the browser and navigate to the search URL
        print("Opening browser and navigating to the search URL...")
        
        response = requests.get("https://www.google.com/search?", params={"q": local_query})
        if response.status_code == 200:
            print(f"Opened browser and navigated to {url}")
            self.display_results(response.text)
            #return response.text
        else:
            print(f"Failed to open browser. Status code: {response.status_code}")
            
            
    def open_browser(self, url: Optional[str | None]) -> None:
        
        url = url or "https://www.google.com"
        # open the browser with the specified URL or default to Google
        print(f"Opening browser with URL: {url}")
        webbrowser.open(url)
        # open the browser and navigate to the search URL
        # print("Opening browser...")
        # webbrowser.open("https://www.google.com")
        
    
    def display_results(self, results: list[str] | str) -> None:
        # display search results in the console
        print("Search Results:")
        for result in results:
            if isinstance(result, str):
                # print each result in a new line
                print(f"- {result}")
            
    def open_tab(self, url: Optional[str | None]) -> None:
        # open a new tab in the browser with the speffic URL
        print(f"Opening a new tab with URL: {url}")
        # use webbrowser to open a new tab
        if not url:
            url = "https://www.google.com" # default URL if none provided
        # this will open a new tab in the default browser
        webbrowser.open_new_tab(url)
        
        
        
    # Note: the appropriate driver will installed and configured
    def open_browser_driver(self, url: Optional[str | None] = None) -> None:
        # open a browser using a web driver (e.g., Selenium)
        print(f"Opening browser with URL: {url}")
        driver = webdriver.Firefox()  # or any other browser driver you are using
        if url:
            driver.get(url)
        else:
            driver.get("https://www.google.com")
        
        
    def close_browser_driver(self) -> None:
        # close the browser
        print("Closing the browser...")
        # may need to find or pass the webbrowser instance to close it  
        # if using webbrowser can try:
        # webbrowser.get().close() # may not work as expected in all environments
        # Selenium:
        driver = webdriver.Firefox()  # or any other browser driver you are using
        driver.quit()  # this will close the browser window opened by Selenium
          

    def selenium_search_driver(self, query: Optional[str | None]) -> list[Any] | None:
        # perform a web search using Selenium
        print(f"Performing web search for '{query}' using Selenium...")
        # TODO: make sure to have the appropriate driver installed and configured
        driver = webdriver.Firefox()
        driver.get(f"https://www.google.com/search?q={query}")
        results = driver.find_elements('search-result')
        return results
 
            
# webSearch = WebSearch()
# webSearch.web_browser_register()
# webSearch.open_browser("https://www.google.com")
# webSearch.search("Python programming")
# webSearch.open_tab("https://www.python.org")
# webSearch.web_browser_registered_manager()     