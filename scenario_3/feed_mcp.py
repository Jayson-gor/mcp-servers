from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FreeCodeCamp Feed Searcher")

FEED_URL = "https://www.freecodecamp.org/news/rss/"

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 5):
    """Search recent freeCodeCamp news posts by title, description, tags, or content.
    Every word in the query must appear somewhere in the post."""
    feed = feedparser.parse(FEED_URL)
    words = query.lower().split()
    results = []

    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        tags = [t.get("term", "") for t in entry.get("tags", [])]
        content = " ".join(c.get("value", "") for c in entry.get("content", []))

        haystack = " ".join([title, summary, " ".join(tags), content]).lower()

        if all(w in haystack for w in words):
            results.append({
                "title": title,
                "url": entry.get("link", ""),
                "tags": tags,
            })
            if len(results) >= max_results:
                break

    return results or [{"message": f"No results found among {len(feed.entries)} recent posts"}]

if __name__ == "__main__":
    mcp.run()